from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)

@app.route("/")
def home():

    return render_template("home.html")


@app.route("/upload", methods=["GET" , "POST"])
def upload():

    if request.method == "POST":

        dataset = request.files["dataset"]
        print(dataset.filename)

        df = pd.read_csv(dataset)

        print(df.head(10))
        
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)