'''
Provided a text file with information about artists and songs:
Joy Division - Love Will Tear Us Apart
Joy Division - New Dawn Fades
Pixies - Where Is My Mind
Pixies - Hey
Genesis - Mama

Write the required classes so the following code works:
music = MusicFile('/Users/ynonperek/music.txt')
print(music.artist('Joy Division').songs)
'''


class MusicFile:

    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'r') as f:
            return f.read().split('\n')

    def artist(self, name):
        artist_obj = Artist(name)
        artist_obj.songs = [item.split(' - ')[1] for item in self.read() if name in item]
        return artist_obj


class Artist:

    def __init__(self, artist):
        self.artist = artist


#music = MusicFile('.\\music.txt')
#sprint(music.artist('Joy Division').songs)




class A:
    def __init__(self, a):
        self.a = a

class B(A):
    def __init__(self, a, b):
        super().__init__(a)

        self._b = b

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        print('setter')
        self._b = value

    def __str__(self):
        return f"Obj of class {self.__class__}; attrs: {self.__dict__}"

    def __repr__(self):
        return "My B class"

    def __add__(self, other):
        return f"sum of B and {other}"

    def __call__(self, *args, **kwargs):
        return f"obj has been called"