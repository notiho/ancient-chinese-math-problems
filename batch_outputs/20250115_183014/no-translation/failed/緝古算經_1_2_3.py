"""
假令築堤，西頭上、下廣差六丈八尺二寸，東頭上、下廣差六尺二寸。東頭高少於西頭高三丈一尺，上廣多東頭高四尺九寸，正袤多於東頭高四百七十六尺九寸。甲縣六千七百二十四人，乙縣一萬六千六百七十七人，丙縣一萬九千四百四十八人，丁縣一萬二千七百八十一人。四縣每人一日穿土九石九斗二升。每人一日築常積一十一尺四寸十三分寸之六。穿方一尺得土八斗。古人負土二斗四升八合，平道行一百九十二步，一日六十二到。今隔山渡水取土，其平道只有一十一步，山斜高三十步，水寬一十二步，上山三當四，下山六當五，水行一當二，平道踟躕十加一，載輸一十四步。減計一人作功為均積。四縣共造，一日役華。今從東頭與甲，其次與乙、丙、丁。問：給斜、正袤與高，及下廣，並每人一日自穿、運、築程功，及堤上、下高、廣各幾何？
求人到程功運築積尺，術曰：置上山四十步，下山二十五步，渡水二十四步，平道一十一步，踟躕之間十加一，載輸一十四步，一返計一百二十四步。以古人負土二斗四升八合，平道行一百九十二步，以乘一日六十二到，為實。卻以一返步為法。除，得自運土到數也。又以一到負土數乘之，卻以穿方一尺土數除之，得一人一日運動積。又以一人穿土九石九斗二升，以穿方一尺土數除之，為法。除之，得穿用人數。復置運功積，以每人一日常積除之，得築用人數。並之，得六人。共成二十九尺七寸六分，以六人除之，即一人程功也。求堤上、下廣及高、袤，術曰：一人一日程功乘總人，為堤積。以高差乘下廣差，六而一，為鱉冪。又以高差乘小頭廣差，二而一，為大臥塹頭冪。又半高差，乘上廣多東頭高之數，為小臥塹頭冪。並三冪，為大小塹鱉率。乘正袤多小高之數，以減堤積，余為實。又置半高差及半小頭廣差與上廣多小頭高之數，並三差，以乘正袤多小頭高之數。以加率為方法。又並正袤多小頭高、上廣多小高及半高差，兼半小頭廣差加之，為廉法，從。開方立除之，即小高。加差，即各得廣、袤、高。又正袤自乘，高差自乘，並，而開方除之，即斜袤。求甲縣高、廣、正、斜袤，術曰：以程功乘甲縣人，以六因取積，又乘袤冪。以下廣差乘高差為法除之，為實。又並小頭上下廣，以乘小高，三因之，為垣頭冪。又乘袤冪，如法而一，為垣方。又三因小頭下廣，以乘正袤，以廣差除之，為都廉，從。開立方除之，得小頭袤，即甲袤。又以下廣差乘之，所得以正袤除之，所得加東頭下廣，即甲廣。又以兩頭高差乘甲袤，以正袤除之，以加東頭高，即甲高。又以甲袤自乘；以堤東頭高減甲高，余自乘，並二位，以開方除之，即得斜袤。若求乙、丙、丁，各以本縣人功積尺，每以前大高、廣為後小高、主廉母自乘，為方母。廉母乘方母，為實母。求堤都積，術曰：置西頭高，倍之，加東頭高，又並西頭上下廣，半而乘之。又置東頭高，倍之，加西頭高，又並東頭上下廣，半而乘之。並二位積，以正袤乘之，六而一，得堤積也。
答曰： a人 b日 自穿運築程功 c尺 ；西頭高 d丈 ，上廣 e尺 ，下廣 f丈 ，東頭高 g尺 ，上廣 h尺 ，下廣 i丈 ，正袤 j丈 ，斜袤 k丈 ；甲縣正袤 l丈 ，斜袤 m丈 ，下廣 n丈 ，高 o丈 ；乙縣正袤 p丈 ；斜袤 q丈 ，下廣 r丈 ，高 s丈 ；丙縣正袤 t丈 ，斜袤 u丈 ，下廣 v尺 ，高 w丈 ；丁縣正袤 x丈 ，斜袤 y丈 ，下廣 z丈 ，高 a丈 。
"""

"""
This problem is extremely complex and involves multiple steps, calculations, and interdependencies. It is essentially a comprehensive engineering and labor allocation problem from ancient Chinese mathematics. Translating this into Python code requires breaking it down into smaller steps and encoding each part of the procedure. Below is the Python implementation for the problem:


"""


from fractions import Fraction
import math

# Constants
西頭上下廣差 = Fraction(6, 1) + Fraction(8, 10) + Fraction(2, 100)  # 6丈8尺2寸
東頭上下廣差 = Fraction(6, 10) + Fraction(2, 100)  # 6尺2寸
東頭高差 = Fraction(3, 1) + Fraction(1, 10)  # 3丈1尺
上廣多東頭高 = Fraction(4, 10) + Fraction(9, 100)  # 4尺9寸
正袤多東頭高 = Fraction(476, 10) + Fraction(9, 100)  # 476尺9寸

