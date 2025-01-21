"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
術曰：以入表乘表間為實。相多為法，除之。加入表，即得松高。求表去山遠近者：置表間，以前表卻行乘之為實。相多為法，除之，得山去表。
答曰：松高 a丈 ；山去表 b里 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the height of a tree (松高, represented as `a`) and the distance from the mountain to the table (山去表, represented as `b`). Here's the Python code:


"""


from fractions import Fraction

# Given data
height_of_table = Fraction(2)  # 2丈
distance_between_tables = Fraction(50)  # 50步
front_table_to_observer = Fraction(7) + Fraction(4, 10)  # 7步4尺 = 7.4步
rear_table_to_observer = Fraction(8) + Fraction(5, 10)  # 8步5尺 = 8.5步
front_table_entry = Fraction(2, 10) + Fraction(8, 100)  # 2尺8寸 = 0.28步

# Step 1: Calculate the height of the tree (松高, a)
# Formula: a = (入表 * 表間) / (前後相去 - 入表) + 表高
a = (front_table_entry * distance_between_tables) / (front_table_to_observer - front_table_entry) + height_of_table

# Step 2: Calculate the distance from the mountain to the table (山去表, b)
# Formula: b = (表間 * 前表卻行) / (前後相去 - 入表)
b = (distance_between_tables * front_table_to_observer) / (front_table_to_observer - front_table_entry)

# Results
a  # 松高 in 丈
b  # 山去表 in 步


"""


### Explanation of the Code:
1. **Given Data**: The problem provides measurements in 丈 (zhang), 步 (bu), 尺 (chi), and 寸 (cun). These are converted into consistent units (步) using the relationships: 1丈 = 10步, 1步 = 10尺, 1尺 = 10寸.
2. **Formulas**: The formulas for `a` (tree height) and `b` (distance from the mountain to the table) are derived from the problem's description.
3. **Fraction Usage**: The `Fraction` class is used to ensure precise calculations, especially for non-integer values.

### Results:
- `a` represents the height of the tree in 丈.
- `b` represents the distance from the mountain to the table in 步.
"""


"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 353/89
Variable 'b' has wrong value. Expected: 23/21, Actual: 4625/89"""
