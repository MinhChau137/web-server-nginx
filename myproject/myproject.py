from crypt import methods
from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
app = Flask(__name__, template_folder='templates')
import mysql.connector

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'mc'
app.config['MYSQL_PASSWORD'] = '1234567890'
app.config['MYSQL_DB'] = 'users'

mysql = MySQL(app)

@app.route("/", methods = ['GET', 'POST'])
def index():
    # if request.method == 'GET':
    #     cur = mysql.connection.cursor()
    #     cur.execute("SHOW DATABASE")
    #     for db in cur:
    #         print(db)
    #     mysql.connection.commit()
    #     return render_template('get.html')

    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s);", (firstName, lastName))
        cur.close()
        mysql.connection.commit()
        return 'success'
        # return render_template('get.html')
    return render_template("post.html")
    # return ("<h1>{}</h1>").format(details['fname'])


# def hello():
#     return ("<h1>hello</h1>")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

