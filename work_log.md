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

