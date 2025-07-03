import logging

# Configure logging (both to file and console)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

def parse_line(line):
    """Parses a line of input and returns a tuple (name, age, city)."""
    parts = line.strip().split(',')
    if len(parts) != 3:
        raise ValueError(f"Invalid format: {line.strip()}")

    name = parts[0].strip()
    try:
        age = int(parts[1].strip())  # May raise ValueError
    except ValueError:
        raise ValueError(f"Invalid age for {name}: {parts[1].strip()}")

    city = parts[2].strip()
    return name, age, city

def main():
    try:
        with open('data.txt', 'r') as infile, open('output.txt', 'w') as outfile:
            for line in infile:
                if not line.strip():
                    continue  # Skip blank lines
                try:
                    name, age, city = parse_line(line)
                    output = f"{name} is {age} years old and lives in {city}.\n"
                    outfile.write(output)
                    logging.info(f"Processed: {name}")
                except ValueError as ve:
                    logging.warning(f"Skipping line due to error: {ve}")
    except FileNotFoundError:
        logging.critical("Input file 'data.txt' not found.")
    except Exception as e:
        logging.exception("Unexpected error occurred during processing.")

if __name__ == "__main__":
    main()
    print("Done! Check output.txt and app.log.")

