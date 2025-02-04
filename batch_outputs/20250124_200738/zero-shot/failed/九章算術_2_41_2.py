"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，斤 b錢 。其 c斤 ，斤 d錢 。
"""

"""
To solve this problem, we need to compute the cost per unit weight (斤, or "jin") of silk. The total cost is given as 13,970 units of money, and the total weight is expressed in a combination of 石 (shi), 鈞 (jun), 斤 (jin), 兩 (liang), and 銖 (zhu). We need to convert the total weight into a single unit (斤, jin) and then calculate the cost per jin.

### Conversion factors:
1 石 = 4 鈞  
1 鈞 = 30 斤  
1 斤 = 16 兩  
1 兩 = 24 銖  

### Given:
- Total cost = 13,970
- Total weight = 1 石, 2 鈞, 28 斤, 3 兩, 5 銖

### Steps:
1. Convert the total weight into 斤 (jin).
2. Calculate the cost per 斤 (jin).

Here is the Python code to compute the values:


"""

#----- content starts here -----

from fractions import Fraction

# Conversion factors
shi_to_jun = 4
jun_to_jin = 30
jin_to_liang = 16
liang_to_zhu = 24

# Total weight in various units
shi = 1
jun = 2
jin = 28
liang = 3
zhu = 5

# Total cost
total_cost = 13970

# Convert total weight to jin
total_weight_in_jin = (
    shi * shi_to_jun * jun_to_jin +
    jun * jun_to_jin +
    jin +
    Fraction(liang, jin_to_liang) +
    Fraction(zhu, jin_to_liang * liang_to_zhu)
)

# Calculate the cost per jin
cost_per_jin = Fraction(total_cost, total_weight_in_jin)

# Assign the results to variables
a = total_weight_in_jin  # Total weight in jin
b = cost_per_jin         # Cost per jin

# Output the results
a, b
#----- content ends here -----


"""


### Explanation of Variables:
- `a` represents the total weight in 斤 (jin).
- `b` represents the cost per 斤 (jin).

### Solution:
When you run the code, it will compute the values of `a` (total weight in jin) and `b` (cost per jin).
"""


"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 79949/384
Variable 'b' has wrong value. Expected: 67, Actual: 5364480/79949
Missing variable in output: 'c'
Missing variable in output: 'd'"""
