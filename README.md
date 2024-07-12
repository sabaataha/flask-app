
# SQLAlchemy & Alembic
Manage your database efficiently through `SQLAlchemy` and `Alembic`.


* create a Python virtual environment and install all the required packages
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
* initialize Alembic
```bash
alembic init alembic
```
* edit the `alembic.ini` file and proivide your database URL and mode.
* create migration
```bash
alembic revision --autogenerate -m "YOUR COMMENT"
```
* push the migration to database
```bash
alembic upgrade head
```
