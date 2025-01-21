"""
今有城不知大小去人逺近於城西北隅而立四表相去各六丈令左兩表與城西北隅南北望參相直從右後表望城西北隅入右前表一尺二寸又望西南隅亦入右前表四寸又望東北隅亦入左後表二丈四尺問城去左後表及大小各㡬何
術曰置表相去自乗以望城西北隅入數而一得城去表又以望城西南隅入數而一所得減城去表餘為城之南北以望城東北隅入左後表數減城去表餘以乗表相去又以入左後表數而一即得城之東西
答曰城去左後表 a里 東西 b里 南北 c里
"""

"""
This is a complex ancient Chinese surveying problem involving geometry and trigonometry. The problem describes a scenario where measurements are taken from specific points relative to a city wall to determine the distance to the city and the dimensions of the city. Translating this into Python code requires careful interpretation of the procedure ("術") provided.

Let's break it down step by step and translate it into Python code:


"""


from fractions import Fraction

# 表相去各六丈 (The distance between the survey markers is 6 zhang)
表距 = 6  # in 丈

# 入右前表 measurements
入西北隅 = Fraction(1, 10) * 12  # 1 丈 2 尺 = 1.2 丈
入西南隅 = Fraction(4, 10)       # 4 尺 = 0.4 丈
入東北隅 = 2 + Fraction(4, 10)   # 2 丈 4 尺 = 2.4 丈

# 城去左後表 (Distance from the city to the left-rear marker)
# 置表相去自乘 (Square the distance between the markers)
表距平方 = 表距 ** 2

# 以望城西北隅入數而一 (Divide the square of the distance by the 入西北隅 measurement)
城去左後表 = Fraction(表距平方, 入西北隅)

# 城之南北 (North-South dimension of the city)
# 以望城西南隅入數而一所得減城去表 (Divide 表距平方 by 入西南隅, then subtract 城去左後表)
城南北 = Fraction(表距平方, 入西南隅) - 城去左後表

# 城之東西 (East-West dimension of the city)
# 以望城東北隅入左後表數減城去表餘 (Subtract 城去左後表 from 入東北隅)
東西餘 = 入東北隅 - 城去左後表

# 以乘表相去 (Multiply 東西餘 by 表距)
東西乘積 = 東西餘 * 表距

# 又以入左後表數而一 (Divide 東西乘積 by 入東北隅)
城東西 = Fraction(東西乘積, 入東北隅)

# Convert results to li (里), where 1 里 = 300 丈
城去左後表_里 = 城去左後表 / 300
城東西_里 = 城東西 / 300
城南北_里 = 城南北 / 300

# Final answers
a = 城去左後表_里
b = 城東西_里
c = 城南北_里

print(f"城去左後表 {a} 里")
print(f"東西 {b} 里")
print(f"南北 {c} 里")


"""


### Explanation of the Code:
1. **表距**: The distance between the survey markers is given as 6 zhang.
2. **入 measurements**: The 入 values (how much the city wall appears to "enter" the line of sight from the markers) are converted into zhang.
3. **城去左後表**: The distance from the city to the left-rear marker is calculated using the square of the distance between the markers divided by the 入 measurement for the northwest corner.
4. **城南北**: The north-south dimension of the city is calculated by dividing the square of the distance between the markers by the 入 measurement for the southwest corner, then subtracting the distance to the left-rear marker.
5. **城東西**: The east-west dimension of the city is calculated using the 入 measurement for the northeast corner, adjusted by the distance to the left-rear marker, and scaled by the distance between the markers.
6. **Conversion to 里**: The final results are converted from 丈 to 里 (1 里 = 300 丈).

### Final Output:
The program will output the distance to the city and its dimensions in 里 (li).
"""


"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 1/10
Variable 'b' has wrong value. Expected: 62/15, Actual: -23/100
Variable 'c' has wrong value. Expected: 10/3, Actual: 1/5"""
