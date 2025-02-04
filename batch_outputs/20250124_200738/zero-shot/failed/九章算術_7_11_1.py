"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves two mice digging through a wall, with their digging rates changing daily. We will compute the number of days (`a`) it takes for them to meet, as well as the distances each mouse digs (`b` for the large mouse and `c` for the small mouse).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Wall thickness
wall_thickness = 5  # in 尺

# Rates of digging
large_mouse_rate_day_1 = Fraction(1, 1)  # 1 尺 per day
small_mouse_rate_day_1 = Fraction(1, 1)  # 1 尺 per day

# Daily rate changes
large_mouse_rate_multiplier = 2  # Large mouse doubles its rate daily
small_mouse_rate_multiplier = Fraction(1, 2)  # Small mouse halves its rate daily

# Initialize variables
large_mouse_total = Fraction(0)  # Total distance dug by the large mouse
small_mouse_total = Fraction(0)  # Total distance dug by the small mouse
days = 0  # Number of days

# Simulate the digging process
while large_mouse_total + small_mouse_total < wall_thickness:
    days += 1
    # Calculate the distances dug on the current day
    large_mouse_dig_today = large_mouse_rate_day_1 * (large_mouse_rate_multiplier ** (days - 1))
    small_mouse_dig_today = small_mouse_rate_day_1 * (small_mouse_rate_multiplier ** (days - 1))
    
    # Update the total distances dug
    large_mouse_total += large_mouse_dig_today
    small_mouse_total += small_mouse_dig_today

# The number of days it takes for the mice to meet
a = days

# The distances each mouse digs
b = large_mouse_total
c = small_mouse_total

# Output the results
a, b, c
#----- content ends here -----


"""


### Explanation:
1. **Wall Thickness**: The wall is 5 尺 thick.
2. **Digging Rates**: Both mice start digging at a rate of 1 尺 per day. The large mouse doubles its rate daily, while the small mouse halves its rate daily.
3. **Simulation**: We simulate the digging process day by day, updating the total distance dug by each mouse until their combined distance equals or exceeds the wall thickness.
4. **Results**: The number of days (`a`), the distance dug by the large mouse (`b`), and the distance dug by the small mouse (`c`) are calculated.

### Output:
The variables `a`, `b`, and `c` will contain the results:
- `a`: Number of days it takes for the mice to meet.
- `b`: Distance dug by the large mouse.
- `c`: Distance dug by the small mouse.
"""


"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 3
Variable 'b' has wrong value. Expected: 59/17, Actual: 7
Variable 'c' has wrong value. Expected: 26/17, Actual: 7/4"""
