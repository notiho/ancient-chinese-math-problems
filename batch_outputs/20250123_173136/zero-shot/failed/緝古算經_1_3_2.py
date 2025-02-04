"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
求龍尾堤廣、袤、高，術曰：以程功乘總人，為堤積。又六因之，為虛積。以少高乘少袤，為隅冪。以少上廣乘之，為鱉隅積。以減虛積，余，三約之，所得為實。並少高、袤，以少上廣乘之，為鱉從橫廉冪。三而一，加隅冪，為方法。又三除少上廣，以少袤、少高加之，為廉法，從。開立方除之，得下廣。加差，即高、廣、袤。求逐縣均給積尺受廣、袤，術曰：以程功乘當縣人，當積尺。各六因積尺。又乘袤冪。廣差乘高，為法。除之，為實。又三因末廣，以袤乘之，廣差而一，為都廉，從。開立方除之，即甲袤。以本高乘之，以本袤除之，即甲高。又以廣差乘甲袤，以本袤除之，所得加末廣，即甲上廣。其甲上廣即乙末廣，其甲高即垣高。求實與都廉，如前。又並甲上下廣，三之，乘甲高，又乘袤冪，以法除之，得垣方，從。開立方除之，即乙袤。余放此。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves calculating the dimensions of a dam (堤) and distributing the work among three counties (甲, 乙, 丙). The solution involves using the class `Fraction` to handle non-integer values.

Here is the Python code:


"""


from fractions import Fraction

# Given data
差 = Fraction(6)  # Difference between upper and lower widths
少高 = Fraction(12)  # Lower height in 丈
少袤 = Fraction(48)  # Lower length in 丈
甲人 = 2375  # People from 甲 county
乙人 = 2378  # People from 乙 county
丙人 = 5247  # People from 丙 county
程功 = Fraction(19, 10)  # Work per person per day in 尺

# Total people
總人 = 甲人 + 乙人 + 丙人

# Step 1: Calculate the total volume of the dam
堤積 = 程功 * 總人  # Total work in cubic 尺
虛積 = 堤積 * 6  # Virtual volume

# Step 2: Calculate the corner volume
隅冪 = 少高 * 少袤  # Corner area
鱉隅積 = 隅冪 * (少高 + 差)  # Turtle corner volume
實積 = (虛積 - 鱉隅積) / 3  # Actual volume

# Step 3: Calculate the dimensions of the dam
鱉從橫廉冪 = (少高 + 少袤) * (少高 + 差) * 少袤 / 3 + 隅冪  # Method for width
廉法 = (少袤 + 少高 + (少高 + 差)) / 3  # Method for length
下廣 = (實積 / 鱉從橫廉冪) ** Fraction(1, 3)  # Lower width
上廣 = 下廣 + 差  # Upper width
高 = 少高 + 下廣  # Height
袤 = 少袤 + 下廣  # Length

# Assign the results to variables
a = 高
b = 上廣
c = 下廣
d = 袤

# Step 4: Calculate the dimensions for each county
def calculate_county_dimensions(人數, 上廣, 高, 袤, 差):
    當積尺 = 程功 * 人數  # Work for the county in cubic 尺
    積尺 = 當積尺 * 6  # Virtual volume
    廣差 = 差
    廉法 = (袤 ** 2) * 高 * 廣差
    都廉 = 廣差 * 袤 * 高 / 3
    末廣 = (積尺 / 廉法) ** Fraction(1, 3)
    縣袤 = 末廣 * 廣差
    縣高 = 高 * 縣袤 / 袤
    縣上廣 = 廣差 * 縣袤 / 袤 + 末廣
    return 縣高, 縣袤, 縣上廣

# Calculate for 甲 county
e, f, g = calculate_county_dimensions(甲人, 上廣, 高, 袤, 差)

# Calculate for 乙 county
h, i, j = calculate_county_dimensions(乙人, g, e, f, 差)

# Calculate for 丙 county
k, l, m = calculate_county_dimensions(丙人, j, h, i, 差)

# Final results
print(f"高 a = {a} 丈")
print(f"上廣 b = {b} 丈")
print(f"下廣 c = {c} 丈")
print(f"袤 d = {d} 丈")
print(f"甲縣高 e = {e} 丈")
print(f"甲縣袤 f = {f} 丈")
print(f"甲縣上廣 g = {g} 丈")
print(f"乙縣高 h = {h} 丈")
print(f"乙縣袤 i = {i} 丈")
print(f"乙縣上廣 j = {j} 丈")
print(f"丙縣高 k = {k} 丈")
print(f"丙縣袤 l = {l} 丈")
print(f"丙縣上廣 m = {m} 丈")


"""


This code calculates the dimensions of the dam and the work distribution among the three counties. The results are stored in variables `a`, `b`, `c`, `d`, `e`, `f`, `g`, `h`, `i`, `j`, `k`, `l`, and `m`, as required.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 13.246032822762741
Variable 'b' has wrong value. Expected: 17/5, Actual: 7.246032822762742
Variable 'c' has wrong value. Expected: 9/5, Actual: 1.2460328227627417
Variable 'd' has wrong value. Expected: 33/5, Actual: 49.24603282276274
Variable 'e' has wrong value. Expected: 3/2, Actual: 0.8389359199368775
Variable 'f' has wrong value. Expected: 33/10, Actual: 3.118991656008079
Variable 'g' has wrong value. Expected: 21/10, Actual: 0.8998412320132133
Variable 'h' has wrong value. Expected: 21/10, Actual: 13.25160775306016
Variable 'i' has wrong value. Expected: 33/25, Actual: 49.26675927000055
Variable 'j' has wrong value. Expected: 111/50, Actual: 102.9855242419581
Variable 'k' has wrong value. Expected: 3, Actual: 1.0921824513232867
Variable 'l' has wrong value. Expected: 99/50, Actual: 4.0605103102178415
Variable 'm' has wrong value. Expected: 12/5, Actual: 1.1712648997174981"""
