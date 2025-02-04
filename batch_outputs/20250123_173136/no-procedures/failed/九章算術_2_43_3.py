"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
To solve this problem, we need to calculate the price per unit weight of silk in terms of **銖 per 錢** for both 鈞 (jun) and 石 (shi). Here's the breakdown of the problem:

---

### Problem Breakdown:
1. **Total money spent**: 13,970 (in 錢).
2. **Total weight of silk purchased**: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖.
   - 1 石 = 4 鈞
   - 1 鈞 = 30 斤
   - 1 斤 = 16 兩
   - 1 兩 = 24 銖
3. **Goal**: Calculate the price per 鈞 and per 石 in terms of 銖 per 錢.

---

### Step 1: Convert the total weight into 銖
We first convert the total weight into 銖 (the smallest unit):

\[
\text{Total weight in 銖} = (1 \times 4 \times 30 \times 16 \times 24) + (2 \times 30 \times 16 \times 24) + (28 \times 16 \times 24) + (3 \times 24) + 5
\]

Breaking it down:
- 1 石 = \( 4 \times 30 \times 16 \times 24 = 46,080 \) 銖
- 2 鈞 = \( 2 \times 30 \times 16 \times 24 = 23,040 \) 銖
- 28 斤 = \( 28 \times 16 \times 24 = 10,752 \) 銖
- 3 兩 = \( 3 \times 24 = 72 \) 銖
- 5 銖 = 5 銖

Adding these together:
\[
\text{Total weight in 銖} = 46,080 + 23,040 + 10,752 + 72 + 5 = 79,949 \, \text{銖}
\]

---

### Step 2: Calculate the price per 銖
The total money spent is 13,970 錢. The price per 銖 is:

\[
\text{Price per 銖} = \frac{\text{Total money}}{\text{Total weight in 銖}} = \frac{13,970}{79,949}
\]

---

### Step 3: Convert the price into 鈞 and 石 units
1. **Price per 鈞**:
   - 1 鈞 = \( 30 \times 16 \times 24 = 11,520 \) 銖.
   - Price per 鈞 = \( \text{Price per 銖} \times 11,520 \).

2. **Price per 石**:
   - 1 石 = \( 4 \times 11,520 = 46,080 \) 銖.
   - Price per 石 = \( \text{Price per 銖} \times 46,080 \).

---

### Final Python Code:


"""


from fractions import Fraction

# Total money spent (in 錢)
total_money = 13970

# Total weight in 銖
total_weight_in_zhu = (
    (1 * 4 * 30 * 16 * 24) +  # 1 石
    (2 * 30 * 16 * 24) +      # 2 鈞
    (28 * 16 * 24) +          # 28 斤
    (3 * 24) +                # 3 兩
    5                         # 5 銖
)

# Price per 銖
price_per_zhu = Fraction(total_money, total_weight_in_zhu)

# Price per 鈞
zhu_per_jun = 30 * 16 * 24  # 1 鈞 in 銖
price_per_jun = price_per_zhu * zhu_per_jun

# Price per 石
zhu_per_shi = 4 * zhu_per_jun  # 1 石 in 銖
price_per_shi = price_per_zhu * zhu_per_shi

# Results
a = price_per_jun.numerator
b = price_per_jun.denominator
c = price_per_shi.numerator
d = price_per_shi.denominator

print(f"其 {a} 鈞 ， {b} 銖 一錢。 其 {c} 石 ， {d} 銖 一錢。")


"""


---

### Explanation of Results:
- `a` and `b` represent the price per 鈞 in terms of 銖 per 錢.
- `c` and `d` represent the price per 石 in terms of 銖 per 錢.
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 160934400
Variable 'b' has wrong value. Expected: 5, Actual: 79949
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 643737600
Variable 'd' has wrong value. Expected: 6, Actual: 79949"""
