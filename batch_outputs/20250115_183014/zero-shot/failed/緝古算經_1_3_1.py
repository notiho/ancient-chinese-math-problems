"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
求龍尾堤廣、袤、高，術曰：以程功乘總人，為堤積。又六因之，為虛積。以少高乘少袤，為隅冪。以少上廣乘之，為鱉隅積。以減虛積，余，三約之，所得為實。並少高、袤，以少上廣乘之，為鱉從橫廉冪。三而一，加隅冪，為方法。又三除少上廣，以少袤、少高加之，為廉法，從。開立方除之，得下廣。加差，即高、廣、袤。求逐縣均給積尺受廣、袤，術曰：以程功乘當縣人，當積尺。各六因積尺。又乘袤冪。廣差乘高，為法。除之，為實。又三因末廣，以袤乘之，廣差而一，為都廉，從。開立方除之，即甲袤。以本高乘之，以本袤除之，即甲高。又以廣差乘甲袤，以本袤除之，所得加末廣，即甲上廣。其甲上廣即乙末廣，其甲高即垣高。求實與都廉，如前。又並甲上下廣，三之，乘甲高，又乘袤冪，以法除之，得垣方，從。開立方除之，即乙袤。余放此。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical text into Python code. The problem involves calculating the dimensions of a dam (堤) and the contributions of three counties (甲, 乙, 丙) to its construction. The calculations involve determining the height (高), width (廣), and length (袤) of the dam, as well as the contributions of each county.

Here is the Python code:


"""


from fractions import Fraction

# Given data
差 = Fraction(6)  # Difference between upper and lower width (上廣 - 下廣)
少高 = Fraction(12)  # Lower height (少高) in 尺
少袤 = Fraction(48)  # Lower length (少袤) in 尺
程功 = Fraction(19, 10)  # Work done per person per day (程功) in 尺
甲人 = 2375  # Number of people in 甲縣
乙人 = 2378  # Number of people in 乙縣
丙人 = 5247  # Number of people in 丙縣

# Total people
總人 = 甲人 + 乙人 + 丙人

# Total work volume
堤積 = 程功 * 總人
虛積 = 堤積 * 6

# Calculating the dimensions of the dam
隅冪 = 少高 * 少袤
鱉隅積 = 隅冪 * (少高 + 差)
實 = (虛積 - 鱉隅積) / 3

鱉從橫廉冪 = (少高 + 差) * 少袤 * (少高 + 差) / 3 + 隅冪
廉法 = (少袤 + 少高 + (少高 + 差)) / 3
下廣 = (實 / 鱉從橫廉冪) ** Fraction(1, 3)
上廣 = 下廣 + 差
高 = 下廣 + 差
袤 = 少袤 + 差

# Assigning the results to variables
a = 高
b = 上廣
c = 下廣
d = 袤

# Contributions of each county
def calculate_county_contribution(縣人, 縣積尺):
    縣積尺 = 程功 * 縣人
    縣虛積 = 縣積尺 * 6
    縣實 = 縣虛積 / 鱉從橫廉冪
    縣袤 = (縣實 / 鱉從橫廉冪) ** Fraction(1, 3)
    縣高 = 縣袤 * 高 / 袤
    縣上廣 = 縣袤 * (上廣 - 下廣) / 袤 + 下廣
    return 縣高, 縣袤, 縣上廣

e, f, g = calculate_county_contribution(甲人, 堤積)
h, i, j = calculate_county_contribution(乙人, 堤積)
k, l, m = calculate_county_contribution(丙人, 堤積)

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


This Python code follows the ancient algorithm described in the problem. It calculates the dimensions of the dam and the contributions of each county. The results are stored in variables `a`, `b`, `c`, `d`, `e`, `f`, `g`, `h`, `i`, `j`, `k`, `l`, and `m`, which correspond to the unknowns in the problem.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 7.816840129701766
Variable 'b' has wrong value. Expected: 17/5, Actual: 7.816840129701766
Variable 'c' has wrong value. Expected: 9/5, Actual: 1.8168401297017656
Variable 'd' has wrong value. Expected: 33/5, Actual: 54
Variable 'e' has wrong value. Expected: 3/2, Actual: 0.013527326408891482
Variable 'f' has wrong value. Expected: 33/10, Actual: 0.0934489658173436
Variable 'g' has wrong value. Expected: 21/10, Actual: 1.8272233481259148
Variable 'h' has wrong value. Expected: 21/10, Actual: 0.013533019728759331
Variable 'i' has wrong value. Expected: 33/25, Actual: 0.09348829619480593
Variable 'j' has wrong value. Expected: 111/50, Actual: 1.8272277181678551
Variable 'k' has wrong value. Expected: 3, Actual: 0.01761818311734091
Variable 'l' has wrong value. Expected: 99/50, Actual: 0.12170926775404158
Variable 'm' has wrong value. Expected: 12/5, Actual: 1.830363381674437"""
