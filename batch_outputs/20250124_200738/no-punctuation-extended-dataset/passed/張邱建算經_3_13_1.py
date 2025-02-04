"""
今有甲乙丙三人持錢不知多少甲言我得乙大半得丙少半可滿一百乙言我得甲大半得丙半可滿一百丙言我得甲乙各大半可滿一百問甲乙丙持錢各幾何
術曰三甲二乙一丙錢三百四甲六乙三丙錢六百二甲二乙三丙錢三百如方程即得
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
答曰甲 a 乙 b 丙 c
"""

#----- content starts here -----
"""
Suppose there are three people: Jia, Yi, and Bing, holding an unknown amount of money.
Jia says: If I take more than half of Yi's money and less than half of Bing's money, I can reach 100.
Yi says: If I take more than half of Jia's money and half of Bing's money, I can reach 100.
Bing says: If I take more than half of both Jia's and Yi's money, I can reach 100.
Question: How much money does each of Jia, Yi, and Bing hold?

The procedure says:
- Form the equations:
  3 Jia + 2 Yi + 1 Bing = 300
  4 Jia + 6 Yi + 3 Bing = 600
  2 Jia + 2 Yi + 3 Bing = 300
- Solve these equations using the method of elimination.

The answer says: Jia holds *a*, Yi holds *b*, and Bing holds *c*.
"""

# Define the coefficients and constants of the equations
# 3甲 + 2乙 + 1丙 = 300
eq1 = {"甲": 3, "乙": 2, "丙": 1, "constant": 300}

# 4甲 + 6乙 + 3丙 = 600
eq2 = {"甲": 4, "乙": 6, "丙": 3, "constant": 600}

# 2甲 + 2乙 + 3丙 = 300
eq3 = {"甲": 2, "乙": 2, "丙": 3, "constant": 300}

# Step 1: Eliminate one variable (丙) using the first two equations
# Multiply eq1 by 3 to align 丙 coefficients with eq2
eq1_scaled = {key: value * 3 for key, value in eq1.items()}

# Subtract eq1_scaled from eq2 to eliminate 丙
eq4 = {
    "甲": eq2["甲"] - eq1_scaled["甲"],
    "乙": eq2["乙"] - eq1_scaled["乙"],
    "丙": eq2["丙"] - eq1_scaled["丙"],
    "constant": eq2["constant"] - eq1_scaled["constant"],
}

# Step 2: Eliminate 丙 using eq1 and eq3
# Multiply eq1 by 3 to align 丙 coefficients with eq3
eq1_scaled_again = {key: value * 3 for key, value in eq1.items()}

# Subtract eq1_scaled_again from eq3 to eliminate 丙
eq5 = {
    "甲": eq3["甲"] - eq1_scaled_again["甲"],
    "乙": eq3["乙"] - eq1_scaled_again["乙"],
    "丙": eq3["丙"] - eq1_scaled_again["丙"],
    "constant": eq3["constant"] - eq1_scaled_again["constant"],
}

# Step 3: Solve for 乙 using eq4 and eq5
# Eliminate 甲 by aligning coefficients
eq4_scaled = {key: value * eq5["甲"] for key, value in eq4.items()}
eq5_scaled = {key: value * eq4["甲"] for key, value in eq5.items()}

# Subtract eq5_scaled from eq4_scaled to eliminate 甲
eq6 = {
    "甲": eq4_scaled["甲"] - eq5_scaled["甲"],
    "乙": eq4_scaled["乙"] - eq5_scaled["乙"],
    "丙": eq4_scaled["丙"] - eq5_scaled["丙"],
    "constant": eq4_scaled["constant"] - eq5_scaled["constant"],
}

# Solve for 乙
乙 = Fraction(eq6["constant"], eq6["乙"])

# Step 4: Solve for 甲 using eq5
甲 = Fraction(
    eq5["constant"] - eq5["乙"] * 乙,
    eq5["甲"],
)

# Step 5: Solve for 丙 using eq1
丙 = Fraction(
    eq1["constant"] - eq1["甲"] * 甲 - eq1["乙"] * 乙,
    eq1["丙"],
)

# Final results
a = 甲
b = 乙
c = 丙#----- content ends here -----

"""
"""
