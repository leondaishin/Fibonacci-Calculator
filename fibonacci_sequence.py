### Fibonacci Calculator

def main(): 
    # letting user prompt the things he wants to know about fibonacci numbers and sequences
    print("           WELCOME\n")
    print("             TO\n")
    print("(-: FIBONACCI CALCULATOR :-)\n\n")

    # starting a loop for the person to get to know more about fibonacci numbers
    while True: 
        print("1. Find the nth Fibonacci Number")
        print("2. Find the nth Fibonacci Sequence")
        print("3. Check if the number is a Fibonacci Number")
        print("4. Find the index of the Fibonacci Number")
        print("5. Find the sum of the first n + 1 Fibonacci Number")
        print("6. Find the sum of the first n + 1 Fibonacci Numbers squared")
        print("7. Find out if 2 given Fibonacci numbers are divisible by the other")
        print("8. Find out the modulo of a given Fibonacci Number")
        print("9. Find out the Cassini's Identity of the given Fibonacci Number")
        print("10. Calculate a Fibonacci Number using Fast Doubling")
        print("0. Exit \n\n")

        choice = input("Choose an option: ").strip()

        if choice == "1": 
            number = int(input("Enter the position n: "))
            print(f"f_{number} = ", fibonacci(number))

        elif choice == "2": 
            number = int(input("How many Fibonacci numbers would you like to see in the sequence? "))
            print(fibonacci_sequence(number))

        elif choice == "3": 
            number = int(input("Enter a number: "))

            if is_fibonacci(number): 
                print(f"{number} is a Fibonacci Number. ")
            else: 
                print(f"{number} is not a Fibonacci Number. ")

        elif choice == "4": 
            number = int(input("Enter a Fibonacci number: "))
            print(fibonacci_index(number))

        elif choice == "5": 
            number = int(input("Enter n: "))
            print(fibonacci_sum(number))

        elif choice == "6": 
            number = int(input("Enter n: "))
            print(fibonacci_square_sum(number))

        elif choice == "7": 
            number_1 = int(input("Enter the first index n: "))
            number_2 = int(input("Enter the second index m: "))
            print(fibonacci_divisible(number_1, number_2))

        elif choice == "8": 
            number = int(input("Enter a Fibonacci Number: "))
            modulo = int(input("Enter the modulo m: "))
            print(fibonacci_mod(number, modulo))

        elif choice == "9": 
            number = int(input("Enter n (n >= 1): "))
            if number >= 1: 
                print(fibonacci_cassini(number))
            else: 
                print(f"{number} is not at least 1. ")

        elif choice == "10": 
            number = int(input("Enter the position n: "))
            print(fibonacci_doubling(number))

        elif choice == "0": 
            print("\nThank you for using Fibonacci Claculator!\n")
            break

        else: 
            print("Invalid Choice")

        print()




def fibonacci(n): 
    # returns the fibonacci number at position n#
    # defining the binets formula with square root of 5 etc

    square_root_5 = 5 ** 0.5

    first_part = ((1 + square_root_5) / 2) ** n
    second_part = ((1 - square_root_5) / 2) ** n

    f_n = (first_part - second_part) / square_root_5

    # binets formula for fibonacci numbers
    return round(f_n)
    




def fibonacci_sequence(n): 
    # returns the first n fibonacci numbers
    # the set starts with an empty set
    sequence = []

    for i in range(n): 
        sequence.append(fibonacci(i))

    return sequence





def is_fibonacci(number): 
    # checks whether a given integer belongs to the Fibonacci sequence
    # i meaning the i-th element of the list of sequence 

    i = 0

    while fibonacci(i) <= number: 
        if fibonacci(i) == number: 
            return True 

        i += 1 

    return False






def fibonacci_index(number): 
    # finds the position of a fibonacci number in the sequence
    
    i = 0

    while fibonacci(i) <= number: 
        if fibonacci(i) == number: 
            return i

        i += 1

    return "This is not a valid Fibonacci Number. "






def fibonacci_sum(n): 
    # return the sum of the first n + 1 Fibonacci Numbers
    # sum of all fn from 0 to n is == fn-2 - 1 (induction proof)
    return fibonacci(n + 2) - 1






def fibonacci_square_sum(n): 
    # returns the sum of squares of Fibonacci number 
    # the sum of f_n ** 2 == f_n * f_n+1
    return fibonacci(n) * fibonacci(n + 1)






def fibonacci_divisible(n, m): 
    # checks whether one Fibonacci number is divisible by another fibonacci number
    return fibonacci(n) % fibonacci(m) == 0






def fibonacci_mod(n, m): 
    # returns the nth Fibonacci number modulo m 
    return fibonacci(n) % m 






def fibonacci_cassini(n): 
    # verifies Cassini's identity: 

    left_side = fibonacci(n + 1) * fibonacci(n - 1) - fibonacci(n) ** 2
    right_side = (-1) ** n

    return left_side == right_side






def fibonacci_doubling(n): 
    # given a fibonacci number with the formula the number will be doubled 
    
    if n == 0: 
        return 0

    a, b = fibonacci_doubling_pair(n)

    return a





def fibonacci_doubling_pair(n): 
    # returns f_n and f_n+1:
    if n == 0: 
        return 0, 1
    a, b = fibonacci_doubling_pair(n // 2)

    c = a * (2 * b - a)
    d = a ** 2 + b ** 2

    if n % 2 == 0: 
        return c, d
    else: 
        return d, c + d


if __name__ == "__main__": 
    main() 
    