def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type."
    else:
        return result
    finally:
        print("Execution completed.")

print(divide(10, 2))
print(divide(10, 0))
print(divide(10, "a"))
