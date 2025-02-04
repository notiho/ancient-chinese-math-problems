"""
假令穿河，袤一裏二百七十六步，下廣六步一尺二寸；北頭深一丈八尺六寸，上廣十二步二尺四寸；南頭深二百四十一尺八寸；上廣八十六步四尺八寸。運土於河西岸造漘，北頭高二百二十三尺二寸，南頭無高，下廣四百六尺七寸五厘，袤與河同。甲郡二萬二千三百二十人，乙郡六萬八千七十六人，丙郡五萬九千九百八十五人，丁郡三萬七千九百四十四人。自穿、負、築，各人程功常積三尺七寸二分。限九十六日役，河漘俱了。四郡分共造漘，其河自北頭先給甲郡，以次與乙，合均賦積尺。問：逐郡各給斜、正袤，上廣及深，並漘上廣各多少？
答曰：漘上廣 a丈 ；甲郡正袤 b丈 ，斜袤 c丈 ，上廣 d丈 ，深 e丈 ；乙郡正袤 f丈 ，斜袤 g丈 ，上廣 h丈 ，深 i丈 ；丙郡正袤 j丈 ，斜袤 k丈 ，上廣 l丈 ，深 m丈 ，丁郡正袤 n丈 ，斜袤 o丈 ，上廣 p丈 ，深 q丈 。
"""

"""
This problem is extremely complex and involves multiple steps, including calculating the dimensions of the river, the embankments, and distributing the workload among four counties. I'll break it down into manageable steps and translate it into Python code.

---

### Problem Breakdown:
1. **River Dimensions**:
   - Length (袤): 1 li 276 bu.
   - Width and depth vary at the north and south ends.
   - North end: depth = 1 zhang 8 chi 6 cun, upper width = 12 bu 2 chi 4 cun.
   - South end: depth = 241 chi 8 cun, upper width = 86 bu 4 chi 8 cun.
   - Bottom width: 6 bu 1 chi 2 cun.

2. **Embankment (漘)**:
   - Built on the west bank of the river.
   - North end height = 223 chi 2 cun, south end height = 0.
   - Bottom width = 406 chi 7 cun 5 li.
   - Length matches the river's length.

3. **Workforce**:
   - Four counties (甲, 乙, 丙, 丁) with different populations.
   - Each person can complete 3 chi 7 cun 2 fen of work per day.
   - Total time = 96 days.

4. **Work Distribution**:
   - The river is divided among the counties, starting with 甲郡 at the north end, then 乙郡, and so on.
   - The embankment is shared equally among the counties.

5. **Output**:
   - Calculate the dimensions (正袤, 斜袤, 上廣, 深) for each county's portion of the river.
   - Calculate the embankment's upper width (漘上廣).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Constants
li_to_bu = 300  # 1 li = 300 bu
bu_to_chi = 6   # 1 bu = 6 chi
chi_to_cun = 10 # 1 chi = 10 cun
cun_to_li = 10  # 1 cun = 10 li

# River dimensions
river_length_bu = 1 * li_to_bu + 276  # 1 li 276 bu
bottom_width_chi = 6 * bu_to_chi + 1 * chi_to_cun + 2  # 6 bu 1 chi 2 cun
north_depth_chi = 1 * 10 + 8 + Fraction(6, 10)  # 1 zhang 8 chi 6 cun
north_upper_width_chi = 12 * bu_to_chi + 2 * chi_to_cun + 4  # 12 bu 2 chi 4 cun
south_depth_chi = 241 + Fraction(8, 10)  # 241 chi 8 cun
south_upper_width_chi = 86 * bu_to_chi + 4 * chi_to_cun + 8  # 86 bu 4 chi 8 cun

# Embankment dimensions
north_embankment_height_chi = 223 + Fraction(2, 10)  # 223 chi 2 cun
south_embankment_height_chi = 0  # No height at the south end
embankment_bottom_width_chi = 406 + Fraction(7, 10) + Fraction(5, 100)  # 406 chi 7 cun 5 li

# Workforce
county_population = {
    "甲": 22320,
    "乙": 68076,
    "丙": 59985,
    "丁": 37944
}
total_population = sum(county_population.values())
work_per_person_per_day = 3 + Fraction(7, 10) + Fraction(2, 100)  # 3 chi 7 cun 2 fen
total_days = 96

# Total work completed by all counties
total_work = total_population * work_per_person_per_day * total_days

# Embankment work (shared equally)
embankment_length_chi = river_length_bu * bu_to_chi
embankment_work = embankment_length_chi * embankment_bottom_width_chi * (north_embankment_height_chi / 2)
embankment_work_per_county = embankment_work / 4

# River work (distributed proportionally)
river_work = total_work - embankment_work
river_work_per_person = river_work / total_population

# Calculate dimensions for each county
results = {}
remaining_length_chi = river_length_bu * bu_to_chi

for county, population in county_population.items():
    # Work completed by this county
    county_work = population * work_per_person_per_day * total_days - embankment_work_per_county

    # Calculate the portion of the river this county is responsible for
    county_length_chi = county_work / river_work_per_person
    if county_length_chi > remaining_length_chi:
        county_length_chi = remaining_length_chi

    # Calculate dimensions (正袤, 斜袤, 上廣, 深)
    upper_width_chi = north_upper_width_chi + (south_upper_width_chi - north_upper_width_chi) * (county_length_chi / (river_length_bu * bu_to_chi))
    depth_chi = north_depth_chi + (south_depth_chi - north_depth_chi) * (county_length_chi / (river_length_bu * bu_to_chi))
    diagonal_length_chi = (county_length_chi**2 + depth_chi**2)**0.5

    results[county] = {
        "正袤": county_length_chi,
        "斜袤": diagonal_length_chi,
        "上廣": upper_width_chi,
        "深": depth_chi
    }

    remaining_length_chi -= county_length_chi

# Embankment upper width
embankment_upper_width_chi = embankment_bottom_width_chi / 2

# Output results
print(f"漘上廣: {embankment_upper_width_chi} 丈")
for county, dimensions in results.items():
    正袤 = dimensions["正袤"] / 10  # Convert chi to zhang
    斜袤 = dimensions["斜袤"] / 10  # Convert chi to zhang
    上廣 = dimensions["上廣"] / 10  # Convert chi to zhang
    深 = dimensions["深"] / 10     # Convert chi to zhang
    print(f"{county}郡 正袤: {正袤} 丈, 斜袤: {斜袤} 丈, 上廣: {上廣} 丈, 深: {深} 丈")
#----- content ends here -----


"""


---

### Explanation:
1. **River Dimensions**:
   - Convert all measurements to `chi` for consistency.
   - Use linear interpolation to calculate the upper width and depth for each county's portion.

2. **Workforce**:
   - Calculate the total work completed by all counties.
   - Subtract the embankment work (shared equally) to determine the river work.

3. **Work Distribution**:
   - Distribute the river work proportionally among the counties based on their populations.
   - Calculate the dimensions for each county's portion of the river.

4. **Output**:
   - Print the embankment's upper width.
   - Print the dimensions (正袤, 斜袤, 上廣, 深) for each county.

---

This code provides the required dimensions for the river and embankment for each county. Let me know if you need further clarification!
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
Missing variable in output: 'q'"""
