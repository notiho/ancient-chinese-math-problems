"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
術曰：以入表乘表間為實。相多為法，除之。加入表，即得松高。求表去山遠近者：置表間，以前表卻行乘之為實。相多為法，除之，得山去表。
答曰：松高 a丈 ；山去表 b里 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the height of a pine tree (`a`) and the distance from the mountain to the reference point (`b`). Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
height_of_pole = Fraction(2)  # 2丈
distance_between_poles = Fraction(50)  # 50步
front_pole_retreat = Fraction(7) + Fraction(4, 10)  # 7步4尺 = 7.4步
front_pole_inward = Fraction(2, 10) + Fraction(8, 100)  # 2尺8寸 = 0.28步
rear_pole_retreat = Fraction(8) + Fraction(5, 10)  # 8步5尺 = 8.5步

# Calculating the height of the pine tree (松高, a)
numerator_a = front_pole_inward * distance_between_poles
denominator_a = front_pole_retreat - front_pole_inward
a = numerator_a / denominator_a + height_of_pole

# Calculating the distance from the mountain to the reference point (山去表, b)
numerator_b = distance_between_poles * rear_pole_retreat
denominator_b = rear_pole_retreat - front_pole_retreat
b = numerator_b / denominator_b

# Results
a  # 松高 in 丈
b  # 山去表 in 步
#----- content ends here -----


"""


### Explanation:
1. **松高 (a)**:
   - Use the formula: `(入表 * 表間) / (前表卻行 - 入表) + 表高`.
   - Here, `入表` is the inward distance of the front pole, `表間` is the distance between the two poles, and `表高` is the height of the pole.

2. **山去表 (b)**:
   - Use the formula: `(表間 * 後表卻行) / (後表卻行 - 前表卻行)`.
   - Here, `後表卻行` is the retreat distance from the rear pole, and `前表卻行` is the retreat distance from the front pole.

3. **Units**:
   - The height of the pine tree (`a`) is in 丈.
   - The distance from the mountain to the reference point (`b`) is in 步.

### Final Output:
- `a` is the height of the pine tree in 丈.
- `b` is the distance from the mountain to the reference point in 步.
"""


"""
Variable 'a' has wrong value. Expected: 307/25, Actual: 353/89
Variable 'b' has wrong value. Expected: 23/21, Actual: 4250/11"""
