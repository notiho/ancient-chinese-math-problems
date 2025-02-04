"""
今有城不知大小去人逺近於城西北隅而立四表相去各六丈令左兩表與城西北隅南北望參相直從右後表望城西北隅入右前表一尺二寸又望西南隅亦入右前表四寸又望東北隅亦入左後表二丈四尺問城去左後表及大小各㡬何
術曰置表相去自乗以望城西北隅入數而一得城去表又以望城西南隅入數而一所得減城去表餘為城之南北以望城東北隅入左後表數減城去表餘以乗表相去又以入左後表數而一即得城之東西
答曰城去左後表 a里 東西 b里 南北 c里
"""

"""
This problem involves a complex geometric calculation based on ancient Chinese surveying techniques. The procedure describes how to calculate the distance from a reference point to a city and the dimensions of the city (east-west and north-south). Let's translate this into Python step by step.

### Problem Setup
We are given:
- Four markers (表) placed in a square, each 6 zhang apart.
- Observations of how much the city corners (城隅) "enter" or align with the markers when viewed from specific positions.

The procedure involves:
1. Calculating the distance from the city to a specific marker (城去表).
2. Calculating the north-south dimension of the city.
3. Calculating the east-west dimension of the city.

Let's encode this step by step.


"""

#----- content starts here -----

from fractions import Fraction

# 表相去 (distance between markers) = 6 丈
表相去 = 6

# Observations of how much the city corners "enter" the markers:
# 城西北隅入右前表 1 尺 2 寸 = 1 丈 + 2/10 丈
城西北隅入 = Fraction(1, 10) * 2 + 1

# 城西南隅入右前表 4 寸 = 4/10 丈
城西南隅入 = Fraction(4, 10)

# 城東北隅入左後表 2 丈 4 尺 = 2 丈 + 4/10 丈
城東北隅入 = 2 + Fraction(4, 10)

# Step 1: Calculate 城去表 (distance from the city to the left-back marker)
# 置表相去自乘
表相去自乘 = 表相去 ** 2

# 以望城西北隅入數而一
城去表 = Fraction(表相去自乘, 城西北隅入)

# Step 2: Calculate 城之南北 (north-south dimension of the city)
# 以望城西南隅入數而一
城西南隅距離 = Fraction(表相去自乘, 城西南隅入)

# 所得減城去表餘為城之南北
城之南北 = 城西南隅距離 - 城去表

# Step 3: Calculate 城之東西 (east-west dimension of the city)
# 以望城東北隅入左後表數減城去表餘
城東北隅距離 = 城東北隅入 - 城去表

# 餘以乘表相去
東西乘積 = 城東北隅距離 * 表相去

# 又以入左後表數而一
城之東西 = Fraction(東西乘積, 城東北隅入)

# Convert results to li (1 丈 = 1/300 里)
城去左後表_里 = 城去表 / 300
城之東西_里 = 城之東西 / 300
城之南北_里 = 城之南北 / 300

# Final answers
a = 城去左後表_里
b = 城之東西_里
c = 城之南北_里

print(f"城去左後表 {a} 里, 東西 {b} 里, 南北 {c} 里")
#----- content ends here -----


"""


### Explanation of the Code
1. **表相去自乘**: The square of the distance between the markers is calculated.
2. **城去表**: The distance from the city to the left-back marker is calculated using the observation of the northwest corner of the city.
3. **城之南北**: The north-south dimension of the city is calculated by subtracting the distance to the marker from the distance calculated using the southwest corner observation.
4. **城之東西**: The east-west dimension of the city is calculated using the observation of the northeast corner and the left-back marker.

### Final Output
The program will output the distance from the city to the left-back marker (`a`), the east-west dimension (`b`), and the north-south dimension (`c`) in li.
"""


"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 1/10
Variable 'b' has wrong value. Expected: 62/15, Actual: -23/100
Variable 'c' has wrong value. Expected: 10/3, Actual: 1/5"""
