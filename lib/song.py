class Song:
    count = 0
    genres =[]
    artists =[]
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)
        self.add_to_genre_count(self.genre)
        self.add_to_artist_count(self.artist)

    def __repr__(self):
        return f"{self.artist}"
        
    @classmethod
    def add_song_to_count(cls,increment = 1):
        cls.count += increment
        return cls.count
    
    @classmethod
    def add_to_genres(cls,genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_artist_count(cls, artist):
        # class-level dictionary (artist_count) where:
        # Key = artist name (e.g. "Adele")
        # Value = number of songs by that artist (e.g. 2)
        if artist in cls.artist_count: #if in dict -> add one
            cls.artist_count[artist] += 1
        else:
            # the first song by this artist.
            cls.artist_count[artist] = 1
        
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
           cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
        

song1 = Song("99 Problems", "Jay Z", "Rap")
song2 = Song("Hey Ya!", "Outkast", "Rap")
song3 = Song("Someone Like You", "Adele", "Pop")
song4 = Song("Lose Yourself", "Eminem", "Rap")
song5 = Song("Rolling in the Deep", "Adele", "Pop")

print(Song.artists)
print(Song.artist_count)
print(Song.genre_count)



