from flask import Flask, send_file, render_template
import cv2 as cv
app = Flask(__name__)


@app.route('/')
def hello_world():
    img = cv.imread('testPic.jpg', 0)
    cv.imwrite('temp/edit.jpg', img)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
