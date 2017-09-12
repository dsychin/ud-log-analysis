# Logs Analysis Project
### A Udacity Full Stack Web Developer Project

## Description
The aim of this project is to use python to run SQL queries to PostgreSQL
and answer a few questions by querying data from the database provided.

## Prerequisites
- PostgreSQL
- Python 3

## Instructions
### Preparation
1. Clone or download this repository.
2. Unzip to a folder of your choice.

### Database setup
1. Place newsdata.sql acquired from the course in your working directory.
2. Add the database to psql with the following command in your terminal:
```psql -d news -f newsdata.sql```

### Running the program
1. Navigate to where log_analysis.py is located.
2. Run the following command:
```python3 log_analysis.py```
or
```python log_analysis.py```
depending on how your python path is set up.

## Sample Output
```
What are the most popular three articles of all time?
        "Candidate is jerk, alleges rival" — 338647 views
        "Bears love berries, alleges bear" — 253801 views
        "Bad things gone, say good people" — 170098 views
Who are the most popular article authors of all time?
        "Ursula La Multa" — 507594 views
        "Rudolf von Treppenwitz" — 423457 views
        "Anonymous Contributor" — 170098 views
        "Markoff Chaney" — 84557 views
On which days did more than 1% of requests lead to errors?
        "July 17, 2016" — 2.3% errors
vagrant@vagrant:/vagrant/log_analysis$ python3 log_analysis.py
What are the most popular three articles of all time?
        "Candidate is jerk, alleges rival" — 338647 views
        "Bears love berries, alleges bear" — 253801 views
        "Bad things gone, say good people" — 170098 views
Who are the most popular article authors of all time?
        "Ursula La Multa" — 507594 views
        "Rudolf von Treppenwitz" — 423457 views
        "Anonymous Contributor" — 170098 views
        "Markoff Chaney" — 84557 views
On which days did more than 1% of requests lead to errors?
        "July 17, 2016" — 2.3% errors
```