"""
今有良馬與駑馬發長安至齊。齊去長安三千里。良馬初日行一百九十三里，日增十三里。駑馬初日行九十七里，日減半里。良馬先至齊，復還迎駑馬。問︰幾何日相逢及各行幾何？
術曰：假令十五日，不足三百三十七里半。令之十六日，多一百四十里。以盈、不足維乘假令之數，并而為實。并盈不足為法。實如法而一，得日數。不盡者，以等數除之而命分。
荅曰： a日 而相逢。良馬行 b里 。駑馬行 c里 。
"""

"""
This is a classic ancient Chinese math problem involving arithmetic progressions and relative motion. Let's break it down step by step and translate the procedure into Python code.

### Problem Description:
- The distance from Chang'an to Qi is 3000 li.
- A good horse (良馬) starts by traveling 193 li on the first day and increases its daily travel by 13 li each day.
- A slow horse (駑馬) starts by traveling 97 li on the first day and decreases its daily travel by 0.5 li each day.
- The good horse reaches Qi first, then returns to meet the slow horse.
- Question: How many days until they meet, and how far has each horse traveled?

### Procedure:
1. Assume a certain number of days (e.g., 15 days) and calculate the total distance traveled by each horse.
2. Adjust the number of days based on whether the distance difference is too much or too little.
3. Use the method of excess and deficiency (盈、不足) to calculate the exact number of days.
4. Compute the total distance traveled by each horse.

Here is the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Problem constants
distance_to_qi = 3000  # Total distance in li
good_horse_initial = 193  # Initial daily distance for the good horse
good_horse_increase = 13  # Daily increase for the good horse
slow_horse_initial = 97  # Initial daily distance for the slow horse
slow_horse_decrease = Fraction(1, 2)  # Daily decrease for the slow horse

# Function to calculate the total distance traveled by a horse in n days
def total_distance_good_horse(n):
    return n * good_horse_initial + good_horse_increase * (n * (n - 1)) // 2

def total_distance_slow_horse(n):
    return n * slow_horse_initial - slow_horse_decrease * (n * (n - 1)) // 2

# Step 1: Assume a number of days (e.g., 15 and 16) and calculate the difference
n1 = 15
n2 = 16

# Distance traveled by the good horse in n1 and n2 days
good_horse_n1 = total_distance_good_horse(n1)
good_horse_n2 = total_distance_good_horse(n2)

# Distance traveled by the slow horse in n1 and n2 days
slow_horse_n1 = total_distance_slow_horse(n1)
slow_horse_n2 = total_distance_slow_horse(n2)

# Distance difference when the good horse returns to meet the slow horse
difference_n1 = 2 * good_horse_n1 - distance_to_qi - slow_horse_n1
difference_n2 = 2 * good_horse_n2 - distance_to_qi - slow_horse_n2

# Step 2: Use the method of excess and deficiency to calculate the exact number of days
excess = difference_n2  # 多 (excess)
deficiency = -difference_n1  # 不足 (deficiency)

# Calculate the exact number of days
numerator = n1 * excess + n2 * deficiency
denominator = excess + deficiency
days = Fraction(numerator, denominator)

# Step 3: Calculate the total distance traveled by each horse
good_horse_distance = 2 * total_distance_good_horse(days) - distance_to_qi
slow_horse_distance = total_distance_slow_horse(days)

# Results
a = days  # Number of days until they meet
b = good_horse_distance  # Distance traveled by the good horse
c = slow_horse_distance  # Distance traveled by the slow horse

# Output the results
print(f"良馬和駑馬相逢需要 {a} 日。")
print(f"良馬行了 {b} 里。")
print(f"駑馬行了 {c} 里。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Arithmetic Progression**: The total distance traveled by each horse is calculated using the formula for the sum of an arithmetic progression.
2. **Excess and Deficiency Method**: This method is used to refine the estimate for the number of days until the horses meet.
3. **Fraction Handling**: The `Fraction` class is used to handle non-integer results accurately.
4. **Final Calculation**: Once the number of days is determined, the total distance traveled by each horse is calculated.

### Answer:
After running the code, you will get the following results:
- `a`: The number of days until the horses meet.
- `b`: The total distance traveled by the good horse.
- `c`: The total distance traveled by the slow horse.
"""


"""
Variable 'a' has wrong value. Expected: 3000/191, Actual: 6188/687
Variable 'b' has wrong value. Expected: 866040/191, Actual: 970600/687
Variable 'c' has wrong value. Expected: 279960/191, Actual: 587870/687"""
