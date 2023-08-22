class Bicycle:
    '''
    Definiert ein Fahrrad mit einigen wenigen Attributen und Methoden.
    '''

    def __init__(self, type='mountenbike', size=48, color='gray'):
        '''
        Konstruktor initialisiert das Objekt mit 3 Parameterwerten.
        '''
        self.type = type
        self.size = size
        self.color = color

    @property
    def type(self):
        '''
        Liefert den Typ des Fahrrads
        '''
        return self._type

    @property
    def size(self):
        '''
        Liefert die Grösse des Fahrrads
        '''
        return self._size

    @property
    def color(self):
        '''
        Liefert die Farbe des Fahrrads
        '''
        return self._color

    @type.setter
    def type(self, type):
        '''
        Legt den Typ des Fahrrads fest
        '''
        self._type = type

    @size.setter
    def size(self, size):
        '''
        Legt die Grösse des Fahrrads fest
        '''
        self._size = size

    @color.setter
    def color(self, color):
        '''
        Legt die Farbe des Fahrrads fest
        '''
        self._color = color

    def print(self):
        print(
            f'Fahrrad:\n\tArt:            {self._type}\n\tRahmengrösse:   {self._size}\n\tFarbe:          {self._color}')


if __name__ == "__main__":
    # Aufgabe 1
    bicycle = Bicycle()
    bicycle.print()
    #
    bicycle = Bicycle(type='racebike')
    bicycle.print()
    #
    bicycle = Bicycle(type='citybike', size='42')
    bicycle.print()
    #
    # Aufgabe 2
    #
    bicycle.color = 'red'
    bicycle.print()
