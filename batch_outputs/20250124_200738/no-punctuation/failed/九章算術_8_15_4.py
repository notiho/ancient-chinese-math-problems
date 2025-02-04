"""
今有令一人吏五人從者一十人食雞一十令一十人吏一人從者五人食雞八令五人吏一十人從者一人食雞六問令吏從者食雞各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰令一人食 a雞 吏一人食 b雞 從者一人食 c雞 
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is described in the "方程術" (method of solving systems of equations). Below is the Python implementation of the procedure:

### Problem Setup:
We are tasked with determining how many chickens are consumed by one "令" (commander), one "吏" (official), and one "從者" (attendant), based on the following conditions:
1. 1 commander, 5 officials, and 10 attendants consume 10 chickens.
2. 10 commanders, 1 official, and 5 attendants consume 8 chickens.
3. 5 commanders, 10 officials, and 1 attendant consume 6 chickens.

### Procedure:
We will solve this system of equations step by step using the elimination method described in the "方程術."


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Equation 1: 1令 + 5吏 + 10從者 = 10
令1, 吏1, 從者1, 實1 = 1, 5, 10, 10

# Equation 2: 10令 + 1吏 + 5從者 = 8
令2, 吏2, 從者2, 實2 = 10, 1, 5, 8

# Equation 3: 5令 + 10吏 + 1從者 = 6
令3, 吏3, 從者3, 實3 = 5, 10, 1, 6

# Step 1: Eliminate 從者 (attendant) from the first two equations
# Multiply the first equation by 5 and the second equation by 10 to align 從者 coefficients
k1 = 5
k2 = 10
令1, 吏1, 從者1, 實1 = k1 * 令1, k1 * 吏1, k1 * 從者1, k1 * 實1
令2, 吏2, 從者2, 實2 = k2 * 令2, k2 * 吏2, k2 * 從者2, k2 * 實2

# Subtract the modified equations to eliminate 從者
令4 = 令2 - 令1
吏4 = 吏2 - 吏1
從者4 = 從者2 - 從者1
實4 = 實2 - 實1

# Step 2: Eliminate 從者 from the first and third equations
# Multiply the first equation by 1 and the third equation by 10 to align 從者 coefficients
k3 = 1
k4 = 10
令1, 吏1, 從者1, 實1 = k3 * 令1, k3 * 吏1, k3 * 從者1, k3 * 實1
令3, 吏3, 從者3, 實3 = k4 * 令3, k4 * 吏3, k4 * 從者3, k4 * 實3

# Subtract the modified equations to eliminate 從者
令5 = 令3 - 令1
吏5 = 吏3 - 吏1
從者5 = 從者3 - 從者1
實5 = 實3 - 實1

# Step 3: Solve for 吏 (official) by eliminating 令 (commander) from the two new equations
# Multiply the first new equation by 吏5 and the second new equation by 吏4 to align 吏 coefficients
k5 = 吏5
k6 = 吏4
令4, 吏4, 實4 = k5 * 令4, k5 * 吏4, k5 * 實4
令5, 吏5, 實5 = k6 * 令5, k6 * 吏5, k6 * 實5

# Subtract the modified equations to eliminate 吏
令6 = 令5 - 令4
吏6 = 吏5 - 吏4
實6 = 實5 - 實4

# Solve for 令 (commander)
a = Fraction(實6, 令6)

# Solve for 吏 (official)
b = Fraction(實4 - 令4 * a, 吏4)

# Solve for 從者 (attendant)
c = Fraction(實1 - 令1 * a - 吏1 * b, 從者1)

# Output the results
print(f"令一人食 {a} 雞")
print(f"吏一人食 {b} 雞")
print(f"從者一人食 {c} 雞")
#----- content ends here -----


"""


### Explanation:
1. The system of equations is solved step by step using elimination, as described in the "方程術."
2. Fractions are used to ensure precise calculations.
3. The final results are the number of chickens consumed by one commander, one official, and one attendant, respectively.

### Answer:
令一人食 `a` 雞  
吏一人食 `b` 雞  
從者一人食 `c` 雞
"""


"""
Variable 'a' has wrong value. Expected: 45/122, Actual: 4/13
Variable 'b' has wrong value. Expected: 41/122, Actual: -2/39
Variable 'c' has wrong value. Expected: 97/122, Actual: 194/195"""
