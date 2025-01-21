"""
今有出錢五百七十六，買竹七十八箇。欲其大小率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a箇 ，箇 b錢 。其 c箇 ，箇 d錢 。
"""

"""
This problem involves dividing 576 coins among 78 bamboo pieces, with the goal of determining the price per piece for two categories of bamboo (e.g., large and small). The procedure provided describes a proportional distribution based on the "rate" (大小率). Let's break it down and solve step by step.

### Problem Restatement:
- Total money: 576 coins.
- Total bamboo: 78 pieces.
- The bamboo is divided into two categories: large and small.
- The rates (大小率) for the two categories are not explicitly given in the problem, so we will assume a ratio of 2:1 (e.g., large bamboo is twice as expensive as small bamboo).
- Question: How many pieces of each category, and how much does each piece cost?

### Procedure Explanation:
1. **Rate Setup**: The rates for the two categories are set (e.g., large:small = 2:1).
2. **Proportional Distribution**: Use the rates to divide the total bamboo into two groups.
3. **Calculate Costs**: Assign costs to each category based on the rates and total money.
4. **Adjust for Remainders**: If there are any remainders, adjust the distribution accordingly.

### Solution in Python Code:


"""


from fractions import Fraction

# Total money and bamboo
total_money = 576
total_bamboo = 78

# Rates for large and small bamboo (assumed 2:1)
large_rate = 2
small_rate = 1

# Total rate (sum of the rates)
total_rate = large_rate + small_rate

# Proportional distribution of bamboo
large_bamboo = Fraction(large_rate, total_rate) * total_bamboo
small_bamboo = Fraction(small_rate, total_rate) * total_bamboo

# Cost per piece for each category
large_cost = Fraction(large_rate, total_rate) * total_money / large_bamboo
small_cost = Fraction(small_rate, total_rate) * total_money / small_bamboo

# Results
a = large_bamboo
b = large_cost
c = small_bamboo
d = small_cost

# Output
a, b, c, d


"""


### Explanation of Variables:
- `a`: Number of large bamboo pieces.
- `b`: Cost per large bamboo piece.
- `c`: Number of small bamboo pieces.
- `d`: Cost per small bamboo piece.

### Final Answer:
The code will calculate the exact values for `a`, `b`, `c`, and `d` based on the assumed rate of 2:1. If the rates are different, they can be adjusted in the `large_rate` and `small_rate` variables.
"""


"""
Variable 'a' has wrong value. Expected: 48, Actual: 52
Variable 'b' has wrong value. Expected: 7, Actual: 96/13
Variable 'c' has wrong value. Expected: 30, Actual: 26
Variable 'd' has wrong value. Expected: 8, Actual: 96/13"""
