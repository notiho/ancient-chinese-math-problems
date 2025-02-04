"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
求龍尾堤廣、袤、高，術曰：以程功乘總人，為堤積。又六因之，為虛積。以少高乘少袤，為隅冪。以少上廣乘之，為鱉隅積。以減虛積，余，三約之，所得為實。並少高、袤，以少上廣乘之，為鱉從橫廉冪。三而一，加隅冪，為方法。又三除少上廣，以少袤、少高加之，為廉法，從。開立方除之，得下廣。加差，即高、廣、袤。求逐縣均給積尺受廣、袤，術曰：以程功乘當縣人，當積尺。各六因積尺。又乘袤冪。廣差乘高，為法。除之，為實。又三因末廣，以袤乘之，廣差而一，為都廉，從。開立方除之，即甲袤。以本高乘之，以本袤除之，即甲高。又以廣差乘甲袤，以本袤除之，所得加末廣，即甲上廣。其甲上廣即乙末廣，其甲高即垣高。求實與都廉，如前。又並甲上下廣，三之，乘甲高，又乘袤冪，以法除之，得垣方，從。開立方除之，即乙袤。余放此。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code. The solution involves calculating the dimensions of the 龙尾堤 (Dragon Tail Dam) and the contributions of each county (甲, 乙, 丙) to its construction. We will use the `Fraction` class to handle non-integer values.

Here is the Python code:


"""


from fractions import Fraction

# Given data
差 = Fraction(6)  # Difference between upper and lower widths (上廣多，下廣少)
少高 = Fraction(12)  # Lower height (少高)
少袤 = Fraction(48)  # Lower length (少袤)
程功 = Fraction(19, 10)  # Work per person per day (常積一尺九寸八分)
甲人 = 2375  # People from 甲縣
乙人 = 2378  # People from 乙縣
丙人 = 5247  # People from 丙縣

# Total people
總人 = 甲人 + 乙人 + 丙人

# Step 1: Calculate the total volume of the dam
堤積 = 程功 * 總人  # Total work volume
虛積 = 堤積 * 6  # 虛積 = 堤積 * 6

# Step 2: Calculate 隅冪 and 鱉隅積
隅冪 = 少高 * 少袤
鱉隅積 = 隅冪 * (少高 + 差)

# Step 3: Calculate the actual volume (實)
實 = (虛積 - 鱉隅積) / 3

# Step 4: Calculate 鱉從橫廉冪 and 方法
鱉從橫廉冪 = (少高 + 少袤) * (少高 + 差) * 少袤 / 3
方法 = 鱉從橫廉冪 + 隅冪

# Step 5: Calculate 廉法 and 下廣
廉法 = (少袤 + 少高 + (少高 + 差)) / 3
下廣 = (實 / 方法) ** Fraction(1, 3)

# Step 6: Calculate 上廣, 高, and 袤
c = 下廣
b = c + 差
a = b + 差
d = 少袤 + (實 / (少高 * 少袤))

# Step 7: Calculate contributions for each county
def calculate_county(人數, 上廣, 高, 袤):
    當積尺 = 程功 * 人數
    實 = (當積尺 * 6) / (袤 ** 2)
    廉法 = (上廣 * 高) / 實
    廉 = (實 / 廉法) ** Fraction(1, 3)
    袤 = 廉
    高 = (實 / (袤 * 上廣))
    上廣 = 上廣 + (實 / (袤 * 高))
    return 高, 袤, 上廣

# Calculate for 甲縣
e, f, g = calculate_county(甲人, b, a, d)

# Calculate for 乙縣
h, i, j = calculate_county(乙人, g, e, f)

# Calculate for 丙縣
k, l, m = calculate_county(丙人, j, h, i)

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


This code follows the ancient Chinese mathematical procedure step by step. It calculates the dimensions of the 龙尾堤 and the contributions of each county to its construction. The results are stored in variables `a`, `b`, `c`, `d`, `e`, `f`, `g`, `h`, `i`, `j`, `k`, `l`, and `m`.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 13.246032822762743
Variable 'b' has wrong value. Expected: 17/5, Actual: 7.246032822762742
Variable 'c' has wrong value. Expected: 9/5, Actual: 1.2460328227627417
Variable 'd' has wrong value. Expected: 33/5, Actual: 3887/36
Variable 'e' has wrong value. Expected: 3/2, Actual: 0.8367772665754748
Variable 'f' has wrong value. Expected: 33/10, Actual: 0.38303125705277713
Variable 'g' has wrong value. Expected: 21/10, Actual: 14.492065645525486
Variable 'h' has wrong value. Expected: 21/10, Actual: 9.02954470589382
Variable 'i' has wrong value. Expected: 33/25, Actual: 1412.0566645034228
Variable 'j' has wrong value. Expected: 111/50, Actual: 28.98413129105097
Variable 'k' has wrong value. Expected: 3, Actual: 0.06857286801359429
Variable 'l' has wrong value. Expected: 99/50, Actual: 0.015093816420431677
Variable 'm' has wrong value. Expected: 12/5, Actual: 57.96826258210194"""
