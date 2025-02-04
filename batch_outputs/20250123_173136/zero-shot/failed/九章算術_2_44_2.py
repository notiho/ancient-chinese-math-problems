"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a翭 ， b翭 一錢 其 c翭 ， d翭 一錢
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the rates (貴賤率) of two types of items (a翭 and c翭) based on the total money spent and the total quantity of items purchased.

Here is the Python code:


"""


from fractions import Fraction

# Given data
total_money = 610  # Total money spent (錢數)
total_items = 2100  # Total items purchased (羽)

# Step 1: Calculate the rates
# Let a翭 = 1翭 per 1錢 (貴 rate)
# Let c翭 = 1翭 per 1錢 (賤 rate)
# The problem states that the rates are inversely proportional to their quantities.

# Calculate the quantities
a = Fraction(total_money, total_items)  # 貴翭 rate (a翭 per 錢)
b = Fraction(total_items, total_money)  #賤翭 rate

# Output the results
print("a翭:", a翭)
print("b翭:", b翭)


"""

"""


"""
Code error: name 'a翭' is not defined"""
