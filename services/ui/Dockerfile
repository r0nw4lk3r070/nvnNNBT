FROM nginx:alpine

# Remove default nginx config
RUN rm /etc/nginx/conf.d/default.conf

# Install our proxy config
COPY nginx.conf /etc/nginx/conf.d/nvnnnbt.conf

# Static management pages
COPY agents.html /usr/share/nginx/html/agents.html
COPY index.html  /usr/share/nginx/html/index.html

EXPOSE 80
