"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
This problem involves calculating the price per unit weight of silk based on the total cost and the total weight. The weight is given in a traditional Chinese system (石, 鈞, 斤, 兩, 銖), and the task is to determine the price per unit for each weight category.

### Problem Breakdown:
1. **Total Money**: 13,970 (in some monetary unit).
2. **Total Weight**: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖.
3. **Goal**: Calculate the price per 石 and per 鈞.

### Conversion of Weight:
We need to convert the total weight into a single unit for calculation. The traditional Chinese weight system is as follows:
- 1 石 = 4 鈞
- 1 鈞 = 30 斤
- 1 斤 = 16 兩
- 1 兩 = 24 銖

Thus, the total weight in 銖 (the smallest unit) is:
\[
\text{Total Weight} = (1 \times 4 \times 30 \times 16 \times 24) + (2 \times 30 \times 16 \times 24) + (28 \times 16 \times 24) + (3 \times 24) + 5
\]

### Price Calculation:
The price per unit weight is calculated by dividing the total money by the total weight in the desired unit. For example:
- Price per 石: Divide the total money by the total weight in 石.
- Price per 鈞: Divide the total money by the total weight in 鈞.

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Total money
total_money = 13970

# Conversion factors
石_to_銖 = 4 * 30 * 16 * 24
鈞_to_銖 = 30 * 16 * 24
斤_to_銖 = 16 * 24
兩_to_銖 = 24

# Total weight in 銖
total_weight_銖 = (
    1 * 石_to_銖 +
    2 * 鈞_to_銖 +
    28 * 斤_to_銖 +
    3 * 兩_to_銖 +
    5
)

# Price per 銖
price_per_銖 = Fraction(total_money, total_weight_銖)

# Price per 石
price_per_石 = price_per_銖 * 石_to_銖

# Price per 鈞
price_per_鈞 = price_per_銖 * 鈞_to_銖

# Results
a = price_per_石
b = price_per_銖 * 兩_to_銖  # Price per 兩
c = price_per_鈞
d = price_per_銖 * 斤_to_銖  # Price per 斤

print(f"Price per 石: {a} money")
print(f"Price per 鈞: {c} money")
#----- content ends here -----


"""


### Explanation of Results:
- `a` is the price per 石.
- `b` is the price per 兩.
- `c` is the price per 鈞.
- `d` is the price per 斤.

This code calculates the price for each unit weight based on the given total cost and weight.
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 643737600/79949
Variable 'b' has wrong value. Expected: 4, Actual: 335280/79949
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 160934400/79949
Variable 'd' has wrong value. Expected: 5, Actual: 5364480/79949"""
