#!/usr/bin/env bash
# set up for web server deployment

sudo apt-get update
sudo apt-get install Nginx -y
sudo mkdir -p /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/
echo "Holbie" | sudo tee /data/web_static/releases/test/index.html
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
content="\\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}"
sudo sed -i "38i $content" /etc/nginx/sites-available/default
sudo service nginx restart
