"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves two mice digging through a wall of thickness 5 feet. The larger mouse doubles its daily progress each day, while the smaller mouse halves its daily progress each day. We need to determine how many days it takes for them to meet and how far each mouse has dug.

Here is the Python code:


"""


from fractions import Fraction

# Wall thickness
wall_thickness = 5  # in feet

# Define the rates of the mice
large_mouse_rate = 1  # in feet per day (initial rate)
small_mouse_rate = 1  # in feet per day (initial rate)

# Define the progress of each mouse
large_mouse_progress = 0
small_mouse_progress = 0

# Day counter
a = 0

# Loop until the mice meet
while large_mouse_progress + small_mouse_progress < wall_thickness:
    a += 1
    # Update progress for each mouse
    large_mouse_progress += large_mouse_rate
    small_mouse_progress += small_mouse_rate
    # Update rates for the next day
    large_mouse_rate *= 2  # Large mouse doubles its rate
    small_mouse_rate /= 2  # Small mouse halves its rate

# Calculate the distances each mouse has dug
b = Fraction(large_mouse_progress)
c = Fraction(small_mouse_progress)

# Output the results
a = Fraction(a)  # Number of days
b = Fraction(b)  # Distance dug by the large mouse
c = Fraction(c)  # Distance dug by the small mouse

# Results
a, b, c


"""


### Explanation:
1. The wall thickness is 5 feet.
2. The large mouse starts digging at 1 foot per day and doubles its progress each day.
3. The small mouse starts digging at 1 foot per day and halves its progress each day.
4. We use a loop to simulate the digging process day by day, updating the progress and rates of each mouse.
5. The loop stops when the combined progress of both mice equals or exceeds the wall thickness.
6. The number of days (`a`), the distance dug by the large mouse (`b`), and the distance dug by the small mouse (`c`) are calculated and stored as fractions.

### Results:
The variables `a`, `b`, and `c` will contain the number of days, the distance dug by the large mouse, and the distance dug by the small mouse, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 3
Variable 'b' has wrong value. Expected: 59/17, Actual: 7
Variable 'c' has wrong value. Expected: 26/17, Actual: 7/4"""
