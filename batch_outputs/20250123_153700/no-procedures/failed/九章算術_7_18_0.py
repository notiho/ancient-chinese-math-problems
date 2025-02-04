"""
今有良馬與駑馬發長安至齊。齊去長安三千里。良馬初日行一百九十三里，日增十三里。駑馬初日行九十七里，日減半里。良馬先至齊，復還迎駑馬。問︰幾何日相逢及各行幾何？
荅曰： a日 而相逢。良馬行 b里 。駑馬行 c里 。
"""

"""
This is a classic problem involving relative motion and arithmetic progressions. Let's solve it step by step using Python.

### Problem Breakdown:
1. The distance between Chang'an and Qi is 3000 li.
2. The **good horse (良馬)** starts by traveling 193 li on the first day and increases its daily travel by 13 li each day.
3. The **slow horse (駑馬)** starts by traveling 97 li on the first day and decreases its daily travel by 0.5 li each day.
4. The good horse reaches Qi first, then returns to meet the slow horse.
5. We need to calculate:
   - The number of days (*a*) until they meet.
   - The total distance traveled by the good horse (*b*).
   - The total distance traveled by the slow horse (*c*).

Here is the Python solution:


"""


from fractions import Fraction

# Given data
distance = 3000  # Distance between Chang'an and Qi in li
good_horse_start = 193  # Initial daily distance of the good horse in li
good_horse_increase = 13  # Daily increase in distance for the good horse in li
slow_horse_start = 97  # Initial daily distance of the slow horse in li
slow_horse_decrease = Fraction(1, 2)  # Daily decrease in distance for the slow horse in li

# Initialize variables
good_horse_distance = 0  # Total distance traveled by the good horse
slow_horse_distance = 0  # Total distance traveled by the slow horse
day = 0  # Day counter

# Daily distances
good_horse_daily = good_horse_start
slow_horse_daily = slow_horse_start

# Phase 1: Good horse reaches Qi
while good_horse_distance < distance:
    day += 1
    good_horse_distance += good_horse_daily
    good_horse_daily += good_horse_increase

# Good horse has reached Qi, now it starts returning
good_horse_daily -= good_horse_increase  # Adjust for the last increment

# Phase 2: Good horse returns to meet the slow horse
while slow_horse_distance < good_horse_distance:
    day += 1
    good_horse_distance += good_horse_daily
    slow_horse_distance += slow_horse_daily
    good_horse_daily += good_horse_increase
    slow_horse_daily -= slow_horse_decrease

# Results
a = day  # Number of days until they meet
b = good_horse_distance  # Total distance traveled by the good horse
c = slow_horse_distance  # Total distance traveled by the slow horse

# Output the results
a, b, c


"""


### Explanation:
1. **Phase 1**: The good horse travels to Qi. We calculate the total distance it travels using an arithmetic progression until it reaches 3000 li.
2. **Phase 2**: The good horse starts returning, and the slow horse continues moving forward. We calculate their respective distances day by day until they meet.
3. The results are:
   - `a`: The number of days until they meet.
   - `b`: The total distance traveled by the good horse.
   - `c`: The total distance traveled by the slow horse.

This code uses the `Fraction` class to handle any fractional values precisely.
"""


"""
Timed out"""
