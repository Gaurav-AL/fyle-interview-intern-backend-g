# Fyle Backend Challenge
## Installation

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below

### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset DB for windows

```
set FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```
### Start Server for windows

```
flask run
```
### Run Tests

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov=core/
# open htmlcov/index.html

```
