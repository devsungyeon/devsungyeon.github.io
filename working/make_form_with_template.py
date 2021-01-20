# Load the file into file_content
file_content = [ line for line in open('data.md') ]

# Overwrite it
writer = open('data.md','w')

for line in file_content:
    # We search for the correct section
    if line.startswith("##"):
        section = line.strip()

    # Re-write the file at each iteration
    writer.write(line)

    # Once we arrive at the correct position, write the new entry
    if section == "## intent:affirm" and line.strip() == "- correct":
        writer.write("- yes, I affirm\n")

writer.close()