"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，斤 b錢 。其 c斤 ，斤 d錢 。
"""

"""
To solve this problem, we need to compute the price per unit weight of silk in terms of "石" (shi), "斤" (jin), and other units. The total cost is 13,970 units of money, and the total weight is given as 1石 (shi), 2鈞 (jun), 28斤 (jin), 3兩 (liang), and 5銖 (zhu). We'll calculate the price per unit weight in terms of "石" and "斤."

The weight units are related as follows:
1石 = 4鈞  
1鈞 = 30斤  
1斤 = 16兩  
1兩 = 24銖  

### Step 1: Convert the total weight into a single unit (斤)
1石 = 4鈞 = 4 × 30斤 = 120斤  
2鈞 = 2 × 30斤 = 60斤  
28斤 = 28斤  
3兩 = 3 × (1/16)斤 = 3/16斤  
5銖 = 5 × (1/16 × 1/24)斤 = 5/(16 × 24)斤 = 5/384斤  

Total weight in 斤:
\[
\text{Total weight} = 120 + 60 + 28 + \frac{3}{16} + \frac{5}{384}
\]

### Step 2: Compute the price per 斤
The total cost is 13,970. To find the price per 斤:
\[
\text{Price per 斤} = \frac{\text{Total cost}}{\text{Total weight}}
\]

### Step 3: Compute the price per 石
Since 1石 = 120斤, the price per 石 is:
\[
\text{Price per 石} = \text{Price per 斤} × 120
\]

### Python Code

"""


from fractions import Fraction

# Total cost
total_cost = 13970

# Total weight in 斤
total_weight = 120 + 60 + 28 + Fraction(3, 16) + Fraction(5, 384)

# Price per 斤
b = Fraction(total_cost, total_weight)

# Price per 石
a = b * 120

# Results
print(f"Price per 石 (a): {a} units of money")
print(f"Price per 斤 (b): {b} units of money")


"""


### Final Answer
The price per 石 is stored in variable `a`, and the price per 斤 is stored in variable `b`.
"""


"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 643737600/79949
Variable 'b' has wrong value. Expected: 67, Actual: 5364480/79949
Missing variable in output: 'c'
Missing variable in output: 'd'"""
