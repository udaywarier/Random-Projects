from manage_connections import ManageConnections

db = ManageConnections()

def get_queue():
    cur = db.open_connection()
    cur.execute('SELECT * FROM PianoQueue')
    res = cur.fetchall()
    db.close_connection(cur)
    return res

def add_song_to_end(song_name, song_artist):
    cur = db.open_connection()
    cur.execute('INSERT INTO PianoQueue (SongName, SongArtist) VALUES (%s, %s)', (song_name, song_artist))
    db.close_connection(cur)
    return

def delete_song_by_id(song_id):
    cur = db.open_connection()
    cur.execute('DELETE FROM PianoQueue WHERE SongID=%s', (song_id, ))
    db.close_connection(cur)
    return