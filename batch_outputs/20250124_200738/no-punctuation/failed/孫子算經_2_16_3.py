"""
今有堤下廣五丈上廣三丈高二丈長六十尺欲以一千尺作一方問計幾何
術曰置堤上廣三丈下廣五丈并之得八丈半之得四丈以二丈乘之得八百尺以長六十尺乘之得四萬八千以一千尺除之即得
答曰 a 方
"""

#----- content starts here -----
"""
Suppose there is a dike with a bottom width of 5 zhang, a top width of 3 zhang, a height of 2 zhang, and a length of 60 chi.
It is desired to use 1000 chi to calculate the number of cubic units.

The procedure says: Take the top width of the dike, 3 zhang, and the bottom width, 5 zhang.
Add them, obtaining 8 zhang.
Halve it, obtaining 4 zhang.
Multiply it by the height, 2 zhang, obtaining 8 chi.
Multiply it by the length, 60 chi, obtaining 48000 chi.
Divide it by 1000 chi, obtaining the result.

The answer says: *a* cubic units.
"""

# 堤上廣三丈
上廣 = 3

# 堤下廣五丈
下廣 = 5

# 高二丈
高 = 2

# 長六十尺
長 = 60

# 以一千尺作一方
方基準 = 1000

# 并之得八丈
總廣 = 上廣 + 下廣

# 半之得四丈
平均廣 = Fraction(總廣, 2)

# 以二丈乘之得八百尺
橫截面積 = 平均廣 * 高

# 以長六十尺乘之得四萬八千
體積 = 橫截面積 * 長

# 以一千尺除之即得
a = Fraction(體積, 方基準)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 48, Actual: 12/25"""
