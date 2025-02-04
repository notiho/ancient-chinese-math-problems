"""
又有積七萬一千八百二十四步。問︰為方幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 71,824 cubic bu (步³).
Question: if it is formed into a cube, what is the length of each side?

Answer: the side length is *a* bu.
"""

# 積七萬一千八百二十四步
volume = 71824

# To find the side length of the cube, take the cube root of the volume.
# Since we cannot use external libraries, we approximate the cube root manually.

# Start with an initial guess
a = 42  # Since 42³ = 74088, which is close to 71824

# Refine the guess manually
while a**3 > volume:
    a -= 1  # Decrease until a³ ≤ volume

# Final result
a = Fraction(a)  # Represent the result as a fraction if needed#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 268, Actual: 41"""
