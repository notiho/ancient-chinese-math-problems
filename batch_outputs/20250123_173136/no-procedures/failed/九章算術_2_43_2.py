"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
This problem involves calculating the price per unit weight of silk based on the total cost and the total weight. Let's break it down step by step:

### Problem:
- Total money spent: **13,970 (錢)**
- Total weight of silk: **1 石, 2 鈞, 28 斤, 3 兩, 5 銖**
- Question: What is the price per 鈞 (錢 per 鈞) and per 石 (錢 per 石)?

---

### Step 1: Convert the total weight into a single unit (銖)
In ancient Chinese measurements:
- 1 石 = 4 鈞
- 1 鈞 = 30 斤
- 1 斤 = 16 兩
- 1 兩 = 24 銖

Thus, the total weight in 銖 is:

\[
\text{Total weight in 銖} = (1 \times 4 \times 30 \times 16 \times 24) + (2 \times 30 \times 16 \times 24) + (28 \times 16 \times 24) + (3 \times 24) + 5
\]

---

### Step 2: Calculate the price per 鈞
Since 1 鈞 = \(30 \times 16 \times 24\) 銖, we can calculate the price per 鈞 by dividing the total money by the total weight in 鈞.

---

### Step 3: Calculate the price per 石
Since 1 石 = \(4 \times 30 \times 16 \times 24\) 銖, we can calculate the price per 石 by dividing the total money by the total weight in 石.

---

### Python Code:


"""


from fractions import Fraction

# Total money spent
total_money = 13970

# Conversion factors
shi_to_jun = 4
jun_to_jin = 30
jin_to_liang = 16
liang_to_zhu = 24

# Total weight in zhu
total_weight_in_zhu = (
    (1 * shi_to_jun * jun_to_jin * jin_to_liang * liang_to_zhu) +  # 1 石
    (2 * jun_to_jin * jin_to_liang * liang_to_zhu) +              # 2 鈞
    (28 * jin_to_liang * liang_to_zhu) +                          # 28 斤
    (3 * liang_to_zhu) +                                          # 3 兩
    5                                                            # 5 銖
)

# Price per 鈞
zhu_per_jun = jun_to_jin * jin_to_liang * liang_to_zhu
price_per_jun = Fraction(total_money, total_weight_in_zhu) * zhu_per_jun

# Price per 石
zhu_per_shi = shi_to_jun * zhu_per_jun
price_per_shi = Fraction(total_money, total_weight_in_zhu) * zhu_per_shi

# Results
a = price_per_jun.numerator
b = price_per_jun.denominator
c = price_per_shi.numerator
d = price_per_shi.denominator

print(f"其 {a} 鈞，{b} 銖 一錢。其 {c} 石，{d} 銖 一錢。")


"""


---

### Explanation of Results:
- **a 鈞, b 銖 一錢**: This gives the price per 鈞 in terms of 銖 per 錢.
- **c 石, d 銖 一錢**: This gives the price per 石 in terms of 銖 per 錢.
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 160934400
Variable 'b' has wrong value. Expected: 5, Actual: 79949
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 643737600
Variable 'd' has wrong value. Expected: 6, Actual: 79949"""
