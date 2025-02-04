"""
今有堤下廣五丈上廣三丈高二丈長六十尺欲以一千尺作一方問計幾何
術曰置堤上廣三丈下廣五丈并之得八丈半之得四丈以二丈乘之得八百尺以長六十尺乘之得四萬八千以一千尺除之即得
答曰 a 方
"""

#----- content starts here -----
"""
Suppose there is a dike with a bottom width of 5 zhang, a top width of 3 zhang, a height of 2 zhang, and a length of 60 chi.
It is desired to calculate how many cubic units (fang) it makes when using 1000 cubic chi as one unit.

The procedure says: Place the top width of the dike, 3 zhang, and the bottom width, 5 zhang.
Add them, obtaining 8 zhang.
Halve this, obtaining 4 zhang.
Multiply it by the height, 2 zhang, obtaining 8 square zhang (800 square chi).
Multiply this by the length, 60 chi, obtaining 48000 cubic chi.
Divide it by 1000 cubic chi, obtaining the number of cubic units.

The answer says: *a* cubic units (fang).
"""

# 堤下廣五丈
下廣 = 5

# 堤上廣三丈
上廣 = 3

# 高二丈
高 = 2

# 長六十尺
長 = 60

# 置堤上廣三丈，下廣五丈，并之得八丈
總廣 = 上廣 + 下廣

# 半之，得四丈
平均廣 = Fraction(總廣, 2)

# 以二丈乘之，得八百尺
橫截面積 = 平均廣 * 高 * 100  # Convert zhang^2 to chi^2 (1 zhang = 10 chi)

# 以長六十尺乘之，得四萬八千
體積 = 橫截面積 * 長

# 以一千尺除之，即得
a = Fraction(體積, 1000)#----- content ends here -----

"""
"""
