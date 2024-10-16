from lib.album import Album


class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        albums = []
        for row in rows:
            album = Album(
                row["id"], 
                row["title"], 
                row["release_year"], 
                row["artist_id"]
            )
            albums.append(album)
        return albums

    # Find a single album by its id
    def find(self, album_id):
        rows = self._connection.execute(
            'SELECT * from albums WHERE id = %s', [album_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])

    # Create a new album
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, album):
        self._connection.execute(
            'INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', 
            [album.title, album.release_year, album.artist_id]
        )
        return None

    # Delete an album by their artist_id
    def delete(self, artist_id):
        self._connection.execute(
            'DELETE FROM albums WHERE id = %s', 
            [artist_id]
        )
        return None 