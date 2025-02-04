"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
求龍尾堤廣、袤、高，術曰：以程功乘總人，為堤積。又六因之，為虛積。以少高乘少袤，為隅冪。以少上廣乘之，為鱉隅積。以減虛積，余，三約之，所得為實。並少高、袤，以少上廣乘之，為鱉從橫廉冪。三而一，加隅冪，為方法。又三除少上廣，以少袤、少高加之，為廉法，從。開立方除之，得下廣。加差，即高、廣、袤。求逐縣均給積尺受廣、袤，術曰：以程功乘當縣人，當積尺。各六因積尺。又乘袤冪。廣差乘高，為法。除之，為實。又三因末廣，以袤乘之，廣差而一，為都廉，從。開立方除之，即甲袤。以本高乘之，以本袤除之，即甲高。又以廣差乘甲袤，以本袤除之，所得加末廣，即甲上廣。其甲上廣即乙末廣，其甲高即垣高。求實與都廉，如前。又並甲上下廣，三之，乘甲高，又乘袤冪，以法除之，得垣方，從。開立方除之，即乙袤。余放此。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
This problem is quite complex and involves multiple steps of calculation. I'll break it down into smaller parts and translate the procedure into Python code step by step. The calculations will follow the structure of the procedure ("術") provided.


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given data
差 = 6  # 上廣差
少高 = Fraction(12, 1)  # 少高 (1丈2尺 = 12尺)
少袤 = Fraction(48, 1)  # 少袤 (4丈8尺 = 48尺)
甲人 = 2375  # 甲縣人數
乙人 = 2378  # 乙縣人數
丙人 = 5247  # 丙縣人數
程功 = Fraction(19, 10) + Fraction(8, 100)  # 每人程功 (1尺9寸8分 = 1.98尺)

# Step 1: Calculate the total堤積
總人 = 甲人 + 乙人 + 丙人
堤積 = 程功 * 總人

# Step 2: Calculate虛積
虛積 = 堤積 * 6

# Step 3: Calculate隅冪 and鱉隅積
隅冪 = 少高 * 少袤
鱉隅積 = 隅冪 * (少高 + 差)

# Step 4: Calculate實
實 = (虛積 - 鱉隅積) / 3

# Step 5: Calculate方法
方法 = 隅冪 + (少高 * 少袤 * (少高 + 差) / 3)

# Step 6: Calculate廉法 and從
廉法 = (少袤 + 少高 + (少高 + 差) / 3) / (少高 + 差)
從 = (實 / 方法) ** Fraction(1, 3)

# Step 7: Calculate下廣, 高, 上廣, and袤
下廣 = 從
高 = 下廣 + 差
上廣 = 高 + 差
袤 = 高 + 少袤

# Step 8: Calculate各縣積尺 and廣,袤 for甲縣
甲積尺 = 程功 * 甲人
甲虛積 = 甲積尺 * 6
甲方法 = 方法
甲從 = (甲虛積 / 甲方法) ** Fraction(1, 3)
甲袤 = 甲從
甲高 = (甲袤 * 高) / 袤
甲上廣 = (甲袤 * (高 + 差)) / 袤 + 下廣

# Step 9: Repeat for乙縣 and丙縣
乙積尺 = 程功 * 乙人
乙虛積 = 乙積尺 * 6
乙方法 = 方法
乙從 = (乙虛積 / 乙方法) ** Fraction(1, 3)
乙袤 = 乙從
乙高 = (乙袤 * 高) / 袤
乙上廣 = (乙袤 * (高 + 差)) / 袤 + 下廣

丙積尺 = 程功 * 丙人
丙虛積 = 丙積尺 * 6
丙方法 = 方法
丙從 = (丙虛積 / 丙方法) ** Fraction(1, 3)
丙袤 = 丙從
丙高 = (丙袤 * 高) / 袤
丙上廣 = (丙袤 * (高 + 差)) / 袤 + 下廣

# Final results
a = 高 / 10  # Convert to丈
b = 上廣 / 10  # Convert to丈
c = 下廣 / 10  # Convert to丈
d = 袤 / 10  # Convert to丈
e = 甲高 / 10  # Convert to丈
f = 甲袤 / 10  # Convert to丈
g = 甲上廣 / 10  # Convert to丈
h = 乙高 / 10  # Convert to丈
i = 乙袤 / 10  # Convert to丈
j = 乙上廣 / 10  # Convert to丈
k = 丙高 / 10  # Convert to丈
l = 丙袤 / 10  # Convert to丈
m = 丙上廣 / 10  # Convert to丈

# Print results
print(f"高 {a}丈 ，上廣 {b}丈 ，下廣 {c}丈 ，袤 {d}丈")
print(f"甲縣高 {e}丈 ，袤 {f}丈 ，上廣 {g}丈")
print(f"乙縣高 {h}丈 ，袤 {i}丈 ，上廣 {j}丈")
print(f"丙縣高 {k}丈 ，袤 {l}丈 ，上廣 {m}丈")
#----- content ends here -----


"""


This Python code follows the procedure step by step to calculate the required values for the龍尾堤 and the contributions of each county. The results are expressed in丈 as requested.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 0.8077328741916263
Variable 'b' has wrong value. Expected: 17/5, Actual: 1.4077328741916264
Variable 'c' has wrong value. Expected: 9/5, Actual: 0.20773287419162628
Variable 'd' has wrong value. Expected: 33/5, Actual: 5.607732874191626
Variable 'e' has wrong value. Expected: 3/2, Actual: 0.027550762189442052
Variable 'f' has wrong value. Expected: 33/10, Actual: 0.19127278308857956
Variable 'g' has wrong value. Expected: 21/10, Actual: 0.25574888899346054
Variable 'h' has wrong value. Expected: 21/10, Actual: 0.027562357629442997
Variable 'i' has wrong value. Expected: 33/25, Actual: 0.1913532851111685
Variable 'j' has wrong value. Expected: 111/50, Actual: 0.2557690977562849
Variable 'k' has wrong value. Expected: 3, Actual: 0.035882506165952614
Variable 'l' has wrong value. Expected: 99/50, Actual: 0.24911640452491843
Variable 'm' has wrong value. Expected: 12/5, Actual: 0.2702696176524496"""
