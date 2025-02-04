"""
今有出錢七百二十，買縑一匹二丈一尺。欲丈率之，問︰丈幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一丈， a錢
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the cost per丈 (unit of length) when 720錢 is spent to buy 1匹 (piece) of silk that is 2丈1尺 in length. Note that 1丈 = 10尺.

### Problem Breakdown:
1. Total money spent = 720錢.
2. Total length of silk = 2丈1尺 = \(2 \times 10 + 1 = 21\) 尺.
3. We need to calculate the cost per丈 (a錢).

The formula provided in the problem is:
\[
\text{Cost per丈 (a)} = \frac{\text{Total money spent (錢)}}{\text{Total length in 丈}}.
\]

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_money = 720  # 錢
total_length_in_zhang = Fraction(21, 10)  # Convert 21尺 to 丈 (1丈 = 10尺)

# Calculate cost per 丈
a = Fraction(total_money, total_length_in_zhang)

# Output the result
a  # Cost per 丈 in 錢
#----- content ends here -----


"""


### Explanation:
1. Convert the total length from 尺 to 丈 using the conversion \(1丈 = 10尺\).
2. Use the formula to calculate the cost per丈.
3. The result `a` will be in terms of 錢 per丈.


"""


"""
Variable 'a' has wrong value. Expected: 7200/61, Actual: 2400/7"""
