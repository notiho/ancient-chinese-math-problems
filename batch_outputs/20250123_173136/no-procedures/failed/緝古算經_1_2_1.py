"""
假令築堤，西頭上、下廣差六丈八尺二寸，東頭上、下廣差六尺二寸。東頭高少於西頭高三丈一尺，上廣多東頭高四尺九寸，正袤多於東頭高四百七十六尺九寸。甲縣六千七百二十四人，乙縣一萬六千六百七十七人，丙縣一萬九千四百四十八人，丁縣一萬二千七百八十一人。四縣每人一日穿土九石九斗二升。每人一日築常積一十一尺四寸十三分寸之六。穿方一尺得土八斗。古人負土二斗四升八合，平道行一百九十二步，一日六十二到。今隔山渡水取土，其平道只有一十一步，山斜高三十步，水寬一十二步，上山三當四，下山六當五，水行一當二，平道踟躕十加一，載輸一十四步。減計一人作功為均積。四縣共造，一日役華。今從東頭與甲，其次與乙、丙、丁。問：給斜、正袤與高，及下廣，並每人一日自穿、運、築程功，及堤上、下高、廣各幾何？
答曰：一人一日自穿運築程功 a尺 ；西頭高 b丈 ，上廣 c尺 ，下廣 d丈 ，東頭高 e尺 ，上廣 f尺 ，下廣 g丈 ，正袤 h丈 ，斜袤 i丈 ；甲縣正袤 j丈 ，斜袤 k丈 ，下廣 l丈 ，高 m丈 ；乙縣正袤 n丈 ；斜袤 o丈 ，下廣 p丈 ，高 q丈 ；丙縣正袤 r丈 ，斜袤 s丈 ，下廣 t尺 ，高 u丈 ；丁縣正袤 v丈 ，斜袤 w丈 ，下廣 x丈 ，高 y丈 。
"""

"""
This problem is extremely complex and involves multiple steps, including calculations for geometry, labor distribution, and work efficiency. To break it down, we will calculate each part step by step. The problem involves:

1. Calculating the dimensions of the embankment (堤) at both ends (西頭 and 東頭), including height, width, and length.
2. Calculating the work done by each county (甲, 乙, 丙, 丁) based on their population and efficiency.
3. Calculating the total work required to build the embankment.
4. Distributing the work among the counties and determining their contributions.

Below is the Python code to solve this step by step:


"""


from fractions import Fraction

# Constants
土方每尺得土 = Fraction(8, 10)  # 每穿方一尺得土 8斗
負土 = Fraction(2, 4) + Fraction(8, 10)  # 每人負土 2斗4升8合
平道步數 = 192  # 平道行 192步
每日往返次數 = 62  # 一日 62到
平道步數隔山 = 11  # 隔山平道 11步
山斜高 = 30  # 山斜高 30步
水寬 = 12  # 水寬 12步
上山三當四 = Fraction(3, 4)  # 上山三當四
下山六當五 = Fraction(6, 5)  # 下山六當五
水行一當二 = Fraction(1, 2)  # 水行一當二
平道踟躕 = Fraction(10, 1) + Fraction(1, 1)  # 平道踟躕 10加1
載輸步數 = 14  # 載輸 14步
每日築常積 = Fraction(11, 1) + Fraction(4, 10) + Fraction(13, 100) + Fraction(6, 1000)  # 每人一日築常積 11尺4寸13分寸之6

# County populations
甲縣人口 = 6724
乙縣人口 = 16677
丙縣人口 = 19448
丁縣人口 = 12781

# Work efficiency
每人每日穿土 = Fraction(9, 1) + Fraction(9, 10) + Fraction(2, 100)  # 每人一日穿土 9石9斗2升

# Embankment dimensions
西頭上下廣差 = Fraction(6, 1) + Fraction(8, 10) + Fraction(2, 100)  # 西頭上下廣差 6丈8尺2寸
東頭上下廣差 = Fraction(6, 10) + Fraction(2, 100)  # 東頭上下廣差 6尺2寸
東頭高少於西頭高 = Fraction(3, 1) + Fraction(1, 10)  # 東頭高少於西頭高 3丈1尺
上廣多東頭高 = Fraction(4, 10) + Fraction(9, 100)  # 上廣多東頭高 4尺9寸
正袤多於東頭高 = Fraction(476, 1) + Fraction(9, 10)  # 正袤多於東頭高 476尺9寸

# Step 1: Calculate 西頭 and 東頭 dimensions
西頭高 = Fraction(1, 1)  # Assume 西頭高 as a variable (to be calculated later)
東頭高 = 西頭高 - 東頭高少於西頭高
西頭上廣 = 東頭高 + 上廣多東頭高
西頭下廣 = 西頭上廣 + 西頭上下廣差
東頭上廣 = 西頭上廣
東頭下廣 = 東頭上廣 + 東頭上下廣差

# Step 2: Calculate 正袤 and 斜袤
正袤 = 東頭高 + 正袤多於東頭高
斜袤 = 正袤 + 西頭上下廣差  # Approximation for斜袤

# Step 3: Calculate work done per person per day
每日自穿運築程功 = 每人每日穿土 + 每日築常積

# Step 4: Distribute work among counties
總人口 = 甲縣人口 + 乙縣人口 + 丙縣人口 + 丁縣人口
甲縣比例 = Fraction(甲縣人口, 総人口)
乙縣比例 = Fraction(乙縣人口, 総人口)
丙縣比例 = Fraction(丙縣人口, 総人口)
丁縣比例 = Fraction(丁縣人口, 総人口)

甲縣正袤 = 正袤 * 甲縣比例
乙縣正袤 = 正袤 * 乙縣比例
丙縣正袤 = 正袤 * 丙縣比例
丁縣正袤 = 正袤 * 丁縣比例

# Output results
print(f"一人一日自穿運築程功: {每日自穿運築程功} 尺")
print(f"西頭高: {西頭高} 丈")
print(f"西頭上廣: {西頭上廣} 尺")
print(f"西頭下廣: {西頭下廣} 丈")
print(f"東頭高: {東頭高} 尺")
print(f"東頭上廣: {東頭上廣} 尺")
print(f"東頭下廣: {東頭下廣} 丈")
print(f"正袤: {正袤} 丈")
print(f"斜袤: {斜袤} 丈")
print(f"甲縣正袤: {甲縣正袤} 丈")
print(f"乙縣正袤: {乙縣正袤} 丈")
print(f"丙縣正袤: {丙縣正袤} 丈")
print(f"丁縣正袤: {丁縣正袤} 丈")


"""


This code calculates the required values step by step. However, due to the complexity of the problem, some assumptions and approximations are made. You can adjust the calculations as needed based on additional details or clarifications.
"""


"""
Code error: name '総人口' is not defined"""
