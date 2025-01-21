"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
This problem involves calculating the price per unit weight of silk in terms of **jin (斤)** and **shi (石)**, based on the total cost and total weight. Let's solve it step by step.

### Problem Breakdown:
- Total money spent: **13,970 (一萬三千九百七十)**
- Total weight of silk: **1 shi (石), 2 jun (鈞), 28 jin (斤), 3 liang (兩), 5 zhu (銖)**

We need to calculate:
1. The price per **jin (斤)** in terms of **zhu (銖)**.
2. The price per **shi (石)** in terms of **zhu (銖)**.

---

### Conversion Factors:
1 shi (石) = 4 jun (鈞)  
1 jun (鈞) = 30 jin (斤)  
1 jin (斤) = 16 liang (兩)  
1 liang (兩) = 24 zhu (銖)

Thus:
1 shi = 4 × 30 × 16 × 24 = **46,080 zhu**  
1 jun = 30 × 16 × 24 = **11,520 zhu**  
1 jin = 16 × 24 = **384 zhu**  
1 liang = 24 zhu  

---

### Step 1: Convert Total Weight to Zhu
The total weight is **1 shi, 2 jun, 28 jin, 3 liang, 5 zhu**. Converting this to zhu:

\[
\text{Total weight in zhu} = (1 \times 46,080) + (2 \times 11,520) + (28 \times 384) + (3 \times 24) + 5
\]

\[
\text{Total weight in zhu} = 46,080 + 23,040 + 10,752 + 72 + 5 = 79,949 \, \text{zhu}
\]

---

### Step 2: Calculate Price per Zhu
The total cost is **13,970**. To find the price per zhu:

\[
\text{Price per zhu} = \frac{\text{Total cost}}{\text{Total weight in zhu}} = \frac{13,970}{79,949}
\]

This simplifies to a fraction:

\[
\text{Price per zhu} = \frac{13,970}{79,949}
\]

---

### Step 3: Calculate Price per Jin and Shi
1. **Price per jin (斤):**
   Since 1 jin = 384 zhu, the price per jin is:

   \[
   \text{Price per jin} = 384 \times \frac{13,970}{79,949}
   \]

2. **Price per shi (石):**
   Since 1 shi = 46,080 zhu, the price per shi is:

   \[
   \text{Price per shi} = 46,080 \times \frac{13,970}{79,949}
   \]

---

### Final Python Code:


"""


from fractions import Fraction

# Total cost
total_cost = 13970

# Total weight in zhu
total_weight_in_zhu = (1 * 46080) + (2 * 11520) + (28 * 384) + (3 * 24) + 5

# Price per zhu
price_per_zhu = Fraction(total_cost, total_weight_in_zhu)

# Price per jin (1 jin = 384 zhu)
price_per_jin = 384 * price_per_zhu

# Price per shi (1 shi = 46080 zhu)
price_per_shi = 46080 * price_per_zhu

# Results
a = price_per_jin.numerator
b = price_per_jin.denominator
c = price_per_shi.numerator
d = price_per_shi.denominator

print(f"Price per jin: {a} zhu per {b} qian.")
print(f"Price per shi: {c} zhu per {d} qian.")


"""


---

### Explanation of Results:
- **a, b**: The price per **jin** is `a zhu per b qian`.
- **c, d**: The price per **shi** is `c zhu per d qian`.
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 5364480
Variable 'b' has wrong value. Expected: 5, Actual: 79949
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 643737600
Variable 'd' has wrong value. Expected: 6, Actual: 79949"""
