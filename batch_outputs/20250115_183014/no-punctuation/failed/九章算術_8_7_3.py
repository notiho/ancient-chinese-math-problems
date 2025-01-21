"""
今有賣牛二羊五以買十三豕有餘錢一千賣牛三豕三以買九羊錢適足賣羊六豕八以買五牛錢不足六百問牛羊豕價各幾何
術曰如方程置牛二羊五正豕一十三負餘錢數正次牛三正羊九負豕三正次牛五負羊六正豕八正不足錢負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰牛價 a 羊價 b 豕價 c 
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, known as the "fangcheng" method. The problem is to determine the prices of a cow (牛), a sheep (羊), and a pig (豕) based on the given transactions.

### Problem Setup:
1. Selling 2 cows and 5 sheep to buy 13 pigs leaves 1000 units of money.
   Equation: `2牛 + 5羊 - 13豕 = 1000`
2. Selling 3 cows and 3 pigs to buy 9 sheep leaves no money.
   Equation: `3牛 - 9羊 + 3豕 = 0`
3. Selling 6 sheep and 8 pigs to buy 5 cows leaves a deficit of 600 units of money.
   Equation: `-5牛 + 6羊 + 8豕 = -600`

We will solve this system using the ancient "fangcheng" method.

---

### Python Code Implementation:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 2牛 + 5羊 - 13豕 = 1000
eq1 = [2, 5, -13, 1000]

# Equation 2: 3牛 - 9羊 + 3豕 = 0
eq2 = [3, -9, 3, 0]

# Equation 3: -5牛 + 6羊 + 8豕 = -600
eq3 = [-5, 6, 8, -600]

# Step 1: Eliminate the first variable (牛) from eq2 and eq3 using eq1
# Multiply eq1 by 3 and eq2 by 2, then subtract
factor1 = 3
factor2 = 2
new_eq2 = [
    factor1 * eq2[i] - factor2 * eq1[i]
    for i in range(4)
]

# Multiply eq1 by 5 and eq3 by 2, then subtract
factor1 = 5
factor2 = 2
new_eq3 = [
    factor1 * eq3[i] - factor2 * eq1[i]
    for i in range(4)
]

# Step 2: Eliminate the second variable (羊) from new_eq3 using new_eq2
# Multiply new_eq2 by 6 and new_eq3 by 45, then subtract
factor1 = 6
factor2 = 45
final_eq = [
    factor1 * new_eq3[i] - factor2 * new_eq2[i]
    for i in range(4)
]

# Step 3: Solve for the third variable (豕)
豕 = Fraction(final_eq[3], final_eq[2])

# Step 4: Back-substitute to solve for 羊
羊 = Fraction(new_eq2[3] - new_eq2[2] * 豕, new_eq2[1])

# Step 5: Back-substitute to solve for 牛
牛 = Fraction(eq1[3] - eq1[2] * 豕 - eq1[1] * 羊, eq1[0])

# Results
a = 牛
b = 羊
c = 豕

# Output the results
a, b, c


"""


---

### Explanation of the Code:
1. **Equation Setup**: Each equation is represented as a list of coefficients `[牛, 羊, 豕, constant]`.
2. **Elimination**: The first variable (牛) is eliminated from the second and third equations using the first equation. This is done by multiplying the equations by appropriate factors and subtracting.
3. **Further Elimination**: The second variable (羊) is eliminated from the third equation using the second equation.
4. **Back-Substitution**: The value of the third variable (豕) is determined from the final equation, and then the values of the second (羊) and first (牛) variables are determined by back-substitution.
5. **Results**: The prices of a cow, a sheep, and a pig are output as fractions.

---

### Answer:
The prices are:
- 牛價 `a` (price of a cow)
- 羊價 `b` (price of a sheep)
- 豕價 `c` (price of a pig)
"""


"""
Variable 'a' has wrong value. Expected: 1200, Actual: 748500/4847
Variable 'b' has wrong value. Expected: 500, Actual: 86000/14541
Variable 'c' has wrong value. Expected: 300, Actual: -20000/393"""
