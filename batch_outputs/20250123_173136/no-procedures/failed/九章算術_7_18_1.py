"""
今有良馬與駑馬發長安至齊。齊去長安三千里。良馬初日行一百九十三里，日增十三里。駑馬初日行九十七里，日減半里。良馬先至齊，復還迎駑馬。問︰幾何日相逢及各行幾何？
荅曰： a日 而相逢。良馬行 b里 。駑馬行 c里 。
"""

"""
This is a classic problem involving arithmetic progressions for both the good horse (良馬) and the slow horse (駑馬). Let's solve it step by step.

---

### Problem Breakdown:
1. The distance between Chang'an and Qi is 3000 li.
2. The good horse (良馬) starts by traveling 193 li on the first day and increases its daily travel by 13 li each day.
3. The slow horse (駑馬) starts by traveling 97 li on the first day and decreases its daily travel by 0.5 li each day.
4. The good horse reaches Qi first, then returns to meet the slow horse.
5. We need to determine:
   - How many days (a) it takes for them to meet.
   - How far the good horse (b) and the slow horse (c) have traveled.

---

### Solution in Python:


"""


from fractions import Fraction

# Total distance between Chang'an and Qi
total_distance = 3000

# Good horse (良馬) initial speed and daily increment
good_horse_initial = 193
good_horse_increment = 13

# Slow horse (駑馬) initial speed and daily decrement
slow_horse_initial = 97
slow_horse_decrement = Fraction(1, 2)

# Variables to track progress
good_horse_distance = 0
slow_horse_distance = 0
day = 0

# Phase 1: Good horse reaches Qi
while good_horse_distance < total_distance:
    day += 1
    good_horse_distance += good_horse_initial + (day - 1) * good_horse_increment

# Record the number of days it took for the good horse to reach Qi
good_horse_days_to_qi = day

# Phase 2: Good horse returns to meet the slow horse
# Reset variables for the slow horse
slow_horse_distance = 0
good_horse_return_distance = 0
day = 0

while True:
    day += 1
    # Slow horse travels
    slow_horse_distance += max(0, slow_horse_initial - (day - 1) * slow_horse_decrement)
    # Good horse travels back
    good_horse_return_distance += good_horse_initial + (good_horse_days_to_qi + day - 1) * good_horse_increment
    
    # Check if they meet
    if good_horse_distance - good_horse_return_distance <= slow_horse_distance:
        break

# Total days until they meet
a = good_horse_days_to_qi + day

# Total distance traveled by the good horse
b = good_horse_distance + good_horse_return_distance

# Total distance traveled by the slow horse
c = slow_horse_distance

# Results
a, b, c


"""


---

### Explanation of the Code:
1. **Phase 1**: We calculate how many days it takes for the good horse to reach Qi using an arithmetic progression formula for its daily travel.
2. **Phase 2**: After reaching Qi, the good horse starts traveling back to meet the slow horse. Meanwhile, the slow horse continues traveling forward. We calculate their respective distances day by day until they meet.
3. The results are:
   - `a`: Total days until they meet.
   - `b`: Total distance traveled by the good horse.
   - `c`: Total distance traveled by the slow horse.


"""


"""
Variable 'a' has wrong value. Expected: 3000/191, Actual: 19
Variable 'b' has wrong value. Expected: 866040/191, Actual: 5890
Variable 'c' has wrong value. Expected: 279960/191, Actual: 1337/2"""
