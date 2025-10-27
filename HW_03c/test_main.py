import unittest
from main import classify_triangle


class TestTriangleClassification(unittest.TestCase):

    def test_equilateral_triangles(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Triangle is equilateral")
        self.assertEqual(classify_triangle(5, 5, 5), "Triangle is equilateral")
        self.assertEqual(classify_triangle(10, 10, 10), "Triangle is equilateral")
    
    def test_isosceles_triangles(self):
        self.assertEqual(classify_triangle(3, 3, 4), "Triangle is isoceles")
        self.assertEqual(classify_triangle(5, 4, 5), "Triangle is isoceles")
        self.assertEqual(classify_triangle(7, 10, 7), "Triangle is isoceles")
    
    def test_scalene_triangles(self):
        self.assertEqual(classify_triangle(3, 4, 6), "Triangle is scalene")
        self.assertEqual(classify_triangle(5, 7, 9), "Triangle is scalene")
        self.assertEqual(classify_triangle(2, 3, 4), "Triangle is scalene")
    
    def test_right_triangles(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Triangle is right")
        self.assertEqual(classify_triangle(5, 12, 13), "Triangle is right")
        self.assertEqual(classify_triangle(8, 15, 17), "Triangle is right")
        self.assertEqual(classify_triangle(7, 24, 25), "Triangle is right")
    
    def test_invalid_triangles(self):
        # Negative or zero values
        self.assertEqual(classify_triangle(-1, 2, 3), "Invalid triangle")
        self.assertEqual(classify_triangle(0, 4, 5), "Invalid triangle")
        self.assertEqual(classify_triangle(3, -2, 4), "Invalid triangle")
        
        # Triangle inequality violations
        self.assertEqual(classify_triangle(1, 2, 5), "Invalid triangle")
        self.assertEqual(classify_triangle(10, 1, 1), "Invalid triangle")
        self.assertEqual(classify_triangle(3, 7, 3), "Invalid triangle")


if __name__ == "__main__":
    unittest.main()
