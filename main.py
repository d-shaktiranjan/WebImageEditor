from flask import Flask, send_file, render_template, request
from os import remove, mkdir, path
from shutil import rmtree
from werkzeug.utils import secure_filename
from filters import *

UPLOAD_FOLDER = 'temp'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        userFile = request.files['uFile']
        fileName = secure_filename(userFile.filename)
        userFile.save(path.join(app.config['UPLOAD_FOLDER'], fileName))
        getName = makeGray(fileName)
        return render_template("preview.html", name=getName)
    return render_template("index.html")


@app.route("/download/<string:name>")
def download(name):
    try:
        return send_file(f"temp/{name}", as_attachment=True)
    except:
        return "Unable to Download"
    finally:
        rmtree("temp", ignore_errors=True)


if __name__ == "__main__":
    app.run(debug=True)
