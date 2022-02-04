import flask

from playSong import songPlayer
from flask import Flask, render_template, Response
from camera import VideoCamera
from playlist import genPlaylist
import pandas as pd
app = Flask(__name__)
data=pd.DataFrame()
mood = ""


def gen(camera):
    i = 0
    pred = []
    while (i < 20):
        frame = camera.get_frame()[0]
        pred.append(camera.get_frame()[1])
        i += 1
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    global data
    global mood
    mood=[i for i in pred if i][-1]
    data= genPlaylist([i for i in pred if i][-1])[1]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result')
def result():
  return render_template('result.html', table=data.to_html(classes="table table-bordered  table-hover", index=False), mood=mood)

@app.route('/playSong')
def playSong():
    global data
    return flask.redirect(songPlayer(data))


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
