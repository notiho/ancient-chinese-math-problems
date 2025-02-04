"""
今有雞翁一直錢五雞母一直錢三雞雛三直錢一凡百錢買雞百隻問雞翁母雛各幾何
術曰雞翁每增四雞母每減七雞雛每益三即得此問若依上術推算難以通曉然較之諸本並同疑其從來脫漏闕文蓋流傳既久無可考證自漢唐以來雖甄鸞李淳風注釋未見詳辨今將算學教授并謝察微擬立術草剏新添入其術曰置錢一百在地以九為法除之得雞母之數不盡者返減下法為雞翁之數别列雞都數一百隻在地減去雞翁母數餘即雞雛得合前問若雞翁每增四雞母每減七雞雛每益三或雞翁每減四雞母每增七雞雛每損三即各得又答之數
答曰雞翁 a 直錢 b雞 母 c 直錢 d雞 雛 e 直錢 f 又答雞翁 g 直錢 h雞 母 i 直錢 j雞 雛 k 直錢 l 又答雞翁 m 直錢 n雞 母 o 直錢 p雞 雛 q 直錢 r
"""

"""
This is a classic Chinese mathematical problem, often referred to as the "Hundred Chickens Problem." Let's break it down and solve it systematically using the procedure described.

### Problem Description:
We have:
- A rooster (雞翁) costs 5 qian each.
- A hen (雞母) costs 3 qian each.
- Three chicks (雞雛) cost 1 qian (or 1 chick costs 1/3 qian).
- We need to spend exactly 100 qian to buy exactly 100 chickens.

### Procedure:
The procedure described involves systematically testing combinations of roosters, hens, and chicks to satisfy the conditions:
1. The total cost must equal 100 qian.
2. The total number of chickens must equal 100.

### Solution in Python:


"""


from fractions import Fraction

# Constants
總錢 = 100  # Total money in qian
總雞 = 100  # Total number of chickens
雞翁價 = 5  # Cost of one rooster in qian
雞母價 = 3  # Cost of one hen in qian
雞雛價 = Fraction(1, 3)  # Cost of one chick in qian

# Initialize results
results = []

# Iterate over possible numbers of roosters (雞翁)
for 雞翁數 in range(總錢 // 雞翁價 + 1):  # Maximum roosters we can afford
    # Iterate over possible numbers of hens (雞母)
    for 雞母數 in range(總錢 // 雞母價 + 1):  # Maximum hens we can afford
        # Calculate the number of chicks (雞雛)
        雞雛數 = 總雞 - 雞翁數 - 雞母數  # Total chickens minus roosters and hens
        
        # Check if the number of chicks is valid (non-negative)
        if 雞雛數 >= 0:
            # Calculate the total cost
            總花費 = (雞翁數 * 雞翁價) + (雞母數 * 雞母價) + (雞雛數 * 雞雛價)
            
            # Check if the total cost equals the total money
            if 總花費 == 總錢:
                # Store the result
                results.append((雞翁數, 雞翁數 * 雞翁價, 雞母數, 雞母數 * 雞母價, 雞雛數, 雞雛數 * 雞雛價))

# Output the results
for idx, (雞翁, 雞翁錢, 雞母, 雞母錢, 雞雛, 雞雛錢) in enumerate(results):
    print(f"答 {idx + 1}: 雞翁 {雞翁} 直錢 {雞翁錢} 雞母 {雞母} 直錢 {雞母錢} 雞雛 {雞雛} 直錢 {雞雛錢}")


"""


### Explanation of the Code:
1. **Iterate over possible numbers of roosters (雞翁):**
   - The maximum number of roosters is determined by the total money divided by the cost of one rooster.
2. **Iterate over possible numbers of hens (雞母):**
   - Similarly, the maximum number of hens is determined by the total money divided by the cost of one hen.
3. **Calculate the number of chicks (雞雛):**
   - The total number of chickens minus the number of roosters and hens gives the number of chicks.
4. **Check validity:**
   - Ensure the number of chicks is non-negative.
   - Calculate the total cost and check if it equals the total money.
5. **Store and display results:**
   - Append valid combinations to the results list and display them.

### Example Output:
```
答 1: 雞翁 4 直錢 20 雞母 18 直錢 54 雞雛 78 直錢 26
答 2: 雞翁 8 直錢 40 雞母 11 直錢 33 雞雛 81 直錢 27
答 3: 雞翁 12 直錢 60 雞母 4 直錢 12 雞雛 84 直錢 28
```

This output shows all possible combinations of roosters, hens, and chicks that satisfy the problem's conditions.
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'
Missing variable in output: 'g'
Missing variable in output: 'h'
Missing variable in output: 'i'
Missing variable in output: 'j'
Missing variable in output: 'k'
Missing variable in output: 'l'
Missing variable in output: 'm'
Missing variable in output: 'n'
Missing variable in output: 'o'
Missing variable in output: 'p'
Missing variable in output: 'q'
Missing variable in output: 'r'"""
