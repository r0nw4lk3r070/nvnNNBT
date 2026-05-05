import socket, json, re

def http_request(method, host, port, path, body_dict=None, headers=None):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(120)
    s.connect((host, port))
    
    if body_dict:
        body_json = json.dumps(body_dict)
        header_lines = [
            f'{method} {path} HTTP/1.1',
            f'Host: {host}:{port}',
            'Content-Type: application/json',
            f'Content-Length: {len(body_json)}',
            'Connection: close',
        ]
    else:
        body_json = ''
        header_lines = [
            f'{method} {path} HTTP/1.1',
            f'Host: {host}:{port}',
            'Accept: application/json',
            'Connection: close',
        ]
    
    if headers:
        for k, v in headers.items():
            header_lines.append(f'{k}: {v}')
    
    req = '\r\n'.join(header_lines) + '\r\n\r\n' + body_json
    s.sendall(req.encode())
    resp = b''
    while True:
        try:
            chunk = s.recv(8192)
            if not chunk:
                break
            resp += chunk
        except socket.timeout:
            break
    s.close()
    
    body_start = resp.find(b'\r\n\r\n')
    status_line = resp.decode().split('\r\n')[0]
    if body_start >= 0:
        body_text = resp[body_start+4:].decode()
        return status_line, body_text
    return status_line, resp.decode()

def parse_sse(text):
    """Parse SSE stream and extract content."""
    content_parts = []
    for line in text.split('\n'):
        line = line.strip()
        if line.startswith('data: '):
            data_str = line[6:]
            try:
                data = json.loads(data_str)
                for choice in data.get('choices', []):
                    delta = choice.get('delta', {})
                    c = delta.get('content', '')
                    if c:
                        content_parts.append(c)
            except json.JSONDecodeError:
                pass
    return ''.join(content_parts)

# Check current config - model is qwen3:1.7b which is too small and defaulting to German
# Need to update config.json to use glm-5.1:cloud
print("=== Current workspace config ===")
status, body = http_request('GET', 'factory', 4000, '/workspaces/larsvanderberg')
data = json.loads(body)
print(f"Current model: {data.get('model')}")

# Let's check what models are available
print("\n=== Checking available agents and their models ===")
status, body = http_request('GET', 'factory', 4000, '/agents')
agents_data = json.loads(body)
for agent in agents_data.get('agents', []):
    print(f"  {agent.get('slug')}: model={agent.get('model')}, status={agent.get('status')}")

# The config.json has glm-5.1:cloud but the workspace shows qwen3:1.7b
# Let's try to update the workspace config
print("\n=== Updating workspace config ===")
with open('/workspace/workspaces/lars-van-der-berg/config.json') as f:
    config = json.loads(f.read())

# Try PUT to update config
update_payload = {
    "model": config['agents']['defaults']['model'],
    "provider": config['agents']['defaults']['provider'],
    "apiBase": config['agents']['defaults'].get('apiBase', ''),
    "maxTokens": config['agents']['defaults']['maxTokens'],
    "temperature": config['agents']['defaults']['temperature'],
}
status, body = http_request('PUT', 'factory', 4000, '/workspaces/larsvanderberg/config', update_payload)
print(f"PUT config: {status} | {body[:300]}")

# Try the full config update approach
status, body = http_request('PUT', 'factory', 4000, '/workspaces/larsvanderberg', update_payload)
print(f"PUT workspace: {status} | {body[:300]}")

# Try POST to recreate agent with updated config
print("\n=== Stopping and respawning agent ===")
status, body = http_request('DELETE', 'factory', 4000, '/agents/larsvanderberg')
print(f"DELETE agent: {status} | {body[:300]}")

# Check if workspace config can be updated
status, body = http_request('GET', 'factory', 4000, '/workspaces/larsvanderberg')
print(f"\nWorkspace after agent delete: {status}")
print(body[:1000])