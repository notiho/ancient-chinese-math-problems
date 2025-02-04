"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
To solve this problem, we need to calculate the price per "斤" (a unit of weight) and the price per "鈞" (another unit of weight). The total weight is given in a mixed unit system, and the total cost is provided. Let's break it down step by step.

### Definitions:
1. **1 石 = 4 鈞**
2. **1 鈞 = 30 斤**
3. **1 斤 = 16 兩**
4. **1 兩 = 24 銖**

The total weight is given as **1 石 2 鈞 28 斤 3 兩 5 銖**, and the total cost is **13,970 錢**.

### Step 1: Convert the total weight into 銖 (the smallest unit).
We will first convert the entire weight into 銖 for easier calculations.

\[
\text{Total weight in 銖} = (1 \times 4 \times 30 \times 16 \times 24) + (2 \times 30 \times 16 \times 24) + (28 \times 16 \times 24) + (3 \times 24) + 5
\]

### Step 2: Calculate the price per 銖.
The price per 銖 is the total cost divided by the total weight in 銖.

### Step 3: Convert the price per 銖 into the price per 斤 and per 鈞.
- **Price per 斤**: Multiply the price per 銖 by \(16 \times 24\).
- **Price per 鈞**: Multiply the price per 銖 by \(30 \times 16 \times 24\).

### Step 4: Calculate the price per 石.
- **Price per 石**: Multiply the price per 鈞 by \(4\).

Here is the Python code to compute the values:


"""


from fractions import Fraction

# Given data
total_cost = 13970  # in 錢
total_weight_stone = 1  # 石
total_weight_jun = 2  # 鈞
total_weight_jin = 28  # 斤
total_weight_liang = 3  # 兩
total_weight_zhu = 5  # 銖

# Conversion factors
stone_to_jun = 4
jun_to_jin = 30
jin_to_liang = 16
liang_to_zhu = 24

# Step 1: Convert total weight to 銖
total_weight_in_zhu = (
    total_weight_stone * stone_to_jun * jun_to_jin * jin_to_liang * liang_to_zhu +
    total_weight_jun * jun_to_jin * jin_to_liang * liang_to_zhu +
    total_weight_jin * jin_to_liang * liang_to_zhu +
    total_weight_liang * liang_to_zhu +
    total_weight_zhu
)

# Step 2: Calculate the price per 銖
price_per_zhu = Fraction(total_cost, total_weight_in_zhu)

# Step 3: Calculate the price per 斤 and per 鈞
price_per_jin = price_per_zhu * (liang_to_zhu * jin_to_liang)
price_per_jun = price_per_jin * jun_to_jin

# Step 4: Calculate the price per 石
price_per_stone = price_per_jun * stone_to_jun

# Assign results to variables
a = price_per_jin  # Price per 斤
b = price_per_jun  # Price per 鈞
c = price_per_stone  # Price per 石
d = price_per_jun  # Price per 鈞 (repeated for 石 context)

# Results
a, b, c, d


"""


### Explanation of Results:
- `a` is the price per 斤 in 錢.
- `b` is the price per 鈞 in 錢.
- `c` is the price per 石 in 錢.
- `d` is the price per 鈞 in 錢 (same as `b`).

This code computes the values using the `Fraction` class to ensure accuracy in calculations involving non-integer results.
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 5364480/79949
Variable 'b' has wrong value. Expected: 2012, Actual: 160934400/79949
Variable 'c' has wrong value. Expected: 19253/11520, Actual: 643737600/79949
Variable 'd' has wrong value. Expected: 2013, Actual: 160934400/79949"""
