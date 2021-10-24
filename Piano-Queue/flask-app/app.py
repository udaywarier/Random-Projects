from flask import Flask, render_template, request
import db_connector, json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    lst = db_connector.get_queue()
    return render_template('queue.html', lst=lst)

@app.route('/addToQueue', methods = ['POST'])
def add_to_queue():
    payload = json.loads(request.form['json'])
    song_name = str(payload['song_name'])
    song_artist = str(payload['song_artist'])
    db_connector.add_song_to_end(song_name, song_artist)
    return 'Everything worked, yay! Song was added! Reload the queue home page to see the changes!'

@app.route('/deleteFromQueue', methods = ['POST'])
def delete_from_queue():
    payload = json.loads(request.form['json'])
    song_id = int(payload['song_id'])
    db_connector.delete_song_by_id(song_id)
    return 'Everything worked, yay! Song was deleted! Reload the queue home page to see the changes!'