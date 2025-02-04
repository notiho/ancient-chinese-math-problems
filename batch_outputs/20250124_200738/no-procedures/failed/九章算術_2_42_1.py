"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
This problem involves calculating the price per unit of weight for silk, given the total cost and the total weight. Let's break it down step by step.

### Problem Breakdown:
- Total money spent: **13,970 qian**.
- Total weight of silk: **1 shi, 2 jun, 28 jin, 3 liang, 5 zhu**.
- We need to calculate:
  1. The price per **shi** (a).
  2. The price per **jin** (b).
  3. The price per **jun** (c).
  4. The price per **liang** (d).

### Unit Conversions:
1 shi = 4 jun  
1 jun = 30 jin  
1 jin = 16 liang  
1 liang = 24 zhu  

### Total Weight in Jin:
We first convert the total weight into a single unit (jin):
- 1 shi = 4 jun = 4 × 30 = 120 jin
- 2 jun = 2 × 30 = 60 jin
- 28 jin = 28 jin
- 3 liang = 3 ÷ 16 = 0.1875 jin
- 5 zhu = 5 ÷ (16 × 24) = 0.01302 jin

Total weight in jin = 120 + 60 + 28 + 0.1875 + 0.01302 = **208.20052 jin**

### Price per Unit:
1. Price per shi (a):  
   Since 1 shi = 120 jin, the price per shi is:  
   **a = (13,970 ÷ total weight in jin) × 120**

2. Price per jin (b):  
   The price per jin is:  
   **b = 13,970 ÷ total weight in jin**

3. Price per jun (c):  
   Since 1 jun = 30 jin, the price per jun is:  
   **c = (13,970 ÷ total weight in jin) × 30**

4. Price per liang (d):  
   Since 1 liang = 1 ÷ 16 jin, the price per liang is:  
   **d = (13,970 ÷ total weight in jin) ÷ 16**

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
total_money = 13970

# Total weight in jin
total_weight_in_jin = 120 + 60 + 28 + Fraction(3, 16) + Fraction(5, 16 * 24)

# Price per jin
price_per_jin = Fraction(total_money, total_weight_in_jin)

# Price per shi (120 jin)
a = price_per_jin * 120

# Price per jin
b = price_per_jin

# Price per jun (30 jin)
c = price_per_jin * 30

# Price per liang (1/16 jin)
d = price_per_jin / 16

# Output results
a, b, c, d
#----- content ends here -----


"""


### Final Answer:
- **a**: Price per shi.
- **b**: Price per jin.
- **c**: Price per jun.
- **d**: Price per liang.
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 643737600/79949
Variable 'b' has wrong value. Expected: 4, Actual: 5364480/79949
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 160934400/79949
Variable 'd' has wrong value. Expected: 5, Actual: 335280/79949"""
