tags = {
        "beatles": {'tag': 'beatles', "songs": "6 songs"},
        "rock": {'tag': 'rock', "songs": "23 songs"},
        "uk": {'tag': 'uk', "songs": "23 songs"},
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

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', tags = tags, albums = albums)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/albums')
def list_albums():
    return render_template('albums.html', albums=albums)


@app.route('/albums/<id>')
def get_album(id):
    playlist = playlists.get(id)
    return render_template('playlists.html', playlist=playlist, albums = albums)



@app.route('/tags/<tag>')
def the_tag(tag):
    tag = tags.get(tag)
    return render_template('tags.html', tag=tag)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


app.run()
