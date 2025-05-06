from flask import Flask

app = Flask(__name__)

app.route("/")
def home():
  return "Hello, Welcome to my simple GAE application for LP2 Practical!"

if __name__ == "__main__":
  app.run()
