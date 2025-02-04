"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
This problem involves calculating the price per unit weight (銖 rate) of silk based on the total cost and total weight. Let's break it down and encode the solution in Python.

### Problem Breakdown:
- **Total money spent**: 13,970 (錢)
- **Total weight of silk**: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
- **Goal**: Calculate the price per 銖 (smallest unit of weight).

### Conversion of weights:
1 石 = 4 鈞  
1 鈞 = 30 斤  
1 斤 = 16 兩  
1 兩 = 24 銖  

Thus, we first convert the total weight into 銖.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
total_money = 13970  # 錢

# Total weight of silk in 石, 鈞, 斤, 兩, 銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Conversion factors
石_to_銖 = 4 * 30 * 16 * 24
鈞_to_銖 = 30 * 16 * 24
斤_to_銖 = 16 * 24
兩_to_銖 = 24

# Convert total weight to 銖
total_weight_銖 = (
    石 * 石_to_銖 +
    鈞 * 鈞_to_銖 +
    斤 * 斤_to_銖 +
    兩 * 兩_to_銖 +
    銖
)

# Calculate price per 銖
price_per_銖 = Fraction(total_money, total_weight_銖)

# Convert price per 銖 back to 鈞 and 石 rates
銖_per_鈞 = 鈞_to_銖
銖_per_石 = 石_to_銖

price_per_鈞 = price_per_銖 * 銖_per_鈞
price_per_石 = price_per_銖 * 銖_per_石

# Extract integer and fractional parts for 鈞 and 石
a = price_per_鈞.numerator // price_per_鈞.denominator  # Integer part for 鈞
b = price_per_鈞 - a                                   # Fractional part for 鈞

c = price_per_石.numerator // price_per_石.denominator  # Integer part for 石
d = price_per_石 - c                                   # Fractional part for 石

# Output the results
print(f"其 {a} 鈞, {b} 銖 一錢。其 {c} 石, {d} 銖 一錢。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Weight Conversion**: The total weight is converted into 銖, the smallest unit, using the given conversion factors.
2. **Price per 銖**: The total money is divided by the total weight in 銖 to get the price per 銖.
3. **Price per 鈞 and 石**: The price per 鈖 is scaled up to calculate the price per 鈞 and per 石.
4. **Integer and Fractional Parts**: The integer and fractional parts of the price per 鈞 and per 石 are extracted for the final answer.

---

### Final Output:
The program will output the price per 鈞 and per 石 in the format:
```
其 a 鈞, b 銖 一錢。其 c 石, d 銖 一錢。
```
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 2012
Variable 'b' has wrong value. Expected: 5, Actual: 77012/79949
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 8051
Variable 'd' has wrong value. Expected: 6, Actual: 68201/79949"""
