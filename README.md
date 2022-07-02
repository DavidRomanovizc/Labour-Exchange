# Labour Exchange

> A project created for educational purposes. REST API labor exchange on FastAPI with Docker. Also in this project I implemented authentication using JWT tokens

## 🎨 Used technology

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![FASTAPI](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![PSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## 📝 Installation
#### First check if you have Python installed

Before installing this DatingBot-project you need to check if you have python\
To check if you have python installed, run this command in your terminal:

```sh
python -V
```

If you get an answer like this, it means that `Python` is installed.

```sh
Python 3.9.5
```

#### Fork the Labour-Exchange

```sh
https://github.com/DavidRomanovizc/Labour-Exchange
```

#### And install requirements.txt
```sh
pip install -r requirements.txt
```

## 🔨 Environment variables
File `.env.dist` rename to `.env` and then put your data in the url
```env
EE_DATABASE_URL="postgresql://PG_USER:PG_PASSWORD@PG_HOST:PG_PORT/PG_NAME"
```
PG_USER - username of the database owner
PG_PASSWORD - password from the database
PG_HOST - IP address of the database
PG_NAME - database name

File `core/config.py`
```py
SECRET_KEY = config("EE_SECRET_KEY", cast=str,
                    default="TOKEN")
```
TOKEN generated using the command 
```sh
openssl rand -hex 32
```
![image](https://user-images.githubusercontent.com/72649244/176979577-affe5405-2120-43f4-b619-63ca28755b2e.png)
