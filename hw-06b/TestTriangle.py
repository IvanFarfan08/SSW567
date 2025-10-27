# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    #TD-01
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
    
    #TD-02
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
    
    #TD-03
    def testIsoceles(self):
        self.assertEqual(classifyTriangle(5,5,3),'Isoceles','5,5,3 should be isoceles')

    #TD-04
    def testIsocelesPermutationB(self):
        self.assertEqual(classifyTriangle(5,3,5),'Isoceles','5,3,5 should be isoceles')
    #TD-05
    def testIsocelesPermutationC(self):
        self.assertEqual(classifyTriangle(3,5,5),'Isoceles','3,5,5 should be isoceles')
    #TD-06
    def testScalene(self):
        self.assertEqual(classifyTriangle(4,5,6),'Scalene','4,5,6 should be scalene')
    #TD-07
    def testScaleneAdditional(self):
        self.assertEqual(classifyTriangle(10,12,13),'Scalene','10,12,13 should be scalene')
    #TD-08
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    #TD-09
    def testEquilateralBoundaryMax(self):
        self.assertEqual(classifyTriangle(200,200,200),'Equilateral','200,200,200 should be equilateral (boundary)')
    #TD-10
    def testInvalidTriangle(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1,2,3 should be NotATriangle')
    #TD-11
    def testNotATriangleInequalityLess(self):
        self.assertEqual(classifyTriangle(1,1,3),'NotATriangle','1,1,3 violates triangle inequality')
    #TD-12
    def testNotATriangleBoundaryEqual(self):
        self.assertEqual(classifyTriangle(100,100,200),'NotATriangle','100,100,200 has sum equal to third side')
    #TD-13
    def testNotATriangleInequalityEqual(self):
        self.assertEqual(classifyTriangle(10,4,6),'NotATriangle','10,4,6 has sum equal to third side')
    #TD-14
    def testInvalidInputTooLarge(self):
        self.assertEqual(classifyTriangle(201,10,10),'InvalidInput','Sides > 200 should be InvalidInput')
    #TD-15
    def testInvalidInputZero(self):
        self.assertEqual(classifyTriangle(0,10,10),'InvalidInput','Zero side length should be InvalidInput')
    #TD-16
    def testInvalidInputNegative(self):
        self.assertEqual(classifyTriangle(-1,10,10),'InvalidInput','Negative side length should be InvalidInput')
    #TD-17
    def testInvalidInputFloat(self):
        self.assertEqual(classifyTriangle(3.5,4,5),'InvalidInput','Non-integer sides should be InvalidInput')
    #TD-18
    def testInvalidInputString(self):
        self.assertEqual(classifyTriangle('3',4,5),'InvalidInput','Non-integer sides should be InvalidInput')
    #TD-19
    def testInvalidInputMixedBounds(self):
        self.assertEqual(classifyTriangle(200,201,199),'InvalidInput','Any side > 200 should be InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


