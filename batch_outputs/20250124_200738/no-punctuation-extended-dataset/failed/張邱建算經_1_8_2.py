"""
今有城不知大小去人逺近於城西北隅而立四表相去各六丈令左兩表與城西北隅南北望參相直從右後表望城西北隅入右前表一尺二寸又望西南隅亦入右前表四寸又望東北隅亦入左後表二丈四尺問城去左後表及大小各㡬何
術曰置表相去自乗以望城西北隅入數而一得城去表又以望城西南隅入數而一所得減城去表餘為城之南北以望城東北隅入左後表數減城去表餘以乗表相去又以入左後表數而一即得城之東西
答曰城去左後表 a里 東西 b里 南北 c里
"""

"""
This problem involves a complex geometric calculation based on ancient Chinese surveying techniques. Translating this into Python code requires careful adherence to the procedure described. Let's break it down and implement the solution step by step.


"""

#----- content starts here -----

from fractions import Fraction

# 城西北隅與四表相去各六丈
表距離 = 6  # 丈

# 望城西北隅入右前表一尺二寸
西北隅入右前表 = Fraction(1, 10) * 12 + Fraction(2, 10)  # 尺轉換為丈

# 望城西南隅入右前表四寸
西南隅入右前表 = Fraction(4, 10)  # 尺轉換為丈

# 望城東北隅入左後表二丈四尺
東北隅入左後表 = 2 + Fraction(4, 10)  # 丈

# 置表相去自乘
表距離平方 = 表距離 ** 2

# 以望城西北隅入數而一，得城去表
城去表 = Fraction(表距離平方, 西北隅入右前表)

# 以望城西南隅入數而一，所得減城去表，餘為城之南北
南北距離 = Fraction(表距離平方, 西南隅入右前表) - 城去表

# 以望城東北隅入左後表數減城去表，餘以乘表相去
東西距離 = (東北隅入左後表 - 城去表) * 表距離

# 又以入左後表數而一，即得城之東西
東西距離 = Fraction(東西距離, 東北隅入左後表)

# 答案
a = 城去表 / 100  # 轉換為里
b = 東西距離 / 100  # 轉換為里
c = 南北距離 / 100  # 轉換為里

print(f"城去左後表 {a} 里")
print(f"東西 {b} 里")
print(f"南北 {c} 里")
#----- content ends here -----


"""


### Explanation:
1. **表距離**: The distance between the four markers is given as 6 丈.
2. **西北隅入右前表**: The offset for the northwest corner is converted from 尺 and 寸 to 丈.
3. **西南隅入右前表**: Similarly, the offset for the southwest corner is converted.
4. **東北隅入左後表**: The offset for the northeast corner is converted.
5. **表距離平方**: The square of the distance between the markers is calculated.
6. **城去表**: The distance from the city to the marker is calculated using the offset for the northwest corner.
7. **南北距離**: The north-south dimension of the city is calculated by subtracting the distance to the marker from the offset for the southwest corner.
8. **東西距離**: The east-west dimension of the city is calculated using the offset for the northeast corner and the distance to the marker.
9. **Conversion to 里**: All distances are converted from 丈 to 里 (1 里 = 100 丈).

This code follows the procedure described in the problem and provides the required distances in 里.
"""


"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 9/35
Variable 'b' has wrong value. Expected: 62/15, Actual: -102/175
Variable 'c' has wrong value. Expected: 10/3, Actual: 9/14"""
