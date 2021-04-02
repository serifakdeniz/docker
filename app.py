from flask import Flask

import os



app = Flask(__name__)



@app.route("/staj")

def hello():

    return "“Hello World from Kartaca!"





if __name__ == "__main__":

    port = int(os.environ.get("PORT", 4444))

    app.run(debug=True,host='0.0.0.0',port=port)

