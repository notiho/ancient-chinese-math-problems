"""
今有兵一千三百六十二人，人給絹二丈八尺五寸。問：計㡬何？
術曰：列兵一千三百六十二人，以絹二十八尺五寸乘之，得三萬八千八百一十七尺，以四十尺除之即得。
答曰： a疋 。
"""

"""
To solve this problem, we need to calculate how many bolts of silk ("疋") are required to distribute to 1,362 soldiers, where each soldier is given 2丈8尺5寸 of silk. In ancient Chinese units:

1 丈 = 10 尺  
1 尺 = 10 寸  
1 疋 = 40 尺  

The given amount of silk per soldier is 2丈8尺5寸, which we convert entirely into 尺 for simplicity:

2丈 = 20尺  
8尺 = 8尺  
5寸 = 0.5尺  

Thus, the total silk per soldier is:  
20尺 + 8尺 + 0.5尺 = 28.5尺  

Now, we calculate the total silk required for 1,362 soldiers:  
Total silk = 1,362 × 28.5 尺  

Finally, we divide the total silk by 40 (since 1 疋 = 40 尺) to find the total number of bolts of silk required.

Here is the Python code to compute the answer:


"""


from fractions import Fraction

# Given values
soldiers = 1362
silk_per_soldier = Fraction(28, 1) + Fraction(5, 10)  # 28.5 尺
silk_per_bolt = 40  # 1 疋 = 40 尺

# Total silk required
total_silk = soldiers * silk_per_soldier

# Total bolts of silk required
a = total_silk / silk_per_bolt

# Result
a  # This is the answer in 疋


"""


The variable `a` will contain the total number of bolts of silk required.
"""


"""
"""
