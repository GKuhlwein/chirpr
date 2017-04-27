# Chirpr

This is the skeleton of a Twitter clone project!

## Install Python 3 and Sqlite3

The project will require Python 3. Please install Python 3.5 and make sure the appropriate version of pip is available
from the command line. 

Alse Sqlite 3 will be needed.

Some of these instructions have not been tested on Windows. You may have a better experience if you use Git Bash
instead of CMD.

## Fork and clone repo

1. Log into GitHub
1. Click the fork button [here](https://github.com/ewilson/chirpr)
1. Execute `git clone https://github.com/ewilson/chirpr.git` in the terminal, in the directory you want the project to be.

## Install dependencies in virtualenvironment

Execute the following commands in PowerShell or Bash

1. `cd chirpr`
1. `pyvenv venv`
1. `source venv/bin/activate`
1. `pip3 install -r requirements.txt`

## Running the application

    $ python chirpr.py

Now navigate to [localhost:5000](http://localhost:5000/) to verify that it is running locally. 

## DB setup

To set up the test database, run

    $ ./init_db.py

To set up an empty database, without example data, run

    $ ./init_db.py new

## DB Migrations

When you need to make changes to the DB structure -- suppose you add a column to a table --
you will need to add a migration script to `data/migrations`. This scripts should follow a naming
convention like follows:

- `01_Example_change.sql`
- `02_Another_change.sql`

This series of scripts should allow another user to run `data/db_migrate.py` in order to transform
the test database into the structure that your changes require.

It will be common for changes to the application to require changes to the database structure.

## Trello and Pull requests 

Here is an outline of our workflow.

1. We discuss the card in Trello that you will implement next. We will try at this point
to resolve confusions about the requirements. This card will then be moved to the "Doing" column
in Trello.

2. You implement and test the feature. Asking questions during this step may be useful.

3. When you think the feature is done, move the Trello card to the "Review" column, and open a
Pull Request. A Pull Request is a GitHub feature that will allow for me to see and comment on your
changes.

4. I will give comments on the things that need to be improved, both in code style and in defects
discovered. You will need to fix these issues and push them to your pull request branch.

5. When I am satisfied that the feature is complete, I will merge your code, and the card is moved to done.
We now return to step 1.

## Useful documentation

- [Flask](http://flask.pocoo.org/docs/0.11/)
- [Jinja2](http://jinja.pocoo.org/docs/dev/)
- [Sqlite](https://sqlite.org/docs.html)
- [Python DB-API interface for SQLite](https://docs.python.org/3/library/sqlite3.html)
