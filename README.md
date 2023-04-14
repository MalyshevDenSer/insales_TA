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
Make sure you have installed all the following prerequisites on your development machine:
- Python - [Download & Install Python](https://www.python.org/downloads/).
- Redis - [Download & Install Redis](https://redis.io/docs/getting-started/installation/). 
- PostgreSQL - [Download & Install PostgreSQL](https://www.postgresql.org/download/).

You can also use package management systems like [Homebrew](https://brew.sh/), API etc.

For this project I used Python 3.11, Redis 7.0 and PostgreSQL 14.

## Installation



