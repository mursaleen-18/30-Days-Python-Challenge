def calculate_rectangle_area():
    """Calculates the area of a rectangle based on user input."""
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

        if length <= 0 or width <= 0:
            print("Length and width must be positive values.")
            return

        area = length * width
        print(f"The area of the rectangle is: {area}")

    except ValueError:
        print("Invalid input. Please enter numeric values for length and width.")

if __name__ == "__main__":
    calculate_rectangle_area()