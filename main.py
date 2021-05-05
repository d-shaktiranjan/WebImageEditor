from flask import Flask, send_file, render_template
import cv2 as cv
app = Flask(__name__)


@app.route('/')
def hello_world():
    img = cv.imread('testPic.jpg', 0)
    cv.imwrite('temp/edit.jpg', img)
    return render_template("index.html")


@app.route("/download")
def download():
    return send_file("temp/edit.jpg", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
