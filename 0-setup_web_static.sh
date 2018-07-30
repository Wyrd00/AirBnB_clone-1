#!/usr/bin/env bash
# set up for web server deployment

sudo apt-get -y update
sudo apt-get install -y Nginx
sudo mkdir -p /data/ /data/web_static/ /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/
echo "Holbie" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
content="location /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}"
sudo sed -i "39i $content" /etc/nginx/sites-available/default
sudo service nginx restart
