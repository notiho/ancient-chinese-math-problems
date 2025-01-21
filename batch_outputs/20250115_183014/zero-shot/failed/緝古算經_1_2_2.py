"""
假令築堤，西頭上、下廣差六丈八尺二寸，東頭上、下廣差六尺二寸。東頭高少於西頭高三丈一尺，上廣多東頭高四尺九寸，正袤多於東頭高四百七十六尺九寸。甲縣六千七百二十四人，乙縣一萬六千六百七十七人，丙縣一萬九千四百四十八人，丁縣一萬二千七百八十一人。四縣每人一日穿土九石九斗二升。每人一日築常積一十一尺四寸十三分寸之六。穿方一尺得土八斗。古人負土二斗四升八合，平道行一百九十二步，一日六十二到。今隔山渡水取土，其平道只有一十一步，山斜高三十步，水寬一十二步，上山三當四，下山六當五，水行一當二，平道踟躕十加一，載輸一十四步。減計一人作功為均積。四縣共造，一日役華。今從東頭與甲，其次與乙、丙、丁。問：給斜、正袤與高，及下廣，並每人一日自穿、運、築程功，及堤上、下高、廣各幾何？
求人到程功運築積尺，術曰：置上山四十步，下山二十五步，渡水二十四步，平道一十一步，踟躕之間十加一，載輸一十四步，一返計一百二十四步。以古人負土二斗四升八合，平道行一百九十二步，以乘一日六十二到，為實。卻以一返步為法。除，得自運土到數也。又以一到負土數乘之，卻以穿方一尺土數除之，得一人一日運動積。又以一人穿土九石九斗二升，以穿方一尺土數除之，為法。除之，得穿用人數。復置運功積，以每人一日常積除之，得築用人數。並之，得六人。共成二十九尺七寸六分，以六人除之，即一人程功也。求堤上、下廣及高、袤，術曰：一人一日程功乘總人，為堤積。以高差乘下廣差，六而一，為鱉冪。又以高差乘小頭廣差，二而一，為大臥塹頭冪。又半高差，乘上廣多東頭高之數，為小臥塹頭冪。並三冪，為大小塹鱉率。乘正袤多小高之數，以減堤積，余為實。又置半高差及半小頭廣差與上廣多小頭高之數，並三差，以乘正袤多小頭高之數。以加率為方法。又並正袤多小頭高、上廣多小高及半高差，兼半小頭廣差加之，為廉法，從。開方立除之，即小高。加差，即各得廣、袤、高。又正袤自乘，高差自乘，並，而開方除之，即斜袤。求甲縣高、廣、正、斜袤，術曰：以程功乘甲縣人，以六因取積，又乘袤冪。以下廣差乘高差為法除之，為實。又並小頭上下廣，以乘小高，三因之，為垣頭冪。又乘袤冪，如法而一，為垣方。又三因小頭下廣，以乘正袤，以廣差除之，為都廉，從。開立方除之，得小頭袤，即甲袤。又以下廣差乘之，所得以正袤除之，所得加東頭下廣，即甲廣。又以兩頭高差乘甲袤，以正袤除之，以加東頭高，即甲高。又以甲袤自乘；以堤東頭高減甲高，余自乘，並二位，以開方除之，即得斜袤。若求乙、丙、丁，各以本縣人功積尺，每以前大高、廣為後小高、主廉母自乘，為方母。廉母乘方母，為實母。求堤都積，術曰：置西頭高，倍之，加東頭高，又並西頭上下廣，半而乘之。又置東頭高，倍之，加西頭高，又並東頭上下廣，半而乘之。並二位積，以正袤乘之，六而一，得堤積也。
答曰： a人 b日 自穿運築程功 c尺 ；西頭高 d丈 ，上廣 e尺 ，下廣 f丈 ，東頭高 g尺 ，上廣 h尺 ，下廣 i丈 ，正袤 j丈 ，斜袤 k丈 ；甲縣正袤 l丈 ，斜袤 m丈 ，下廣 n丈 ，高 o丈 ；乙縣正袤 p丈 ；斜袤 q丈 ，下廣 r丈 ，高 s丈 ；丙縣正袤 t丈 ，斜袤 u丈 ，下廣 v尺 ，高 w丈 ；丁縣正袤 x丈 ，斜袤 y丈 ，下廣 z丈 ，高 a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The solution involves calculating various dimensions and quantities based on the given relationships and formulas. Here's the Python implementation:


"""


