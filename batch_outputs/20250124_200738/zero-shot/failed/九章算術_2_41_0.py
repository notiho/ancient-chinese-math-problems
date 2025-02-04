"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，斤 b錢 。其 c斤 ，斤 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight of silk. The total cost is given as 13,970 (錢), and the total weight is given as 1石 2鈞 28斤 3兩 5銖. We need to compute the price per 斤 (斤率).

### Conversion of weights:
1石 = 4鈞  
1鈞 = 30斤  
1斤 = 16兩  
1兩 = 24銖  

Thus, the total weight in 銖 (the smallest unit) is:  
\[ \text{Total weight in 銖} = (1 \times 4 \times 30 \times 16 \times 24) + (2 \times 30 \times 16 \times 24) + (28 \times 16 \times 24) + (3 \times 24) + 5 \]

We then convert the total weight back to 斤 (the unit we are interested in) by dividing by the number of 銖 in 1斤:  
\[ 1斤 = 16 \times 24 \text{ 銖} \]

Finally, the price per 斤 is calculated by dividing the total cost (13,970錢) by the total weight in 斤.

Here is the Python code to compute the values:


"""

#----- content starts here -----

from fractions import Fraction

# Total cost in 錢
total_cost = 13970

# Conversion factors
shi_to_jin = 4 * 30  # 1石 = 4鈞, 1鈞 = 30斤
jin_to_liang = 16    # 1斤 = 16兩
liang_to_zhu = 24    # 1兩 = 24銖

# Total weight in 銖
total_weight_in_zhu = (1 * shi_to_jin * jin_to_liang * liang_to_zhu) + \
                      (2 * 30 * jin_to_liang * liang_to_zhu) + \
                      (28 * jin_to_liang * liang_to_zhu) + \
                      (3 * liang_to_zhu) + \
                      5

# Convert total weight to 斤
total_weight_in_jin = Fraction(total_weight_in_zhu, jin_to_liang * liang_to_zhu)

# Price per 斤
price_per_jin = Fraction(total_cost, total_weight_in_jin)

# Assigning the results to variables
a = total_weight_in_jin  # Total weight in 斤
b = price_per_jin        # Price per 斤

# Output the results
a, b
#----- content ends here -----


"""


### Explanation of Variables:
- `a`: Total weight in 斤 (斤數)
- `b`: Price per 斤 (斤率)

### Final Answer:
The code will compute the values of `a` (total weight in 斤) and `b` (price per 斤 in 錢).
"""


"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 79949/384
Variable 'b' has wrong value. Expected: 67, Actual: 5364480/79949
Missing variable in output: 'c'
Missing variable in output: 'd'"""
