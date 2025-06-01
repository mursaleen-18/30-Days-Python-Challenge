# This code defines a function to compute the sum and average of a list of numbers.

def compute_sum_and_average(numbers):
    if not numbers:
        return 0, 0.0  # Edge case: empty list
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

# Example usage:
nums = [10, 20, 30, 40]
total, average = compute_sum_and_average(nums)
print(f"Sum: {total}, Average: {average}")
