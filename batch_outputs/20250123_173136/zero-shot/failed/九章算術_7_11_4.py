"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves two mice digging through a wall of 5 feet thickness. The larger mouse digs 1 foot per day and doubles its progress each day, while the smaller mouse digs 1 foot per day and halves its progress each day. We need to determine how many days it takes for them to meet and how far each mouse has dug.

Here is the Python code:


"""


from fractions import Fraction

# Wall thickness
wall_thickness = 5  # in feet

# Rates of digging
large_mouse_rate = 1  # in feet per day
small_mouse_rate = 1  # in feet per day

# Progression factors
large_mouse_factor = 2  # doubles each day
small_mouse_factor = Fraction(1, 2)  # halves each day

# Initialize variables
large_mouse_progress = 0
small_mouse_progress = 0
a = 0  # days

# Simulate the digging process
while large_mouse_progress + small_mouse_progress < wall_thickness:
    a += 1
    large_mouse_progress += large_mouse_rate * (large_mouse_factor ** (a - 1))
    small_mouse_progress += small_mouse_rate * (small_mouse_factor ** (a - 1))

# Assign the results
b = large_mouse_progress
c = small_mouse_progress

# Print the results
a = Fraction(a)  # days
b = Fraction(b)  # feet
c = Fraction(c)  # feet

a, b, c


"""


This code calculates the number of days (`a`) it takes for the two mice to meet and the distance each mouse has dug (`b` for the large mouse and `c` for the small mouse). The results are stored in variables `a`, `b`, and `c` as fractions.
"""


"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 3
Variable 'b' has wrong value. Expected: 59/17, Actual: 7
Variable 'c' has wrong value. Expected: 26/17, Actual: 7/4"""
