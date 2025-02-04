"""
今有田積一十二萬七千四百四十九步問為方㡬何
術曰以開方除之即得
答曰 a步
"""

#----- content starts here -----
"""
Suppose there is a field with an area of 127449 bu².
Question: what is the side length of the square field?

The procedure says: Take the square root of the area, and you will obtain the side length.

Answer: *a* bu.
"""

# 田積一十二萬七千四百四十九步
田積 = 127449

# 開方 (square root)
# To calculate the square root manually, we use an iterative approximation method (Babylonian method).

def square_root(n, iterations=10):
    guess = n / 2  # Initial guess
    for _ in range(iterations):
        guess = (guess + n / guess) / 2
    return guess

# Calculate the side length
a = square_root(田積)

# Convert to Fraction for exact representation
a = Fraction(int(a), 1)  # Since the result is an integer, we represent it as a Fraction.#----- content ends here -----

"""
"""
