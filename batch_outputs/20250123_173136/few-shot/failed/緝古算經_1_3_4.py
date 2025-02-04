"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
求龍尾堤廣、袤、高，術曰：以程功乘總人，為堤積。又六因之，為虛積。以少高乘少袤，為隅冪。以少上廣乘之，為鱉隅積。以減虛積，余，三約之，所得為實。並少高、袤，以少上廣乘之，為鱉從橫廉冪。三而一，加隅冪，為方法。又三除少上廣，以少袤、少高加之，為廉法，從。開立方除之，得下廣。加差，即高、廣、袤。求逐縣均給積尺受廣、袤，術曰：以程功乘當縣人，當積尺。各六因積尺。又乘袤冪。廣差乘高，為法。除之，為實。又三因末廣，以袤乘之，廣差而一，為都廉，從。開立方除之，即甲袤。以本高乘之，以本袤除之，即甲高。又以廣差乘甲袤，以本袤除之，所得加末廣，即甲上廣。其甲上廣即乙末廣，其甲高即垣高。求實與都廉，如前。又並甲上下廣，三之，乘甲高，又乘袤冪，以法除之，得垣方，從。開立方除之，即乙袤。余放此。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
This problem is very complex and involves multiple steps of calculation. I'll break it down into smaller parts and encode the procedure step by step in Python. The problem involves calculating the dimensions of a trapezoidal dam (龍尾堤) and distributing the work among three counties (甲縣, 乙縣, 丙縣). Let's proceed:

### Definitions and Initial Values


### Step 1: Calculate the total dam volume


### Step 2: Calculate the dimensions of the dam


### Step 3: Distribute the work among counties


### Final Answer

"""


from fractions import Fraction

# Initial values
差 = 6  # Difference between top and bottom width (in chi)
少高 = Fraction(12, 1)  # Lower height (in chi, 1丈 = 10尺)
少袤 = Fraction(48, 1)  # Lower length (in chi, 1丈 = 10尺)
少上廣 = Fraction(6, 1)  # Lower top width (in chi)
少下廣 = 少上廣 - 差  # Lower bottom width (in chi)

# People from each county
甲縣人 = 2375
乙縣人 = 2378
丙縣人 = 5247

# Work per person per day
程功 = Fraction(19, 10)  # 1尺9寸8分 = 1.98尺

# Total number of people
總人 = 甲縣人 + 乙縣人 + 丙縣人

# Total dam volume
堤積 = 程功 * 總人

# 虛積 (虚 volume)
虛積 = 堤積 * 6

# 隅冪 (corner area)
隅冪 = 少高 * 少袤

# 鱉隅積 (trapezoidal corner volume)
鱉隅積 = 隅冪 * 少上廣

# Subtract 虛積 to get the remaining volume
余 = 虛積 - 鱉隅積

# Divide by 3 to get the actual volume
實 = Fraction(余, 3)

# Combine lower height and length
少高袤 = 少高 + 少袤

# 鱉從橫廉冪 (trapezoidal cross-sectional area)
鱉從橫廉冪 = (少高袤 * 少上廣) / 3 + 隅冪

# 廉法 (width law)
廉法 = (少上廣 / 3) + 少高袤

# Solve for 下廣 (bottom width)
下廣 = (實 / 鱉從橫廉冪) ** Fraction(1, 3)

# Calculate the top width, height, and length
上廣 = 下廣 + 差
高 = 下廣
袤 = 下廣

# Function to calculate dimensions for each county
def calculate_county_dimensions(縣人, 上廣, 高, 袤):
    # Calculate the total work for the county
    當積尺 = 程功 * 縣人

    # Multiply by 6 to get the adjusted volume
    積尺 = 當積尺 * 6

    # Calculate the trapezoidal cross-sectional area
    廣差 = 上廣 - 少上廣
    法 = 廣差 * 高

    # Solve for the length
    縣袤 = (積尺 / 法) ** Fraction(1, 3)

    # Solve for the height
    縣高 = (高 * 縣袤) / 袤

    # Solve for the top width
    縣上廣 = (廣差 * 縣袤) / 袤 + 少上廣

    return 縣高, 縣袤, 縣上廣

# Calculate dimensions for each county
甲高, 甲袤, 甲上廣 = calculate_county_dimensions(甲縣人, 上廣, 高, 袤)
乙高, 乙袤, 乙上廣 = calculate_county_dimensions(乙縣人, 上廣, 高, 袤)
丙高, 丙袤, 丙上廣 = calculate_county_dimensions(丙縣人, 上廣, 高, 袤)

# Final dimensions of the dam
a = 高 / 10  # Convert to 丈
b = 上廣 / 10  # Convert to 丈
c = 下廣 / 10  # Convert to 丈
d = 袤 / 10  # Convert to 丈

# Dimensions for each county
e = 甲高 / 10  # Convert to 丈
f = 甲袤 / 10  # Convert to 丈
g = 甲上廣 / 10  # Convert to 丈

h = 乙高 / 10  # Convert to 丈
i = 乙袤 / 10  # Convert to 丈
j = 乙上廣 / 10  # Convert to 丈

k = 丙高 / 10  # Convert to 丈
l = 丙袤 / 10  # Convert to 丈
m = 丙上廣 / 10  # Convert to 丈

# Print the results
print(f"高 {a}丈 ，上廣 {b}丈 ，下廣 {c}丈 ，袤 {d}丈")
print(f"甲縣高 {e}丈 ，袤 {f}丈 ，上廣 {g}丈")
print(f"乙縣高 {h}丈 ，袤 {i}丈 ，上廣 {j}丈")
print(f"丙縣高 {k}丈 ，袤 {l}丈 ，上廣 {m}丈")


"""


This code follows the procedure described in the problem and calculates the required dimensions for the dam and the work distribution among the counties.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 0.3754927536806519
Variable 'b' has wrong value. Expected: 17/5, Actual: 0.9754927536806519
Variable 'c' has wrong value. Expected: 9/5, Actual: 0.3754927536806519
Variable 'd' has wrong value. Expected: 33/5, Actual: 0.3754927536806519
Variable 'e' has wrong value. Expected: 3/2, Actual: 1.2429541676302966
Variable 'f' has wrong value. Expected: 33/10, Actual: 1.2429541676302966
Variable 'g' has wrong value. Expected: 21/10, Actual: 1.8429541676302967
Variable 'h' has wrong value. Expected: 21/10, Actual: 1.2434772965504906
Variable 'i' has wrong value. Expected: 33/25, Actual: 1.2434772965504906
Variable 'j' has wrong value. Expected: 111/50, Actual: 1.8434772965504904
Variable 'k' has wrong value. Expected: 3, Actual: 1.6188412602640176
Variable 'l' has wrong value. Expected: 99/50, Actual: 1.6188412602640176
Variable 'm' has wrong value. Expected: 12/5, Actual: 2.218841260264018"""
