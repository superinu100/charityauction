virtualenv -p python3 venv
source venv/bin/activate
cd backend
pip install -r ./requirements.txt
./manage.py migrate
cd ..
deactivate
cd frontend
yarn
yarn run build
cd ..
sudo cp -f ./configs/gunicorn.conf /etc/init/
sudo service gunicorn start
sudo yum -y install nginx
sudo cp -f ./configs/charibin /etc/nginx/sites-available
sudo ln -s /etc/nginx/sites-available/charibin /etc/nginx/sites-enabled/charibin
sudo service nginx restart