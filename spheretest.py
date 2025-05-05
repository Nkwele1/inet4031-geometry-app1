import unittest
import sphere

class SphereTest(unittest.TestCase):

    def test_volume1(self):
        self.assertAlmostEqual(sphere.volume(1), (4/3) * 3.141592653589793 * 1**3, places=5)

    def test_volume2(self):
        self.assertAlmostEqual(sphere.volume(2), (4/3) * 3.141592653589793 * 8, places=5)

    def test_volume3(self):
        self.assertAlmostEqual(sphere.volume(5), (4/3) * 3.141592653589793 * 125, places=5)

if __name__ == '__main__':
    unittest.main()
