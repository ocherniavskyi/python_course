fibonacci_numbers = [1, 1]


def fill_fibonacci_numbers(position):
    while len(fibonacci_numbers) < position:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])


def generate_fibonacci(position):
    #position = int(position)
    if position < 1:
        raise ValueError("Value should be greater than 0")
    if len(fibonacci_numbers) < position:
        fill_fibonacci_numbers(position)
    return fibonacci_numbers[position - 1]


def main():
    print("generate_fibonacci(5)={}".format(generate_fibonacci(5)))
    print("generate_fibonacci(10)={}".format(generate_fibonacci(10)))
    print("generate_fibonacci(15)={}".format(generate_fibonacci(15)))


if __name__ == "__main__":
    main()
