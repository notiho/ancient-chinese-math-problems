"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (石, 鈞, etc.) based on the total amount of money spent and the total weight of silk purchased. Here's the step-by-step procedure encoded in Python:


"""


from fractions import Fraction

# 出錢一萬三千九百七十
錢數 = 13970

# 買絲一石二鈞二十八斤三兩五銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# 各置所買石、鈞、斤、兩以為法
石法 = 1
鈞法 = 10  # 1 石 = 10 鈞
斤法 = 100  # 1 石 = 100 斤
兩法 = 1000  # 1 石 = 1000 兩
銖法 = 16000  # 1 石 = 16000 銖

# Convert the total weight into 銖 (smallest unit)
總銖 = (
    石 * 銖法 +
    鈞 * (銖法 // 鈞法) +
    斤 * (銖法 // 斤法) +
    兩 * (銖法 // 兩法) +
    銖
)

# Calculate the price per 銖
銖價 = Fraction(錢數, 總銖)

# Convert 銖價 to 鈞 and 石 rates
鈞價 = 銖價 * (銖法 // 鈞法)
石價 = 銖價 * 銖法

# Results
a = 鈞價.numerator
b = 鈞價.denominator
c = 石價.numerator
d = 石價.denominator

# Output
print(f"其 {a} 鈞 ，石 {b} 錢 。其 {c} 石 ，石 {d} 錢 。")


"""


### Explanation:
1. **Weight Conversion**: The total weight of silk is converted into the smallest unit (銖) for precise calculations.
2. **Price per Unit**: The price per 銖 is calculated by dividing the total money by the total weight in 銖.
3. **Unit Conversion**: The price per 鈞 and per 石 is derived by multiplying the price per 銖 by the respective conversion factors.
4. **Fraction Representation**: The results are expressed as fractions to maintain precision.

### Answer:
The output will provide the price per 鈞 and per 石 in terms of 錢.
"""


"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 22352000
Variable 'b' has wrong value. Expected: 8051, Actual: 23733
Variable 'c' has wrong value. Expected: 68201/46080, Actual: 223520000
Variable 'd' has wrong value. Expected: 8052, Actual: 23733"""
