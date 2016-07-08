# -*- coding: utf-8 -*-

import unittest

from minecrafttools.colorsmap      import ColorsMap
from minecrafttools.intcoordinates import IntCoordinates
from minecrafttools.intdimensions  import IntDimensions
from minecrafttools.minecraftmap   import MinecraftMap

class TestMinecraftMap(unittest.TestCase):

    def setUp(self):
        self.testCoordinates = IntCoordinates(-125, 367)
        self.testDimensions  = IntDimensions(2, 3)
        self.testSubject     = MinecraftMap(
            0,
            self.testCoordinates,
            ColorsMap(
                self.testDimensions,
                2,
                [0, 1, 2, 3, 4, 5]
            )
        )

    def test_coordinates(self):
        # longitude
        self.assertEqual(
            self.testCoordinates.longitude(),
            self.testSubject.coordinates().longitude()
        )
        # latitude
        self.assertEqual(
            self.testCoordinates.latitude(),
            self.testSubject.coordinates().latitude()
        )

    def test_dimensions(self):
        # height
        self.assertEqual(
            self.testDimensions.height(),
            self.testSubject.dimensions().height()
        )
        # width
        self.assertEqual(
            self.testDimensions.width(),
            self.testSubject.dimensions().width()
        )

    def test_id(self):
        pass

    def test_scale(self):
        self.assertEqual(2, self.testSubject.scale())

if __name__ == '__main__':
    unittest.main()
