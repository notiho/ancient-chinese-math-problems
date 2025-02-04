"""
今有田積一十二萬七千四百四十九步問為方㡬何
術曰以開方除之即得
答曰 a步
"""

"""
Suppose there is a field with an area of 127449 bu².
Question: what is the side length of the square field?

The procedure says: Take the square root of the area, and you will obtain the side length.

Answer: *a* bu.
"""

# 田積一十二萬七千四百四十九步
田積 = 127449

# 開方 (square root)
# To calculate the square root manually using the Babylonian method (since no external functions are allowed):
def 開方(n, iterations=10):
    # Start with an initial guess (half of the number)
    guess = n / 2
    for _ in range(iterations):
        guess = (guess + n / guess) / 2
    return guess

# Calculate the side length
a = 開方(田積)
"""
Variable 'a' has wrong value. Expected: 357, Actual: 357.0074271280838"""
