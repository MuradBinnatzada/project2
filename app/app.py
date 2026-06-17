import os
from flask import Flask

app = Flask(__name__)

MYSQL_HOST = os.getenv('DB_HOST')
MYSQL_USER = os.getenv('DB_USER')
MYSQL_PASSWORD = os.getenv('DB_PASSWORD')

@app.route("/")
def mainpage():
  return "hello"

@app.route("/health")
def health_check():
  return "OK", 200

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
