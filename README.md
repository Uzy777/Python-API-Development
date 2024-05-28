# Python-API-Development
 Python API Development - Comprehensive Course for Beginners


 Following this video course - https://www.youtube.com/watch?v=0sOvCWFmrtA


# Require
vscode

postman

postgresql


# Setup the following on initial
python -m venv venv

source venv/bin/activate


# Install the following packages (PIP)
pip install fastapi[all]
pip install psycopg2
pip install sqlalchemy


# Useful Commands for Startup
uvicorn app.main:app --reload

pgadmin4


# Postgres & PGAdmin - Arch Setup
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

Details in here - https://ravinderfzk.medium.com/install-postgresql-and-pgadmin4-in-arch-linux-eb013b45540f