"""
今有良馬與駑馬發長安至齊。齊去長安三千里。良馬初日行一百九十三里，日增十三里。駑馬初日行九十七里，日減半里。良馬先至齊，復還迎駑馬。問︰幾何日相逢及各行幾何？
荅曰： a日 而相逢。良馬行 b里 。駑馬行 c里 。
"""

"""
This is a classic problem involving arithmetic progressions for the distances traveled by two horses, one fast (良馬) and one slow (駑馬). Let us solve step by step.

---

### Problem Breakdown:
1. The distance between Chang'an and Qi is 3000 li.
2. The fast horse (良馬):
   - On the first day, it travels 193 li.
   - Each day, it increases its distance by 13 li.
3. The slow horse (駑馬):
   - On the first day, it travels 97 li.
   - Each day, it decreases its distance by 0.5 li.
4. The fast horse reaches Qi first, then returns to meet the slow horse.
5. We need to find:
   - The number of days (*a*) until they meet.
   - The total distance traveled by the fast horse (*b*).
   - The total distance traveled by the slow horse (*c*).

---

### Solution in Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total distance between Chang'an and Qi
total_distance = 3000

# 良馬 (fast horse) initial values
fast_initial = 193
fast_increment = 13

# 駑馬 (slow horse) initial values
slow_initial = 97
slow_decrement = Fraction(1, 2)

# Variables to track progress
fast_distance = 0
slow_distance = 0
days = 0

# Step 1: Fast horse reaches Qi
while fast_distance < total_distance:
    days += 1
    fast_distance += fast_initial + (days - 1) * fast_increment

# Record the number of days it took the fast horse to reach Qi
fast_days_to_qi = days

# Step 2: Fast horse returns to meet the slow horse
fast_distance = total_distance  # Reset fast horse's position at Qi
slow_distance = 0  # Reset slow horse's position at Chang'an
days = 0

while fast_distance > slow_distance:
    days += 1
    # Fast horse travels back
    fast_distance += fast_initial + (fast_days_to_qi + days - 1) * fast_increment
    # Slow horse continues forward
    slow_distance += slow_initial - (days - 1) * slow_decrement

# Step 3: Calculate total distances traveled
a = fast_days_to_qi + days  # Total days until they meet
b = fast_distance  # Total distance traveled by the fast horse
c = slow_distance  # Total distance traveled by the slow horse

# Output results
a, b, c
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Fast Horse Reaches Qi**:
   - The fast horse travels an arithmetic progression: `193, 206, 219, ...`.
   - We calculate the total distance traveled until it reaches 3000 li.

2. **Fast Horse Returns to Meet Slow Horse**:
   - After reaching Qi, the fast horse starts traveling back, while the slow horse continues forward.
   - Both horses' distances are updated daily until they meet.

3. **Final Results**:
   - `a` is the total number of days until they meet.
   - `b` is the total distance traveled by the fast horse.
   - `c` is the total distance traveled by the slow horse.

---

This code will calculate the exact values for `a`, `b`, and `c` using arithmetic progressions and simple loops.
"""


"""
Timed out"""
