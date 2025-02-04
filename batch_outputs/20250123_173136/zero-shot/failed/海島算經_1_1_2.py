"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
術曰：以入表乘表間為實。相多為法，除之。加入表，即得松高。求表去山遠近者：置表間，以前表卻行乘之為實。相多為法，除之，得山去表。
答曰：松高 a丈 ；山去表 b里 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves determining the height of a pine tree (`a`) and the distance from the mountain to the table (`b`). We'll use the `Fraction` class to handle fractional calculations.

Here is the Python code:


"""


from fractions import Fraction

# Given data
height_of_table = Fraction(2)  # 2丈
distance_between_tables = Fraction(50)  # 50步
front_table_step_back = Fraction(7) + Fraction(4, 10)  # 7步4尺 (1步 = 10尺)
front_table_entry = Fraction(2, 10) + Fraction(8, 100)  # 2尺8寸 (1尺 = 10寸)
back_table_step_back = Fraction(8) + Fraction(5, 10)  # 8步5尺

# Calculating the height of the pine tree (a)
numerator_a = front_table_entry * distance_between_tables
denominator_a = front_table_step_back - back_table_step_back
a = numerator_a / denominator_a + height_of_table

# Calculating the distance from the mountain to the table (b)
numerator_b = distance_between_tables * front_table_step_back
denominator_b = front_table_step_back - back_table_step_back
b = numerator_b / denominator_b

# Results
a = a  # 松高 in 丈
b = b  # 山去表 in 步

# Output the results
a, b


"""


### Explanation of the Code:
1. **Height of the Pine Tree (`a`)**:
   - The formula for the height of the pine tree is derived from the problem:
     \[
     a = \frac{\text{入表} \times \text{表間}}{\text{前表卻行} - \text{後表卻行}} + \text{表高}
     \]
   - Here, `入表` is the entry of the front table (2尺8寸), `表間` is the distance between the two tables (50步), and the difference between the steps back from the front and back tables is used in the denominator.

2. **Distance from the Mountain to the Table (`b`)**:
   - The formula for the distance is:
     \[
     b = \frac{\text{表間} \times \text{前表卻行}}{\text{前表卻行} - \text{後表卻行}}
     \]
   - This uses the same denominator as the height calculation but with a different numerator.

3. **Units**:
   - The height of the pine tree (`a`) is in 丈.
   - The distance from the mountain to the table (`b`) is in 步.

### Output:
The variables `a` and `b` will contain the height of the pine tree and the distance from the mountain to the table, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 307/25, Actual: -118/11
Variable 'b' has wrong value. Expected: 23/21, Actual: -3700/11"""
