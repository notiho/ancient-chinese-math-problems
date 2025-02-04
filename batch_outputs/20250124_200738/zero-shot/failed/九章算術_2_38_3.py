"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，斤 b錢 。其 c石 ，斤 d錢 。
"""

"""
To solve this problem, we need to calculate the cost per unit weight (斤) for silk, given the total cost and the total weight. The weight is given in a combination of 石 (stone), 鈞 (jun), and 斤 (jin), and the total cost is 1120 units of money. The problem asks us to compute the cost per 鈞 (a) and the cost per 石 (c), as well as the cost per 斤 in each case (b and d, respectively).

Here is the Python code to compute the values:


"""

#----- content starts here -----

from fractions import Fraction

# Total cost in money
total_cost = 1120

# Total weight in 石, 鈞, and 斤
stones = 1  # 1 石
juns = 2    # 2 鈞
jins = 18   # 18 斤

# Conversion factors
jins_per_jun = 30  # 1 鈞 = 30 斤
jins_per_stone = 300  # 1 石 = 300 斤

# Total weight in 斤
total_weight_in_jins = stones * jins_per_stone + juns * jins_per_jun + jins

# Cost per 斤
cost_per_jin = Fraction(total_cost, total_weight_in_jins)

# Cost per 鈞 (a) and per 斤 in 鈞 (b)
a = cost_per_jin * jins_per_jun  # Cost per 鈞
b = cost_per_jin  # Cost per 斤 in 鈞

# Cost per 石 (c) and per 斤 in 石 (d)
c = cost_per_jin * jins_per_stone  # Cost per 石
d = cost_per_jin  # Cost per 斤 in 石

# Results
a, b, c, d
#----- content ends here -----


"""


### Explanation of the Code:
1. **Total Weight Calculation**:
   - Convert the total weight into 斤 using the conversion factors: 1 石 = 300 斤, 1 鈞 = 30 斤.
   - Add up the weights in 石, 鈞, and 斤 to get the total weight in 斤.

2. **Cost per 斤**:
   - Divide the total cost by the total weight in 斤 to get the cost per 斤.

3. **Cost per 鈞 and per 石**:
   - Multiply the cost per 斤 by the number of 斤 in 1 鈞 (30) to get the cost per 鈞.
   - Multiply the cost per 斤 by the number of 斤 in 1 石 (300) to get the cost per 石.

4. **Output**:
   - The variables `a`, `b`, `c`, and `d` store the respective costs as required.

### Results:
The variables `a`, `b`, `c`, and `d` will contain the following values:
- `a`: Cost per 鈞
- `b`: Cost per 斤 in 鈞
- `c`: Cost per 石
- `d`: Cost per 斤 in 石
"""


"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 800/9
Variable 'b' has wrong value. Expected: 5, Actual: 80/27
Variable 'c' has wrong value. Expected: 13/12, Actual: 8000/9
Variable 'd' has wrong value. Expected: 6, Actual: 80/27"""
