"""
今有女子善織，日自倍，五日織通五尺。問：日織幾何？
術曰：各置列衰副，并得三十一為法，以五尺乘并者，各自為實，實如法而一，即得。
答曰：初日織 a寸 ，次日織 b寸 ，次日織 c寸 ，次日織 d尺 ，次日織 e尺 。
"""

"""
To translate the ancient Chinese math problem into Python code, we will compute the values of the unknowns \(a\), \(b\), \(c\), \(d\), and \(e\) based on the description provided. The problem describes a scenario where a woman weaves cloth, doubling her output each day, and completes 5 feet (or 60 inches) of cloth in 5 days.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total cloth woven in 5 days is 5 feet = 60 inches
total_inches = 60

# The weaving doubles each day: a, 2a, 4a, 8a, 16a
# Total woven: a + 2a + 4a + 8a + 16a = 31a
# Solve for a: 31a = total_inches
a = Fraction(total_inches, 31)  # First day's weaving in inches

# Compute the weaving for each day
b = 2 * a  # Second day's weaving in inches
c = 4 * a  # Third day's weaving in inches
d = 8 * a  # Fourth day's weaving in inches
e = 16 * a  # Fifth day's weaving in inches

# Outputs
a, b, c, d, e
#----- content ends here -----


"""


### Explanation:
1. The total cloth woven in 5 days is 5 feet, which is converted to 60 inches (since 1 foot = 12 inches).
2. The weaving doubles each day, so the amounts woven each day are \(a\), \(2a\), \(4a\), \(8a\), and \(16a\).
3. The total woven is \(a + 2a + 4a + 8a + 16a = 31a\), which equals 60 inches.
4. Solving for \(a\), we find \(a = \frac{60}{31}\).
5. The subsequent days' weaving amounts (\(b\), \(c\), \(d\), \(e\)) are calculated by multiplying \(a\) by 2, 4, 8, and 16, respectively.

### Results:
- \(a = \frac{60}{31}\) inches
- \(b = \frac{120}{31}\) inches
- \(c = \frac{240}{31}\) inches
- \(d = \frac{480}{31}\) inches
- \(e = \frac{960}{31}\) inches
"""


"""
Variable 'a' has wrong value. Expected: 50/31, Actual: 60/31
Variable 'b' has wrong value. Expected: 100/31, Actual: 120/31
Variable 'c' has wrong value. Expected: 200/31, Actual: 240/31
Variable 'd' has wrong value. Expected: 40/31, Actual: 480/31
Variable 'e' has wrong value. Expected: 80/31, Actual: 960/31"""
