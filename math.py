class MyMath:

    def calculate(self, operation, n):

        if operation == "sum":
            s = 0
            for i in range(1, n+1):
                s = s + i
            print("Sum of first", n, "natural numbers =", s)

        elif operation == "prime":
            print("First", n, "prime numbers:")
            count = 0
            num = 2

            while count < n:
                prime = True
                for i in range(2, num):
                    if num % i == 0:
                        prime = False
                        break

                if prime == True:
                    print(num, end=" ")
                    count = count + 1

                num = num + 1
            print()

        elif operation == "fibonacci":
            a = 0
            b = 1
            print("Fibonacci series:")
            for i in range(n):
                print(a, end=" ")
                c = a + b
                a = b
                b = c
            print()

        elif operation == "factorial":
            fact = 1
            for i in range(1, n+1):
                fact = fact * i
            print("Factorial of", n, "=", fact)

        else:
            print("Invalid operation")


m = MyMath()

op = input("Enter operation (sum / prime / fibonacci / factorial): ")
n = int(input("Enter value of n: "))

m.calculate(op, n)
