"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
This problem involves calculating the price per unit weight of silk based on the total cost and total weight. Let's break it down and translate it into Python code step by step, following the ancient Chinese mathematical procedure.

### Problem Setup:
- Total money spent: 13,970 (in some unit of currency).
- Total weight of silk: 1 石 (shi), 2 鈞 (jun), 28 斤 (jin), 3 兩 (liang), 5 銖 (zhu).
- The goal is to calculate the price per 銖 (zhu) and express the result in terms of 鈞 (jun) and 銖 (zhu) per unit of money.

### Procedure:
The procedure involves reversing the rate to find the price per unit weight. The steps are as follows:
1. Use the total money as the divisor (法, "the law").
2. Use the total weight as the dividend (實, "the actual").
3. Perform the division to find the rate per unit weight.
4. If the dividend is less than the divisor, adjust accordingly.
5. Multiply the result by the total weight to verify the calculation.

Let's implement this in Python:


"""


from fractions import Fraction

# Total money spent
錢數 = 13970

# Total weight in 銖 (convert all units to 銖 for consistency)
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Conversion factors
石_to_銖 = 120000  # 1 石 = 120000 銖
鈞_to_銖 = 10000   # 1 鈞 = 10000 銖
斤_to_銖 = 160     # 1 斤 = 160 銖
兩_to_銖 = 10      # 1 兩 = 10 銖

# Total weight in 銖
總銖 = (石 * 石_to_銖) + (鈞 * 鈞_to_銖) + (斤 * 斤_to_銖) + (兩 * 兩_to_銖) + 銖

# Perform the division to find the rate per 銖
銖率 = Fraction(錢數, 總銖)

# Convert the rate back to 鈞 and 銖 for readability
銖率_鈞 = 銖率 * 鈞_to_銖  # Convert 銖 rate to 鈞 rate
a = 銖率_鈞.numerator // 銖率_鈞.denominator  # Whole 鈞
b = 銖率_鈞.numerator % 銖率_鈞.denominator  # Remaining 銖

# Convert the rate back to 石 and 銖 for readability
銖率_石 = 銖率 * 石_to_銖  # Convert 銖 rate to 石 rate
c = 銖率_石.numerator // 銖率_石.denominator  # Whole 石
d = 銖率_石.numerator % 銖率_石.denominator  # Remaining 銖

# Output the results
print(f"其 {a} 鈞, {b} 銖 一錢。其 {c} 石, {d} 銖 一錢。")


"""


### Explanation of the Code:
1. **Conversion to 銖:** All weight units are converted to 銖 for consistency, using the given conversion factors.
2. **Division:** The total money is divided by the total weight in 銖 to find the rate per 銖.
3. **Conversion Back:** The rate per 銖 is converted back to 鈞 and 銖, as well as 石 and 銖, for readability.
4. **Output:** The results are displayed in the required format.

### Answer:
The output will provide the rate in terms of 鈞 and 銖 per unit of money, as well as 石 and 銖 per unit of money.
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 966
Variable 'b' has wrong value. Expected: 5, Actual: 19702
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 11600
Variable 'd' has wrong value. Expected: 6, Actual: 5200"""
