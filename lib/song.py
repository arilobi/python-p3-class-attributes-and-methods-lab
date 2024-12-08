class Song:
    
    count = 0
    # when using set, it helps to not get any duplicates
    genres = set()  
    artists = set()  
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre): 
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment song
        Song.add_song_to_count()

        # Adding to genres and update genre count
        Song.add_to_genres(genre)
        Song.add_to_genre_count(genre)

        # Adding to artists and update artist count
        Song.add_to_artists(artist)
        Song.add_to_artist_count(artist)

    # using class methods
    @classmethod
    def add_song_to_count(cls): 
        cls.count += 1  

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.add(genre)  

    @classmethod
    def add_to_artists(cls, artist): 
        cls.artists.add(artist)  

    @classmethod
    def add_to_genre_count(cls, genre):
        # if a genre is inside the genre_count, it will increment itself by one but if it isn't there, it will add itself by 1
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else: 
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else: 
            cls.artist_count[artist] = 1
