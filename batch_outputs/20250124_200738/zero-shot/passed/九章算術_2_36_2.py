"""
今有出錢一萬三千六百七十，買絲一石二鈞一十七斤。欲石率之，問︰石幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一石， a錢
"""

"""
To solve this problem, we need to calculate the cost per stone (石) of silk. The total cost is 13,670 (錢), and the total weight of silk purchased is 1 石, 2 鈞, and 17 斤. Let's first convert the weight into a single unit (斤), then calculate the cost per stone (石).

### Conversion factors:
- 1 石 = 4 鈞
- 1 鈞 = 30 斤

### Steps:
1. Convert the total weight into 斤.
2. Calculate the cost per 石 using the formula provided:
   \[
   \text{Cost per 石} = \frac{\text{Total cost}}{\text{Weight in 石}}
   \]

Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_cost = 13670  # in 錢
weight_stone = 1  # 石
weight_jun = 2  # 鈞
weight_jin = 17  # 斤

# Conversion factors
jun_to_jin = 30  # 1 鈞 = 30 斤
stone_to_jun = 4  # 1 石 = 4 鈞

# Convert total weight to 斤
total_weight_jin = (weight_stone * stone_to_jun * jun_to_jin) + (weight_jun * jun_to_jin) + weight_jin

# Convert total weight to 石
total_weight_stone = Fraction(total_weight_jin, stone_to_jun * jun_to_jin)

# Calculate cost per 石
a = Fraction(total_cost, total_weight_stone)

# Output the result
a  # Cost per 石 in 錢
#----- content ends here -----


"""


### Explanation of the result:
The variable `a` will contain the cost per 石 (in 錢).
"""


"""
"""
