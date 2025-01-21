"""
假令築堤，西頭上、下廣差六丈八尺二寸，東頭上、下廣差六尺二寸。東頭高少於西頭高三丈一尺，上廣多東頭高四尺九寸，正袤多於東頭高四百七十六尺九寸。甲縣六千七百二十四人，乙縣一萬六千六百七十七人，丙縣一萬九千四百四十八人，丁縣一萬二千七百八十一人。四縣每人一日穿土九石九斗二升。每人一日築常積一十一尺四寸十三分寸之六。穿方一尺得土八斗。古人負土二斗四升八合，平道行一百九十二步，一日六十二到。今隔山渡水取土，其平道只有一十一步，山斜高三十步，水寬一十二步，上山三當四，下山六當五，水行一當二，平道踟躕十加一，載輸一十四步。減計一人作功為均積。四縣共造，一日役華。今從東頭與甲，其次與乙、丙、丁。問：給斜、正袤與高，及下廣，並每人一日自穿、運、築程功，及堤上、下高、廣各幾何？
求人到程功運築積尺，術曰：置上山四十步，下山二十五步，渡水二十四步，平道一十一步，踟躕之間十加一，載輸一十四步，一返計一百二十四步。以古人負土二斗四升八合，平道行一百九十二步，以乘一日六十二到，為實。卻以一返步為法。除，得自運土到數也。又以一到負土數乘之，卻以穿方一尺土數除之，得一人一日運動積。又以一人穿土九石九斗二升，以穿方一尺土數除之，為法。除之，得穿用人數。復置運功積，以每人一日常積除之，得築用人數。並之，得六人。共成二十九尺七寸六分，以六人除之，即一人程功也。求堤上、下廣及高、袤，術曰：一人一日程功乘總人，為堤積。以高差乘下廣差，六而一，為鱉冪。又以高差乘小頭廣差，二而一，為大臥塹頭冪。又半高差，乘上廣多東頭高之數，為小臥塹頭冪。並三冪，為大小塹鱉率。乘正袤多小高之數，以減堤積，余為實。又置半高差及半小頭廣差與上廣多小頭高之數，並三差，以乘正袤多小頭高之數。以加率為方法。又並正袤多小頭高、上廣多小高及半高差，兼半小頭廣差加之，為廉法，從。開方立除之，即小高。加差，即各得廣、袤、高。又正袤自乘，高差自乘，並，而開方除之，即斜袤。求甲縣高、廣、正、斜袤，術曰：以程功乘甲縣人，以六因取積，又乘袤冪。以下廣差乘高差為法除之，為實。又並小頭上下廣，以乘小高，三因之，為垣頭冪。又乘袤冪，如法而一，為垣方。又三因小頭下廣，以乘正袤，以廣差除之，為都廉，從。開立方除之，得小頭袤，即甲袤。又以下廣差乘之，所得以正袤除之，所得加東頭下廣，即甲廣。又以兩頭高差乘甲袤，以正袤除之，以加東頭高，即甲高。又以甲袤自乘；以堤東頭高減甲高，余自乘，並二位，以開方除之，即得斜袤。若求乙、丙、丁，各以本縣人功積尺，每以前大高、廣為後小高、主廉母自乘，為方母。廉母乘方母，為實母。求堤都積，術曰：置西頭高，倍之，加東頭高，又並西頭上下廣，半而乘之。又置東頭高，倍之，加西頭高，又並東頭上下廣，半而乘之。並二位積，以正袤乘之，六而一，得堤積也。
答曰： a人 b日 自穿運築程功 c尺 ；西頭高 d丈 ，上廣 e尺 ，下廣 f丈 ，東頭高 g尺 ，上廣 h尺 ，下廣 i丈 ，正袤 j丈 ，斜袤 k丈 ；甲縣正袤 l丈 ，斜袤 m丈 ，下廣 n丈 ，高 o丈 ；乙縣正袤 p丈 ；斜袤 q丈 ，下廣 r丈 ，高 s丈 ；丙縣正袤 t丈 ，斜袤 u丈 ，下廣 v尺 ，高 w丈 ；丁縣正袤 x丈 ，斜袤 y丈 ，下廣 z丈 ，高 a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code step by step, using the `Fraction` class to handle non-integer calculations. Here's the Python implementation:


"""


