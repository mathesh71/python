# Read data.txt, parse each line, and write results to output.txt

# Open the input file for reading and output file for writing
with open('data.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        # Strip whitespace and skip blank lines
        line = line.strip()
        if not line:
            continue

        # Split the line into parts
        parts = line.split(',')
        if len(parts) == 3:
            name = parts[0].strip()
            age = parts[1].strip()
            city = parts[2].strip()

            # Format output
            formatted = f"{name} is {age} years old and lives in {city}.\n"

            # Write to output file
            outfile.write(formatted)

print("Finished processing data.")

