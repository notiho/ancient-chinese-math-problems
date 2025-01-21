"""
今有上禾六秉損實一斗八升當下禾一十秉下禾十五秉損實五升當上禾五秉問上下禾實一秉各幾何
術曰如方程置上禾六秉正下禾一十秉負損實一斗八升正次置上禾五秉負下禾一十五秉正損實五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 實 b升 下禾 c秉 實 d升 
"""

"""
This problem involves solving a system of equations using the ancient Chinese method of "fangcheng" (方程), which is equivalent to solving simultaneous linear equations. Here's how we can translate the problem and procedure into Python code:

### Problem Description:
There are two types of grain, "upper grain" (上禾) and "lower grain" (下禾).  
- Six bundles of upper grain lose 1 dou and 8 sheng of grain when processed, equivalent to 18 sheng (since 1 dou = 10 sheng).  
- Ten bundles of lower grain lose the same amount.  
- Five bundles of upper grain lose 5 sheng, while fifteen bundles of lower grain lose the same amount.  

The goal is to find how much grain (實) is in one bundle of upper grain and one bundle of lower grain.

### Procedure:
The procedure uses the "fangcheng" method to solve the system of equations. The steps are described in the problem and involve elimination and substitution.

---


"""


from fractions import Fraction

# Problem setup
# 上禾六秉損實一斗八升
上禾_1 = 6
下禾_1 = 10
損實_1 = 1 * 10 + 8  # Convert 1斗8升 to 18升

# 上禾五秉損實五升
上禾_2 = 5
下禾_2 = 15
損實_2 = 5

# Fangcheng method
# Step 1: Eliminate one variable (e.g., 下禾)
# Multiply the first equation by 下禾_2 and the second equation by 下禾_1
eq1_upper = 上禾_1 * 下禾_2
eq1_loss = 損實_1 * 下禾_2
eq2_upper = 上禾_2 * 下禾_1
eq2_loss = 損實_2 * 下禾_1

# Subtract the two equations to eliminate 下禾
upper_diff = eq1_upper - eq2_upper
loss_diff = eq1_loss - eq2_loss

# Solve for the grain in one bundle of upper grain (上禾實)
上禾實 = Fraction(loss_diff, upper_diff)

# Step 2: Solve for the grain in one bundle of lower grain (下禾實)
# Substitute 上禾實 back into one of the original equations
下禾實 = Fraction(損實_1 - 上禾_1 * 上禾實, 下禾_1)

# Convert results to dou and sheng
def convert_to_dou_sheng(value):
    dou = value // 10
    sheng = value % 10
    return dou, sheng

# Results
a = 上禾實  # Grain in one bundle of upper grain
b_dou, b_sheng = convert_to_dou_sheng(a)

c = 下禾實  # Grain in one bundle of lower grain
d_dou, d_sheng = convert_to_dou_sheng(c)

# Output
print(f"上禾實: {a} 升 ({b_dou} 斗 {b_sheng} 升)")
print(f"下禾實: {c} 升 ({d_dou} 斗 {d_sheng} 升)")


"""


### Explanation of the Code:
1. **Problem Setup**: The given data is converted into numerical values. Since 1 dou = 10 sheng, all quantities are expressed in sheng for consistency.
2. **Fangcheng Method**: The system of equations is solved using elimination. One variable (下禾) is eliminated first, and the remaining variable (上禾實) is solved. Then, the second variable (下禾實) is found by substitution.
3. **Conversion**: The results are converted back into dou and sheng for the final answer.
4. **Output**: The results are displayed in both fractional form and dou-sheng form.

### Final Answer:
The code will output the amount of grain in one bundle of upper grain (上禾) and one bundle of lower grain (下禾) in both fractional and dou-sheng forms.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 11/2
Missing variable in output: 'b'
Variable 'c' has wrong value. Expected: 1, Actual: -3/2
Missing variable in output: 'd'"""
