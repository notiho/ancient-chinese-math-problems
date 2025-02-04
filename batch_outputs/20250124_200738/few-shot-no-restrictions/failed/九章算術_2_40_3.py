"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
This problem involves calculating the price per unit weight (jin and jun) for silk based on the total cost and the total weight purchased. Let's break it down step by step and translate it into Python code.

### Problem Breakdown:
- **Total money spent**: 13,970 (in some currency).
- **Total weight purchased**: 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
- **Goal**: Calculate the price per jin and per jun.

### Conversion Factors:
1 shi = 4 jun  
1 jun = 30 jin  
1 jin = 16 liang  
1 liang = 24 zhu  

### Procedure:
1. Convert the total weight into a single unit (jin).
2. Calculate the price per jin by dividing the total money by the total weight in jin.
3. Calculate the price per jun by multiplying the price per jin by the number of jin in a jun (30 jin = 1 jun).

Now, let's implement this in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
total_money = 13970

# Total weight: 1 shi, 2 jun, 28 jin, 3 liang, 5 zhu
shi_to_jin = 4 * 30  # 1 shi = 4 jun, 1 jun = 30 jin
jun_to_jin = 30
liang_to_jin = Fraction(1, 16)  # 1 jin = 16 liang
zhu_to_jin = Fraction(1, 16 * 24)  # 1 liang = 24 zhu

# Convert total weight to jin
total_weight_in_jin = (
    1 * shi_to_jin +  # 1 shi
    2 * jun_to_jin +  # 2 jun
    28 +  # 28 jin
    3 * liang_to_jin +  # 3 liang
    5 * zhu_to_jin  # 5 zhu
)

# Calculate price per jin
price_per_jin = Fraction(total_money, total_weight_in_jin)

# Calculate price per jun (30 jin = 1 jun)
price_per_jun = price_per_jin * 30

# Results
a = price_per_jin
b = price_per_jun

print(f"Price per jin: {a} money")
print(f"Price per jun: {b} money")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Weight Conversion**: The total weight is converted into a single unit (jin) using the given conversion factors.
2. **Price Calculation**: The price per jin is calculated by dividing the total money by the total weight in jin. The price per jun is then derived by multiplying the price per jin by 30 (since 1 jun = 30 jin).
3. **Fraction Handling**: The `Fraction` class is used to ensure precise calculations, especially when dealing with non-integer values like liang and zhu.

### Final Answer:
- `a`: Price per jin (in money).
- `b`: Price per jun (in money).
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 5364480/79949
Variable 'b' has wrong value. Expected: 2012, Actual: 160934400/79949
Missing variable in output: 'c'
Missing variable in output: 'd'"""
