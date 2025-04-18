"""
今有築城上廣一丈下廣三丈髙四丈今已築髙一丈五尺問已築上廣㡬何
術曰置城下廣以上廣減之又置城髙以減築髙餘相乗以城髙而一所得加城上廣即得
答曰 a丈
"""

#----- content starts here -----
"""
Suppose there is a city wall being constructed. The top width is 1 zhang, the bottom width is 3 zhang, and the height is 4 zhang.
Now, the wall has already been constructed to a height of 1 zhang and 5 chi.
Question: what is the current top width of the constructed portion?

The procedure says: Place the bottom width of the wall and subtract the top width.
Then, place the total height of the wall and subtract the constructed height.
Multiply the remainder by the constructed height.
Divide by the total height of the wall.
Add the result to the top width of the wall, and this gives the answer.

Answer: *a* zhang.
"""

# 城上廣一丈
城上廣 = 1

# 城下廣三丈
城下廣 = 3

# 城髙四丈
城髙 = 4

# 已築髙一丈五尺 (convert to zhang: 1 zhang = 10 chi)
已築髙 = 1 + Fraction(5, 10)

# 置城下廣以上廣減之
廣差 = 城下廣 - 城上廣

# 置城髙以減築髙
髙差 = 城髙 - 已築髙

# 餘相乘
積 = 廣差 * 已築髙

# 以城髙而一
調整值 = Fraction(積, 城髙)

# 所得加城上廣即得
a = 城上廣 + 調整值#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9/4, Actual: 7/4"""
