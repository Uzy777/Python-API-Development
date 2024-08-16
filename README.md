# Python-API-Development
## Description
Python API Development - Comprehensive Course for Beginners

Following this course - [Python API Development](https://www.youtube.com/watch?v=0sOvCWFmrtA)


## Table of Contents
- [Description](#description)
- [Require](#require)
- [Pyenv Setup](#pyenv-setup-arch)
- [Bash Shell Setup](#bash-shell-setup)
- [Fish Shell Setup](#fish-shell-setup)
- [Pyenv](#pyenv)
- [Pyenv](#pyenv)
- [Pyenv](#pyenv)
- [Pyenv](#pyenv)
- [Pyenv](#pyenv)






## Require
```
sudo pacman -S vscode postman postgresql pyenv docker docker-compose
```


## Pyenv Setup (Arch)
```
sudo pacman -S --needed base-devel openssl zlib xz
curl https://pyenv.run | bash
```


## Bash Shell Setup

### add to .bashrc :
```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

if command -v pyenv 1>/dev/null 2>&1; then
   eval "$(pyenv init -)"
fi
```

### add to .bash_profile :
```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```


## Fish Shell Setup

### If you have Fish 3.2.0 or newer, execute this interactively:
```bash
set -Ux PYENV_ROOT $HOME/.pyenv
fish_add_path $PYENV_ROOT/bin
```

### Otherwise, execute the snippet below:
```bash
set -Ux PYENV_ROOT $HOME/.pyenv
set -U fish_user_paths $PYENV_ROOT/bin $fish_user_paths
```

### add to ~/.config/fish/config.fish :
```bash
pyenv init - | source
```


### Restart Shell:
```bash
exec "$SHELL"
```


## Pyenv
```
pyenv install 3.11.0
pyenv local 3.11.0
python -m venv venv
source venv/bin/activate   # bash
. venv/bin/activate.fish   # fish
python --version  
```


## Pip Packages or Pip Install requirements.txt
```
pip install fastapi[all] psycopg2 sqlalchemy pgadmin4 passlib[bcrypt] python-jose[cryptography] alembic
```
```
pip install -r requirements.txt
```


## Useful Commands for Startup
```
source venv/bin/activate   # bash
. venv/bin/activate.fish   # fish
deactivate
uvicorn app.main:app --reload
pgadmin4
```


## Postgres & PGAdmin - Arch Setup
```
sudo -u postgres -i
initdb --locale $LANG -E UTF8 -D '/var/lib/postgres/data/'
exit
sudo systemctl enable --now postgresql
psql -U postgres
postgres=# \password {password_here}
exit
sudo mkdir /var/lib/pgadmin
sudo mkdir /var/log/pgadmin
sudo chown $USER /var/lib/pgadmin
sudo chown $USER /var/log/pgadmin
pip install pgadmin4
pgadmin4
```

Details in here - https://ravinderfzk.medium.com/install-postgresql-and-pgadmin4-in-arch-linux-eb013b45540f


admin@admin.com
admin@123


## Ubuntu VM Setup
### 1. Setup Ubuntu Server VM. (Used QEMU & Virt Manager)
### 2. Setup Directories and Repo:
```
mkdir -p /home/ubuntu/app/src
cd /home/ubuntu/app/src
git clone https://github.com/Uzy777/Python-API-Development.git .
```
### 3. Install / Update Packages:
```
sudo apt update
sudo apt upgrade -y
sudo apt install python3 python3-pip postgresql postgresql-contrib nginx -y
```
### 4. Install Pip Packages:
```
sudo pip3 install virtualenv
```
### 5. Setup Postgresql:
```
psql -U postgres
postgres=# \password
```
#### 5-1. Configure /etc/postgresql/16/main/postgresql.conf
Add the following line in section "CONNECTIONS AND AUTHENTICATION" to allow all ip addresses to connect
 ```
listen_addresses '*'
```
#### 5-2. Configure /etc/postgresql/16/main/pg_hba.conf
Edit the connections section at the bottom to all every machine to connect
```
local    all   postgres             scram-sha-256
local    all   all                  scram-sha-256
host     all   all      0.0.0.0/0   scram-sha-256
host     all   all      ::/0        scram-sha-256
```
### 6. Setup Postgresql Continued...:
```
systemctl restart postgresql
psql -U postgres
```
Should now be able to connect using pgadmin interface
### 7. Virtualenv Setup:
```
cd /home/ubuntu/app
virtualenv venv
source venv/bin/activate
```
### 8. Virtualenv Pip Packages Install:
```
cd /home/ubuntu/app/src
pip install -r requirements.txt
```
### 9. Setup and Configure Environment Variables within /home/ubuntu/.env :
```
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=
DATABASE_NAME=fastapi
DATABASE_USERNAME=postgres
SECRET_KEY=
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=300
```
#### Add to the bottom of /home/ubuntu/.profile (autostart on reboot):
```
set -o allexport; source /home/ubuntu/.env; set +o allexport
```
```
reboot
```
### 10. Setup Alembic:
```
cd /home/ubuntu/app
source venv/bin/activate
cd src
alembic upgrade head
```
### 11. Setup systemctl for gunicorn within /etc/systemd/system/ from github repo:
```
sudo cp /home/ubuntu/app/src/gunicorn.service /etc/systemd/system/api.service
systemctl start api.service
systemctl enable api.service
systemctl status api.service
```
### 12. Setup Nginx and setup config within /etc/nginx/sites-available:
```
systemctl start nginx
```
```
location / {
   proxy_pass http://localhost:8000;
   proxy_http_version 1.1;
   proxy_set_header X-Real-IP $remote_addr;
   proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
   proxy_set_header Upgrade $http_upgrade;
   proxy_set_header Connection 'upgrade';
   proxy_set_header Host $http_host;
   proxy_set_header X-NginX-Proxy true;
   proxy_redirect off;
}
```
```
systemctl restart nginx
```
### 13. UFW Firewall Setup:
```bash
sudo ufw status
sudo ufw allow http
sudo ufw allow https
sudo ufw allow ssh
# sudo ufw allow 5432   (Use to connect in from outside)
sudo ufw enable
sudo ufw status
```

## Docker Setup
### 1. Start Docker Daemon:
```
sudo systemctl start docker.service
sudo systemctl enable docker.service
```
### 2. Add User to Docker Group:
```
sudo usermod -aG docker $USER
newgrp docker
```
### 3. Run Docker Build:
```
sudo docker build -t fastapi .
```
### 4. Run Docker Compose:
```bash
docker-compose up -d
# docker-compose down (Teardown docker build)
```

### x. Docker Useful Commands:
```
docker ps
docker exec -it {IMAGE NAME} bash
docker-compose -f docker-compose-dev.yml up -d
docker-compose -f docker-compose-dev.yml down
```