"""
今有粟八斗六升，欲為鑿飯。問︰得幾何？
術曰：以粟求鑿飯，二十四之，二十五而一。
荅曰：為鑿飯 a斗 。
"""

"""
To solve this problem, we need to calculate how much "鑿飯" (a type of processed grain) can be obtained from 8斗6升 of raw grain (粟). The method provided says to multiply the raw grain by 24 and then divide by 25.

### Assumptions:
1. 1斗 = 10升 (standard unit conversion in ancient Chinese measurements).
2. The total raw grain is 8斗6升 = 8 * 10 + 6 = 86升.

### Formula:
The amount of "鑿飯" obtained is calculated as:
\[ \text{鑿飯} = \frac{\text{raw grain} \times 24}{25} \]

### Python Code:

"""


from fractions import Fraction

# Total raw grain in 升
raw_grain = 8 * 10 + 6  # 8斗6升 = 86升

# Calculate 鑿飯
a = Fraction(raw_grain * 24, 25)  # Apply the formula

# Result
a  # a is in 升


"""


### Explanation:
1. Convert 8斗6升 into 升: \( 8 \times 10 + 6 = 86 \).
2. Multiply the raw grain (86升) by 24.
3. Divide the result by 25 to get the amount of "鑿飯" in 升.

### Final Answer:
The variable `a` will hold the amount of "鑿飯" in 升 as a fraction.
"""


"""
Variable 'a' has wrong value. Expected: 1032/125, Actual: 2064/25"""
