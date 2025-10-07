# Work log
This is a day by day progession of my project detailing the main things I did from the start to completion. Each day will include what I did and new things that I learnt and any challenges.

## Day 1
**Did** 
* Setup stuff
    * Setup virtual environment
    * installed postgresql
    * created requirements.txt.
* Designed database schema
* Created SQLAlchemy models with relationships
* Connected to PostgreSQL
* Inserted a song
* First flask endpoint setup (adding to tracks table)
* Added to database with curl

**Learnt** 
* Dependency management using requirements.txt
* How to create models with SQLAlchemy
* How to use flask to create endpoints
* How to use flask to populate PostgreSQL database tables
* How to use curl to add to database

**Challenges** 
* psql was not a recognized command, had to PostgreSQL bin folder to PATH.
* Initially got "relation tracks does not exist", forgot to call create_all() before querying.

## Day 2
**Did**
* Implemented CRUD requests for tracks
* Implemented input validation
* Started writing README
**Learnt**
* How to get information from a curl url
* Basic format for SQLAlchemy CRUD requests
**Challenges**
* Remembering what one is post and what one is get HAHA
* Tried to declare functions with duplicate decorators, refactored to do them in the same function

## Day 3 (Took a few days off between)
**Did**
* README Done
* Implemented tag functionality
**Learnt**
* How to use many to many relationships in SQLAlchemy

