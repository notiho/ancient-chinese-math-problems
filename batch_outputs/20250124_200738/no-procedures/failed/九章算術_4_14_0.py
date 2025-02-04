"""
又有積五十六萬四千七百五十二步、四分步之一。問︰為方幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a total area of 564,752 and 1/4 bu².
Question: what is the side length of the square field?

Answer: the side length is *a* bu.
"""

# Total area in bu²
total_area = Fraction(564752 * 4 + 1, 4)

# To find the side length of the square, take the square root of the total area.
# Since we cannot use external libraries, we solve this manually by approximation.

# Start with an initial guess for the square root
a = Fraction(750)  # Initial guess based on the approximate square root of 564752

# Refine the guess using the Babylonian method (Newton's method for square roots)
for _ in range(5):  # Perform 5 iterations for better accuracy
    a = Fraction(a + total_area / a, 2)

# The final value of `a` is the side length of the square field in bu.
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1503/2, Actual: 1548751494243428352603620162235931028402886549876754799282893530448982500143590117947440744048003/2060880231860849437928968945091059252698451829509986426191475090417807718088609604720480032000"""
