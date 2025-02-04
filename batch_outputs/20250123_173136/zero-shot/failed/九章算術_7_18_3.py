"""
今有良馬與駑馬發長安至齊。齊去長安三千里。良馬初日行一百九十三里，日增十三里。駑馬初日行九十七里，日減半里。良馬先至齊，復還迎駑馬。問︰幾何日相逢及各行幾何？
術曰：假令十五日，不足三百三十七里半。令之十六日，多一百四十里。以盈、不足維乘假令之數，并而為實。并盈不足為法。實如法而一，得日數。不盡者，以等數除之而命分。
荅曰： a日 而相逢。良馬行 b里 。駑馬行 c里 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. We will calculate the number of days (`a`) it takes for the two horses to meet, as well as the distances traveled by the good horse (`b`) and the slow horse (`c`). Here's the Python code:


"""


from fractions import Fraction

# Given data
distance_to_qi = 3000  # in li
good_horse_initial_speed = 193  # in li/day
good_horse_daily_increase = 13  # in li/day
slow_horse_initial_speed = 97  # in li/day
slow_horse_daily_decrease = Fraction(1, 2)  # in li/day

# Step 1: Calculate the total distance the good horse travels before meeting the slow horse
# Let the number of days to meet be `a`.

# The distance traveled by the good horse in `a` days:
good_horse_distance = lambda a: a * good_horse_initial_speed + (a * (a - 1) // 2) * good_horse_daily_increase

# The distance traveled by the slow horse in `a` days:
slow_horse_distance = lambda a: a * slow_horse_initial_speed - (a * (a - 1) // 2) * slow_horse_daily_decrease

# The good horse travels to Qi and returns to meet the slow horse:
# Total distance traveled by the good horse = 2 * distance_to_qi - slow_horse_distance(a)
# This must equal good_horse_distance(a).

# Solve for `a`:
a = 0
while True:
    if good_horse_distance(a) == 2 * distance_to_qi - slow_horse_distance(a):
        break
    a += 1

# Step 2: Calculate the distances traveled by each horse
b = good_horse_distance(a)  # Distance traveled by the good horse
c = slow_horse_distance(a)  # Distance traveled by the slow horse

# Results
a = Fraction(a)  # Number of days
b = Fraction(b)  # Distance traveled by the good horse
c = Fraction(c)  # Distance traveled by the slow horse

# Output the results
a, b, c


"""


### Explanation:
1. The good horse starts at 193 li/day and increases its speed by 13 li/day each day.
2. The slow horse starts at 97 li/day and decreases its speed by 0.5 li/day each day.
3. The good horse travels to Qi (3000 li) and returns to meet the slow horse. The total distance traveled by the good horse equals the sum of the distances traveled by both horses.
4. We solve for the number of days (`a`) it takes for the two horses to meet.
5. Using the value of `a`, we calculate the distances traveled by the good horse (`b`) and the slow horse (`c`).

The variables `a`, `b`, and `c` will contain the final results.
"""


"""
Timed out"""
