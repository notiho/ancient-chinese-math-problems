"""
今有良馬與駑馬發長安至齊。齊去長安三千里。良馬初日行一百九十三里，日增十三里。駑馬初日行九十七里，日減半里。良馬先至齊，復還迎駑馬。問︰幾何日相逢及各行幾何？
荅曰： a日 而相逢。良馬行 b里 。駑馬行 c里 。
"""

"""
This is a classic problem involving relative motion and arithmetic progressions. Let's solve it step by step.

### Problem Breakdown:
1. The distance between Chang'an and Qi is 3000 li.
2. The **good horse (良馬)** starts by traveling 193 li on the first day and increases its daily distance by 13 li each day.
3. The **slow horse (駑馬)** starts by traveling 97 li on the first day and decreases its daily distance by 0.5 li each day.
4. The good horse reaches Qi first, then returns to meet the slow horse.
5. We need to find:
   - The number of days (*a*) it takes for the two horses to meet.
   - The total distance traveled by the good horse (*b*).
   - The total distance traveled by the slow horse (*c*).

---

### Solution in Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Initial conditions
distance_to_qi = 3000  # Total distance in li
good_horse_start = 193  # Good horse's first-day distance
good_horse_increment = 13  # Good horse's daily increment in li
slow_horse_start = 97  # Slow horse's first-day distance
slow_horse_decrement = Fraction(1, 2)  # Slow horse's daily decrement in li

# Variables to track progress
good_horse_distance = 0  # Total distance traveled by the good horse
slow_horse_distance = 0  # Total distance traveled by the slow horse
good_horse_daily = good_horse_start  # Good horse's daily distance
slow_horse_daily = slow_horse_start  # Slow horse's daily distance
days = 0  # Number of days

# Step 1: Good horse reaches Qi
while good_horse_distance < distance_to_qi:
    good_horse_distance += good_horse_daily
    good_horse_daily += good_horse_increment
    days += 1

# Record the number of days it took for the good horse to reach Qi
good_horse_days_to_qi = days

# Step 2: Good horse returns to meet the slow horse
good_horse_daily = good_horse_start + good_horse_increment * good_horse_days_to_qi  # Reset daily distance for return
while True:
    # Update distances
    good_horse_distance += good_horse_daily
    slow_horse_distance += slow_horse_daily

    # Update daily distances
    good_horse_daily += good_horse_increment
    slow_horse_daily = max(0, slow_horse_daily - slow_horse_decrement)  # Slow horse can't go negative

    # Increment days
    days += 1

    # Check if they meet
    if good_horse_distance >= slow_horse_distance:
        break

# Step 3: Results
a = days  # Total days until they meet
b = good_horse_distance  # Total distance traveled by the good horse
c = slow_horse_distance  # Total distance traveled by the slow horse

# Output results
a, b, c
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Step 1**: The good horse travels to Qi. We calculate the total distance it travels day by day, increasing its daily distance by 13 li each day, until it reaches 3000 li.
2. **Step 2**: The good horse returns to meet the slow horse. Both horses travel day by day, with the good horse increasing its daily distance by 13 li and the slow horse decreasing its daily distance by 0.5 li. We track their total distances until they meet.
3. **Step 3**: The results are calculated:
   - `a`: Total days until they meet.
   - `b`: Total distance traveled by the good horse.
   - `c`: Total distance traveled by the slow horse.

---

### Final Answer:
The code will compute the following:
- `a`: The number of days until they meet.
- `b`: The total distance traveled by the good horse.
- `c`: The total distance traveled by the slow horse.
"""


"""
Variable 'a' has wrong value. Expected: 3000/191, Actual: 13
Variable 'b' has wrong value. Expected: 866040/191, Actual: 3523
Variable 'c' has wrong value. Expected: 279960/191, Actual: 97"""
