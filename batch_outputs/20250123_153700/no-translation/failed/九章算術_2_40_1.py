"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (鈞 rate) for the given amount of money and weight. Let's break it down step by step according to the procedure:

### Definitions and Inputs:
- 出錢 = 13970 (total money spent)
- 買絲 = 1石 2鈞 28斤 3兩 5銖 (total weight)

We need to calculate the rate for each unit (斤, 鈞, 石) based on the total money and weight.

---

### Step 1: Convert all weights into a single unit (銖, the smallest unit).
1石 = 4鈞  
1鈞 = 30斤  
1斤 = 16兩  
1兩 = 24銖  

So, the total weight in 銖 is:
```
總銖 = (1石 × 4鈞 × 30斤 × 16兩 × 24銖) + (2鈞 × 30斤 × 16兩 × 24銖) + (28斤 × 16兩 × 24銖) + (3兩 × 24銖) + 5銖
```

---

### Step 2: Calculate the 鈞 rate (price per 鈞).
The total weight in 鈞 is:
```
總鈞 = 總銖 ÷ (30斤 × 16兩 × 24銖)
```

The 鈞 rate is:
```
鈞率 = 出錢 ÷ 總鈞
```

---

### Step 3: Calculate the price per 斤 and 石.
- 斤 rate:
```
斤率 = 鈞率 ÷ 30
```

- 石 rate:
```
石率 = 鈞率 × 4
```

---

### Step 4: Output the results.
```
a = 斤率
b = 鈞率
c = 石率
d = 鈞率
```

Now let's implement this in Python:


"""


from fractions import Fraction

# Inputs
出錢 = 13970  # Total money spent

# Weight conversion factors
石_to_鈞 = 4
鈞_to_斤 = 30
斤_to_兩 = 16
兩_to_銖 = 24

# Total weight in 銖
總銖 = (
    (1 * 石_to_鈞 * 鈞_to_斤 * 斤_to_兩 * 兩_to_銖) +
    (2 * 鈞_to_斤 * 斤_to_兩 * 兩_to_銖) +
    (28 * 斤_to_兩 * 兩_to_銖) +
    (3 * 兩_to_銖) +
    5
)

# Total weight in 鈞
總鈞 = Fraction(總銖, 鈞_to_斤 * 斤_to_兩 * 兩_to_銖)

# 鈞 rate
鈞率 = Fraction(出錢, 總鈞)

# 斤 rate
斤率 = Fraction(鈞率, 鈞_to_斤)

# 石 rate
石率 = 鈞率 * 石_to_鈞

# Outputs
a = 斤率
b = 鈞率
c = 石率
d = 鈞率

# Results
a, b, c, d


"""


This code calculates the rates for 斤, 鈞, and 石 based on the given money and weight. The results are represented as fractions for precise calculations.
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 5364480/79949
Variable 'b' has wrong value. Expected: 2012, Actual: 160934400/79949
Variable 'c' has wrong value. Expected: 19253/11520, Actual: 643737600/79949
Variable 'd' has wrong value. Expected: 2013, Actual: 160934400/79949"""
