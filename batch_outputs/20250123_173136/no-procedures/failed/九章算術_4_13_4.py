"""
又有積七萬一千八百二十四步。問︰為方幾何？
荅曰： a步 。
"""

"""
Suppose there is a volume of 71824 cubic bu (步³).
Question: if this volume is shaped into a cube, what is the length of one side of the cube?

Answer: the side length is *a* bu (步).
"""

# 積七萬一千八百二十四步
volume = 71824

# To find the side length of the cube, we take the cube root of the volume.
# Since we cannot use external libraries, we will calculate the cube root manually using an iterative method.

# Initial guess for the cube root
a = Fraction(1)

# Iterative approximation for cube root using Newton's method
for _ in range(20):  # Perform 20 iterations for precision
    a = Fraction(2 * a + Fraction(volume, a**2), 3)

# The result is the side length of the cube
a  # This is the side length in bu (步).
"""
Code error: Exceeds the limit (4300) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit"""
