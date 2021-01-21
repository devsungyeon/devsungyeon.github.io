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

#linksubjectsL9start = "../assets/images/civil_service_examinatio/Level9_civil_servant/Level9_"
linksubjectsL9start = "C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level9_civil_servant/Level9_"
linksubjectsL9tail = "_9L/"
#linksubjectsL7start = "../assets/images/civil_service_examinatio/Level7_civil_servant/Level7_"
linksubjectsL7start = "C:/GitHub/devsungyeon.github.io/assets/images/civil_service_examinatio/Level7_civil_servant/Level7_"
linksubjectsL7tail = "_7L/"



print("Select the Level you want (7, 9) : ", end="")
level_input = int(input())
if level_input not in Level:
    sys.exit(0)
print("/n==== Subject List ====")
i = 1
for name in subjectsL7 if Level[0] == level_input else subjectsL9:
    print(f"{i} : {name}")
    i += 1
print("Select the subject number you want : ", end="")
subject_number = int(input())
subject_name = str(subjectsL9[subject_number-1] if level_input == 9 else subjectsL7[subject_number-1])

print("Select the year you want : ", end="")
year_input = int(input())

link = linksubjectsL9start if level_input == 9 else linksubjectsL7start
link += subject_name + "/"
link += str(year_input) + "_" + str(level_input) + "L/"
link += str(year_input) + "_" + str(level_input) + "L_"
print(link)

file_name = "yyyy-mm-dd-Level" + str(level_input) + "-" + subject_name + "_y" + str(year_input) + ".md"
print(file_name)

# Load the file into file_content
file_content = [ line for line in open('data-d.md') ]

# Overwrite it
writer = open('data.md','w')

i = 1
#![2016_9L_1](C:\GitHub\devsungyeon.github.io\assets\images\civil_service_examinatio\Level9_civil_servant\Level9_computerbasic\2016_9L\2016_9L_1.jpg)
problems_year_format = "#![" + str(year_input) + "_" + str(level_input) + "L_"
for line in file_content:
    # Re-write the file at 
    # each iteration
    writer.write(line)

    # We search for the correct section
    if line.startswith(str(i) + "."):
        section = problems_year_format + str(i) + "](" + link + str(i) + ".jpg)"
        print(section)
        writer.write(section)
writer.close()