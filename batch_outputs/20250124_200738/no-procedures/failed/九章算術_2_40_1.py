"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
This problem involves calculating the price per unit weight (jin, and shi) based on the total cost and the total weight of silk purchased.

### Problem Breakdown:
- Total money spent: **13,970 qian**.
- Total weight of silk: **1 shi, 2 jun, 28 jin, 3 liang, 5 zhu**.
- Convert all weights into a single unit (jin), calculate the price per jin, and then calculate the price per shi.

---

### Step-by-Step Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
total_money = 13970  # in qian

# Total weight of silk
shi = 1
jun = 2
jin = 28
liang = 3
zhu = 5

# Conversion factors
jin_per_shi = 120  # 1 shi = 120 jin
jin_per_jun = 30   # 1 jun = 30 jin
liang_per_jin = 16 # 1 jin = 16 liang
zhu_per_liang = 24 # 1 liang = 24 zhu

# Convert all weights to jin
total_jin = (
    shi * jin_per_shi +
    jun * jin_per_jun +
    jin +
    Fraction(liang, liang_per_jin) +
    Fraction(zhu, liang_per_jin * zhu_per_liang)
)

# Calculate price per jin
price_per_jin = Fraction(total_money, total_jin)

# Calculate price per shi
price_per_shi = price_per_jin * jin_per_shi

# Results
a = price_per_jin  # Price per jin in qian
b = price_per_jin * jin_per_jun  # Price per jun in qian
c = price_per_shi  # Price per shi in qian
d = price_per_shi  # Price per shi in qian (same as c)

# Output results
a, b, c, d
#----- content ends here -----


"""


---

### Explanation of Results:
- **a**: Price per jin in qian.
- **b**: Price per jun in qian.
- **c**: Price per shi in qian.
- **d**: Price per shi in qian (same as c).
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 5364480/79949
Variable 'b' has wrong value. Expected: 2012, Actual: 160934400/79949
Variable 'c' has wrong value. Expected: 19253/11520, Actual: 643737600/79949
Variable 'd' has wrong value. Expected: 2013, Actual: 643737600/79949"""
