# Python-API-Development
## Description
Python API Development - Comprehensive Course for Beginners

Following this course - [Python API Development](https://www.youtube.com/watch?v=0sOvCWFmrtA)


## Table of Contents
- [Description](#description)
- [Useful Commands](#useful-commands)
- [Require (Arch)](#require-arch)
- [Pyenv Setup (Arch)](#pyenv-setup-arch)
- [Bash Shell Setup](#bash-shell-setup)
  - [Add to '.bashrc'](#add-to-bashrc)
  - [Add to '.bash_profile'](#add-to-bash_profile)
- [Fish Shell Setup](#fish-shell-setup)
  - [Fish 3.2.0 or newer, execute this interactively](#fish-320-or-newer-execute-this-interactively)
  - [Otherwise execute below](#otherwise-execute-below)
  - [Add to '~/.config/fish/config.fish'](#add-to-configfishconfigfish)
  - [Restart Shell](#restart-shell)
- [Pyenv Final Setup](#pyenv-final-setup)
- [Pip Install 'requirements.txt'](#pip-install-requirementstxt)
- [Postgres & PGAdmin (Arch)](#postgres--pgadmin-arch)
- [Ubuntu VM Setup](#ubuntu-vm-setup)
  - [1. Setup Ubuntu Server VM. (Used QEMU & Virt Manager)](#1-setup-ubuntu-server-vm-used-qemu--virt-manager)
  - [2. Setup Directories and Repo](#2-setup-directories-and-repo)
  - [3. Install / Update Packages](#3-install--update-packages)
  - [4. Install Pip Package](#4-install-pip-package)
  - [5. Setup Postgresql](#5-setup-postgresql)
    - [5-1. Configure '/etc/postgresql/16/main/postgresql.conf'](#5-1-configure-etcpostgresql16mainpostgresqlconf)
    - [5-2. Configure '/etc/postgresql/16/main/pg_hba.conf'](#5-2-configure-etcpostgresql16mainpg_hbaconf)
  - [6. Setup Postgresql Continued...](#6-setup-postgresql-continued)
  - [7. Virtualenv Setup](#7-virtualenv-setup)
  - [8. Pip Install 'requirements.txt'](#8-pip-install-requirementstxt)
  - [9. Setup and Configure Environment Variables within '/home/ubuntu/.env'](#9-setup-and-configure-environment-variables-within-homeubuntuenv)
    - [Add to the bottom of '/home/ubuntu/.profile' (autostart on reboot)](#add-to-the-bottom-of-homeubuntuprofile-autostart-on-reboot)
  - [10. Setup Alembic](#10-setup-alembic)
  - [11. Setup systemctl for gunicorn within '/etc/systemd/system/'](#11-setup-systemctl-for-gunicorn-within-etcsystemdsystem)
  - [12. Setup Nginx and setup config within '/etc/nginx/sites-available'](#12-setup-nginx-and-setup-config-within-etcnginxsites-available)
  - [13. UFW Firewall Configuration](#13-ufw-firewall-configuration)
- [Docker Setup (Arch)](#docker-setup-arch)
  - [1. Start Docker Daemon](#1-start-docker-daemon)
  - [2. Add User to Docker Group](#2-add-user-to-docker-group)
  - [3. Run Docker Build](#3-run-docker-build)
  - [4. Run Docker Compose](#4-run-docker-compose)


## Useful Commands
```shell
source venv/bin/activate   # bash
. venv/bin/activate.fish   # fish
deactivate
uvicorn app.main:app --reload
pgadmin4
docker ps
docker exec -it {IMAGE NAME} bash
docker-compose -f docker-compose-dev.yml up -d
docker-compose -f docker-compose-dev.yml down
pytest -v
pytest --disable-warnings -v
```


## Require (Arch)
```shell
sudo pacman -S vscode postman postgresql pyenv docker docker-compose
```


## Pyenv Setup (Arch)
```shell
sudo pacman -S --needed base-devel openssl zlib xz
curl https://pyenv.run | bash
```


## Bash Shell Setup
### Add to '.bashrc'
```shell
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

### Add to '.bash_profile'
```shell
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```


## Fish Shell Setup
### Fish 3.2.0 or newer, execute this interactively
```shell
set -Ux PYENV_ROOT $HOME/.pyenv
fish_add_path $PYENV_ROOT/bin
```

### Otherwise execute below
```shell
set -Ux PYENV_ROOT $HOME/.pyenv
set -U fish_user_paths $PYENV_ROOT/bin $fish_user_paths
```

### Add to '~/.config/fish/config.fish' 
```shell
pyenv init - | source
```

### Restart Shell
```shell
exec "$SHELL"
```


## Pyenv Final Setup
```shell
pyenv install 3.11.0
pyenv local 3.11.0
python -m venv venv
source venv/bin/activate   # bash
. venv/bin/activate.fish   # fish
python --version  
```


## Pip Install 'requirements.txt'
```shell
pip install -r requirements.txt
```


## Postgres & PGAdmin (Arch)
```shell
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

### 2. Setup Directories and Repo
```shell
mkdir -p /home/ubuntu/app/src
cd /home/ubuntu/app/src
git clone https://github.com/Uzy777/Python-API-Development.git .
```

### 3. Install / Update Packages
```shell
sudo apt update
sudo apt upgrade -y
sudo apt install python3 python3-pip postgresql postgresql-contrib nginx -y
```

### 4. Install Pip Package
```shell
sudo pip3 install virtualenv
```

### 5. Setup Postgresql
```shell
psql -U postgres
postgres=# \password
```

#### 5-1. Configure '/etc/postgresql/16/main/postgresql.conf'
Add the following line in section "CONNECTIONS AND AUTHENTICATION" to allow all ip addresses to connect
 ```
listen_addresses '*'
```

#### 5-2. Configure '/etc/postgresql/16/main/pg_hba.conf'
Edit the connections section at the bottom to all every machine to connect
```
local    all   postgres             scram-sha-256
local    all   all                  scram-sha-256
host     all   all      0.0.0.0/0   scram-sha-256
host     all   all      ::/0        scram-sha-256
```

### 6. Setup Postgresql Continued...
```shell
systemctl restart postgresql
psql -U postgres
```
Should now be able to connect using pgadmin interface

### 7. Virtualenv Setup
```shell
cd /home/ubuntu/app
virtualenv venv
source venv/bin/activate
```

### 8. Pip Install 'requirements.txt'
```shell
cd /home/ubuntu/app/src
pip install -r requirements.txt
```

### 9. Setup and Configure Environment Variables within '/home/ubuntu/.env'
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

#### Add to the bottom of '/home/ubuntu/.profile' (autostart on reboot)
```
set -o allexport; source /home/ubuntu/.env; set +o allexport
```

```shell
reboot
```

### 10. Setup Alembic
```shell
cd /home/ubuntu/app
source venv/bin/activate
cd src
alembic upgrade head
```

### 11. Setup systemctl for gunicorn within '/etc/systemd/system/'
```shell
sudo cp /home/ubuntu/app/src/gunicorn.service /etc/systemd/system/api.service
systemctl start api.service
systemctl enable api.service
systemctl status api.service
```

### 12. Setup Nginx and setup config within '/etc/nginx/sites-available'
```shell
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

```shell
systemctl restart nginx
```

### 13. UFW Firewall Configuration
```shell
sudo ufw status
sudo ufw allow http
sudo ufw allow https
sudo ufw allow ssh
# sudo ufw allow 5432   (Use to connect in from outside)
sudo ufw enable
sudo ufw status
```

## Docker Setup (Arch)
### 1. Start Docker Daemon
```shell
sudo systemctl start docker.service
sudo systemctl enable docker.service
```

### 2. Add User to Docker Group
```shell
sudo usermod -aG docker $USER
newgrp docker
```

### 3. Run Docker Build
```shell
sudo docker build -t fastapi .
```

### 4. Run Docker Compose
```shell
docker-compose up -d
# docker-compose down (Teardown docker build)
```