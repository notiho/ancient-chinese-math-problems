"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
This problem involves calculating the price per unit weight of silk based on the total cost and weight. Let's break it down step by step.

### Problem:
- Total money spent: 13,970 (錢)
- Total weight of silk: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
- Question: Calculate the price per 石 and per 鈞.

---

### Step 1: Convert the total weight into a single unit (斤, for simplicity)
1 石 = 120 斤  
1 鈞 = 30 斤  
1 斤 = 16 兩  
1 兩 = 24 銖  

So, the total weight in 斤 is:
\[
1 \times 120 + 2 \times 30 + 28 + \frac{3}{16} + \frac{5}{(16 \times 24)}
\]

---

### Step 2: Calculate the price per 石 and per 鈞
- Price per 石 = Total money / Total 石
- Price per 鈞 = Total money / Total 鈞

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
total_money = 13970

# Total weight in jin
total_weight_jin = (
    1 * 120 +  # 1 石 = 120 斤
    2 * 30 +   # 2 鈞 = 60 斤
    28 +       # 28 斤
    Fraction(3, 16) +  # 3 兩 = 3/16 斤
    Fraction(5, 16 * 24)  # 5 銖 = 5/(16*24) 斤
)

# Convert total weight to 石 and 鈞
total_weight_shi = total_weight_jin / 120
total_weight_jun = total_weight_jin / 30

# Price per 石
a = Fraction(total_money, total_weight_shi)

# Price per 鈞
b = Fraction(total_money, total_weight_jun)

# Output results
print(f"Price per 石: {a} 錢")
print(f"Price per 鈞: {b} 錢")
#----- content ends here -----


"""


---

### Explanation of Results:
- `a` is the price per 石 in 錢.
- `b` is the price per 鈞 in 錢.

This code calculates the price per 石 and per 鈞 based on the given total cost and weight.
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 643737600/79949
Variable 'b' has wrong value. Expected: 4, Actual: 160934400/79949
Missing variable in output: 'c'
Missing variable in output: 'd'"""
