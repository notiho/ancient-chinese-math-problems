"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
To solve this problem, we need to calculate the price per "斤" (jin) and per "石" (shi) based on the total cost and the total weight of the silk. Here's the Python code to compute the values of the unknowns `a`, `b`, `c`, and `d`:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
total_money = 13970  # in 錢

# Total weight of silk
shi = 1  # 石
jun = 2  # 鈞
jin = 28  # 斤
liang = 3  # 兩
zhu = 5  # 銖

# Conversion factors
jin_per_liang = Fraction(1, 16)  # 1 兩 = 1/16 斤
jin_per_zhu = Fraction(1, 16 * 24)  # 1 銖 = 1/(16*24) 斤
jin_per_jun = 30  # 1 鈞 = 30 斤
jin_per_shi = 300  # 1 石 = 300 斤

# Total weight in 斤
total_weight_in_jin = (
    shi * jin_per_shi +
    jun * jin_per_jun +
    jin +
    liang * jin_per_liang +
    zhu * jin_per_zhu
)

# Price per 斤 (a 錢 per 斤)
a = Fraction(total_money, total_weight_in_jin)

# Price per 鈞 (b 錢 per 鈞)
b = a * jin_per_jun

# Price per 石 (c 錢 per 石)
c = a * jin_per_shi

# Price per 鈞 when considering 石 (d 錢 per 鈞)
d = c / 10  # 1 石 = 10 鈞

# Results
a, b, c, d
#----- content ends here -----


"""


### Explanation:
1. **Total weight calculation**: The total weight is converted into "斤" (jin) using the given conversion factors.
2. **Price per unit**:
   - `a`: Price per "斤" is calculated by dividing the total money by the total weight in "斤".
   - `b`: Price per "鈞" is derived by multiplying the price per "斤" by the number of "斤" in a "鈞".
   - `c`: Price per "石" is derived by multiplying the price per "斤" by the number of "斤" in a "石".
   - `d`: Price per "鈞" when considering "石" is derived by dividing the price per "石" by the number of "鈞" in a "石".

### Output:
The variables `a`, `b`, `c`, and `d` will contain the respective prices in terms of "錢".
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 5364480/149069
Variable 'b' has wrong value. Expected: 2012, Actual: 160934400/149069
Variable 'c' has wrong value. Expected: 19253/11520, Actual: 1609344000/149069
Variable 'd' has wrong value. Expected: 2013, Actual: 160934400/149069"""
