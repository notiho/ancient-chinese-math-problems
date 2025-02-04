"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，斤 b錢 。其 c斤 ，斤 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (斤) based on the total money spent and the total weight purchased. Here's the Python code following the procedure:


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
# 1 石 = 120 斤, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
總斤 = 石 * 120 + 鈞 * 30 + 斤 + Fraction(兩, 16) + Fraction(銖, 16 * 24)

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
斤率 = Fraction(實, 總斤)

# 不滿法者反以實減法，法賤實貴
a = 石
b = 斤率
c = 1  # 每斤
d = 斤率

# Output the results
print(f"其 {a} 石，斤 {b} 錢。其 {c} 斤，斤 {d} 錢。")


"""


### Explanation:
1. **Convert weights to a common unit (斤):**
   - 1 石 = 120 斤
   - 1 鈞 = 30 斤
   - 1 斤 = 16 兩
   - 1 兩 = 24 銖
   - Total weight is calculated in terms of 斤.

2. **Calculate the rate per 斤:**
   - Divide the total money (`錢數`) by the total weight (`總斤`) to get the price per 斤.

3. **Output the results:**
   - The price per 斤 is the same for both the total weight and for 1 斤.

Let me know if you need further clarification!
"""


"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 1
Variable 'b' has wrong value. Expected: 67, Actual: 5364480/79949
Variable 'c' has wrong value. Expected: 7897/384, Actual: 1
Variable 'd' has wrong value. Expected: 68, Actual: 5364480/79949"""
