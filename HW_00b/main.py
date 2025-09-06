def classify_triangle(a: int, b:int, c:int):
    # Ensure positive values
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid triangle"
    
    # Check triangle inequality
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid triangle"

    # Case where the sides are equal -> Equilateral
    if a == b == c:
        return "Triangle is equilateral"

    # Case for right triangles (Pythagoras)
    if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c** 2 == a **2):
        return "Triangle is right"

    # Case for isosceles triangles: two sides equal
    if a == b or a == c or b == c:
        return "Triangle is isoceles"

    return "Triangle is scalene"

