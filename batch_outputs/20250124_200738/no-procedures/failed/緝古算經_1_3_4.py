"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
This problem is a complex ancient Chinese mathematical problem involving the construction of a "Dragon Tail Dike" with varying dimensions and contributions from three counties. Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. The dike has a trapezoidal cross-section:
   - The top width (上廣) decreases from the head to the tail.
   - The bottom width (下廣) is constant.
   - The height (高) decreases from the head to the tail.

2. Dimensions at the tail:
   - Bottom width (下廣): 6 chi less than the top width (上廣).
   - Height (高): 1 zhang 2 chi (12 chi).
   - Length (袤): 4 zhang 8 chi (48 chi).

3. Contributions from counties:
   - County A: 2,375 people.
   - County B: 2,378 people.
   - County C: 5,247 people.
   - Each person completes 1 chi 9 cun 8 fen (1.98 chi³) of work per day.

4. The dike is built from the tail to the head, with contributions from County A, then County B, and finally County C.

5. The task is to calculate:
   - Total dimensions of the dike (height, top width, bottom width, and length).
   - Dimensions of the portions built by each county.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Constants
people_A = 2375  # People in County A
people_B = 2378  # People in County B
people_C = 5247  # People in County C

work_per_person = Fraction(198, 100)  # Work completed by each person in chi³ per day

# Total work completed by each county
work_A = people_A * work_per_person
work_B = people_B * work_per_person
work_C = people_C * work_per_person

# Tail dimensions
tail_height = 12  # chi
tail_length = 48  # chi
tail_bottom_width = 6  # chi
tail_top_width = tail_bottom_width + 6  # chi

# Total work completed by all counties
total_work = work_A + work_B + work_C

# Volume of a trapezoidal prism (cross-sectional area * length)
# Cross-sectional area = (top_width + bottom_width) * height / 2
# Volume = cross_sectional_area * length
def calculate_volume(height, top_width, bottom_width, length):
    cross_sectional_area = (top_width + bottom_width) * height / 2
    return cross_sectional_area * length

# Solve for total dimensions of the dike
# Start with the tail dimensions and calculate the head dimensions iteratively
head_height = tail_height
head_top_width = tail_top_width
head_bottom_width = tail_bottom_width
head_length = tail_length

while True:
    # Calculate the volume of the dike with current dimensions
    current_volume = calculate_volume(head_height, head_top_width, head_bottom_width, head_length)
    
    # Check if the current volume matches the total work
    if current_volume >= total_work:
        break
    
    # Increment the dimensions for the next iteration
    head_height += 1
    head_top_width += 1
    head_length += 1

# Calculate the portion of the dike built by each county
def calculate_county_portion(work, total_work, head_height, tail_height, head_top_width, tail_top_width, head_length, tail_length):
    # Proportion of the total work
    proportion = work / total_work
    
    # Calculate the dimensions for the county's portion
    county_height = tail_height + proportion * (head_height - tail_height)
    county_top_width = tail_top_width + proportion * (head_top_width - tail_top_width)
    county_length = tail_length + proportion * (head_length - tail_length)
    
    return county_height, county_top_width, county_length

# County A's portion
county_A_height, county_A_top_width, county_A_length = calculate_county_portion(
    work_A, total_work, head_height, tail_height, head_top_width, tail_top_width, head_length, tail_length
)

# County B's portion
county_B_height, county_B_top_width, county_B_length = calculate_county_portion(
    work_B, total_work, head_height, tail_height, head_top_width, tail_top_width, head_length, tail_length
)

# County C's portion
county_C_height, county_C_top_width, county_C_length = calculate_county_portion(
    work_C, total_work, head_height, tail_height, head_top_width, tail_top_width, head_length, tail_length
)

# Output the results
print(f"Total Dike Dimensions:")
print(f"Height: {head_height} chi")
print(f"Top Width: {head_top_width} chi")
print(f"Bottom Width: {head_bottom_width} chi")
print(f"Length: {head_length} chi")

print(f"\nCounty A's Portion:")
print(f"Height: {county_A_height} chi")
print(f"Top Width: {county_A_top_width} chi")
print(f"Length: {county_A_length} chi")

print(f"\nCounty B's Portion:")
print(f"Height: {county_B_height} chi")
print(f"Top Width: {county_B_top_width} chi")
print(f"Length: {county_B_length} chi")

print(f"\nCounty C's Portion:")
print(f"Height: {county_C_height} chi")
print(f"Top Width: {county_C_top_width} chi")
print(f"Length: {county_C_length} chi")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Volume Calculation**: The volume of the dike is calculated using the formula for a trapezoidal prism.
2. **Iterative Calculation**: The head dimensions are calculated iteratively by increasing the dimensions until the total volume matches the total work.
3. **County Contributions**: The portion of the dike built by each county is calculated based on their contribution to the total work.

This code provides the total dimensions of the dike and the dimensions of the portions built by each county.
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
Missing variable in output: 'm'"""
