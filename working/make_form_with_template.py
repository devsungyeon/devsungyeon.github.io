# # Load the file into file_content
# file_content = [ line for line in open('data.md') ]

# # Overwrite it
# writer = open('data.md','w')

# for line in file_content:
#     # We search for the correct section
#     if line.startswith("##"):
#         section = line.strip()

#     # Re-write the file at each iteration
#     writer.write(line)

#     # Once we arrive at the correct position, write the new entry
#     if section == "## intent:affirm" and line.strip() == "- correct":
#         writer.write("- yes, I affirm/n")

# writer.close()

import sys

Level = [7, 9]

subjectsL9 = [
    'computerbasic',
    'information',
    'informationsystem',
    'network'
]

subjectsL7 = [
    'database',
    'datastructure',
    'information',
    'softwareeng'
]

linksubjectsL9 = "../assets/images/civil_service_examinatio/Level9_civil_servant/Level9_"
linksubjectsL7 = "../assets/images/civil_service_examinatio/Level7_civil_servant/Level7_"

print("Select the Level you want (7, 9) : ", end="")
level_input = int(input())
if level_input not in Level:
    sys.exit(0)
print("/n==== Subject List ====")
i = 1
for name in subjectsL9 if Level[0] == level_input else subjectsL7:
    print(f"{i} : {name}")
    i += 1
print("Select the subject number you want : ", end="")
subject_number = int(input())

test = "C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_database/2020_7L/2020_7L_1.jpg"
open(test)