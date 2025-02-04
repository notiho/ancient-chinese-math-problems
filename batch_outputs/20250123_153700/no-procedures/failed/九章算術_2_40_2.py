"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
This problem involves calculating the price per unit weight of silk based on the total cost and the total weight. Let's break it down step by step:

### Problem:
- Total money spent: 13,970 (錢)
- Total weight of silk: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
- Question: What is the price per 斤 (jin) and per 鈞 (jun)?

---

### Step 1: Convert the total weight into a single unit (斤).
1 石 = 4 鈞  
1 鈞 = 30 斤  
1 斤 = 16 兩  
1 兩 = 24 銖  

So, the total weight in 斤 is:

\[
\text{Total weight in 斤} = (1 \times 4 \times 30) + (2 \times 30) + 28 + \frac{3}{16} + \frac{5}{16 \times 24}
\]

---

### Step 2: Calculate the price per 斤 (jin).
The price per 斤 is the total money divided by the total weight in 斤.

---

### Step 3: Calculate the price per 鈞 (jun).
The price per 鈞 is the total money divided by the total weight in 鈞.

---

### Python Code:


"""


from fractions import Fraction

# Total money spent
total_money = 13970

# Total weight in jin
total_weight_jin = (1 * 4 * 30) + (2 * 30) + 28 + Fraction(3, 16) + Fraction(5, 16 * 24)

# Price per jin
price_per_jin = Fraction(total_money, total_weight_jin)

# Total weight in jun
total_weight_jun = (1 * 4) + 2 + Fraction(28, 30) + Fraction(3, 30 * 16) + Fraction(5, 30 * 16 * 24)

# Price per jun
price_per_jun = Fraction(total_money, total_weight_jun)

# Results
a = price_per_jin
b = price_per_jun

print(f"Price per jin: {a} 錢")
print(f"Price per jun: {b} 錢")


"""


---

### Explanation of Results:
- `a` is the price per 斤 (jin).
- `b` is the price per 鈞 (jun).
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 5364480/79949
Variable 'b' has wrong value. Expected: 2012, Actual: 160934400/79949
Missing variable in output: 'c'
Missing variable in output: 'd'"""
