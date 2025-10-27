# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """
    # Check types again
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'

    # Check that all sides are positive.
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # Right triangle check
    sides = sorted([a, b, c])
    side1, side2, hyp = sides[0], sides[1], sides[2]

    if side1 * side1 + side2 * side2 == hyp * hyp:
        return 'Right'
    
    # Check equilateral
    if side1 == side2 and side2 == hyp:
        return 'Equilateral'
    
    # Check isoceles
    if (side1 == side2) or (side2 == hyp) or (side1 == hyp):
        return 'Isoceles'

    # If we get here, it's scalene
    else:
        return 'Scalene'

