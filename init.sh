sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn/test
sudo /etc/init.d/nginx restart
sudo gunicorn -c /etc/gunicorn.d/test hello:app
