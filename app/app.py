import os
from flask import Flask
import mysql.connector

app = Flask(__name__)

MYSQL_HOST = os.getenv('DB_HOST')
MYSQL_USER = os.getenv('DB_USER')
MYSQL_PASSWORD = os.getenv('DB_PASSWORD')
MYSQL_NAME = os.getenv('DB_NAME')

@app.route("/")
def mainpage():
    return "hello"

@app.route("/health")
def health_check():
    try:
        connection = mysql.connector.connect(
            host = MYSQL_HOST,
            database = MYSQL_NAME,
            user = MYSQL_USER,
            password = MYSQL_PASSWORD
        )
         
        connection.close()
        return "OK", 200

    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
