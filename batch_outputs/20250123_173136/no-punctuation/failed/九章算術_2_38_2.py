"""
今有出錢一千一百二十買絲一石二鈞十八斤欲其貴賤斤率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a鈞 斤 b錢 其 c石 斤 d錢 
"""

"""
The problem and procedure you provided are a bit complex and involve proportional distribution of money to calculate the price per unit weight of silk. Let me carefully translate and encode the procedure into Python step by step.

### Problem:
Suppose there is 1120 qian spent to buy 1 shi, 2 jun, and 18 jin of silk.  
Question: What is the price per jin (unit rate) for both expensive and cheap silk?

### Procedure:
1. Place the amounts of shi, jun, jin, and liang as the divisor (法, "the base").
2. Multiply the divisor by the total money (錢數) to form the dividend (實, "the product").
3. Divide the dividend by the divisor to calculate the unit rate.
4. If the divisor is not fully divisible, reverse the calculation to adjust the result.

### Answer:
The answer will provide the price per unit weight for both expensive and cheap silk.

Now, let's encode this step by step in Python:


"""


from fractions import Fraction

# 出錢一千一百二十
錢數 = 1120

# 買絲一石二鈞十八斤
石 = 1
鈞 = 2
斤 = 18

# 1 石 = 120 斤, 1 鈞 = 30 斤
總斤 = 石 * 120 + 鈞 * 30 + 斤

# 各置所買石鈞斤兩以為法 (法 = 總斤)
法 = 總斤

# 以所率乘錢數為實 (實 = 錢數)
實 = 錢數

# 實如法而一 (unit rate per jin)
單價 = Fraction(實, 法)

# 不滿法者反以實減法 (adjustments for expensive and cheap rates)
# 貴 (expensive rate)
貴 = 單價 + 1

# 賤 (cheap rate)
賤 = 單價 - 1

# Output results
a = 貴
b = 賤

print(f"其貴每斤 {a} 錢")
print(f"其賤每斤 {b} 錢")


"""


### Explanation:
1. The total weight in jin is calculated by converting shi and jun into jin.
2. The divisor (法) is the total weight in jin.
3. The dividend (實) is the total money spent.
4. The unit price per jin is calculated as `實 / 法`.
5. Adjustments are made for expensive and cheap rates by adding or subtracting 1.

This code will calculate the expensive and cheap rates per jin of silk. Let me know if you need further clarification!
"""


"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 659/99
Variable 'b' has wrong value. Expected: 5, Actual: 461/99
Missing variable in output: 'c'
Missing variable in output: 'd'"""
