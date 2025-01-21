"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
求龍尾堤廣、袤、高，術曰：以程功乘總人，為堤積。又六因之，為虛積。以少高乘少袤，為隅冪。以少上廣乘之，為鱉隅積。以減虛積，余，三約之，所得為實。並少高、袤，以少上廣乘之，為鱉從橫廉冪。三而一，加隅冪，為方法。又三除少上廣，以少袤、少高加之，為廉法，從。開立方除之，得下廣。加差，即高、廣、袤。求逐縣均給積尺受廣、袤，術曰：以程功乘當縣人，當積尺。各六因積尺。又乘袤冪。廣差乘高，為法。除之，為實。又三因末廣，以袤乘之，廣差而一，為都廉，從。開立方除之，即甲袤。以本高乘之，以本袤除之，即甲高。又以廣差乘甲袤，以本袤除之，所得加末廣，即甲上廣。其甲上廣即乙末廣，其甲高即垣高。求實與都廉，如前。又並甲上下廣，三之，乘甲高，又乘袤冪，以法除之，得垣方，從。開立方除之，即乙袤。余放此。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
This problem is highly complex and involves multiple steps of ancient Chinese mathematical procedures. Below is the Python code that follows the described procedure step by step. The solution uses the `Fraction` class to handle precise calculations.


"""


from fractions import Fraction

# Input data
甲縣人 = 2375
乙縣人 = 2378
丙縣人 = 5247
總人 = 甲縣人 + 乙縣人 + 丙縣人

程功 = Fraction(1, 1) + Fraction(9, 10) + Fraction(8, 100)  # 一尺九寸八分
少高 = Fraction(1, 1) + Fraction(2, 10)  # 一丈二尺
少袤 = Fraction(4, 1) + Fraction(8, 10)  # 四丈八尺
少上廣 = Fraction(6, 1)  # 六尺
差 = Fraction(6, 1)  # 上廣多，下廣少，差六尺

# Step 1: Calculate 堤積
堤積 = 程功 * 總人

# Step 2: Calculate 虛積
虛積 = 堤積 * 6

# Step 3: Calculate 隅冪
隅冪 = 少高 * 少袤

# Step 4: Calculate 鱉隅積
鱉隅積 = 少上廣 * 隅冪

# Step 5: Calculate 實
實 = (虛積 - 鱉隅積) / 3

# Step 6: Calculate 方法
方法 = (少高 + 少袤) * 少上廣 / 3 + 隅冪

# Step 7: Calculate 廉法
廉法 = (少上廣 / 3) + 少袤 + 少高

# Step 8: Calculate 下廣
下廣 = (實 / 方法) ** Fraction(1, 3)

# Step 9: Calculate 高, 上廣, 袤
高 = 下廣 + 差
上廣 = 下廣 + 差
袤 = 下廣 + 差

# Step 10: Calculate each county's contribution
def calculate_county(縣人, 縣末廣, 縣高, 縣袤):
    當積尺 = 程功 * 縣人
    積尺 = 當積尺 * 6
    廣差高 = 差 * 縣高
    法 = 廣差高
    實 = 積尺 / 法
    都廉 = (縣末廣 * 縣袤 + 差) ** Fraction(1, 3)
    縣袤 = (實 / 都廉) ** Fraction(1, 3)
    縣高 = 縣高 * 縣袤 / 縣袤
    縣上廣 = 差 * 縣袤 / 縣袤 + 縣末廣
    return 縣高, 縣袤, 縣上廣

# Calculate for 甲縣
甲高, 甲袤, 甲上廣 = calculate_county(甲縣人, 少上廣, 高, 袤)

# Calculate for 乙縣
乙高, 乙袤, 乙上廣 = calculate_county(乙縣人, 甲上廣, 甲高, 甲袤)

# Calculate for 丙縣
丙高, 丙袤, 丙上廣 = calculate_county(丙縣人, 乙上廣, 乙高, 乙袤)

# Final results
a = 高
b = 上廣
c = 下廣
d = 袤
e = 甲高
f = 甲袤
g = 甲上廣
h = 乙高
i = 乙袤
j = 乙上廣
k = 丙高
l = 丙袤
m = 丙上廣

# Output results
print(f"高 {a}丈 ，上廣 {b}丈 ，下廣 {c}丈 ，袤 {d}丈")
print(f"甲縣高 {e}丈 ，袤 {f}丈 ，上廣 {g}丈")
print(f"乙縣高 {h}丈 ，袤 {i}丈 ，上廣 {j}丈")
print(f"丙縣高 {k}丈 ，袤 {l}丈 ，上廣 {m}丈")


"""


This code follows the ancient Chinese procedure step by step, translating the mathematical operations into Python. Note that the calculations for each county are encapsulated in the `calculate_county` function for clarity and reuse. The results are printed at the end.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 19.062970777022258
Variable 'b' has wrong value. Expected: 17/5, Actual: 19.062970777022258
Variable 'c' has wrong value. Expected: 9/5, Actual: 13.062970777022256
Variable 'd' has wrong value. Expected: 33/5, Actual: 19.062970777022258
Variable 'e' has wrong value. Expected: 3/2, Actual: 19.062970777022258
Variable 'f' has wrong value. Expected: 33/10, Actual: 3.6830496632606473
Variable 'g' has wrong value. Expected: 21/10, Actual: 12.0
Variable 'h' has wrong value. Expected: 21/10, Actual: 19.062970777022258
Variable 'i' has wrong value. Expected: 33/25, Actual: 4.060676062902229
Variable 'j' has wrong value. Expected: 111/50, Actual: 18.0
Variable 'k' has wrong value. Expected: 3, Actual: 19.062970777022258
Variable 'l' has wrong value. Expected: 99/50, Actual: 5.026027224865768
Variable 'm' has wrong value. Expected: 12/5, Actual: 24.0"""
