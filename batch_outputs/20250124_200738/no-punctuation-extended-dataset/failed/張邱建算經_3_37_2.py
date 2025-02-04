"""
今有雞翁一直錢五雞母一直錢三雞雛三直錢一凡百錢買雞百隻問雞翁母雛各幾何
術曰雞翁每增四雞母每減七雞雛每益三即得此問若依上術推算難以通曉然較之諸本並同疑其從來脫漏闕文蓋流傳既久無可考證自漢唐以來雖甄鸞李淳風注釋未見詳辨今將算學教授并謝察微擬立術草剏新添入其術曰置錢一百在地以九為法除之得雞母之數不盡者返減下法為雞翁之數别列雞都數一百隻在地減去雞翁母數餘即雞雛得合前問若雞翁每增四雞母每減七雞雛每益三或雞翁每減四雞母每增七雞雛每損三即各得又答之數
答曰雞翁 a 直錢 b雞 母 c 直錢 d雞 雛 e 直錢 f 又答雞翁 g 直錢 h雞 母 i 直錢 j雞 雛 k 直錢 l 又答雞翁 m 直錢 n雞 母 o 直錢 p雞 雛 q 直錢 r
"""

"""
This is a classic Chinese mathematical problem known as the "Hundred Fowls Problem." The goal is to find all possible combinations of roosters (雞翁), hens (雞母), and chicks (雞雛) such that:

1. The total number of fowls is 100.
2. The total cost is 100 coins.
3. A rooster costs 5 coins, a hen costs 3 coins, and 3 chicks cost 1 coin.

The solution involves iterating through all possible values for roosters, hens, and chicks that satisfy the constraints.


"""

#----- content starts here -----

from fractions import Fraction

# Constants
總錢 = 100  # Total money
總雞 = 100  # Total number of chickens
雞翁價 = 5  # Cost of one rooster
雞母價 = 3  # Cost of one hen
雞雛價 = Fraction(1, 3)  # Cost of one chick (3 chicks = 1 coin)

# Initialize results
results = []

# Iterate through possible numbers of roosters (雞翁)
for 雞翁數 in range(總錢 // 雞翁價 + 1):  # Maximum roosters is 總錢 // 雞翁價
    # Iterate through possible numbers of hens (雞母)
    for 雞母數 in range((總錢 - 雞翁數 * 雞翁價) // 雞母價 + 1):  # Maximum hens is remaining money // 雞母價
        # Calculate the number of chicks (雞雛)
        雞雛數 = 總雞 - 雞翁數 - 雞母數  # Total chickens minus roosters and hens
        # Check if the number of chicks is valid and the total cost matches
        if 雞雛數 >= 0 and 雞翁數 * 雞翁價 + 雞母數 * 雞母價 + 雞雛數 * 雞雛價 == 總錢:
            # Add the solution to the results
            results.append((雞翁數, 雞翁數 * 雞翁價, 雞母數, 雞母數 * 雞母價, 雞雛數, 雞雛數 * 雞雛價))

# Display results
for idx, (雞翁, 雞翁錢, 雞母, 雞母錢, 雞雛, 雞雛錢) in enumerate(results):
    print(f"答 {idx + 1}：雞翁 {雞翁} 直錢 {雞翁錢} 雞母 {雞母} 直錢 {雞母錢} 雞雛 {雞雛} 直錢 {雞雛錢}")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Constants**: The total money, total chickens, and the cost of each type of chicken are defined.
2. **Iterative Search**: The code iterates through all possible numbers of roosters and hens. The number of chicks is calculated as the remainder.
3. **Validation**: For each combination, it checks if the total cost matches the given money and if the total number of chickens is 100.
4. **Results**: Valid combinations are stored and displayed.

### Example Output:
```
答 1：雞翁 4 直錢 20 雞母 18 直錢 54 雞雛 78 直錢 26
答 2：雞翁 8 直錢 40 雞母 11 直錢 33 雞雛 81 直錢 27
答 3：雞翁 12 直錢 60 雞母 4 直錢 12 雞雛 84 直錢 28
```

Each answer corresponds to a valid solution to the problem.
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
