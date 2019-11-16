import json
import random
from flask import Flask, render_template
from flask import request
tags = {
        "beatles": {'tag': 'beatles', "songs": "6 songs"},
        "rock": {'tag': 'rock', "songs": "23 songs"},
        "uk": {'tag': 'uk', "songs": "23 songs"},
        }

groups = {
        "beatles": {"group": "beatles", "albums": ["001","003"]},
        "beach_boys": {"group": "Beach Boys", "albums": ["002"]},
        "uk": {"group": "UK", "albums": ["001","002","003"]},
        }


albums = {
"001": {'id': "001", 'title': "The Beatles, ‘Sgt. Pepper’s Lonely Hearts Club Band'",
            'cover': "https://www.rollingstone.com/wp-content/uploads/2018/06/sgt-peppers-e4860c12-4da1-4e6d-bb86-81698a88dbde.jpg?resize=1240,1240&w=385"},
"002": {'id': "002", 'title': "The Beach Boys, ‘Pet Sounds’",
            'cover': "https://www.rollingstone.com/wp-content/uploads/2018/06/rs-136791-eafbc592120358b4d3d14cda5acebf62ae50a522.jpg?resize=1240,1240&w=385"},
"003": {'id': "003", 'title': "The Beatles, ‘Revolver’ ",
            'cover': "https://www.rollingstone.com/wp-content/uploads/2018/06/rs-136792-daa031ec00ad83a2da305fe583d746d030fa46ca.jpg?resize=1240,1240&w=385"},
}

playlists = {
    "001": {
        'id': "001", "title": "Sgt. Pepper’s Lonely Hearts Club Band",
        "tracks": ["Sgt. Pepper's Lonely Hearts Club Band", "With A Little Help From My Friends",
                   "Lucy In The Sky With Diamonds", "Getting Better", "Fixing A Hole"]},
    "002": {
        'id': "002", "title": "Pet Sounds",
        "tracks": ["Wouldn't It Be Nice", "You Still Believe In Me", "That's Not Me",
                   "Don't Talk,I'm Waiting For The Day", "Let's Go Away For A While"]},
    "003": {
        'id': "003", "title": "Revolver",
        "tracks": ["Taxman", "Eleanor Rigby", "I'm Only Sleeping", "Love You To", "Here", "There And Everywhere",
                   "Yellow Submarine"]},
}

with open("data.json", "r") as album_file:
    all_albums = json.load(album_file)


app = Flask(__name__)

# печать рандомных 9
# @app.route('/')
# def main():
#     sample_size = 9
#     sorted_sample = [all_albums[i] for i in sorted(random.sample(range(len(all_albums)), sample_size))]
#     return render_template('index.html', tags = tags, groups=groups,all_albums=all_albums, sorted_sample=sorted_sample)

@app.route('/')
def main():
    sorted_sample = all_albums[0:10]
    return render_template('index.html', tags=tags, groups=groups, all_albums=all_albums,sorted_sample=sorted_sample)

@app.route('/search')
def search():
    return "Выполняем поиск по строке "+request.values.get("s")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/albums')
def list_albums():
    return render_template('all_albums.html', all_albums=all_albums)


@app.route('/albums/<id>')
def get_album(id):
    id = int(id)
    album = all_albums[id-1]
    return render_template('album.html', album=album)




@app.route('/genres/<genre>')
def the_group(genre):
    for album in all_albums:
        if genre == album['genre']:
            album['genre'] = list()
        return render_template('groups.html', all_albums=all_albums, genre=list())

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == '__main__':
    app.run()

