# Python-API-Development
 Python API Development - Comprehensive Course for Beginners
 Following this video course - https://www.youtube.com/watch?v=0sOvCWFmrtA


# Require
```
sudo pacman -S vscode postman postgresql pyenv
```


# Pyenv Setup
```
sudo pacman -S --needed base-devel openssl zlib xz
curl https://pyenv.run | bash
```


# Bash Shell Setup

## add to .bashrc
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

## add to .bash_profile
```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```


# Fish Shell Setup

## If you have Fish 3.2.0 or newer, execute this interactively:
```bash
set -Ux PYENV_ROOT $HOME/.pyenv
fish_add_path $PYENV_ROOT/bin
```

## Otherwise, execute the snippet below:
```bash
set -Ux PYENV_ROOT $HOME/.pyenv
set -U fish_user_paths $PYENV_ROOT/bin $fish_user_paths
```

## add to ~/.config/fish/config.fish
```bash
pyenv init - | source
```


# Restart Shell
```bash
exec "$SHELL"
```


# Pyenv
```
pyenv install 3.11.0
pyenv local 3.11.0
python -m venv venv
source venv/bin/activate   # bash
. venv/bin/activate.fish   # fish
python --version  
```


# Pip Packages
```
pip install fastapi[all] psycopg2 sqlalchemy pgadmin4 passlib[bcrypt] python-jose[cryptography] alembic
```


# Useful Commands for Startup
```
source venv/bin/activate   # bash
. venv/bin/activate.fish   # fish
deactivate
uvicorn app.main:app --reload
pgadmin4
```


# Postgres & PGAdmin - Arch Setup
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