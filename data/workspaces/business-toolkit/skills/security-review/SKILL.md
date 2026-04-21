# Security Review Skill

This skill ensures all code follows security best practices and identifies potential vulnerabilities.

## Tools

- `read_file` — read source code files for security audit
- `write_file` — create security reports and configuration files
- `edit_file` — fix security issues in code
- `exec` — run security scanners, dependency audits, and test commands
- `web_search` — look up CVEs, security advisories, and best practices

## When to Activate

- Implementing authentication or authorization
- Handling user input or file uploads
- Creating new API endpoints
- Working with secrets or credentials
- Implementing payment features
- Storing or transmitting sensitive data
- Integrating third-party APIs
- Pre-deployment security review

## Security Checklist

### 1. Secrets Management

#### FAIL: NEVER Do This
```python
api_key = "sk-proj-xxxxx"  # Hardcoded secret
db_password = "password123"  # In source code
```

#### PASS: ALWAYS Do This
```python
import os

api_key = os.environ["OPENAI_API_KEY"]
db_url = os.environ["DATABASE_URL"]

# Verify secrets exist
if not api_key:
    raise ValueError("OPENAI_API_KEY not configured")
```

#### Verification Steps
- [ ] No hardcoded API keys, tokens, or passwords
- [ ] All secrets in environment variables
- [ ] `.env` files in `.gitignore`
- [ ] No secrets in git history
- [ ] Production secrets in a secrets manager (not env files in production)

### 2. Input Validation

#### Always Validate User Input
```python
from pydantic import BaseModel, EmailStr, Field

class CreateUserInput(BaseModel):
    email: EmailStr
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=0, le=150)

# Validate before processing
def create_user(input_data: dict) -> dict:
    validated = CreateUserInput(**input_data)
    return db.users.create(validated.model_dump())
```

#### File Upload Validation
```python
import os

ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif'}
ALLOWED_MIMETYPES = {'image/jpeg', 'image/png', 'image/gif'}
MAX_SIZE = 5 * 1024 * 1024  # 5MB

def validate_file_upload(filename: str, mimetype: str, size: int) -> bool:
    if size > MAX_SIZE:
        raise ValueError(f'File too large (max {MAX_SIZE // 1024 // 1024}MB)')
    if mimetype not in ALLOWED_MIMETYPES:
        raise ValueError('Invalid file type')
    ext = os.path.splitext(filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError('Invalid file extension')
    return True
```

#### Verification Steps
- [ ] All user inputs validated with schemas (Pydantic, marshmallow, etc.)
- [ ] File uploads restricted (size, type, extension)
- [ ] No direct use of user input in queries
- [ ] Whitelist validation (not blacklist)
- [ ] Error messages don't leak sensitive info

### 3. SQL Injection Prevention

#### FAIL: NEVER Concatenate SQL
```python
# DANGEROUS - SQL Injection vulnerability
query = f"SELECT * FROM users WHERE email = '{user_email}'"
cursor.execute(query)
```

#### PASS: ALWAYS Use Parameterized Queries
```python
# Safe - parameterized query
cursor.execute("SELECT * FROM users WHERE email = %s", (user_email,))

# Or with SQLAlchemy ORM
user = session.query(User).filter(User.email == user_email).first()
```

#### Verification Steps
- [ ] All database queries use parameterized queries or ORM
- [ ] No string concatenation or f-strings in SQL
- [ ] ORM used correctly (no raw SQL bypasses)
- [ ] Query builder used safely if not using ORM

### 4. Authentication & Authorization

#### Token Handling
```python
# FAIL: WRONG: storing tokens in localStorage (vulnerable to XSS)
# Do not return tokens in JSON responses that client-side JS can access

# PASS: CORRECT: httpOnly cookies
from http.cookies import SimpleCookie

response.set_cookie(
    "token", token,
    httponly=True,
    secure=True,
    samesite="Strict",
    max_age=3600
)
```

#### Authorization Checks
```python
def delete_user(user_id: str, requester_id: str):
    requester = db.get_user(requester_id)

    if requester.role != "admin":
        raise PermissionError("Unauthorized")

    # Proceed with deletion
    db.delete_user(user_id)
```

#### Row Level Security (PostgreSQL)
```sql
-- Enable RLS on all tables
ALTER TABLE users ENABLE ROW LEVEL SECURITY;

-- Users can only view their own data
CREATE POLICY "Users view own data"
  ON users FOR SELECT
  USING (auth.uid() = id);

-- Users can only update their own data
CREATE POLICY "Users update own data"
  ON users FOR UPDATE
  USING (auth.uid() = id);
```

#### Verification Steps
- [ ] Tokens stored in httpOnly cookies (not localStorage)
- [ ] Authorization checks before sensitive operations
- [ ] Row Level Security enabled where applicable
- [ ] Role-based access control implemented
- [ ] Session management secure

### 5. XSS Prevention

#### Sanitize HTML
```python
import bleach

def render_user_content(html: str) -> str:
    clean = bleach.clean(
        html,
        tags=['b', 'i', 'em', 'strong', 'p'],
        attributes={},
        strip=True
    )
    return clean
```

