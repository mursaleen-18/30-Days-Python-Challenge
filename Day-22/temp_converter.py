import argparse

def convert_temperature(value, from_unit, to_unit):
    # Convert input to Celsius first
    if from_unit == 'celsius':
        temp_c = value
    elif from_unit == 'fahrenheit':
        temp_c = (value - 32) * 5/9
    elif from_unit == 'kelvin':
        temp_c = value - 273.15
    else:
        raise ValueError("Invalid from_unit")

    # Convert Celsius to target unit
    if to_unit == 'celsius':
        return temp_c
    elif to_unit == 'fahrenheit':
        return temp_c * 9/5 + 32
    elif to_unit == 'kelvin':
        return temp_c + 273.15
    else:
        raise ValueError("Invalid to_unit")

# Argument parser
parser = argparse.ArgumentParser(description="Temperature Converter CLI Tool")

parser.add_argument('--from', dest='from_unit', type=str, required=True,
                    choices=['celsius', 'fahrenheit', 'kelvin'],
                    help="Original temperature unit")

parser.add_argument('--to', dest='to_unit', type=str, required=True,
                    choices=['celsius', 'fahrenheit', 'kelvin'],
                    help="Target temperature unit")

parser.add_argument('--value', type=float, required=True,
                    help="Temperature value to convert")

args = parser.parse_args()

# Perform conversion
result = convert_temperature(args.value, args.from_unit.lower(), args.to_unit.lower())
print(f"{args.value}° {args.from_unit.capitalize()} = {result:.2f}° {args.to_unit.capitalize()}")
