# Simple API for the frond-end application(theme: games)
## Task

You can use any framework:
DjangoRestFramework, Flask, FastApi
Database - any, SQlite is also suitable for task

Data(Models):
1) Game 
  - description, data type - text
  - current stage number, data type - number
  - the end date of the stage, the data type - the text in date format ('dd.mm.yyy') or timestamp
  
  Note: The Game instance will be one (t.e one entry to the database)

Important: the data about the game should be cached.
Any changes in game information should update cache immediately

2) User
  - id, data type - number
  - Name, data type - text
  - Step 1, data type - boolean value
  - Step 2, data type - boolean value
  
  User and Game models are not connected

Functionality:
-Get user data from his ID and game (take from cache).
 GET request, response in JSON format, which will be data about a specific user and game

-Receive data separately only for the game (take from cache).
 GET request, response in JSON format, which will contain information about the game

- Add a new user.
POST request, JSON format

- Change user data by user’s ID
PUT request, JSON format. 
- Everything could be changed except id 

Advantage is:
- Autotests
- Auto Documentation

## Prerequisites
My test server is using Debian 10 as a host operating system.

Make sure you have installed all the following prerequisites on your development machine:
- Python - [Download & Install Python](https://www.python.org/downloads/).
- Redis - [Download & Install Redis](https://redis.io/docs/getting-started/installation/). 
- PostgreSQL - [Download & Install PostgreSQL](https://www.postgresql.org/download/).

You can also use package management systems like [Homebrew](https://brew.sh/), API etc.

For this project I used Python 3.7, Redis 7.0 and PostgreSQL 14.

Note:

1) Install these packages before installing python libraries from requirements.txt.
They are needed for properly working SQLAlchemy with PostgreSQL:

 ```bash
sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev
```

2) I assume that you have created a user for PostgreSQL and managed to connect it.

## Installation
Make sure that PostgreSQl and Redis are running.

First of all, clone the repository:

```bash
git clone https://github.com/MalyshevDenSer/insales_TA
```

Secondly, create database using PostgreSQL on localhost with any name. For example:

```bash
insales
```

After that create ```env.envs``` from ```env.sample``` in the project folder and fill it. 
You can find there tips which will be helpful.

```bash
# Use 1 for True and 0 for False
SQL_ECHO=0
# Fill in your details
POSTGRES_DB_URL=postgresql://username:password@host:port/database
```

Finally, run the application in the project folder:

```bash
uvicorn server:app --reload --host 0.0.0.0:8000
```

## Documentation

FastAPI autodocumentation you can find on ```http://127.0.0.1:8000/docs```
Here is the simple version of it:

### URLs:


1) ```/get_user_get_user_and_game_get``` - Getting user data by his ID and game(take from the cache)
2) ```/get_game``` - Receiving data about the game (take from the cache).
3) ```/add_user``` - Adding a new user. ID autogenerates.
4) ```/edit_user``` - Change user data by user’s ID. Chaning ID is not supported.

#### Additional URLs:

5) ```/update_game``` - Updating game by stage_number.
6) ```/add_the_game``` - Creating the game. Only 1 game is supported. 

All responses are sent in JSON format.