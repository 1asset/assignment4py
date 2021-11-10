# Assignment 4 SE-2004 (Asset Kanatov, Dias Karibaev, Yeskendir Iskakov)
Writing program to input a coin name into text field, displaying a list of paragraphs and storing parsed news & blogs in the database (almost like how we did with Assignment 2, but now connected with SQL).
# Installation
Before starting to use the code you must install required packages and modules. All packages and libraries will be provided in requirements.txt file, that is uploaded in the repository. Basically, you'll need the packages that are provided below:
```
flask (https://flask.palletsprojects.com/en/2.0.x/)
flask_sqlalchemy (https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
requests  (https://pypi.org/project/requests/)
beautifulSoup (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask
```
# Usage
At first we need to create a database in DBMS application(SQL server,Pgadmin) or other database management system. After that, you need to successfully connect your server with the database. We called our database "assignment4" as it is shown in the code. Also, it's important to know the login and password of your database, ours is postgres and 5432.
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:5432@localhost/flask'
```
The next step is to create a table in your new database, the database name is assignment4.
```
CREATE TABLE Paragraphs (
id INTEGER PRIMARY KEY,
coin_name VARCHAR,
title VARCHAR,
body VARCHAR, 
link VARCHAR
)
```
Further step is to run main.py file, you'll get the IP-address in the terminal that you need to follow, after following it, you need to add /coin after this address. 
```
http://127.0.0.1:5000/coin
```
Then you will see the page with the input field and one button, here you need to input the existing coin from the coin market, for example Bitcoin. It will afterwards output some articles, news, paragraphs regarding this coin. Also, all the parsed information will be stored in the database.

# Examples
At the beggining you will have an empty page, except the input field and the check button. You need to enter the coin.
![1](https://user-images.githubusercontent.com/82859085/141158434-d9e2920f-cc20-4ec9-9b7b-e022bbcef0b7.PNG)