#### Content Security Policy
```python
# In your web framework response headers
CSP_HEADER = (
    "default-src 'self'; "
    "script-src 'self'; "
    "style-src 'self' 'unsafe-inline'; "
    "img-src 'self' data: https:; "
    "font-src 'self'; "
    "connect-src 'self' https://api.example.com"
)

# Add to all responses
response.headers["Content-Security-Policy"] = CSP_HEADER
```

#### Verification Steps
- [ ] User-provided HTML sanitized
- [ ] CSP headers configured
- [ ] No unvalidated dynamic content rendering
- [ ] Template engine auto-escaping enabled

### 6. CSRF Protection

#### CSRF Tokens
```python
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)

# Or manually verify CSRF tokens
def verify_csrf(token: str, session_token: str) -> bool:
    return hmac.compare_digest(token, session_token)
```

#### SameSite Cookies
```python
response.set_cookie(
    "session", session_id,
    httponly=True,
    secure=True,
    samesite="Strict"
)
```

#### Verification Steps
- [ ] CSRF tokens on state-changing operations
- [ ] SameSite=Strict on all cookies
- [ ] Double-submit cookie pattern implemented where needed

### 7. Rate Limiting

#### API Rate Limiting
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(app, key_func=get_remote_address)

# Apply to routes
@app.route("/api/data")
@limiter.limit("100/15minute")
def get_data():
    return data
```

#### Expensive Operations
```python
# Stricter limits for expensive operations
@app.route("/api/search")
@limiter.limit("10/minute")
def search():
    return search_results
```

#### Verification Steps
- [ ] Rate limiting on all API endpoints
- [ ] Stricter limits on expensive operations
- [ ] IP-based rate limiting
- [ ] User-based rate limiting (authenticated)

### 8. Sensitive Data Exposure

#### Logging
```python
# FAIL: WRONG: Logging sensitive data
print(f"User login: {email}, {password}")
print(f"Payment: {card_number}, {cvv}")

# PASS: CORRECT: Redact sensitive data
import logging
logger.info(f"User login: {email}, user_id={user_id}")
logger.info(f"Payment: last4={card[-4:]}, user_id={user_id}")
```

#### Error Messages
```python
# FAIL: WRONG: Exposing internal details
try:
    result = process_payment(data)
except Exception as e:
    return {"error": str(e), "traceback": traceback.format_exc()}, 500

# PASS: CORRECT: Generic error messages
try:
    result = process_payment(data)
except Exception as e:
    logger.exception("Payment processing failed")
    return {"error": "An error occurred. Please try again."}, 500
```

#### Verification Steps
- [ ] No passwords, tokens, or secrets in logs
- [ ] Error messages generic for users
- [ ] Detailed errors only in server logs
- [ ] No stack traces exposed to users

### 9. Dependency Security

#### Regular Updates
```bash
# Check for vulnerabilities
pip audit

# Or with safety
safety check

# Update dependencies
pip install --upgrade -r requirements.txt

# Check for outdated packages
pip list --outdated
```

#### Lock Files
```bash
# ALWAYS commit lock files
git add requirements.lock

# Or with pip-tools
pip-compile requirements.in
pip-sync requirements.txt

# Use exact versions in production
pip install -r requirements.txt
```

#### Verification Steps
- [ ] Dependencies up to date
- [ ] No known vulnerabilities (pip audit / safety check clean)
- [ ] Lock files committed
- [ ] Dependabot or similar enabled on GitHub
- [ ] Regular security updates

## Security Testing

### Automated Security Tests
```python
import pytest

def test_requires_authentication(client):
    response = client.get("/api/protected")
    assert response.status_code == 401

def test_requires_admin_role(client, auth_headers):
    response = client.get("/api/admin", headers=auth_headers["user"])
    assert response.status_code == 403

def test_rejects_invalid_input(client, auth_headers):
    response = client.post(
        "/api/users",
        json={"email": "not-an-email"},
        headers=auth_headers["admin"]
    )
    assert response.status_code == 400

def test_rate_limiting(client):
    for _ in range(101):
        response = client.get("/api/endpoint")
    assert response.status_code == 429
```

## Pre-Deployment Security Checklist

Before ANY production deployment:

- [ ] **Secrets**: No hardcoded secrets, all in env vars or secrets manager
- [ ] **Input Validation**: All user inputs validated
- [ ] **SQL Injection**: All queries parameterized
- [ ] **XSS**: User content sanitized
- [ ] **CSRF**: Protection enabled
- [ ] **Authentication**: Proper token handling
- [ ] **Authorization**: Role checks in place
- [ ] **Rate Limiting**: Enabled on all endpoints
- [ ] **HTTPS**: Enforced in production
- [ ] **Security Headers**: CSP, X-Frame-Options configured
- [ ] **Error Handling**: No sensitive data in errors
- [ ] **Logging**: No sensitive data logged
- [ ] **Dependencies**: Up to date, no vulnerabilities
- [ ] **CORS**: Properly configured
- [ ] **File Uploads**: Validated (size, type)

## Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Web Security Academy](https://portswigger.net/web-security)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)

---

**Remember**: Security is not optional. One vulnerability can compromise the entire platform. When in doubt, err on the side of caution.