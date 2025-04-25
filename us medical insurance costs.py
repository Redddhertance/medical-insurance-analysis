# Goal: Analyze demographic and behavioral factors (age, region, smoking status, children) to understand their relationship with insurance charges.
# Data: .csv File consisting of information regarding patients split into: age,sex,bmi,children,smoker,region,charges. The .csv contains 1339 entries for this analysis.

import csv

# Creates lists for later analysis
ages = []
sexes = []
bmis = []
children = []
smokers = []
regions = []
charges = []

# Opens file for analysis, includes commented out loop to print first 5 rows to check file can be accessed by system.
with open('insurance.csv') as insurance_csv:
    insurance_content = csv.DictReader(insurance_csv)
    data = list(insurance_content)
#    for row in data[:5]:
#        print(row)

# Converts data to python objects in lists outside of the with statement
    for row in data:
        ages.append(int(row['age']))
        sexes.append(row['sex'])
        bmis.append(float(row['bmi']))
        children.append(int(row['children']))
        smokers.append(row['smoker'])
        regions.append(row['region'])
        charges.append(float(row['charges']))

# Function to identify averages (simplifies to 2dp), easy to call on in the future when kept as a function.
def average_calculator(averages):
    total = 0
    frequency = (len(averages))
    # Guards against division by 0
    if frequency == 0:
        return 0
    for num in averages:
        total += num
    average = round((total/frequency), 2)

    return average

# Identifies average ages, bmis and charges and prints them to the terminal for surface information.
average_ages = average_calculator(ages)
average_bmis = average_calculator(bmis)
average_charges = average_calculator(charges)
print('The average age and BMI of all individuals in this dataset is {} and  {} respectively. On average they pay ${} for insurance.'.format(average_ages, average_bmis, average_charges))

# Function to identify cost differences, only applicable to binary values for factor1 and factor2 is the desired output to be compiled into lists.
def cost_differences(factor1, factor2, factor3):
    factor1_list = []
    nonfactor1_list = []

    for i in range(len(factor1)):
        if factor1[i] == factor3:
            factor1_list.append(factor2[i])
        else:
            nonfactor1_list.append(factor2[i])
    return factor1_list, nonfactor1_list

# Breaks down cost differences by smoker status and prints to terminal. Utilises cost_differences and average_calculator functions

smoker_charges, nonsmoker_charges = cost_differences(smokers, charges, 'yes')

average_smoker_charge = average_calculator(smoker_charges)
average_nonsmoker_charge = average_calculator(nonsmoker_charges)
smoker_nonsmoker_avg_difference = (average_smoker_charge - average_nonsmoker_charge)
print('The average insurance cost for a smoker is ${}, whereas for a nonsmoker it is ${}. The difference is ${}.'.format(average_smoker_charge, average_nonsmoker_charge, smoker_nonsmoker_avg_difference))

# Breaks down cost differences by sex and prints to terminal. Utilises cost_differences and average_calculator functions

male_charges, female_charges = cost_differences(sexes, charges, 'male')

average_male_charge = average_calculator(male_charges)
average_female_charge = average_calculator(female_charges)
male_female_avg_difference = (average_male_charge - average_female_charge)
print('The average insurance cost for a male is ${}, whereas for a female it is ${}. The difference is ${}.'.format(average_male_charge, average_female_charge, male_female_avg_difference))

# Identifies average age of people with children and compares it to people without children.

parent = []
for i in (range(len(children))):
    if children[i] > 0:
        parent.append(True)
    else:
        parent.append(False)

parent_ages, nonparent_ages = cost_differences(parent, ages, True)
average_parent_age = average_calculator(parent_ages)
average_nonparent_age = average_calculator(nonparent_ages)
difference_parent_nonparent = (average_parent_age - average_nonparent_age)
print('The average age for a parent is {} years old, whereas for a nonparent it is {} years old. The difference is {} years'.format(average_parent_age, average_nonparent_age, difference_parent_nonparent))

# Breaks down differences by region to see if local economic conditions affect costs and returns a dictionary of region averages using nested average_calculator function within region_costs function. Also returns most expensive and cheapest area and prints it to the terminal.
def region_costs(regions, charges):
    unique_regions = set(regions)
    region_averages = {}
    for region in unique_regions:
        region_charges = []
        for i in range(len(regions)):
            if regions[i] == region:
                region_charges.append(charges[i])
        average = average_calculator(region_charges)
        region_averages[region] = average
    max = float('-inf')
    min = float('inf')
    max_region = None
    min_region = None
    for region, cost in region_averages.items():
        if cost < min:
            min = cost
            min_region = region
        if cost > max:
            max = cost
            max_region = region
    return region_averages, min_region, max_region

region_average, max_charge_area, min_charge_area = region_costs(regions, charges)
print(max_charge_area, min_charge_area, region_average)

print('The most costly area for insurance is the {} area. The cheapest area for insurance is the {} area.'.format(max_charge_area, min_charge_area))