"""
假令築堤西頭上下廣差六丈八尺二寸東頭上下廣差六尺二寸東頭高少於西頭高三丈一尺上廣多東頭高四尺九寸正袤多於東頭高四百七十六尺九寸甲縣六千七百二十四人乙縣一萬六千六百七十七人丙縣一萬九千四百四十八人丁縣一萬二千七百八十一人四縣每人一日穿土九石九斗二升每人一日築常積一十一尺四寸十三分寸之六穿方一尺得土八斗古人負土二斗四升八合平道行一百九十二步一日六十二到今隔山渡水取土其平道只有一十一步山斜高三十步水寬一十二步上山三當四下山六當五水行一當二平道踟躕十加一載輸一十四步減計一人作功為均積四縣共造一日役華今從東頭與甲其次與乙丙丁問給斜正袤與高及下廣並每人一日自穿運築程功及堤上下高廣各幾何
求人到程功運築積尺術曰置上山四十步下山二十五步渡水二十四步平道一十一步踟躕之間十加一載輸一十四步一返計一百二十四步以古人負土二斗四升八合平道行一百九十二步以乘一日六十二到為實卻以一返步為法除得自運土到數也又以一到負土數乘之卻以穿方一尺土數除之得一人一日運動積又以一人穿土九石九斗二升以穿方一尺土數除之為法除之得穿用人數復置運功積以每人一日常積除之得築用人數並之得六人共成二十九尺七寸六分以六人除之即一人程功也求堤上下廣及高袤術曰一人一日程功乘總人為堤積以高差乘下廣差六而一為鱉冪又以高差乘小頭廣差二而一為大臥塹頭冪又半高差乘上廣多東頭高之數為小臥塹頭冪並三冪為大小塹鱉率乘正袤多小高之數以減堤積余為實又置半高差及半小頭廣差與上廣多小頭高之數並三差以乘正袤多小頭高之數以加率為方法又並正袤多小頭高上廣多小高及半高差兼半小頭廣差加之為廉法從開方立除之即小高加差即各得廣袤高又正袤自乘高差自乘並而開方除之即斜袤求甲縣高廣正斜袤術曰以程功乘甲縣人以六因取積又乘袤冪以下廣差乘高差為法除之為實又並小頭上下廣以乘小高三因之為垣頭冪又乘袤冪如法而一為垣方又三因小頭下廣以乘正袤以廣差除之為都廉從開立方除之得小頭袤即甲袤又以下廣差乘之所得以正袤除之所得加東頭下廣即甲廣又以兩頭高差乘甲袤以正袤除之以加東頭高即甲高又以甲袤自乘以堤東頭高減甲高余自乘並二位以開方除之即得斜袤若求乙丙丁各以本縣人功積尺每以前大高廣為後小高主廉母自乘為方母廉母乘方母為實母求堤都積術曰置西頭高倍之加東頭高又並西頭上下廣半而乘之又置東頭高倍之加西頭高又並東頭上下廣半而乘之並二位積以正袤乘之六而一得堤積也
答曰 a人 b日 自穿運築程功 c尺 西頭高 d丈 上廣 e尺 下廣 f丈 東頭高 g尺 上廣 h尺 下廣 i丈 正袤 j丈 斜袤 k丈 甲縣正袤 l丈 斜袤 m丈 下廣 n丈 高 o丈 乙縣正袤 p丈 斜袤 q丈 下廣 r丈 高 s丈 丙縣正袤 t丈 斜袤 u丈 下廣 v尺 高 w丈 丁縣正袤 x丈 斜袤 y丈 下廣 z丈 高 a丈 
"""

"""
This problem is extremely complex and involves multiple steps, calculations, and interdependencies. It is essentially a comprehensive engineering and labor allocation problem, combining geometry, arithmetic, and logistics. Translating this into Python code requires breaking it down into manageable parts and encoding each step of the procedure systematically.

Here is the Python code for this problem:


"""


from fractions import Fraction
from math import sqrt

# Constants and initial values
穿方一尺土數 = Fraction(8, 1)  # 每穿方一尺得土8斗
古人負土 = Fraction(2, 4) + Fraction(8, 10)  # 古人負土2斗4升8合
平道步數 = 192  # 平道行192步
一日到數 = 62  # 一日62到
隔山渡水平道步數 = 11  # 隔山渡水平道11步
上山步數 = 30  # 山斜高30步
水寬步數 = 12  # 水宽12步
上山三當四 = Fraction(4, 3)  # 上山3当4
下山六當五 = Fraction(5, 6)  # 下山6当5
水行一當二 = Fraction(2, 1)  # 水行1当2
踟躕十加一 = Fraction(11, 10)  # 踟躕10加1
載輸十四步減 = Fraction(14, 1)  # 载输14步减

