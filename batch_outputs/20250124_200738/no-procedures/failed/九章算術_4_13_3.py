"""
又有積七萬一千八百二十四步。問︰為方幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 71,824 cubic bu (步³).
Question: if it forms a cube, what is the length of one side?

Answer: the side length is *a* bu (步).
"""

# 積七萬一千八百二十四步
volume = 71824

# To find the side length of the cube, we take the cube root of the volume.
# Since we cannot use external libraries, we will calculate the cube root manually using an iterative method.

def cube_root(n):
    # Start with an initial guess
    guess = n // 3
    while True:
        # Refine the guess using the formula: guess = (2 * guess + n / guess^2) / 3
        new_guess = (2 * guess + n // (guess * guess)) // 3
        if new_guess == guess:
            break
        guess = new_guess
    return guess

# Calculate the cube root of the volume
a = cube_root(volume)

# The side length of the cube is:
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 268, Actual: 41"""
