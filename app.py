from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("home.html")


@app.route("/upload", methods=["GET" , "POST"])
def upload():

    if request.method == "POST":

        dataset = request.files["dataset"]
        print(dataset.filename)
        
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)