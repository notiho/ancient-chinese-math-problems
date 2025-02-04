"""
今有兵三千一百四十八人，人給布一丈二尺三寸。問：計㡬何？
術曰：列兵三千一百四十八人，以布一十二尺三寸乘之，得三萬八千七百二十尺四寸，以五十尺除之即得。
答曰： a端 。
"""

"""
To solve this problem, we first need to understand the units and the calculations. The problem states that there are 3,148 soldiers, and each soldier is given 1丈2尺3寸 of cloth. The question asks how many bolts of cloth (each bolt is 50尺) are needed in total.

1丈 = 10尺  
1尺 = 10寸  

Thus, 1丈2尺3寸 = 12尺3寸 = 12.3尺.

Now, we calculate the total amount of cloth needed for 3,148 soldiers and then divide it by the length of one bolt (50尺) to find the number of bolts required.

Here is the Python code:


"""


from fractions import Fraction

# Given data
soldiers = 3148
cloth_per_soldier = Fraction(12, 1) + Fraction(3, 10)  # 12尺3寸 = 12.3尺
bolt_length = 50  # 1 bolt = 50尺

# Total cloth needed
total_cloth = soldiers * cloth_per_soldier  # in 尺

# Number of bolts needed
a = total_cloth / bolt_length

# Result
a  # This is the answer in bolts


"""


The variable `a` will contain the number of bolts required, expressed as a `Fraction`.
"""


"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/125"""