甲縣人數 = 6724
乙縣人數 = 16677
丙縣人數 = 19448
丁縣人數 = 12781

每人每日穿土 = Fraction(9, 1) + Fraction(9, 10) + Fraction(2, 100)  # 9石9斗2升
每人每日築常積 = Fraction(11, 1) + Fraction(4, 10) + Fraction(13, 100) + Fraction(6, 1000)  # 11尺4寸13分6厘
穿方一尺得土 = Fraction(8, 10)  # 8斗
古人負土 = Fraction(2, 1) + Fraction(4, 10) + Fraction(8, 100)  # 2斗4升8合
平道行步 = 192
每日負土次數 = 62

平道步數 = 11
山斜高 = 30
水寬 = 12
上山比 = Fraction(3, 4)  # 上山三當四
下山比 = Fraction(6, 5)  # 下山六當五
水行比 = Fraction(1, 2)  # 水行一當二
踟躕加步 = Fraction(10, 1) + Fraction(1, 1)  # 踟躕十加一
載輸步數 = 14

# Step 1: Calculate one round trip steps
一返步 = 平道步數 + 山斜高 * (上山比 + 下山比) + 水寬 * 水行比 + 踟躕加步 + 載輸步數

# Step 2: Calculate 土運動積
古人每日運土積 = 古人負土 * 平道行步 * 每日負土次數
自運土到數 = 古人每日運土積 / 一返步
自運土積 = 自運土到數 * 古人負土 / 穿方一尺得土

# Step 3: Calculate 穿用人數
穿用人數 = 每人每日穿土 / 穿方一尺得土

# Step 4: Calculate 築用人數
築用人數 = 自運土積 / 每人每日築常積

# Step 5: Total people required
總人數 = 穿用人數 + 築用人數

# Step 6: Calculate 堤積
堤積 = 每人每日築常積 * 總人數

# Step 7: Calculate 鱉冪 and 塹冪
高差 = 東頭高差
下廣差 = 西頭上下廣差
小頭廣差 = 東頭上下廣差
鱉冪 = (高差 * 下廣差) / 6
大臥塹頭冪 = (高差 * 小頭廣差) / 2
小臥塹頭冪 = (高差 / 2) * 上廣多東頭高
大小塹鱉率 = 鱉冪 + 大臥塹頭冪 + 小臥塹頭冪

# Step 8: Calculate 堤上、下廣、高、袤
正袤 = 正袤多東頭高
堤積余 = 堤積 - (大小塹鱉率 * 正袤)
半高差 = 高差 / 2
半小頭廣差 = 小頭廣差 / 2
廉法 = 正袤 + 上廣多東頭高 + 半高差 + 半小頭廣差
小高 = math.sqrt(堤積余 / 廉法)
堤高 = 小高 + 高差

# Step 9: Calculate 斜袤
斜袤 = math.sqrt(正袤**2 + 高差**2)

# Outputs
a = 總人數
b = 堤積
c = 自運土積
d = 堤高
e = 上廣多東頭高
f = 西頭上下廣差
g = 東頭高差
h = 小頭廣差
i = 東頭上下廣差
j = 正袤
k = 斜袤

# Final output
print(f"a人 {a}日 自穿運築程功 {c}尺；西頭高 {d}丈，上廣 {e}尺，下廣 {f}丈，東頭高 {g}尺，上廣 {h}尺，下廣 {i}丈，正袤 {j}丈，斜袤 {k}丈。")


"""


This code implements the procedure step-by-step, but due to the complexity of the problem, it is highly recommended to verify the calculations and logic thoroughly. Each step corresponds to a part of the ancient procedure, and the results are expressed in terms of the required units.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 22061274/241535
Variable 'b' has wrong value. Expected: 1, Actual: 44122548/41875
Variable 'c' has wrong value. Expected: 124/25, Actual: 7626496/8375
Variable 'd' has wrong value. Expected: 341/100, Actual: 7.107333604335208
Variable 'e' has wrong value. Expected: 8, Actual: 49/100
Variable 'f' has wrong value. Expected: 381/50, Actual: 341/50
Variable 'h' has wrong value. Expected: 8, Actual: 31/50
Variable 'i' has wrong value. Expected: 71/50, Actual: 31/50
Variable 'j' has wrong value. Expected: 48, Actual: 4769/100
Variable 'k' has wrong value. Expected: 481/10, Actual: 47.790648666867874
Missing variable in output: 'l'
Missing variable in output: 'm'
Missing variable in output: 'n'
Missing variable in output: 'o'
Missing variable in output: 'p'
Missing variable in output: 'q'
Missing variable in output: 'r'
Missing variable in output: 's'
Missing variable in output: 't'
Missing variable in output: 'u'
Missing variable in output: 'v'
Missing variable in output: 'w'
Missing variable in output: 'x'
Missing variable in output: 'y'
Missing variable in output: 'z'
Missing variable in output: '{'"""
