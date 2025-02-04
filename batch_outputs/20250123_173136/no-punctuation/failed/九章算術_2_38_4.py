"""
今有出錢一千一百二十買絲一石二鈞十八斤欲其貴賤斤率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a鈞 斤 b錢 其 c石 斤 d錢 
"""

"""
The problem and procedure you provided are a bit complex and involve proportional distribution of money across weights of silk. Let me carefully translate the problem and procedure into Python code step by step.

### Problem:
Suppose there is 1120 qian (units of money) used to buy 1 shi, 2 jun, and 18 jin of silk.  
The question asks for the price per jin (unit weight) of silk, dividing the total cost proportionally across the weights.

### Procedure:
1. Place the weights (shi, jun, jin, liang) as the divisor (法).
2. Multiply the total money (錢數) by the respective rates (所率) to get the dividend (實).
3. Divide the dividend by the divisor to get the price per unit.
4. If the divisor does not fully divide the dividend, adjust by subtracting the remainder.

### Answer:
The price per jun and jin is *a* qian, and the price per shi and jin is *c* qian.

---

Let's implement this step by step in Python:


"""


from fractions import Fraction

# 出錢一千一百二十
錢數 = 1120

# 買絲一石二鈞十八斤
石 = 1
鈞 = 2
斤 = 18

# 1 石 = 120 斤, 1 鈞 = 30 斤
總斤數 = 石 * 120 + 鈞 * 30 + 斤

# 各置所買石鈞斤兩以為法
法 = 總斤數

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
每斤價錢 = Fraction(實, 法)

# Convert to 鈞 and 石 prices
每鈞價錢 = 每斤價錢 * 30
每石價錢 = 每斤價錢 * 120

# Extract the results
a = 每鈞價錢
b = 每斤價錢
c = 每石價錢
d = 每斤價錢

# Output the results
print(f"其 {a} 鈞 斤 {b} 錢")
print(f"其 {c} 石 斤 {d} 錢")


"""


### Explanation:
1. **Weights Conversion**: Convert the weights into total jin (斤) since 1 shi = 120 jin and 1 jun = 30 jin.
2. **法 (Divisor)**: The total weight in jin is used as the divisor.
3. **實 (Dividend)**: The total money (1120 qian) is used as the dividend.
4. **Division**: Divide the total money by the total weight to get the price per jin. Multiply by 30 to get the price per jun and by 120 to get the price per shi.

Let me know if you need further clarification!
"""


"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 5600/33
Variable 'b' has wrong value. Expected: 5, Actual: 560/99
Variable 'c' has wrong value. Expected: 13/12, Actual: 22400/33
Variable 'd' has wrong value. Expected: 6, Actual: 560/99"""
