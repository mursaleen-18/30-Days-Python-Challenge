def read_numbers_from_file(filename):
    total = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    num = float(line.strip())
                    total += num
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Processing complete.")
    
    return total


# Example usage:
filename = "numbers.txt"  # Make sure to create this file with some numbers and invalid data.
result = read_numbers_from_file(filename)
print(f"Total sum of valid numbers: {result}")
# This code reads numbers from a file, handles errors for invalid lines, and reports if the file is not found.
# It also ensures that the processing is complete by using a finally block.