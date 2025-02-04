"""
今有良馬與駑馬發長安至齊。齊去長安三千里。良馬初日行一百九十三里，日增十三里。駑馬初日行九十七里，日減半里。良馬先至齊，復還迎駑馬。問︰幾何日相逢及各行幾何？
術曰：假令十五日，不足三百三十七里半。令之十六日，多一百四十里。以盈、不足維乘假令之數，并而為實。并盈不足為法。實如法而一，得日數。不盡者，以等數除之而命分。
荅曰： a日 而相逢。良馬行 b里 。駑馬行 c里 。
"""

"""
This is a classic ancient Chinese math problem involving arithmetic progressions. Let's break it down and solve it step by step using Python.

---

### Problem Breakdown:
- **Distance from Chang'an to Qi**: 3000 li.
- **Good horse (良馬)**:
  - First day: 193 li.
  - Daily increment: 13 li.
- **Inferior horse (駑馬)**:
  - First day: 97 li.
  - Daily decrement: 0.5 li.
- The good horse reaches Qi first, then returns to meet the inferior horse.
- We need to calculate:
  1. How many days until they meet.
  2. How far each horse travels.

---

### Procedure:
1. **Good horse's distance**:
   - The distance traveled by the good horse in `n` days is an arithmetic progression:
     \[
     S_{\text{良馬}} = n \cdot a + \frac{n(n-1)}{2} \cdot d
     \]
     where \(a = 193\) (initial distance) and \(d = 13\) (daily increment).

2. **Inferior horse's distance**:
   - The distance traveled by the inferior horse in `n` days is also an arithmetic progression:
     \[
     S_{\text{駑馬}} = n \cdot a + \frac{n(n-1)}{2} \cdot d
     \]
     where \(a = 97\) (initial distance) and \(d = -0.5\) (daily decrement).

3. **Meeting condition**:
   - The good horse first reaches Qi (3000 li), then turns back to meet the inferior horse.
   - The total distance traveled by the good horse when they meet equals the sum of the distance traveled by the inferior horse and the distance the good horse covered on its return.

4. **Iterative calculation**:
   - We calculate the distances day by day until the meeting condition is satisfied.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Constants
distance_to_qi = 3000  # Total distance in li
good_horse_initial = 193  # Initial daily distance for the good horse
good_horse_increment = 13  # Daily increment for the good horse
inferior_horse_initial = 97  # Initial daily distance for the inferior horse
inferior_horse_decrement = -0.5  # Daily decrement for the inferior horse

# Function to calculate the distance traveled by a horse in n days (arithmetic progression)
def distance_traveled(initial, increment, days):
    return days * initial + (days * (days - 1) // 2) * increment

# Iterative calculation to find the meeting day
days = 0
good_horse_distance = 0
inferior_horse_distance = 0

while True:
    days += 1
    # Distance traveled by the good horse to Qi
    good_horse_to_qi = distance_traveled(good_horse_initial, good_horse_increment, days)
    
    # If the good horse hasn't reached Qi yet, continue
    if good_horse_to_qi < distance_to_qi:
        continue
    
    # Distance traveled by the inferior horse in the same time
    inferior_horse_distance = distance_traveled(inferior_horse_initial, inferior_horse_decrement, days)
    
    # Distance the good horse travels back after reaching Qi
    good_horse_return = good_horse_to_qi - distance_to_qi
    
    # Check if the good horse meets the inferior horse
    if good_horse_return >= (distance_to_qi - inferior_horse_distance):
        break

# Calculate the total distance traveled by each horse
good_horse_total_distance = good_horse_to_qi + (good_horse_return - (distance_to_qi - inferior_horse_distance))
inferior_horse_total_distance = inferior_horse_distance

# Results
a = days
b = good_horse_total_distance
c = inferior_horse_total_distance

print(f"良馬和駑馬在 {a} 日相逢。")
print(f"良馬行 {b} 里。")
print(f"駑馬行 {c} 里。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Distance Calculation**:
   - The function `distance_traveled` computes the total distance traveled by a horse in `n` days using the formula for the sum of an arithmetic progression.

2. **Iterative Search**:
   - We increment the number of days (`days`) until the good horse reaches Qi and returns to meet the inferior horse.

3. **Meeting Condition**:
   - The good horse's return distance must equal or exceed the remaining distance the inferior horse has to travel.

4. **Final Results**:
   - The total distance traveled by each horse is calculated and printed.

---

### Answer:
After running the code, the output will be:

```
良馬和駑馬在 a 日相逢。
良馬行 b 里。
駑馬行 c 里。
```

Where `a`, `b`, and `c` are the computed values for the number of days, the distance traveled by the good horse, and the distance traveled by the inferior horse, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 3000/191, Actual: 16
Variable 'b' has wrong value. Expected: 866040/191, Actual: 4788.0
Variable 'c' has wrong value. Expected: 279960/191, Actual: 1492.0"""
