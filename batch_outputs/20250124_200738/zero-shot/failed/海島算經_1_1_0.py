"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
術曰：以入表乘表間為實。相多為法，除之。加入表，即得松高。求表去山遠近者：置表間，以前表卻行乘之為實。相多為法，除之，得山去表。
答曰：松高 a丈 ；山去表 b里 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the height of a pine tree (`a`) and the distance from the mountain to the front marker (`b`). We'll use the `Fraction` class to ensure accuracy with fractional values.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
height_of_marker = Fraction(2)  # 2丈
distance_between_markers = Fraction(50)  # 50步
front_marker_retreat = Fraction(7) + Fraction(4, 10)  # 7步4尺 = 7.4步
front_marker_entry = Fraction(2) + Fraction(8, 10)  # 2尺8寸 = 2.8步
rear_marker_retreat = Fraction(8) + Fraction(5, 10)  # 8步5尺 = 8.5步

# Calculating the height of the pine tree (松高, a)
numerator_a = front_marker_entry * distance_between_markers
denominator_a = front_marker_retreat - rear_marker_retreat
a = numerator_a / denominator_a + height_of_marker

# Calculating the distance from the mountain to the front marker (山去表, b)
numerator_b = front_marker_retreat * distance_between_markers
denominator_b = front_marker_retreat - rear_marker_retreat
b = numerator_b / denominator_b

# Results
a = a  # 松高 in 丈
b = b / 180  # 山去表 in 里 (1里 = 180步)

# Output the results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Height of the Pine Tree (`a`)**:
   - The formula for the height of the pine tree is derived from the problem:
     \[
     a = \frac{\text{入表} \times \text{表間}}{\text{前表卻行} - \text{後表卻行}} + \text{表高}
     \]
   - Here, `入表` is the front marker entry (2.8步), `表間` is the distance between the markers (50步), and the difference between the retreats is `(7.4 - 8.5)`.

2. **Distance from the Mountain to the Front Marker (`b`)**:
   - The formula for the distance is:
     \[
     b = \frac{\text{前表卻行} \times \text{表間}}{\text{前表卻行} - \text{後表卻行}}
     \]
   - This gives the distance in steps, which is then converted to `里` by dividing by 180 (since 1里 = 180步).

3. **Units**:
   - The height of the pine tree (`a`) is in 丈.
   - The distance from the mountain to the front marker (`b`) is in 里.

### Final Results:
The variables `a` and `b` will contain the height of the pine tree in 丈 and the distance from the mountain to the front marker in 里, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 307/25, Actual: -1378/11
Variable 'b' has wrong value. Expected: 23/21, Actual: -185/99"""
