"""
又有倉從一丈九尺廣一丈五尺高一丈三尺。問：受粟㡬何？
答曰： a斛 奇 b分 。
"""

#----- content starts here -----
"""
Suppose there is a granary with a length of 1 zhang 9 chi, a width of 1 zhang 5 chi, and a height of 1 zhang 3 chi.
Question: how much millet can it hold?

Answer: it holds *a* hu and *b* fen.
"""

# Dimensions of the granary
length = 1 * 10 + 9  # 1 zhang 9 chi = 10 chi + 9 chi
width = 1 * 10 + 5   # 1 zhang 5 chi = 10 chi + 5 chi
height = 1 * 10 + 3  # 1 zhang 3 chi = 10 chi + 3 chi

# Volume of the granary in cubic chi
volume = length * width * height

# Conversion: 1 hu = 10 cubic chi
a = volume // 10  # Number of hu
b = volume % 10   # Remaining fen (cubic chi)

a, b  # Output the result as hu and fen#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 228703/100, Actual: 370
Variable 'b' has wrong value. Expected: 57/50, Actual: 5"""
