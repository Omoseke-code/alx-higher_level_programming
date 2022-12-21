#!/usr/bin/python3
""" Class Square that defines a square """


class Square:
    """ Class Square """
    def __init__(self, size=0, position=(0, 0)):
        """ Constructor """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Getter size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Getter position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter position """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Calculatre square area """
        return(self.__size * self.__size)

    def my_print(self):
        """ Print square """
        if self.size != 0:
            if self.position[1] != 0:
                print('\n' * self.position[1], end='')
            for ch in range(self.size):
                print(' ' * self.position[0], end='')
                print('#' * self.size)
        else:
            print()

    def __str__(self):
        """printable"""
        to_print = ''
        if self.size != 0:
            if self.position[1] is not 0:
                to_print += '\n' * self.position[1]
            for ch in range(self.size):
                to_print += ' ' * self.position[0]
                to_print += '#' * self.size
                if ch != self.__size - 1:
                    to_print += '\n'
        else:
            to_print = ''
        return str(to_print)
