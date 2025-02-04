"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
To solve this problem, we need to carefully follow the ancient Chinese mathematical procedure described in the problem. Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. **Given:**
   - Money spent: 13,970 (出錢一萬三千九百七十)
   - Silk purchased: 1 石 (shi), 2 鈞 (jun), 28 斤 (jin), 3 兩 (liang), 5 銖 (zhu).

2. **Goal:**
   - Find the price per 銖 (zhu) and 鈞 (jun), as well as the price per 石 (shi).

3. **Procedure:**
   - Use the total money as the "法" (divisor).
   - Use the total silk weight as the "實" (numerator).
   - Divide the total weight by the total money to find the rate per unit.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
money = 13970  # 出錢一萬三千九百七十
silk_stone = 1  # 石
silk_jun = 2  # 鈞
silk_jin = 28  # 斤
silk_liang = 3  # 兩
silk_zhu = 5  # 銖

# Conversion factors
jin_to_liang = 16  # 1 斤 = 16 兩
liang_to_zhu = 24  # 1 兩 = 24 銖
jun_to_jin = 30  # 1 鈞 = 30 斤
stone_to_jun = 4  # 1 石 = 4 鈞

# Convert total silk weight to 銖 (zhu)
total_zhu = (
    silk_stone * stone_to_jun * jun_to_jin * jin_to_liang * liang_to_zhu +
    silk_jun * jun_to_jin * jin_to_liang * liang_to_zhu +
    silk_jin * jin_to_liang * liang_to_zhu +
    silk_liang * liang_to_zhu +
    silk_zhu
)

# Find the rate per 銖 (zhu)
rate_per_zhu = Fraction(money, total_zhu)

# Convert the rate to 鈞 (jun) and 石 (shi)
zhu_per_jun = jun_to_jin * jin_to_liang * liang_to_zhu
zhu_per_stone = stone_to_jun * zhu_per_jun

rate_per_jun = rate_per_zhu * zhu_per_jun
rate_per_stone = rate_per_zhu * zhu_per_stone

# Results
a = rate_per_jun  # Rate per 鈞
b = rate_per_zhu  # Rate per 銖
c = rate_per_stone  # Rate per 石
d = rate_per_zhu  # Rate per 銖 (same as b)

# Output
a, b, c, d
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Conversion to 銖 (zhu):**
   - All units of silk weight are converted to the smallest unit, 銖 (zhu), using the given conversion factors.

2. **Rate Calculation:**
   - The rate per 銖 is calculated by dividing the total money by the total weight in 銖.

3. **Conversion to Larger Units:**
   - The rate per 鈞 (jun) and 石 (shi) is calculated by multiplying the rate per 銖 by the number of 銖 in a 鈞 and 石, respectively.

4. **Output:**
   - The results are stored in variables `a`, `b`, `c`, and `d` as required.

---

### Final Answer:
- `a` 鈞, `b` 銖 一錢.
- `c` 石, `d` 銖 一錢.

This code adheres to the ancient Chinese mathematical procedure and provides the required results.
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 160934400/79949
Variable 'b' has wrong value. Expected: 5, Actual: 13970/79949
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 643737600/79949
Variable 'd' has wrong value. Expected: 6, Actual: 13970/79949"""
