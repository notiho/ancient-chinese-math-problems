"""
今有良馬與駑馬發長安至齊。齊去長安三千里。良馬初日行一百九十三里，日增十三里。駑馬初日行九十七里，日減半里。良馬先至齊，復還迎駑馬。問︰幾何日相逢及各行幾何？
術曰：假令十五日，不足三百三十七里半。令之十六日，多一百四十里。以盈、不足維乘假令之數，并而為實。并盈不足為法。實如法而一，得日數。不盡者，以等數除之而命分。
荅曰： a日 而相逢。良馬行 b里 。駑馬行 c里 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. We will calculate the number of days (`a`) it takes for the two horses to meet, as well as the distances traveled by the good horse (`b`) and the slow horse (`c`). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
distance_to_qi = 3000  # in li
good_horse_initial_speed = 193  # in li/day
good_horse_daily_increase = 13  # in li/day
slow_horse_initial_speed = 97  # in li/day
slow_horse_daily_decrease = Fraction(1, 2)  # in li/day

# Step 1: Calculate the total distance the good horse travels before meeting the slow horse
# Let `a` be the number of days until they meet.

# The distance traveled by the good horse in `a` days:
good_horse_distance = lambda a: a * good_horse_initial_speed + (a * (a - 1) // 2) * good_horse_daily_increase

# The distance traveled by the slow horse in `a` days:
slow_horse_distance = lambda a: a * slow_horse_initial_speed - (a * (a - 1) // 2) * slow_horse_daily_decrease

# The good horse travels to Qi and returns to meet the slow horse:
# good_horse_distance(a) = distance_to_qi + slow_horse_distance(a)

# Solve for `a`:
# good_horse_initial_speed * a + (a * (a - 1) // 2) * good_horse_daily_increase = distance_to_qi + slow_horse_initial_speed * a - (a * (a - 1) // 2) * slow_horse_daily_decrease

# Combine terms:
# (good_horse_initial_speed - slow_horse_initial_speed) * a + ((a * (a - 1) // 2) * (good_horse_daily_increase + slow_horse_daily_decrease)) = distance_to_qi

# Define the equation:
def equation(a):
    return (good_horse_initial_speed - slow_horse_initial_speed) * a + ((a * (a - 1) // 2) * (good_horse_daily_increase + slow_horse_daily_decrease)) - distance_to_qi

# Solve for `a` by trial and error (since the equation is quadratic):
a = 1
while equation(a) < 0:
    a += 1

# Calculate the exact value of `a` using the method described in the problem:
excess = equation(a)  # This is the "盈" (excess)
deficit = -equation(a - 1)  # This is the "不足" (deficit)
a = a - Fraction(deficit, excess + deficit)

# Step 2: Calculate the distances traveled by each horse:
b = good_horse_distance(a)  # Distance traveled by the good horse
c = slow_horse_distance(a)  # Distance traveled by the slow horse

# Results:
a = float(a)
b = float(b)
c = float(c)
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 3000/191, Actual: 15.522613065326633
Variable 'b' has wrong value. Expected: 866040/191, Actual: 4451.86432160804
Variable 'c' has wrong value. Expected: 279960/191, Actual: 1449.6934673366834"""