# Step 1: Calculate one round trip steps
上山步 = 上山步數 * 上山三當四
下山步 = 上山步數 * 下山六當五
水步 = 水寬步數 * 水行一當二
平道步 = 隔山渡水平道步數
踟躕步 = 平道步 * 踟躕十加一
載輸步 = 載輸十四步減
一返步 = 上山步 + 下山步 + 水步 + 平道步 + 踟躕步 + 載輸步

# Step 2: Calculate self-transport soil trips
自運土到數 = Fraction(古人負土 * 一日到數, 一返步)

# Step 3: Calculate one person's daily soil transport and construction
一人一日運土積 = Fraction(自運土到數 * 古人負土, 穿方一尺土數)
一人一日穿土積 = Fraction(Fraction(9, 1) + Fraction(9, 10) + Fraction(2, 100), 穿方一尺土數)
一人一日築積 = Fraction(11, 1) + Fraction(4, 10) + Fraction(13, 100) + Fraction(6, 1000)

# Step 4: Calculate total labor and construction
四縣人數 = 6724 + 16677 + 19448 + 12781
總人程功 = 一人一日運土積 + 一人一日穿土積 + 一人一日築積
堤積 = 總人程功 * 四縣人數

# Step 5: Calculate geometric properties of the dam
西頭高 = Fraction(3, 1) + Fraction(1, 10)
東頭高 = 西頭高 - Fraction(3, 1) - Fraction(1, 10)
高差 = 西頭高 - 東頭高
西頭上下廣差 = Fraction(6, 1) + Fraction(8, 10) + Fraction(2, 100)
東頭上下廣差 = Fraction(6, 10) + Fraction(2, 100)
上廣多東頭高 = Fraction(4, 1) + Fraction(9, 10)
正袤多東頭高 = Fraction(476, 1) + Fraction(9, 10)

# Calculate the geometric properties (continued)
鱉冪 = Fraction(高差 * 西頭上下廣差, 6)
大臥塹頭冪 = Fraction(高差 * 東頭上下廣差, 2)
小臥塹頭冪 = Fraction(Fraction(高差, 2) * 上廣多東頭高, 1)
大小塹鱉率 = 鱉冪 + 大臥塹頭冪 + 小臥塹頭冪

# Calculate remaining dam properties
實 = 堤積 - (大小塹鱉率 * 正袤多東頭高)
方法 = (Fraction(高差, 2) + Fraction(東頭上下廣差, 2) + 上廣多東頭高) * 正袤多東頭高
廉法 = 正袤多東頭高 + 上廣多東頭高 + Fraction(高差, 2) + Fraction(東頭上下廣差, 2)
小高 = sqrt(Fraction(實, 方法))
正袤 = sqrt(Fraction(實, 廉法))
斜袤 = sqrt(正袤**2 + 高差**2)

# Output results
a = 四縣人數
b = 1  # One day of work
c = 總人程功
d = 西頭高
e = 上廣多東頭高
f = 西頭上下廣差
g = 東頭高
h = 上廣多東頭高
i = 東頭上下廣差
j = 正袤
k = 斜袤

print(f"a人: {a}, b日: {b}, 自穿運築程功: {c}尺")
print(f"西頭高: {d}丈, 上廣: {e}尺, 下廣: {f}丈")
print(f"東頭高: {g}尺, 上廣: {h}尺, 下廣: {i}丈")
print(f"正袤: {j}丈, 斜袤: {k}丈")


"""


This code calculates the required values step by step according to the procedure described in the problem. Note that this is a simplified version of the problem, and further refinements may be necessary to handle all edge cases and ensure accuracy.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 55630
Variable 'c' has wrong value. Expected: 124/25, Actual: 1249347/97000
Variable 'd' has wrong value. Expected: 341/100, Actual: 31/10
Variable 'e' has wrong value. Expected: 8, Actual: 49/10
Variable 'f' has wrong value. Expected: 381/50, Actual: 341/50
Variable 'g' has wrong value. Expected: 31/10, Actual: 0
Variable 'h' has wrong value. Expected: 8, Actual: 49/10
Variable 'i' has wrong value. Expected: 71/50, Actual: 31/50
Variable 'j' has wrong value. Expected: 48, Actual: 38.33426781058832
Variable 'k' has wrong value. Expected: 481/10, Actual: 38.45940832324268
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
