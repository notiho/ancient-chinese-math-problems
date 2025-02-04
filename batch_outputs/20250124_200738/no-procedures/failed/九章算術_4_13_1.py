"""
又有積七萬一千八百二十四步。問︰為方幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 71,824 cubic bu (步³).
Question: if this volume is shaped into a cube, what is the length of one side?

Answer: the side length is *a* bu.
"""

# 積七萬一千八百二十四步
積 = 71824

# To find the side length of the cube, take the cube root of the volume
# a³ = 積
# a = 積^(1/3)

# Since we are not using external libraries, we will approximate the cube root manually
# Start with an initial guess and refine iteratively
a = 1
while a**3 < 積:
    a += 1

# Check if the exact cube root was found
if a**3 > 積:
    a -= 1  # Step back to the largest integer whose cube is less than or equal to 積

# Final result
a = Fraction(a)  # Represent the result as a fraction if needed#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 268, Actual: 41"""
