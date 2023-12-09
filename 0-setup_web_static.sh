#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static
sudo mkdir -p /data/web_static/releases/test/
sudo bash -c 'cat  >/data/web_static/releases/test/index.html <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF'
target="/data/web_static/releases/test/"
link_path="/data/web_static/current"
if [ -L "$link_path" ]; then
    sudo rm "$link_path"
fi
sudo ln -s "$target" "$link_path"
sudo chown -R ubuntu:ubuntu /data/

site_config="/etc/nginx/sites-enabled/mysite.conf"
web_static_path="/data/web_static/current/"
alias_path="/hbnb_static"
domain="souf.tech"
# Check if the configuration block already exists
touch "$site_config"
if ! grep -q "location $alias_path {" "$site_config"; then
    # Append the configuration block
    echo "server { 
        listen 80;
        server_name $domain;
        location $alias_path {
            alias $web_static_path;
        }

        # Additional Nginx configuration...

        # Include other configurations or server blocks if necessary.

        error_page 404 /404.html;
        location = /404.html {
            root /usr/share/nginx/html;
            internal;
        }
    }" > "$site_config"
fi

# Restart Nginx
sudo service nginx restart