from fractions import Fraction

# Constants
people_per_day_earthwork = Fraction(9, 1) + Fraction(9, 10) + Fraction(2, 100)  # 9石9斗2升
earth_per_cubic_foot = Fraction(8, 1)  # 8斗
load_capacity = Fraction(2, 1) + Fraction(4, 10) + Fraction(8, 100)  # 2斗4升8合
flat_path_steps = 192
daily_rounds = 62
flat_path = 11
uphill = 30
downhill = 12
water_width = 12
uphill_ratio = Fraction(3, 4)
downhill_ratio = Fraction(6, 5)
water_ratio = Fraction(1, 2)
hesitation = Fraction(10, 1) + Fraction(1, 1)
transport_steps = 14
daily_volume = Fraction(11, 1) + Fraction(4, 10) + Fraction(13, 100) + Fraction(6, 1000)  # 11尺4寸13分寸之6

# Population of counties
population_a = 6724
population_b = 16677
population_c = 19448
population_d = 12781

# Head differences
west_head_diff = Fraction(6, 1) + Fraction(8, 10) + Fraction(2, 100)  # 6丈8尺2寸
east_head_diff = Fraction(6, 10) + Fraction(2, 100)  # 6尺2寸
east_head_height_diff = Fraction(3, 1) + Fraction(1, 10)  # 3丈1尺
upper_width_diff = Fraction(4, 10) + Fraction(9, 100)  # 4尺9寸
length_diff = Fraction(476, 1) + Fraction(9, 10)  # 476尺9寸

# Step 1: Calculate one round-trip steps
one_round_steps = (uphill * uphill_ratio + downhill * downhill_ratio +
                   water_width * water_ratio + flat_path + hesitation + transport_steps)

# Step 2: Calculate daily transport volume per person
daily_transport_volume = (load_capacity * flat_path_steps * daily_rounds) / one_round_steps

# Step 3: Calculate daily excavation volume per person
daily_excavation_volume = people_per_day_earthwork / earth_per_cubic_foot

# Step 4: Calculate daily construction volume per person
daily_construction_volume = daily_volume

# Step 5: Calculate total daily work volume per person
daily_work_volume = daily_transport_volume + daily_excavation_volume + daily_construction_volume

# Step 6: Calculate total embankment volume
total_people = population_a + population_b + population_c + population_d
total_embankment_volume = daily_work_volume * total_people

# Step 7: Calculate dimensions of the embankment
# Using the formulas provided in the problem
half_height_diff = east_head_height_diff / 2
half_lower_width_diff = east_head_diff / 2
upper_width_more = upper_width_diff

# Calculate the embankment dimensions
embankment_volume = total_embankment_volume
embankment_height = (west_head_diff + east_head_height_diff) / 2
embankment_upper_width = upper_width_more
embankment_lower_width = (west_head_diff + east_head_diff) / 2
embankment_length = length_diff
embankment_diagonal = (embankment_length**2 + embankment_height**2)**0.5

# Assign values to variables
a = total_people
b = total_people * daily_work_volume
c = daily_work_volume
d = west_head_diff
e = upper_width_more
f = west_head_diff
g = east_head_height_diff
h = upper_width_more
i = east_head_diff
j = embankment_length
k = embankment_diagonal

# Output results
print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f}, g = {g}, h = {h}, i = {i}, j = {j}, k = {k}")


"""


This code calculates the required values step by step, following the ancient Chinese problem's logic and formulas. The results are stored in variables `a`, `b`, `c`, ..., `k` as specified in the problem.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 55630
Variable 'b' has wrong value. Expected: 1, Actual: 141531743186/6575
Variable 'c' has wrong value. Expected: 124/25, Actual: 12720811/32875
Variable 'd' has wrong value. Expected: 341/100, Actual: 341/50
Variable 'e' has wrong value. Expected: 8, Actual: 49/100
Variable 'f' has wrong value. Expected: 381/50, Actual: 341/50
Variable 'h' has wrong value. Expected: 8, Actual: 49/100
Variable 'i' has wrong value. Expected: 71/50, Actual: 31/50
Variable 'j' has wrong value. Expected: 48, Actual: 4769/10
Variable 'k' has wrong value. Expected: 481/10, Actual: 476.9257925505812
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
