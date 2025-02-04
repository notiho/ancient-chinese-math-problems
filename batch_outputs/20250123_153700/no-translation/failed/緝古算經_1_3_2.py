"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
求龍尾堤廣、袤、高，術曰：以程功乘總人，為堤積。又六因之，為虛積。以少高乘少袤，為隅冪。以少上廣乘之，為鱉隅積。以減虛積，余，三約之，所得為實。並少高、袤，以少上廣乘之，為鱉從橫廉冪。三而一，加隅冪，為方法。又三除少上廣，以少袤、少高加之，為廉法，從。開立方除之，得下廣。加差，即高、廣、袤。求逐縣均給積尺受廣、袤，術曰：以程功乘當縣人，當積尺。各六因積尺。又乘袤冪。廣差乘高，為法。除之，為實。又三因末廣，以袤乘之，廣差而一，為都廉，從。開立方除之，即甲袤。以本高乘之，以本袤除之，即甲高。又以廣差乘甲袤，以本袤除之，所得加末廣，即甲上廣。其甲上廣即乙末廣，其甲高即垣高。求實與都廉，如前。又並甲上下廣，三之，乘甲高，又乘袤冪，以法除之，得垣方，從。開立方除之，即乙袤。余放此。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
This problem is highly complex and involves multiple steps of ancient Chinese mathematical procedures. I'll translate the problem into Python code step by step, adhering to the structure of the procedure ("術") provided.


"""


from fractions import Fraction
from math import pow

# Input data
甲縣人 = 2375
乙縣人 = 2378
丙縣人 = 5247
總人 = 甲縣人 + 乙縣人 + 丙縣人

程功 = Fraction(1, 1) + Fraction(9, 10) + Fraction(8, 100)  # 每人程功常積一尺九寸八分
少高 = Fraction(1, 1) + Fraction(2, 10)  # 少高一丈二尺
少袤 = Fraction(4, 1) + Fraction(8, 10)  # 少袤四丈八尺
少上廣 = Fraction(6, 1)  # 上廣差六尺

# Step 1: 求龍尾堤廣、袤、高
# 以程功乘總人，為堤積
堤積 = 程功 * 總人

# 又六因之，為虛積
虛積 = 6 * 堤積

# 以少高乘少袤，為隅冪
隅冪 = 少高 * 少袤

# 以少上廣乘之，為鱉隅積
鱉隅積 = 少上廣 * 隅冪

# 以減虛積，余，三約之，所得為實
實 = (虛積 - 鱉隅積) / 3

# 並少高、袤，以少上廣乘之，為鱉從橫廉冪
鱉從橫廉冪 = (少高 + 少袤) * 少上廣 / 3 + 隅冪

# 又三除少上廣，以少袤、少高加之，為廉法，從
廉法 = pow(鱉從橫廉冪, 1 / 3)  # 開立方除之，得下廣
下廣 = 廉法 + 少上廣

# 加差，即高、廣、袤
高 = 下廣
廣 = 下廣
袤 = 下廣

# Step 2: 求逐縣均給積尺受廣、袤
# For 甲縣
甲積尺 = 程功 * 甲縣人
甲虛積 = 6 * 甲積尺
甲實 = (甲虛積 - 鱉隅積) / 3
甲廉法 = pow(甲實, 1 / 3)
甲袤 = 甲廉法
甲高 = 甲袤
甲上廣 = 甲袤

# For 乙縣
乙積尺 = 程功 * 乙縣人
乙虛積 = 6 * 乙積尺
乙實 = (乙虛積 - 鱉隅積) / 3
乙廉法 = pow(乙實, 1 / 3)
乙袤 = 乙廉法
乙高 = 乙袤
乙上廣 = 乙袤

# For 丙縣
丙積尺 = 程功 * 丙縣人
丙虛積 = 6 * 丙積尺
丙實 = (丙虛積 - 鱉隅積) / 3
丙廉法 = pow(丙實, 1 / 3)
丙袤 = 丙廉法
丙高 = 丙袤
丙上廣 = 丙袤

# Final results
a = 高
b = 廣
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


"""


This code follows the structure of the ancient Chinese mathematical procedure provided. However, due to the complexity of the problem, some steps may require further refinement or clarification. Let me know if you'd like me to adjust or clarify any part of the solution.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 8.609041500040908
Variable 'b' has wrong value. Expected: 17/5, Actual: 8.609041500040908
Variable 'c' has wrong value. Expected: 9/5, Actual: 8.609041500040908
Variable 'd' has wrong value. Expected: 33/5, Actual: 8.609041500040908
Variable 'e' has wrong value. Expected: 3/2, Actual: 21.099662326229826
Variable 'f' has wrong value. Expected: 33/10, Actual: 21.099662326229826
Variable 'g' has wrong value. Expected: 21/10, Actual: 21.099662326229826
Variable 'h' has wrong value. Expected: 21/10, Actual: 21.10855354263568
Variable 'i' has wrong value. Expected: 33/25, Actual: 21.10855354263568
Variable 'j' has wrong value. Expected: 111/50, Actual: 21.10855354263568
Variable 'k' has wrong value. Expected: 3, Actual: 27.48664916680466
Variable 'l' has wrong value. Expected: 99/50, Actual: 27.48664916680466
Variable 'm' has wrong value. Expected: 12/5, Actual: 27.48664916680466"""
