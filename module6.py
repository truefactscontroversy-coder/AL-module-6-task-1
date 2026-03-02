from flask import Flask

app = Flask(__name__)

@app.route("/")

def welcome():
    return "welcome to my module 6 app for downloading and sorting csv files " \
           "this app also comes with a random file generator to fill an ftp server"

if __name__ == "__main__":
    app.run(port=5000, debug=False)
