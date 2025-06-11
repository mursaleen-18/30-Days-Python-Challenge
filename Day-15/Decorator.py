import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Function '{func.__name__}' executed in {duration:.6f} seconds.")
        return result
    return wrapper

# Example usage
@log_execution_time
def slow_function():
    time.sleep(2)
    print("Finished sleeping")

slow_function()