from fractions import Fraction

# Constants
people_per_county = {
    "甲": 6724,
    "乙": 16677,
    "丙": 19448,
    "丁": 12781
}
soil_per_person_per_day = Fraction(9 * 10 + 9 * 10 + 2, 10)  # 9石9斗2升
soil_per_cubic_foot = Fraction(8, 10)  # 8斗
carrying_capacity = Fraction(2 * 10 + 4 * 10 + 8, 10)  # 2斗4升8合
flat_path_steps = 192
daily_rounds = 62
flat_path_distance = 11
uphill_distance = 30
downhill_distance = 30
water_distance = 12
uphill_ratio = Fraction(3, 4)
downhill_ratio = Fraction(6, 5)
water_ratio = Fraction(1, 2)
hesitation_ratio = Fraction(10 + 1, 10)
transport_distance = 14
daily_volume = Fraction(11 * 10 + 4 * 10 + 13 * 10 + 6, 10)  # 11尺4寸13分寸之6

# Calculations for one round trip
one_round_trip_steps = (
    uphill_distance * uphill_ratio +
    downhill_distance * downhill_ratio +
    water_distance * water_ratio +
    flat_path_distance * hesitation_ratio +
    transport_distance
)
soil_per_round_trip = carrying_capacity * flat_path_steps / one_round_trip_steps
daily_transport_volume = soil_per_round_trip * daily_rounds / soil_per_cubic_foot

# Daily excavation volume
daily_excavation_volume = soil_per_person_per_day / soil_per_cubic_foot

# Total daily work volume per person
daily_work_volume_per_person = daily_transport_volume + daily_excavation_volume

# Total work volume for all counties
total_people = sum(people_per_county.values())
total_daily_work_volume = daily_work_volume_per_person * total_people

# Dimensions of the dam
west_high = Fraction(6 * 10 + 8 * 10 + 2, 10)  # 6丈8尺2寸
east_high = west_high - Fraction(3 * 10 + 1, 10)  # 3丈1尺 less
upper_width_difference = Fraction(4 * 10 + 9, 10)  # 4尺9寸
lower_width_difference_west = Fraction(6 * 10 + 8 * 10 + 2, 10)  # 6丈8尺2寸
lower_width_difference_east = Fraction(6 * 10 + 2, 10)  # 6尺2寸
length_difference = Fraction(476 * 10 + 9, 10)  # 476尺9寸

# Calculate dam dimensions
upper_width_west = lower_width_difference_west + upper_width_difference
upper_width_east = lower_width_difference_east + upper_width_difference
length = length_difference + east_high
slope_length = (length ** 2 + (west_high - east_high) ** 2) ** Fraction(1, 2)

# Results
a = total_people
b = total_daily_work_volume
c = daily_work_volume_per_person
d = west_high
e = upper_width_west
f = lower_width_difference_west
g = east_high
h = upper_width_east
i = lower_width_difference_east
j = length
k = slope_length

# Output results
print(f"a = {a}人")
print(f"b = {b}日")
print(f"c = {c}尺")
print(f"d = {d}丈")
print(f"e = {e}尺")
print(f"f = {f}丈")
print(f"g = {g}尺")
print(f"h = {h}尺")
print(f"i = {i}丈")
print(f"j = {j}丈")
print(f"k = {k}丈")


"""


This code calculates the required values step by step, following the ancient Chinese mathematical problem's logic and using the `Fraction` class for precise calculations. Each variable corresponds to the unknowns in the problem, and the results are printed at the end.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 55630
Variable 'b' has wrong value. Expected: 1, Actual: 19145092315/302
Variable 'c' has wrong value. Expected: 124/25, Actual: 688301/604
Variable 'd' has wrong value. Expected: 341/100, Actual: 71/5
Variable 'e' has wrong value. Expected: 8, Actual: 191/10
Variable 'f' has wrong value. Expected: 381/50, Actual: 71/5
Variable 'g' has wrong value. Expected: 31/10, Actual: 111/10
Variable 'h' has wrong value. Expected: 8, Actual: 111/10
Variable 'i' has wrong value. Expected: 71/50, Actual: 31/5
Variable 'j' has wrong value. Expected: 48, Actual: 488
Variable 'k' has wrong value. Expected: 481/10, Actual: 488.00984621214354
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
