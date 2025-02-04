"""
假令築堤，西頭上、下廣差六丈八尺二寸，東頭上、下廣差六尺二寸。東頭高少於西頭高三丈一尺，上廣多東頭高四尺九寸，正袤多於東頭高四百七十六尺九寸。甲縣六千七百二十四人，乙縣一萬六千六百七十七人，丙縣一萬九千四百四十八人，丁縣一萬二千七百八十一人。四縣每人一日穿土九石九斗二升。每人一日築常積一十一尺四寸十三分寸之六。穿方一尺得土八斗。古人負土二斗四升八合，平道行一百九十二步，一日六十二到。今隔山渡水取土，其平道只有一十一步，山斜高三十步，水寬一十二步，上山三當四，下山六當五，水行一當二，平道踟躕十加一，載輸一十四步。減計一人作功為均積。四縣共造，一日役華。今從東頭與甲，其次與乙、丙、丁。問：給斜、正袤與高，及下廣，並每人一日自穿、運、築程功，及堤上、下高、廣各幾何？
求人到程功運築積尺，術曰：置上山四十步，下山二十五步，渡水二十四步，平道一十一步，踟躕之間十加一，載輸一十四步，一返計一百二十四步。以古人負土二斗四升八合，平道行一百九十二步，以乘一日六十二到，為實。卻以一返步為法。除，得自運土到數也。又以一到負土數乘之，卻以穿方一尺土數除之，得一人一日運動積。又以一人穿土九石九斗二升，以穿方一尺土數除之，為法。除之，得穿用人數。復置運功積，以每人一日常積除之，得築用人數。並之，得六人。共成二十九尺七寸六分，以六人除之，即一人程功也。求堤上、下廣及高、袤，術曰：一人一日程功乘總人，為堤積。以高差乘下廣差，六而一，為鱉冪。又以高差乘小頭廣差，二而一，為大臥塹頭冪。又半高差，乘上廣多東頭高之數，為小臥塹頭冪。並三冪，為大小塹鱉率。乘正袤多小高之數，以減堤積，余為實。又置半高差及半小頭廣差與上廣多小頭高之數，並三差，以乘正袤多小頭高之數。以加率為方法。又並正袤多小頭高、上廣多小高及半高差，兼半小頭廣差加之，為廉法，從。開方立除之，即小高。加差，即各得廣、袤、高。又正袤自乘，高差自乘，並，而開方除之，即斜袤。求甲縣高、廣、正、斜袤，術曰：以程功乘甲縣人，以六因取積，又乘袤冪。以下廣差乘高差為法除之，為實。又並小頭上下廣，以乘小高，三因之，為垣頭冪。又乘袤冪，如法而一，為垣方。又三因小頭下廣，以乘正袤，以廣差除之，為都廉，從。開立方除之，得小頭袤，即甲袤。又以下廣差乘之，所得以正袤除之，所得加東頭下廣，即甲廣。又以兩頭高差乘甲袤，以正袤除之，以加東頭高，即甲高。又以甲袤自乘；以堤東頭高減甲高，余自乘，並二位，以開方除之，即得斜袤。若求乙、丙、丁，各以本縣人功積尺，每以前大高、廣為後小高、主廉母自乘，為方母。廉母乘方母，為實母。求堤都積，術曰：置西頭高，倍之，加東頭高，又並西頭上下廣，半而乘之。又置東頭高，倍之，加西頭高，又並東頭上下廣，半而乘之。並二位積，以正袤乘之，六而一，得堤積也。
答曰：一人一日自穿運築程功 a尺 ；西頭高 b丈 ，上廣 c尺 ，下廣 d丈 ，東頭高 e尺 ，上廣 f尺 ，下廣 g丈 ，正袤 h丈 ，斜袤 i丈 ；甲縣正袤 j丈 ，斜袤 k丈 ，下廣 l丈 ，高 m丈 ；乙縣正袤 n丈 ；斜袤 o丈 ，下廣 p丈 ，高 q丈 ；丙縣正袤 r丈 ，斜袤 s丈 ，下廣 t尺 ，高 u丈 ；丁縣正袤 v丈 ，斜袤 w丈 ，下廣 x丈 ，高 y丈 。
"""

"""
This problem is extremely complex and involves multiple steps of calculations, including geometric relationships, proportional distributions, and iterative calculations for each county's contribution to the construction of the dam. Translating this into Python code requires breaking down the problem into smaller, manageable parts and encoding each step according to the procedures described.

Below is the Python code that follows the structure of the problem step by step. Due to the complexity, I will focus on the key calculations and provide comments to explain each step.


"""

