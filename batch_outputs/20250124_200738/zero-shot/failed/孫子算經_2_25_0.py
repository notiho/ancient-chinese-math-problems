"""
今有女子善織，日自倍，五日織通五尺。問：日織幾何？
術曰：各置列衰副，并得三十一為法，以五尺乘并者，各自為實，實如法而一，即得。
答曰：初日織 a寸 ，次日織 b寸 ，次日織 c寸 ，次日織 d尺 ，次日織 e尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem describes a woman weaving cloth, where her daily output doubles each day, and in five days, she weaves a total of 5 feet (or 60 inches, since 1 foot = 12 inches). We need to find how much she weaves each day.

The solution involves setting up the equations based on the doubling pattern and solving for the unknowns \(a\), \(b\), \(c\), \(d\), and \(e\), which represent the amount woven each day.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total woven in 5 days = 5 feet = 60 inches
total_inches = 5 * 12

# Let the amount woven each day be:
# Day 1: a inches
# Day 2: b inches = 2 * a
# Day 3: c inches = 2 * b = 4 * a
# Day 4: d inches = 2 * c = 8 * a
# Day 5: e inches = 2 * d = 16 * a

# Total woven in 5 days:
# a + b + c + d + e = total_inches
# a + 2a + 4a + 8a + 16a = total_inches
# 31a = total_inches

# Solve for a
a = Fraction(total_inches, 31)

# Calculate b, c, d, e
b = 2 * a
c = 4 * a
d = 8 * a
e = 16 * a

# The results
a, b, c, d, e
#----- content ends here -----


"""


### Explanation:
1. The total woven in 5 days is given as 5 feet, which we convert to inches (60 inches).
2. The amount woven each day doubles, so we express each day's output in terms of \(a\), the amount woven on the first day.
3. The total woven over 5 days is the sum of the daily outputs: \(a + 2a + 4a + 8a + 16a = 31a\).
4. Solving for \(a\), we divide the total inches by 31.
5. Using \(a\), we calculate \(b\), \(c\), \(d\), and \(e\) by multiplying \(a\) by the appropriate factors.

### Output:
The variables \(a\), \(b\), \(c\), \(d\), and \(e\) will contain the amount woven each day in inches as fractions.
"""


"""
Variable 'a' has wrong value. Expected: 50/31, Actual: 60/31
Variable 'b' has wrong value. Expected: 100/31, Actual: 120/31
Variable 'c' has wrong value. Expected: 200/31, Actual: 240/31
Variable 'd' has wrong value. Expected: 40/31, Actual: 480/31
Variable 'e' has wrong value. Expected: 80/31, Actual: 960/31"""
