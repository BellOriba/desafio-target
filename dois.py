def fibonacci(limit):
        fibonacci = [0, 1]
        while fibonacci[-1] < limit:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        return fibonacci

def pertence_fibonacci(num):
    sequence = fibonacci(num)
    if num in sequence:
        return f"{num} pertence à Fibonacci"
    else:
        return f"{num} não pertence à Fibonacci"

def main():
    num = 34
    print(pertence_fibonacci(num))

if __name__ == "__main__":
    main()