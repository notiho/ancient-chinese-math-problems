"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
This problem involves calculating the price per unit weight of silk based on the total cost and the total weight. The weight is given in a traditional Chinese system (石, 鈞, 斤, 兩, 銖), and the task is to determine the price per unit for each weight unit.

### Problem Breakdown:
- **Total money spent**: 13,970 錢.
- **Total weight**: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖.
- **Goal**: Calculate the price per 石 and per 鈞.

---

### Step 1: Convert the weight into a single unit (銖).
The traditional Chinese weight system is hierarchical:
- 1 石 = 4 鈞
- 1 鈞 = 30 斤
- 1 斤 = 16 兩
- 1 兩 = 24 銖

Thus, the total weight in 銖 is:
\[
\text{Total weight in 銖} = (1 \times 4 \times 30 \times 16 \times 24) + (2 \times 30 \times 16 \times 24) + (28 \times 16 \times 24) + (3 \times 24) + 5
\]

---

### Step 2: Calculate the price per 銖.
The price per 銖 is:
\[
\text{Price per 銖} = \frac{\text{Total money spent}}{\text{Total weight in 銖}}
\]

---

### Step 3: Calculate the price per 石 and per 鈞.
- **Price per 石**: Multiply the price per 銖 by the number of 銖 in 1 石.
- **Price per 鈞**: Multiply the price per 銖 by the number of 銖 in 1 鈞.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
total_money = 13970  # 錢

# Conversion factors
銖_per_兩 = 24
兩_per_斤 = 16
斤_per_鈞 = 30
鈞_per_石 = 4

# Total weight in 石, 鈞, 斤, 兩, 銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Convert total weight to 銖
total_weight_in_銖 = (
    石 * 鈞_per_石 * 斤_per_鈞 * 兩_per_斤 * 銖_per_兩 +
    鈞 * 斤_per_鈞 * 兩_per_斤 * 銖_per_兩 +
    斤 * 兩_per_斤 * 銖_per_兩 +
    兩 * 銖_per_兩 +
    銖
)

# Price per 銖
price_per_銖 = Fraction(total_money, total_weight_in_銖)

# Price per 石
銖_per_石 = 鈞_per_石 * 斤_per_鈞 * 兩_per_斤 * 銖_per_兩
price_per_石 = price_per_銖 * 銖_per_石

# Price per 鈞
銖_per_鈞 = 斤_per_鈞 * 兩_per_斤 * 銖_per_兩
price_per_鈞 = price_per_銖 * 銖_per_鈞

# Results
a = price_per_石  # Price per 石
b = price_per_銖  # Price per 銖
c = price_per_鈞  # Price per 鈞
d = price_per_銖  # Price per 銖

print(f"Price per 石: {a} 錢")
print(f"Price per 鈞: {c} 錢")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Weight Conversion**: The total weight is converted into 銖, the smallest unit, for easier calculations.
2. **Price per 銖**: The total money is divided by the total weight in 銖 to get the price per 銖.
3. **Price per 石 and 鈞**: The price per 銖 is multiplied by the number of 銖 in 1 石 and 1 鈞, respectively.

---

### Final Answer:
- **Price per 石**: `a` 錢.
- **Price per 鈞**: `c` 錢.
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 643737600/79949
Variable 'b' has wrong value. Expected: 4, Actual: 13970/79949
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 160934400/79949
Variable 'd' has wrong value. Expected: 5, Actual: 13970/79949"""
