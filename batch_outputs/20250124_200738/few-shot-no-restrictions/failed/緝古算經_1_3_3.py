"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
求龍尾堤廣、袤、高，術曰：以程功乘總人，為堤積。又六因之，為虛積。以少高乘少袤，為隅冪。以少上廣乘之，為鱉隅積。以減虛積，余，三約之，所得為實。並少高、袤，以少上廣乘之，為鱉從橫廉冪。三而一，加隅冪，為方法。又三除少上廣，以少袤、少高加之，為廉法，從。開立方除之，得下廣。加差，即高、廣、袤。求逐縣均給積尺受廣、袤，術曰：以程功乘當縣人，當積尺。各六因積尺。又乘袤冪。廣差乘高，為法。除之，為實。又三因末廣，以袤乘之，廣差而一，為都廉，從。開立方除之，即甲袤。以本高乘之，以本袤除之，即甲高。又以廣差乘甲袤，以本袤除之，所得加末廣，即甲上廣。其甲上廣即乙末廣，其甲高即垣高。求實與都廉，如前。又並甲上下廣，三之，乘甲高，又乘袤冪，以法除之，得垣方，從。開立方除之，即乙袤。余放此。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
This is a complex ancient Chinese problem involving the construction of a tapered dam (referred to as "Dragon Tail Dam") with varying dimensions and contributions from three counties. The problem involves calculating the dimensions of the dam (height, width, and length) as well as the contributions of each county in terms of the dam's dimensions.

To solve this problem step by step, we will translate the ancient procedure into Python code. The solution involves calculating the total volume of the dam, distributing the work among the counties, and determining the specific dimensions for each county's contribution.

### Problem Breakdown:
1. **Input Data:**
   - The dam tapers from a wider top to a narrower bottom.
   - The difference between the top and bottom widths is 6 chi (尺).
   - The bottom width is 1 zhang 2 chi (12 chi).
   - The bottom height is 1 zhang 2 chi (12 chi).
   - The bottom length is 4 zhang 8 chi (48 chi).
   - The work contribution per person is 1 chi 9 cun 8 fen (1.98 chi³).
   - The number of workers from each county:
     - County A: 2375 people
     - County B: 2378 people
     - County C: 5247 people

2. **Procedure:**
   - Calculate the total volume of the dam.
   - Distribute the work among the counties based on their number of workers.
   - Calculate the dimensions (height, width, and length) of the dam for each county's contribution.

3. **Output:**
   - The total dimensions of the dam (height, top width, bottom width, and length).
   - The dimensions of the dam contributed by each county.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Input data
差 = 6  # Difference between top and bottom widths (chi)
少下廣 = Fraction(12)  # Bottom width (chi)
少高 = Fraction(12)  # Bottom height (chi)
少袤 = Fraction(48)  # Bottom length (chi)
程功 = Fraction(1, 1) + Fraction(9, 10) + Fraction(8, 100)  # Work per person (chi³)
甲人 = 2375  # Workers from County A
乙人 = 2378  # Workers from County B
丙人 = 5247  # Workers from County C

# Step 1: Calculate the total volume of the dam
總人 = 甲人 + 乙人 + 丙人  # Total workers
堤積 = 程功 * 總人  # Total volume of the dam (chi³)

# Step 2: Calculate the "虚积" (virtual volume)
虛積 = 堤積 * 6

# Step 3: Calculate the "隅冪" (corner area)
隅冪 = 少高 * 少袤

# Step 4: Calculate the "鱉隅積" (tapered corner volume)
鱉隅積 = 隅冪 * 少下廣

# Step 5: Subtract 虛積 to get the remaining volume
餘積 = 虛積 - 鱉隅積

# Step 6: Divide by 3 to get the "實積" (actual volume)
實積 = 餘積 / 3

# Step 7: Calculate the "鱉從橫廉冪" (tapered horizontal area)
鱉從橫廉冪 = (少高 + 少袤) * 少下廣 / 3 + 隅冪

# Step 8: Calculate the "方法" (method divisor)
方法 = 鱉從橫廉冪 / 3

# Step 9: Calculate the bottom width
下廣 = pow(float(實積 / 方法), 1/3)

# Step 10: Calculate the top width, height, and length
上廣 = 下廣 + 差
高 = 少高 + 差
袤 = 少袤 + 差

# Step 11: Distribute the work among the counties
def calculate_county_dimensions(人數, 程功, 上廣, 下廣, 高, 袤):
    當積尺 = 程功 * 人數  # Volume contributed by the county
    實積 = 當積尺 * 6  # Adjusted volume
    廣差 = 上廣 - 下廣  # Width difference
    法 = 廣差 * 高  # Divisor
    廣 = pow(float(實積 / 法), 1/3)  # Width
    高 = 高  # Height remains the same
    袤 = pow(float(實積 / (廣差 * 高)), 1/3)  # Length
    return 高, 袤, 廣

# Calculate dimensions for each county
甲高, 甲袤, 甲上廣 = calculate_county_dimensions(甲人, 程功, 上廣, 下廣, 高, 袤)
乙高, 乙袤, 乙上廣 = calculate_county_dimensions(乙人, 程功, 上廣, 下廣, 高, 袤)
丙高, 丙袤, 丙上廣 = calculate_county_dimensions(丙人, 程功, 上廣, 下廣, 高, 袤)

# Output results
print(f"Total Dam Dimensions: 高 {高}丈, 上廣 {上廣}丈, 下廣 {下廣}丈, 袤 {袤}丈")
print(f"County A Dimensions: 高 {甲高}丈, 袤 {甲袤}丈, 上廣 {甲上廣}丈")
print(f"County B Dimensions: 高 {乙高}丈, 袤 {乙袤}丈, 上廣 {乙上廣}丈")
print(f"County C Dimensions: 高 {丙高}丈, 袤 {丙袤}丈, 上廣 {丙上廣}丈")
#----- content ends here -----


"""


### Explanation:
1. **Total Volume Calculation:** The total volume of the dam is calculated based on the number of workers and their work contribution.
2. **Virtual Volume Adjustment:** The virtual volume is used to account for the tapering shape of the dam.
3. **County Contributions:** Each county's contribution is calculated proportionally based on the number of workers.
4. **Dimensions Calculation:** The height, width, and length for each county's contribution are calculated using the given formulas.

### Output:
The program will output the total dimensions of the dam and the dimensions for each county's contribution.
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'
Missing variable in output: 'g'
Missing variable in output: 'h'
Missing variable in output: 'i'
Missing variable in output: 'j'
Missing variable in output: 'k'
Missing variable in output: 'l'
Missing variable in output: 'm'"""
