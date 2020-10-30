# -*- coding: utf-8 -*-

class Point(object):

    def __init__(self, name, x, y, z=0):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Point(nr="{self.name}", x={self.x}, y={self.y}, z={self.z})'


