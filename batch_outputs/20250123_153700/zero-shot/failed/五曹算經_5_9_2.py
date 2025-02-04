"""
今有錢二百三十八貫五百七十三文足欲為九十二陌。問：得㡬何？
術曰：列錢二百三十八貫五百七十三文足以九十二除之即得。
答曰： a貫 奇足錢 b分 。
"""

"""
To solve this problem, we need to divide the total amount of money (238貫573文) by 92陌 to find how much money corresponds to one陌. Here's the Python code to compute the values:


"""


from fractions import Fraction

# Total money in 文 (1貫 = 1000文)
total_money = 238 * 1000 + 573  # Convert 貫 and 文 into 文
num_mo = 92  # Number of 陌

# Divide total money by the number of 陌
money_per_mo = Fraction(total_money, num_mo)

# Convert the result back into 貫 and 文
a = money_per_mo // 1000  # Whole 貫
b = money_per_mo % 1000   # Remaining 文

# Results
a = int(a)  # 貫
b = int(b)  # 文


"""


### Solution:
- `a` is the number of 貫.
- `b` is the number of 文.
"""


"""
Variable 'a' has wrong value. Expected: 129659/500, Actual: 2
Variable 'b' has wrong value. Expected: 22/5, Actual: 593"""
