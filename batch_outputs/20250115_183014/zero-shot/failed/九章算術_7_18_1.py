"""
今有良馬與駑馬發長安至齊。齊去長安三千里。良馬初日行一百九十三里，日增十三里。駑馬初日行九十七里，日減半里。良馬先至齊，復還迎駑馬。問︰幾何日相逢及各行幾何？
術曰：假令十五日，不足三百三十七里半。令之十六日，多一百四十里。以盈、不足維乘假令之數，并而為實。并盈不足為法。實如法而一，得日數。不盡者，以等數除之而命分。
荅曰： a日 而相逢。良馬行 b里 。駑馬行 c里 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the number of days (`a`) it takes for the two horses to meet, as well as the distances traveled by the good horse (`b`) and the slow horse (`c`).

Here is the Python code:


"""


from fractions import Fraction

# Given data
distance = 3000  # Total distance from Chang'an to Qi in li
good_horse_initial = 193  # Good horse's initial daily distance in li
good_horse_increment = 13  # Good horse's daily increment in li
slow_horse_initial = 97  # Slow horse's initial daily distance in li
slow_horse_decrement = Fraction(1, 2)  # Slow horse's daily decrement in li

# Step 1: Calculate the total distance each horse travels in `n` days
def good_horse_distance(n):
    return n * good_horse_initial + good_horse_increment * (n * (n - 1)) // 2

def slow_horse_distance(n):
    return n * slow_horse_initial - slow_horse_decrement * (n * (n - 1)) // 2

# Step 2: Find the number of days `a` when they meet
# The good horse travels to Qi and returns to meet the slow horse
# Total distance traveled by the good horse = distance + distance - slow_horse_distance(a)
# Total distance traveled by the slow horse = slow_horse_distance(a)
# Solve for `a` such that the distances match

# Using the ancient method:
# Assume 15 days: good_horse_distance(15) - slow_horse_distance(15) < distance
# Assume 16 days: good_horse_distance(16) - slow_horse_distance(16) > distance

n1 = 15
n2 = 16

good_horse_15 = good_horse_distance(n1)
slow_horse_15 = slow_horse_distance(n1)
difference_15 = good_horse_15 - slow_horse_15 - distance

good_horse_16 = good_horse_distance(n2)
slow_horse_16 = slow_horse_distance(n2)
difference_16 = good_horse_16 - slow_horse_16 - distance

# Calculate the exact number of days `a` using the ancient method
numerator = abs(difference_15) * n2 + abs(difference_16) * n1
denominator = abs(difference_15) + abs(difference_16)
a = Fraction(numerator, denominator)

# Step 3: Calculate the distances traveled by each horse
b = good_horse_distance(a)  # Distance traveled by the good horse
c = slow_horse_distance(a)  # Distance traveled by the slow horse

# Results
a = float(a)  # Convert to a float for clarity
b = float(b)  # Convert to a float for clarity
c = float(c)  # Convert to a float for clarity


"""


The variables `a`, `b`, and `c` now contain the number of days it takes for the horses to meet, the distance traveled by the good horse, and the distance traveled by the slow horse, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 3000/191, Actual: 15.478260869565217
Variable 'b' has wrong value. Expected: 866040/191, Actual: 4443.304347826087
Variable 'c' has wrong value. Expected: 279960/191, Actual: 1445.391304347826"""
