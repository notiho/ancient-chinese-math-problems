"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves two mice digging through a wall of 5 feet thickness. The large mouse doubles its progress each day, while the small mouse halves its progress each day. We need to calculate the number of days until they meet and the distance each mouse has dug.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Wall thickness
wall_thickness = 5  # in feet

# Rates of progress
large_mouse_rate = 1  # in feet per day
small_mouse_rate = 1  # in feet per day

# Large mouse doubles its progress each day
# Small mouse halves its progress each day

# Using the method described in the problem:
# After 2 days, the combined progress is less than 5 feet by 5/10 feet (0.5 feet).
# After 3 days, the combined progress exceeds 5 feet by 3.75 feet.

# Applying the "盈不足術" (excess and deficiency method):
# Excess = 3.75 feet
# Deficiency = 0.5 feet
# Rate difference = 3 days - 2 days = 1 day

# Calculate the number of days until they meet
a = Fraction(2 * 3.75 - 3 * 0.5, 3.75 - 0.5)

# Calculate the distance each mouse has dug
b = Fraction(a * large_mouse_rate)  # Distance dug by the large mouse
c = Fraction(a * small_mouse_rate)  # Distance dug by the small mouse

# Results
a  # Number of days until they meet
b  # Distance dug by the large mouse
c  # Distance dug by the small mouse
#----- content ends here -----


"""


### Explanation:
1. The problem uses the "盈不足術" (excess and deficiency method) to solve for the number of days (`a`) until the two mice meet.
2. The excess is 3.75 feet, and the deficiency is 0.5 feet. The rate difference is 1 day.
3. Using the formula from the method, we calculate `a` as the number of days.
4. The distances dug by the large mouse (`b`) and the small mouse (`c`) are proportional to their respective rates.

### Final Values:
- `a`: Number of days until they meet.
- `b`: Distance dug by the large mouse.
- `c`: Distance dug by the small mouse.
"""


"""
Code error: both arguments should be Rational instances"""
