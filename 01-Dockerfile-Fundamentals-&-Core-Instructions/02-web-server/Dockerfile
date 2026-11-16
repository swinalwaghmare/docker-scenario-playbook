FROM nginx:1.25-alpine

# Copy the HTML page
COPY index.html /usr/share/nginx/html/index.html

# Copy static assets
COPY assets/ /usr/share/nginx/html/assets/

# Document the port used by Nginx
EXPOSE 80

# No CMD required because the Nginx base image already provides one