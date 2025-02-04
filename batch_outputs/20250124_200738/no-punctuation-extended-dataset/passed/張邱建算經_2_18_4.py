"""
今有田積一十二萬七千四百四十九步問為方㡬何
術曰以開方除之即得
答曰 a步
"""

#----- content starts here -----
"""
Suppose there is a field with an area of 127,449 bu².
Question: what is the side length of the square field?

The procedure says: Take the square root of the area, and the result is obtained.

Answer: *a* bu.
"""

# 田積一十二萬七千四百四十九步
田積 = 127449

# 開方 (finding the square root using an iterative method)
def 開方(數):
    # Start with an initial guess
    根 = 數 // 2
    while True:
        新根 = (根 + 數 // 根) // 2
        if 新根 == 根:
            return 根
        根 = 新根

# 以開方除之即得
a = 開方(田積)#----- content ends here -----

"""
"""
