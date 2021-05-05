from flask import Flask, send_file, render_template
import cv2 as cv
from os import remove, mkdir
from shutil import rmtree
app = Flask(__name__)


@app.route('/')
def hello_world():
    img = cv.imread('testPic.jpg', 0)
    try:
        mkdir("temp")
    except:
        pass
    cv.imwrite('temp/edit3.jpg', img)
    return render_template("index.html")


@app.route("/download")
def download():
    try:
        return send_file("temp/edit3.jpg", as_attachment=True)
    except:
        return "Unable to Download"
    finally:
        rmtree("temp", ignore_errors=True)


if __name__ == "__main__":
    app.run(debug=True)
