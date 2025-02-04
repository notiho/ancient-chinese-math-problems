"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
求龍尾堤廣、袤、高，術曰：以程功乘總人，為堤積。又六因之，為虛積。以少高乘少袤，為隅冪。以少上廣乘之，為鱉隅積。以減虛積，余，三約之，所得為實。並少高、袤，以少上廣乘之，為鱉從橫廉冪。三而一，加隅冪，為方法。又三除少上廣，以少袤、少高加之，為廉法，從。開立方除之，得下廣。加差，即高、廣、袤。求逐縣均給積尺受廣、袤，術曰：以程功乘當縣人，當積尺。各六因積尺。又乘袤冪。廣差乘高，為法。除之，為實。又三因末廣，以袤乘之，廣差而一，為都廉，從。開立方除之，即甲袤。以本高乘之，以本袤除之，即甲高。又以廣差乘甲袤，以本袤除之，所得加末廣，即甲上廣。其甲上廣即乙末廣，其甲高即垣高。求實與都廉，如前。又並甲上下廣，三之，乘甲高，又乘袤冪，以法除之，得垣方，從。開立方除之，即乙袤。余放此。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
This problem is highly complex and involves multiple steps of ancient Chinese mathematical procedures. I'll translate the procedure into Python code step by step, adhering to the structure of the procedure ("術"). The calculations will use the `Fraction` class to ensure precision.


"""


from fractions import Fraction

# Input data
甲縣人數 = 2375
乙縣人數 = 2378
丙縣人數 = 5247
總人數 = 甲縣人數 + 乙縣人數 + 丙縣人數

程功 = Fraction(1, 1) + Fraction(9, 10) + Fraction(8, 100)  # 每人程功一尺九寸八分
少高 = Fraction(1, 1) + Fraction(2, 10)  # 少高一丈二尺
少袤 = Fraction(4, 1) + Fraction(8, 10)  # 少袤四丈八尺
少上廣 = Fraction(6, 1)  # 差六尺
少下廣 = 少上廣 - Fraction(6, 1)

# Step 1: Calculate 堤積 and 虛積
堤積 = 程功 * 總人數
虛積 = 堤積 * 6

# Step 2: Calculate 隅冪 and 鱉隅積
隅冪 = 少高 * 少袤
鱉隅積 = 隅冪 * 少上廣

# Step 3: Calculate 實
實 = (虛積 - 鱉隅積) / 3

# Step 4: Calculate 方法
鱉從橫廉冪 = (少高 + 少袤) * 少上廣 / 3
方法 = 鱉從橫廉冪 + 隅冪

# Step 5: Calculate 廉法 and 下廣
廉法 = (少上廣 / 3) + 少袤 + 少高
下廣 = (實 / 方法) ** Fraction(1, 3)

# Step 6: Calculate 高, 廣, and 袤
高 = 下廣 + 少高
上廣 = 下廣 + 少上廣
袤 = 下廣 + 少袤

# Step 7: Calculate each county's contribution
def calculate_county(縣人數, 總人數, 程功, 少上廣, 少袤, 少高, 廣差):
    當積尺 = 程功 * 縣人數
    積尺 = 當積尺 * 6
    廣差高 = 廣差 * 少高
    法 = 廣差高
    實 = 積尺 / 法
    都廉 = (實 * 少袤) / 廣差
    縣袤 = (實 / 都廉) ** Fraction(1, 3)
    縣高 = (少高 * 縣袤) / 少袤
    縣上廣 = (廣差 * 縣袤) / 少袤 + 少上廣
    return 縣袤, 縣高, 縣上廣

廣差 = 少上廣 - 少下廣

甲袤, 甲高, 甲上廣 = calculate_county(甲縣人數, 總人數, 程功, 少上廣, 少袤, 少高, 廣差)
乙袤, 乙高, 乙上廣 = calculate_county(乙縣人數, 總人數, 程功, 甲上廣, 甲袤, 甲高, 廣差)
丙袤, 丙高, 丙上廣 = calculate_county(丙縣人數, 總人數, 程功, 乙上廣, 乙袤, 乙高, 廣差)

# Final results
a = 高
b = 上廣
c = 下廣
d = 袤
e, f, g = 甲高, 甲袤, 甲上廣
h, i, j = 乙高, 乙袤, 乙上廣
k, l, m = 丙高, 丙袤, 丙上廣

# Output results
print(f"高 {a}丈 ，上廣 {b}丈 ，下廣 {c}丈 ，袤 {d}丈")
print(f"甲縣高 {e}丈 ，袤 {f}丈 ，上廣 {g}丈")
print(f"乙縣高 {h}丈 ，袤 {i}丈 ，上廣 {j}丈")
print(f"丙縣高 {k}丈 ，袤 {l}丈 ，上廣 {m}丈")


"""


This code follows the ancient procedure step by step, ensuring that each calculation adheres to the described method. The results are expressed in terms of `Fraction` to maintain precision.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 14.262970777022256
Variable 'b' has wrong value. Expected: 17/5, Actual: 19.062970777022258
Variable 'c' has wrong value. Expected: 9/5, Actual: 13.062970777022256
Variable 'd' has wrong value. Expected: 33/5, Actual: 17.862970777022255
Variable 'e' has wrong value. Expected: 3/2, Actual: 0.2693043362539855
Variable 'f' has wrong value. Expected: 33/10, Actual: 1.077217345015942
Variable 'g' has wrong value. Expected: 21/10, Actual: 7.346521681269928
Variable 'h' has wrong value. Expected: 21/10, Actual: 0.4431553325284398
Variable 'i' has wrong value. Expected: 33/25, Actual: 1.7726213301137592
Variable 'j' has wrong value. Expected: 111/50, Actual: 17.219856927765754
Variable 'k' has wrong value. Expected: 3, Actual: 0.3753632653876943
Variable 'l' has wrong value. Expected: 99/50, Actual: 1.5014530615507773
Variable 'm' has wrong value. Expected: 12/5, Actual: 22.302001780849814"""
