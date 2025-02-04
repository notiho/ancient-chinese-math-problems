"""
假令築堤，西頭上、下廣差六丈八尺二寸，東頭上、下廣差六尺二寸。東頭高少於西頭高三丈一尺，上廣多東頭高四尺九寸，正袤多於東頭高四百七十六尺九寸。甲縣六千七百二十四人，乙縣一萬六千六百七十七人，丙縣一萬九千四百四十八人，丁縣一萬二千七百八十一人。四縣每人一日穿土九石九斗二升。每人一日築常積一十一尺四寸十三分寸之六。穿方一尺得土八斗。古人負土二斗四升八合，平道行一百九十二步，一日六十二到。今隔山渡水取土，其平道只有一十一步，山斜高三十步，水寬一十二步，上山三當四，下山六當五，水行一當二，平道踟躕十加一，載輸一十四步。減計一人作功為均積。四縣共造，一日役華。今從東頭與甲，其次與乙、丙、丁。問：給斜、正袤與高，及下廣，並每人一日自穿、運、築程功，及堤上、下高、廣各幾何？
求人到程功運築積尺，術曰：置上山四十步，下山二十五步，渡水二十四步，平道一十一步，踟躕之間十加一，載輸一十四步，一返計一百二十四步。以古人負土二斗四升八合，平道行一百九十二步，以乘一日六十二到，為實。卻以一返步為法。除，得自運土到數也。又以一到負土數乘之，卻以穿方一尺土數除之，得一人一日運動積。又以一人穿土九石九斗二升，以穿方一尺土數除之，為法。除之，得穿用人數。復置運功積，以每人一日常積除之，得築用人數。並之，得六人。共成二十九尺七寸六分，以六人除之，即一人程功也。求堤上、下廣及高、袤，術曰：一人一日程功乘總人，為堤積。以高差乘下廣差，六而一，為鱉冪。又以高差乘小頭廣差，二而一，為大臥塹頭冪。又半高差，乘上廣多東頭高之數，為小臥塹頭冪。並三冪，為大小塹鱉率。乘正袤多小高之數，以減堤積，余為實。又置半高差及半小頭廣差與上廣多小頭高之數，並三差，以乘正袤多小頭高之數。以加率為方法。又並正袤多小頭高、上廣多小高及半高差，兼半小頭廣差加之，為廉法，從。開方立除之，即小高。加差，即各得廣、袤、高。又正袤自乘，高差自乘，並，而開方除之，即斜袤。求甲縣高、廣、正、斜袤，術曰：以程功乘甲縣人，以六因取積，又乘袤冪。以下廣差乘高差為法除之，為實。又並小頭上下廣，以乘小高，三因之，為垣頭冪。又乘袤冪，如法而一，為垣方。又三因小頭下廣，以乘正袤，以廣差除之，為都廉，從。開立方除之，得小頭袤，即甲袤。又以下廣差乘之，所得以正袤除之，所得加東頭下廣，即甲廣。又以兩頭高差乘甲袤，以正袤除之，以加東頭高，即甲高。又以甲袤自乘；以堤東頭高減甲高，余自乘，並二位，以開方除之，即得斜袤。若求乙、丙、丁，各以本縣人功積尺，每以前大高、廣為後小高、主廉母自乘，為方母。廉母乘方母，為實母。求堤都積，術曰：置西頭高，倍之，加東頭高，又並西頭上下廣，半而乘之。又置東頭高，倍之，加西頭高，又並東頭上下廣，半而乘之。並二位積，以正袤乘之，六而一，得堤積也。
答曰：一人一日自穿運築程功 a尺 ；西頭高 b丈 ，上廣 c尺 ，下廣 d丈 ，東頭高 e尺 ，上廣 f尺 ，下廣 g丈 ，正袤 h丈 ，斜袤 i丈 ；甲縣正袤 j丈 ，斜袤 k丈 ，下廣 l丈 ，高 m丈 ；乙縣正袤 n丈 ；斜袤 o丈 ，下廣 p丈 ，高 q丈 ；丙縣正袤 r丈 ，斜袤 s丈 ，下廣 t尺 ，高 u丈 ；丁縣正袤 v丈 ，斜袤 w丈 ，下廣 x丈 ，高 y丈 。
"""

"""
This problem is extremely complex and involves multiple steps of ancient Chinese mathematical procedures, including proportional calculations, geometric relationships, and iterative computations. Translating this into Python code requires careful decomposition of the problem into smaller steps. Below is a Python implementation of the problem, step by step, using the `Fraction` class for precise calculations.

---

### Python Code Implementation


"""

#----- content starts here -----

from fractions import Fraction
from math import sqrt

# Constants and initial values
穿方一尺得土 = Fraction(8, 10)  # 1 cubic chi of soil yields 8 dou of soil
古人負土 = Fraction(2, 1) + Fraction(4, 10) + Fraction(8, 100)  # 2 dou 4 sheng 8 ge
古人平道步 = 192  # 192 steps on flat ground
古人一日到數 = 62  # 62 trips per day
平道步 = 11  # Flat ground steps
山斜高 = 30  # Slope height in steps
水寬 = 12  # Water width in steps
上山比 = Fraction(3, 4)  # Ratio for climbing uphill
下山比 = Fraction(6, 5)  # Ratio for descending downhill
水行比 = Fraction(1, 2)  # Ratio for crossing water
踟躕加 = Fraction(10, 1) + Fraction(1, 1)  # Hesitation adds 10 + 1 steps
載輸步 = 14  # Steps for carrying soil
穿土每日 = Fraction(9, 1) + Fraction(9, 10) + Fraction(2, 100)  # 9 shi 9 dou 2 sheng per day
築常積 = Fraction(11, 1) + Fraction(4, 10) + Fraction(13, 100) + Fraction(6, 1000)  # 11 chi 4 cun 13 fen 6 li
甲縣人 = 6724
乙縣人 = 16677
丙縣人 = 19448
丁縣人 = 12781
總人數 = 甲縣人 + 乙縣人 + 丙縣人 + 丁縣人

# Step 1: Calculate one person's daily transportation work
一返步 = 平道步 + 山斜高 * 上山比 + 山斜高 * 下山比 + 水寬 * 水行比 + 踟躕加 + 載輸步
一返步 = int(一返步)  # Convert to integer for simplicity
負土每日步 = 古人負土 * 古人平道步 * 古人一日到數
自運土到數 = 負土每日步 / 一返步
自運土積 = 自運土到數 * 古人負土 / 穿方一尺得土

# Step 2: Calculate one person's daily excavation work
穿土積 = 穿土每日 / 穿方一尺得土

# Step 3: Calculate one person's daily construction work
築積 = 積 = 積#----- content ends here -----


"""

"""


"""
Code error: name '積' is not defined"""
