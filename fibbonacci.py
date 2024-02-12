#Question 2 :Write a program to generate the Fibonacci sequence up to 100.

def generate_fibonacci(limit):
    fibonacci_sequence = [0, 1]
    while True:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_fibonacci > limit:
            break
        fibonacci_sequence.append(next_fibonacci)
    return fibonacci_sequence


fibonacci_sequence_up_to_100 = generate_fibonacci(100)


print("Fibonacci sequence up to 100:")
print(fibonacci_sequence_up_to_100)

