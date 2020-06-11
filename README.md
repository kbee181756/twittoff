# twittoff

```sh
git clone 
cd twittoff
```

# Setup 
```sh
pipenv install
```

Migrate the database: 
```sh
FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade
```

# Usage
```sh
FLASK_APP=web_app flask run 
```