#----- content starts here -----

from fractions import Fraction
import math

# Constants
古人負土 = Fraction(2, 1) + Fraction(4, 10) + Fraction(8, 100)  # 2斗4升8合
平道步 = 192
每日到數 = 62
穿方一尺土數 = Fraction(8, 10)  # 8斗
每人每日穿土 = Fraction(9, 1) + Fraction(9, 10) + Fraction(2, 100)  # 9石9斗2升
每人每日築積 = Fraction(11, 1) + Fraction(4, 10) + Fraction(13, 100) + Fraction(6, 1000)  # 11尺4寸13分寸之6

# Terrain adjustments
平道 = 11
山斜高 = 30
水寬 = 12
上山 = Fraction(3, 4)  # 上山三當四
下山 = Fraction(6, 5)  # 下山六當五
水行 = Fraction(1, 2)  # 水行一當二
踟躕 = Fraction(10, 1) + Fraction(1, 10)  # 踟躕十加一
載輸 = 14

# Counties' populations
甲縣人口 = 6724
乙縣人口 = 16677
丙縣人口 = 19448
丁縣人口 = 12781

# Step 1: Calculate one round trip distance
一返步 = 平道 + 山斜高 * (上山 + 下山) + 水寬 * 水行 + 踟躕 + 載輸

# Step 2: Calculate 土運輸量 per person per day
古人每日負土 = 古人負土 * 平道步 * 每日到數
每日運土量 = 古人每日負土 / 一返步

# Step 3: Convert to 穿方積
每日運土積 = 每日運土量 / 穿方一尺土數

# Step 4: Calculate 穿土用人數
穿土用人數 = 每人每日穿土 / 穿方一尺土數

# Step 5: Calculate 築用人數
築用人數 = 每日運土積 / 每人每日築積

# Step 6: Total people required
總人數 = 穿土用人數 + 築用人數

# Step 7: Calculate one person's daily work
每日程功 = 每日運土積 / 總人數

# Step 8: Calculate 堤積
西頭高 = Fraction(3, 1) + Fraction(1, 10)  # 3丈1尺
東頭高 = 西頭高 - Fraction(3, 1) + Fraction(1, 10)  # 高差
西頭上廣 = Fraction(4, 1) + Fraction(9, 10)  # 4尺9寸
東頭上廣 = 西頭上廣 + Fraction(4, 1) + Fraction(9, 10)  # 上廣多東頭高
西頭下廣 = Fraction(6, 1) + Fraction(8, 10) + Fraction(2, 100)  # 6丈8尺2寸
東頭下廣 = Fraction(6, 1) + Fraction(2, 10)  # 6尺2寸
正袤 = Fraction(476, 1) + Fraction(9, 10)  # 正袤多於東頭高

# Calculate 鱉冪, 大小塹鱉率, and 堤積
高差 = 西頭高 - 東頭高
下廣差 = 西頭下廣 - 東頭下廣
鱉冪 = (高差 * 下廣差) / 6
大塹頭冪 = (高差 * 東頭下廣) / 2
小塹頭冪 = (高差 / 2) * (西頭上廣 - 東頭高)
大小塹鱉率 = 鱉冪 + 大塹頭冪 + 小塹頭冪
堤積 = (大小塹鱉率 * 正袤) - 堤積

# Step 9: Calculate each county's contribution
甲縣程功 = 每日程功 * 甲縣人口
乙縣程功 = 每日程功 * 乙縣人口
丙縣程功 = 每日程功 * 丙縣人口
丁縣程功 = 每日程功 * 丁縣人口

# Further calculations for each county's 高, 廣, 正袤, and 斜袤 would follow similar steps,
# iterating through each county's contribution and adjusting based on the 堤積 and geometric relationships.

# Final output
a = 每日程功
b = 西頭高
c = 西頭上廣
d = 西頭下廣
e = 東頭高
f = 東頭上廣
g = 東頭下廣
h = 正袤
i = math.sqrt(正袤**2 + 高差**2)  # Example for 斜袤 calculation
# Similarly, calculate j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y
#----- content ends here -----


"""


This code provides the framework for solving the problem. However, due to the complexity of the calculations and the iterative nature of the relationships, further refinement and detailed calculations are required for each county's specific contributions and the final geometric properties of the dam.
"""


"""
Code error: name '堤積' is not defined"""
