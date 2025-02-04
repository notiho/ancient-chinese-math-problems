"""
今有良馬與駑馬發長安至齊。齊去長安三千里。良馬初日行一百九十三里，日增十三里。駑馬初日行九十七里，日減半里。良馬先至齊，復還迎駑馬。問︰幾何日相逢及各行幾何？
術曰：假令十五日，不足三百三十七里半。令之十六日，多一百四十里。以盈、不足維乘假令之數，并而為實。并盈不足為法。實如法而一，得日數。不盡者，以等數除之而命分。
荅曰： a日 而相逢。良馬行 b里 。駑馬行 c里 。
"""

"""
This is a classic ancient Chinese math problem involving arithmetic progressions for both the good horse (良馬) and the slow horse (駑馬). Let's solve it step by step using Python.

### Problem Breakdown:
- Distance between Chang'an and Qi: 3000 li.
- 良馬 (good horse):
  - First day: 193 li.
  - Increases by 13 li per day.
- 駑馬 (slow horse):
  - First day: 97 li.
  - Decreases by 0.5 li per day.
- 良馬 reaches Qi first, then returns to meet 駑馬.
- We need to calculate:
  1. How many days until they meet.
  2. How far each horse travels.

### Procedure:
1. Use the method of excess and deficiency (盈不足術) to calculate the number of days.
2. Calculate the total distance traveled by each horse.

Here is the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
distance = 3000  # Distance between Chang'an and Qi in li

# 良馬 (good horse)
good_horse_first_day = 193  # li
good_horse_increase = 13  # li per day

# 駑馬 (slow horse)
slow_horse_first_day = 97  # li
slow_horse_decrease = Fraction(1, 2)  # li per day

# Step 1: Define the distance formulas for each horse
def good_horse_distance(day):
    """Calculate the total distance traveled by the good horse in 'day' days."""
    return day * good_horse_first_day + (day * (day - 1) // 2) * good_horse_increase

def slow_horse_distance(day):
    """Calculate the total distance traveled by the slow horse in 'day' days."""
    return day * slow_horse_first_day - (day * (day - 1) // 2) * slow_horse_decrease

# Step 2: Use the method of excess and deficiency to find the meeting day
# Assume the good horse travels to Qi and back, then meets the slow horse
# We need to solve for the day where the distances match:
# good_horse_distance(day) = distance + (distance - slow_horse_distance(day))

# Start with an approximate range for the number of days
day = 15  # Initial guess
good_horse_to_qi_and_back = 2 * distance  # Good horse travels to Qi and back

# Calculate excess and deficiency
excess = good_horse_distance(day + 1) - (good_horse_to_qi_and_back + slow_horse_distance(day + 1))
deficiency = (good_horse_to_qi_and_back + slow_horse_distance(day)) - good_horse_distance(day)

# Calculate the exact number of days using the method of excess and deficiency
numerator = (day + 1) * deficiency + day * excess
denominator = excess + deficiency
meeting_day = Fraction(numerator, denominator)

# Step 3: Calculate the total distance traveled by each horse
good_horse_total_distance = good_horse_distance(meeting_day)
slow_horse_total_distance = slow_horse_distance(meeting_day)

# Results
a = meeting_day
b = good_horse_total_distance
c = slow_horse_total_distance

print(f"良馬和駑馬相逢於 {a} 日。")
print(f"良馬行 {b} 里。")
print(f"駑馬行 {c} 里。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Distance Calculation**:
   - The good horse's distance is calculated using the arithmetic progression formula: \( \text{distance} = \text{first day} \times \text{days} + \frac{\text{days} \times (\text{days} - 1)}{2} \times \text{increase per day} \).
   - Similarly, the slow horse's distance is calculated, but with a decrease per day.

2. **Excess and Deficiency**:
   - We calculate the excess and deficiency for the approximate number of days and use the formula:
     \[
     \text{days} = \frac{(\text{day} + 1) \times \text{deficiency} + \text{day} \times \text{excess}}{\text{excess} + \text{deficiency}}
     \]

3. **Final Results**:
   - The meeting day is calculated as a fraction.
   - The total distances traveled by both horses are calculated using their respective formulas.

### Output:
The program will output:
- The day they meet (*a* days).
- The total distance traveled by the good horse (*b* li).
- The total distance traveled by the slow horse (*c* li).
"""


"""
Variable 'a' has wrong value. Expected: 3000/191, Actual: 5080/199
Variable 'b' has wrong value. Expected: 866040/191, Actual: 1790171/199
Variable 'c' has wrong value. Expected: 279960/191, Actual: 923233/398"""
