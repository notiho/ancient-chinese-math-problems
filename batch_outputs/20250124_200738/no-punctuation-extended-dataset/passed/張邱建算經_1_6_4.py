"""
今有葮生於池中出水三尺去岸一丈引葮趨岸不及一尺問葮長及水深各㡬何
術曰置葮去岸尺數以不及尺數減之餘自相乗以出水尺數而一所得加出水而半之得葮長減出水尺數即得水深
答曰葮長 a丈 水深 b丈
"""

#----- content starts here -----
"""
Suppose there is a lotus growing in a pond. It extends 3 chi above the water and is 1 zhang away from the shore. 
When the lotus is pulled toward the shore, it falls short by 1 chi.
Question: what is the length of the lotus and the depth of the water?

The procedure says: Place the number of chi the lotus is away from the shore.
Subtract the number of chi it falls short by.
Square the remainder and divide it by the number of chi the lotus extends above the water.
Add the result to the number of chi the lotus extends above the water, then halve it to obtain the length of the lotus.
Subtract the number of chi the lotus extends above the water from its length to obtain the depth of the water.

Answer: the length of the lotus is *a* zhang, and the depth of the water is *b* zhang.
"""

# 出水三尺
出水 = 3

# 去岸一丈 (convert to chi: 1丈 = 10尺)
去岸 = 10

# 不及一尺
不及 = 1

# 置葮去岸尺數，以不及尺數減之
餘 = 去岸 - 不及

# 餘自相乘
餘平方 = 餘 * 餘

# 以出水尺數而一所得
所得 = Fraction(餘平方, 出水)

# 加出水而半之，得葮長
葮長 = Fraction(所得 + 出水, 2)

# 減出水尺數，即得水深
水深 = 葮長 - 出水

# Convert results to zhang (1丈 = 10尺)
a = Fraction(葮長, 10)
b = Fraction(水深, 10)#----- content ends here -----

"""
"""
