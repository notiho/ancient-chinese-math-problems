"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
To solve this problem, we need to calculate the price per "斤" (jin) and per "石" (shi) based on the total cost and the total weight. The total weight is given in a combination of units: 石 (shi), 鈞 (jun), 斤 (jin), 兩 (liang), and 銖 (zhu). We will convert all these units into a single unit (斤) for simplicity.

### Conversion factors:
1 石 = 4 鈞  
1 鈞 = 30 斤  
1 斤 = 16 兩  
1 兩 = 24 銖  

### Given:
- Total cost = 13,970 錢
- Total weight = 1 石 2 鈞 28 斤 3 兩 5 銖

We will calculate the price per 斤 (`a`) and the price per 鈞 (`b`), as well as the price per 石 (`c`) and the price per 鈞 (`d`).

Here is the Python code to compute the values:


"""


from fractions import Fraction

# Conversion factors
shi_to_jun = 4
jun_to_jin = 30
jin_to_liang = 16
liang_to_zhu = 24

# Total cost in 錢
total_cost = 13970

# Total weight in 石, 鈞, 斤, 兩, 銖
shi = 1
jun = 2
jin = 28
liang = 3
zhu = 5

# Convert total weight to 斤
total_weight_in_jin = (
    shi * shi_to_jun * jun_to_jin +
    jun * jun_to_jin +
    jin +
    liang / jin_to_liang +
    zhu / (jin_to_liang * liang_to_zhu)
)

# Price per 斤 (a 錢 per 斤)
a = Fraction(total_cost, total_weight_in_jin)

# Price per 鈞 (b 錢 per 鈞)
b = a * jun_to_jin

# Price per 石 (c 錢 per 石)
c = b * shi_to_jun

# Price per 鈞 (d 錢 per 鈞, same as b)
d = b

# Results
a, b, c, d


"""


### Explanation of the Code:
1. Convert the total weight into 斤 using the given conversion factors.
2. Calculate the price per 斤 (`a`) by dividing the total cost by the total weight in 斤.
3. Calculate the price per 鈞 (`b`) by multiplying the price per 斤 (`a`) by the number of 斤 in a 鈞.
4. Calculate the price per 石 (`c`) by multiplying the price per 鈞 (`b`) by the number of 鈞 in a 石.
5. The price per 鈞 (`d`) is the same as `b`.

### Output:
The variables `a`, `b`, `c`, and `d` will contain the respective prices in 錢 for each unit.
"""


"""
Code error: both arguments should be Rational instances"""
