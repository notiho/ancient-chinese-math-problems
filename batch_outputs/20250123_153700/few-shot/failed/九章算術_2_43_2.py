"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
This problem involves calculating the price per unit weight of silk based on the total cost and the total weight. Let's break it down step by step according to the procedure provided.

### Problem Breakdown:
- Total money spent: 13,970 (錢)
- Total weight of silk: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
- The goal is to calculate the price per 銖 (smallest unit of weight).

### Weight Conversion:
1 石 = 4 鈞  
1 鈞 = 30 斤  
1 斤 = 16 兩  
1 兩 = 24 銖  

Thus, the total weight in 銖 is calculated as follows:
- 1 石 = 4 鈞 = 4 × 30 × 16 × 24 銖
- 2 鈞 = 2 × 30 × 16 × 24 銖
- 28 斤 = 28 × 16 × 24 銖
- 3 兩 = 3 × 24 銖
- 5 銖 = 5 銖

### Procedure:
The procedure ("反其率術") involves calculating the price per 銖 by dividing the total money by the total weight in 銖. Then, the price per 銖 can be used to calculate the price per 鈞 and per 石.

### Python Code:

"""


from fractions import Fraction

# Total money spent
錢數 = 13970

# Total weight in 銖
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

# Total weight in 銖
總銖 = (石 * 石_to_銖) + (鈞 * 鈞_to_銖) + (斤 * 斤_to_銖) + (兩 * 兩_to_銖) + 銖

# Price per 銖
銖率 = Fraction(錢數, 總銖)

# Price per 鈞
鈞率 = 銖率 * 鈞_to_銖

# Price per 石
石率 = 銖率 * 石_to_銖

# Results
a = 鈞率.numerator  # 鈞 rate (numerator of the fraction)
b = 鈞率.denominator  # 鈞 rate (denominator of the fraction)
c = 石率.numerator  # 石 rate (numerator of the fraction)
d = 石率.denominator  # 石 rate (denominator of the fraction)

# Output
print(f"其 {a} 鈞 ， {b} 銖 一錢。 其 {c} 石 ， {d} 銖 一錢。")


"""


### Explanation of the Code:
1. **Weight Conversion**: The total weight in 銖 is calculated by converting 石, 鈞, 斤, 兩, and 銖 into the smallest unit (銖).
2. **Price per 銖**: The total money is divided by the total weight in 銖 to get the price per 銖.
3. **Price per 鈞 and 石**: Using the price per 銖, the price per 鈞 and 石 is calculated by multiplying by the respective conversion factors.
4. **Fraction Representation**: The results are represented as fractions to maintain precision.

### Final Output:
The program will output the price per 鈞 and per 石 in terms of 銖 per 錢.
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 160934400
Variable 'b' has wrong value. Expected: 5, Actual: 79949
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 643737600
Variable 'd' has wrong value. Expected: 6, Actual: 79949"""
