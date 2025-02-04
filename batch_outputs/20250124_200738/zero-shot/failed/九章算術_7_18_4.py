"""
今有良馬與駑馬發長安至齊。齊去長安三千里。良馬初日行一百九十三里，日增十三里。駑馬初日行九十七里，日減半里。良馬先至齊，復還迎駑馬。問︰幾何日相逢及各行幾何？
術曰：假令十五日，不足三百三十七里半。令之十六日，多一百四十里。以盈、不足維乘假令之數，并而為實。并盈不足為法。實如法而一，得日數。不盡者，以等數除之而命分。
荅曰： a日 而相逢。良馬行 b里 。駑馬行 c里 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. We will calculate the number of days (`a`) it takes for the two horses to meet, as well as the distances traveled by the good horse (`b`) and the slow horse (`c`).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
distance_to_qi = 3000  # in li
good_horse_initial_speed = 193  # li per day
good_horse_daily_increase = 13  # li per day
slow_horse_initial_speed = 97  # li per day
slow_horse_daily_decrease = Fraction(1, 2)  # li per day

# Step 1: Calculate the total distance the good horse travels before meeting the slow horse
# Let the number of days to meet be `a`.

# Total distance traveled by the good horse in `a` days:
good_horse_distance = lambda a: a * good_horse_initial_speed + (a - 1) * a * good_horse_daily_increase // 2

# Total distance traveled by the slow horse in `a` days:
slow_horse_distance = lambda a: a * slow_horse_initial_speed - (a - 1) * a * slow_horse_daily_decrease // 2

# The good horse travels to Qi and back to meet the slow horse:
# good_horse_distance(a) = distance_to_qi + slow_horse_distance(a)

# Solve for `a`:
# good_horse_initial_speed * a + (a - 1) * a * good_horse_daily_increase // 2 = distance_to_qi + slow_horse_initial_speed * a - (a - 1) * a * slow_horse_daily_decrease // 2

# Rearrange terms to isolate `a`:
# This requires solving a quadratic equation. For simplicity, we will use trial and error to find the integer solution.

a = 0
while True:
    good_horse_total = good_horse_initial_speed * a + (a - 1) * a * good_horse_daily_increase // 2
    slow_horse_total = slow_horse_initial_speed * a - (a - 1) * a * slow_horse_daily_decrease // 2
    if good_horse_total == distance_to_qi + slow_horse_total:
        break
    a += 1

# Step 2: Calculate the distances traveled by each horse
b = good_horse_initial_speed * a + (a - 1) * a * good_horse_daily_increase // 2
c = slow_horse_initial_speed * a - (a - 1) * a * slow_horse_daily_decrease // 2

# Results
a = Fraction(a)  # Number of days
b = Fraction(b)  # Distance traveled by the good horse
c = Fraction(c)  # Distance traveled by the slow horse
#----- content ends here -----


"""


This code calculates the number of days (`a`) it takes for the two horses to meet, as well as the distances traveled by the good horse (`b`) and the slow horse (`c`). The results are stored in the variables `a`, `b`, and `c`.
"""


"""
Timed out"""
