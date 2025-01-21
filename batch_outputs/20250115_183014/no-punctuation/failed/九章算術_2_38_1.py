"""
今有出錢一千一百二十買絲一石二鈞十八斤欲其貴賤斤率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a鈞 斤 b錢 其 c石 斤 d錢 
"""

"""
The problem you provided is quite complex and involves proportional distribution of money across weights of silk (石, 鈞, 斤, etc.). However, the description of the procedure ("術") is somewhat ambiguous and requires careful interpretation. Based on the text, I will attempt to translate the procedure into Python code.

### Problem Breakdown:
- You have **1120 units of money**.
- You are buying **1 石, 2 鈞, and 18 斤** of silk.
- The goal is to determine the price per unit weight (斤 rate) and the distribution of money across the weights.

### Procedure ("術"):
1. Place the weights (石, 鈞, 斤, etc.) as the divisor (法).
2. Multiply the total money by the weights to calculate the dividend (實).
3. Divide the dividend by the divisor to determine the rate.
4. If there is a remainder, adjust the calculation by subtracting the remainder from the divisor.
5. The result gives the price per unit weight.

### Python Code:

"""


from fractions import Fraction

# 出錢一千一百二十
錢數 = 1120

# 買絲一石二鈞十八斤
石 = 1
鈞 = 2
斤 = 18

# 各置所買石鈞斤兩以為法
法 = 石 * 100 + 鈞 * 20 + 斤  # Convert everything to 斤 (1 石 = 100 斤, 1 鈞 = 20 斤)

# 以所率乘錢數為實
實 = 錢數 * 法

# 實如法而一
斤率 = Fraction(錢數, 法)  # Price per 斤

# 不滿法者反以實減法法賤實貴
# (This step is ambiguous in the original text, but it seems to involve adjusting for remainders if needed.)

# Calculate the distribution of money:
# Price for 1 石
石價 = 斤率 * 100

# Price for 2 鈞
鈞價 = 斤率 * 20 * 2

# Price for 18 斤
斤價 = 斤率 * 18

# Results
a = 石價  # Price for 1 石
b = 鈞價  # Price for 2 鈞
c = 斤價  # Price for 18 斤

print(f"其 1 石價 {a} 錢, 其 2 鈞價 {b} 錢, 其 18 斤價 {c} 錢")


"""


### Explanation of Variables:
- `錢數`: Total money (1120).
- `石`, `鈞`, `斤`: Weights of silk being purchased.
- `法`: Total weight converted to 斤.
- `斤率`: Price per 斤.
- `石價`, `鈞價`, `斤價`: Distribution of money across the weights.

### Output:
The code will calculate and display the price for 1 石, 2 鈞, and 18 斤 of silk. If further clarification of the procedure is needed, adjustments can be made.
"""


"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 56000/79
Variable 'b' has wrong value. Expected: 5, Actual: 22400/79
Variable 'c' has wrong value. Expected: 13/12, Actual: 10080/79
Missing variable in output: 'd'"""
