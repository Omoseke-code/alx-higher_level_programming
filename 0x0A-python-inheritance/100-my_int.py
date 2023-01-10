#!/usr/bin/python3
"""100-my_int module"""


class MyInt(int):
    """MyInt that inherits from int"""
    def __eq__(self, other):
        """Overides and inverts == operator"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Overides and inverts != operator"""
        return int(self) == int(other)
