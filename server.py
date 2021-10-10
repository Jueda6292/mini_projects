import csv
from flask import Flask, render_template, request
app = Flask(__name__)

DATABASE = 'data.csv'

def read_csv():
    payload = []
    with open(DATABASE, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            payload.append(row)
    return payload

def write_to_csv(data):
    with open(DATABASE, 'a', newline = '\n') as csvfile:
        writer = csv.DictWriter(csvfile, data.keys())
        writer.writerow(data)
    return 'success'

music_collection = read_csv()
print ('I love music', music_collection)

@app.route('/music/')
def music_collection_index():
    return render_template('index.html', music_collection=music_collection, title='Music collection')

@app.route('/music/<song_id>')
def music_collection_show(song_id):
    for song in music_collection:
        if song['id'] == song_id:
            return render_template('show.html', song=song)
    return 'Not Found', 404

@app.route('/music/', methods=['POST'])
def music_collection_create():
    new_music = request.get_json()
    new_music['id'] = len(music_collection) + 1
    music_collection.append(new_music)

app.run()
