"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit of silk at different levels of measurement (per shi, per jin, etc.). Here's how we can break it down:

---

### Problem Breakdown:
- Total money spent: **13,970 qian**.
- Total silk purchased: **1 shi, 2 jun, 28 jin, 3 liang, 5 zhu**.
- Conversion factors:
  - 1 shi = 4 jun
  - 1 jun = 30 jin
  - 1 jin = 16 liang
  - 1 liang = 24 zhu

We first convert the total silk into the smallest unit (zhu), calculate the price per zhu, and then scale it back up to find the price per shi and per jin.

---

### Python Code:


"""


from fractions import Fraction

# Total money spent
total_money = 13970  # in qian

# Total silk purchased
shi = 1
jun = 2
jin = 28
liang = 3
zhu = 5

# Conversion factors
shi_to_jun = 4
jun_to_jin = 30
jin_to_liang = 16
liang_to_zhu = 24

# Convert all silk to zhu
total_zhu = (
    shi * shi_to_jun * jun_to_jin * jin_to_liang * liang_to_zhu +
    jun * jun_to_jin * jin_to_liang * liang_to_zhu +
    jin * jin_to_liang * liang_to_zhu +
    liang * liang_to_zhu +
    zhu
)

# Calculate price per zhu
price_per_zhu = Fraction(total_money, total_zhu)

# Calculate price per shi
zhu_per_shi = shi_to_jun * jun_to_jin * jin_to_liang * liang_to_zhu
price_per_shi = price_per_zhu * zhu_per_shi

# Calculate price per jin
zhu_per_jin = jin_to_liang * liang_to_zhu
price_per_jin = price_per_zhu * zhu_per_jin

# Results
a = price_per_shi  # Price per shi in qian
b = price_per_zhu  # Price per zhu in qian
c = price_per_jin  # Price per jin in qian
d = price_per_zhu  # Price per zhu in qian

# Print results
print(f"Price per shi: {a} qian")
print(f"Price per zhu: {b} qian")
print(f"Price per jin: {c} qian")
print(f"Price per zhu: {d} qian")


"""


---

### Explanation:
1. **Convert all silk to zhu**: This ensures we work with the smallest unit for accurate calculations.
2. **Calculate price per zhu**: Divide the total money by the total amount of silk in zhu.
3. **Scale up to larger units**: Multiply the price per zhu by the number of zhu in a shi or jin to find the price for those units.

This approach ensures precise calculations using fractions to avoid rounding errors.
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 643737600/79949
Variable 'b' has wrong value. Expected: 4, Actual: 13970/79949
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 5364480/79949
Variable 'd' has wrong value. Expected: 5, Actual: 13970/79949"""
