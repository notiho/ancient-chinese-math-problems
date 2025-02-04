"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
求龍尾堤廣、袤、高，術曰：以程功乘總人，為堤積。又六因之，為虛積。以少高乘少袤，為隅冪。以少上廣乘之，為鱉隅積。以減虛積，余，三約之，所得為實。並少高、袤，以少上廣乘之，為鱉從橫廉冪。三而一，加隅冪，為方法。又三除少上廣，以少袤、少高加之，為廉法，從。開立方除之，得下廣。加差，即高、廣、袤。求逐縣均給積尺受廣、袤，術曰：以程功乘當縣人，當積尺。各六因積尺。又乘袤冪。廣差乘高，為法。除之，為實。又三因末廣，以袤乘之，廣差而一，為都廉，從。開立方除之，即甲袤。以本高乘之，以本袤除之，即甲高。又以廣差乘甲袤，以本袤除之，所得加末廣，即甲上廣。其甲上廣即乙末廣，其甲高即垣高。求實與都廉，如前。又並甲上下廣，三之，乘甲高，又乘袤冪，以法除之，得垣方，從。開立方除之，即乙袤。余放此。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
This problem is a complex ancient Chinese mathematical problem involving the construction of a "Dragon Tail Dam" (龍尾堤). It requires calculating the dimensions of the dam (height, length, and width) and distributing the workload among three counties based on their labor contributions. The solution involves multiple steps, including volume calculations, proportional distributions, and cubic root extractions.

Below is the Python implementation of the solution:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given data
差 = 6  # Difference between top and bottom widths (in chi)
少下廣 = Fraction(12, 1)  # Bottom width at the tail (in chi)
少高 = Fraction(12, 1)  # Height at the tail (in chi)
少袤 = Fraction(48, 1)  # Length at the tail (in chi)

甲縣人 = 2375  # Number of workers in County A
乙縣人 = 2378  # Number of workers in County B
丙縣人 = 5247  # Number of workers in County C

程功 = Fraction(19, 10)  # Work completed per person per day (in cubic chi)

# Step 1: Calculate the total volume of the dam
總人 = 甲縣人 + 乙縣人 + 丙縣人  # Total number of workers
堤積 = 程功 * 總人  # Total volume of the dam (in cubic chi)

# Step 2: Calculate the "虚积" (virtual volume)
虛積 = 堤積 * 6

# Step 3: Calculate the "隅冪" (corner area) and "鱉隅積" (corner volume)
隅冪 = 少高 * 少袤
鱉隅積 = 隅冪 * 少下廣

# Step 4: Subtract the virtual volume to get the real volume
實積 = (虛積 - 鱉隅積) / 3

# Step 5: Calculate the "方法" (method volume)
鱉從橫廉冪 = (少高 + 少袤) * 少下廣 / 3 + 隅冪
方法 = 鱉從橫廉冪 / 3

# Step 6: Calculate the bottom width (下廣)
下廣 = pow(float(實積 / 方法), 1/3)

# Step 7: Calculate the top width (上廣), height (高), and length (袤)
上廣 = 下廣 + 差
高 = 上廣 - 差
袤 = 實積 / (高 * (上廣 + 下廣) / 2)

# Step 8: Calculate the workload distribution for each county
def calculate_county_dimensions(縣人, 縣名, 上廣, 高, 袤):
    當積尺 = 程功 * 縣人
    當積尺虛 = 當積尺 * 6
    廣差 = 差
    廣法 = 高 * 廣差
    縣袤 = pow(float(當積尺虛 / 廣法), 1/3)
    縣高 = 高 * 縣袤 / 袤
    縣上廣 = 廣差 * 縣袤 / 袤 + 上廣
    return 縣高, 縣袤, 縣上廣

甲高, 甲袤, 甲上廣 = calculate_county_dimensions(甲縣人, "甲縣", 上廣, 高, 袤)
乙高, 乙袤, 乙上廣 = calculate_county_dimensions(乙縣人, "乙縣", 甲上廣, 甲高, 甲袤)
丙高, 丙袤, 丙上廣 = calculate_county_dimensions(丙縣人, "丙縣", 乙上廣, 乙高, 乙袤)

# Final results
print(f"龍尾堤總體: 高 {高}丈，上廣 {上廣}丈，下廣 {下廣}丈，袤 {袤}丈")
print(f"甲縣: 高 {甲高}丈，袤 {甲袤}丈，上廣 {甲上廣}丈")
print(f"乙縣: 高 {乙高}丈，袤 {乙袤}丈，上廣 {乙上廣}丈")
print(f"丙縣: 高 {丙高}丈，袤 {丙袤}丈，上廣 {丙上廣}丈")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**: The given dimensions, differences, and worker contributions are translated into Python variables.
2. **Volume Calculations**: The total volume of the dam is calculated based on the work completed by all workers.
3. **Virtual and Real Volume**: Intermediate calculations for virtual and real volumes are performed using the given formulas.
4. **Dimensions of the Dam**: The bottom width, top width, height, and length of the dam are calculated using the formulas provided in the problem.
5. **County Workload Distribution**: The workload for each county is calculated proportionally, and their respective dimensions are determined.
6. **Output**: The final dimensions of the dam and the contributions of each county are printed.

This code follows the ancient procedure described in the problem and provides the required dimensions for the dam and the contributions of each county.
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
