"""
今有物，不知其數。三三數之，賸二；五五數之，賸三；七七數之，賸二。問：物幾何？
術曰：三三數之，賸二，置一百四十；五五數之，賸三，置六十三；七七數之，賸二，置三十。并之，得二百三十三，以二百一十減之，即得。凡三三數之，賸一，則置七十；五五數之，賸一，則置二十一；七七數之，賸一，則置十五。一百六以上，以一百五減之，即得。
答曰： a 。
"""

"""
This is a classic Chinese Remainder Theorem problem from ancient Chinese mathematics. Let's solve it step by step using the method described in the problem.

### Problem:
There is an unknown number of objects.  
- When divided by 3, the remainder is 2.  
- When divided by 5, the remainder is 3.  
- When divided by 7, the remainder is 2.  

Question: What is the number of objects?

### Procedure:
1. For the remainder when divided by 3, place 140.  
2. For the remainder when divided by 5, place 63.  
3. For the remainder when divided by 7, place 30.  
4. Add these together and subtract 210 to get the result.  

### Solution in Python:


"""

#----- content starts here -----

from sympy import mod_inverse

# Given remainders and moduli
remainders = [2, 3, 2]
moduli = [3, 5, 7]

# Step 1: Compute the product of all moduli
M = 1
for mod in moduli:
    M *= mod

# Step 2: Compute the individual terms
terms = []
for i in range(len(moduli)):
    Mi = M // moduli[i]  # M_i = M / mod_i
    inverse = mod_inverse(Mi, moduli[i])  # Modular inverse of M_i mod mod_i
    terms.append(remainders[i] * Mi * inverse)

# Step 3: Sum the terms and reduce modulo M
x = sum(terms) % M

# Answer
a = x
print(f"The number of objects is: {a}")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Remainders and Moduli**: The remainders are `[2, 3, 2]` for moduli `[3, 5, 7]`.
2. **Product of Moduli**: Compute the product \( M = 3 \times 5 \times 7 = 105 \).
3. **Individual Terms**: For each modulus \( m_i \), compute \( M_i = M / m_i \), find the modular inverse of \( M_i \) modulo \( m_i \), and multiply by the remainder.
4. **Sum and Reduce**: Add all the terms together and reduce modulo \( M \) to find the solution.

### Answer:
The number of objects is:

```plaintext
a = 23
```

This means the unknown number is **23**.
"""


"""
"""
