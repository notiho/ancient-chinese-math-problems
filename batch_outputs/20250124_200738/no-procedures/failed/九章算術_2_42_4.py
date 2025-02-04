"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit of silk at different levels of measurement (per shi, per jun, etc.). Here's the breakdown:

### Problem:
- Total money spent: 13,970 qian (錢)
- Total silk purchased: 1 shi (石), 2 jun (鈞), 28 jin (斤), 3 liang (兩), 5 zhu (銖)
- We need to calculate the price per shi (石) and per jun (鈞).

---

### Step-by-step solution:

1. **Convert all silk quantities into a single unit (zhu, the smallest unit):**
   - 1 shi = 120 jin
   - 1 jun = 30 jin
   - 1 jin = 16 liang
   - 1 liang = 24 zhu

   Total silk in zhu:
   \[
   \text{Total silk in zhu} = (1 \times 120 + 2 \times 30 + 28) \times 16 \times 24 + 3 \times 24 + 5
   \]

2. **Calculate the price per zhu:**
   - Price per zhu = Total money / Total silk in zhu.

3. **Convert the price per zhu into the price per shi and per jun:**
   - Price per shi = Price per zhu × (120 jin × 16 liang × 24 zhu).
   - Price per jun = Price per zhu × (30 jin × 16 liang × 24 zhu).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
total_money = 13970  # in qian

# Silk quantities
shi = 1
jun = 2
jin = 28
liang = 3
zhu = 5

# Conversion factors
jin_per_shi = 120
jin_per_jun = 30
liang_per_jin = 16
zhu_per_liang = 24

# Convert all silk quantities into zhu
total_silk_in_zhu = (
    (shi * jin_per_shi + jun * jin_per_jun + jin) * liang_per_jin * zhu_per_liang
    + liang * zhu_per_liang
    + zhu
)

# Price per zhu
price_per_zhu = Fraction(total_money, total_silk_in_zhu)

# Price per shi
price_per_shi = price_per_zhu * (jin_per_shi * liang_per_jin * zhu_per_liang)

# Price per jun
price_per_jun = price_per_zhu * (jin_per_jun * liang_per_jin * zhu_per_liang)

# Results
a = price_per_shi  # Price per shi
b = price_per_zhu * (liang_per_jin * zhu_per_liang)  # Price per jin
c = price_per_jun  # Price per jun
d = price_per_zhu  # Price per zhu

print(f"Price per shi: {a} qian")
print(f"Price per jin: {b} qian")
print(f"Price per jun: {c} qian")
print(f"Price per zhu: {d} qian")
#----- content ends here -----


"""


---

### Explanation of Results:
- `a`: Price per shi (石).
- `b`: Price per jin (斤).
- `c`: Price per jun (鈞).
- `d`: Price per zhu (銖).
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 643737600/79949
Variable 'b' has wrong value. Expected: 4, Actual: 5364480/79949
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 160934400/79949
Variable 'd' has wrong value. Expected: 5, Actual: 13970/79949"""
