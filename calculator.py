from math import pow

def main():
    while True:
        data = raw_input("> ")
        tokens = data.split(" ")

        if tokens[0] == 'q':
            break

        # tokens_to_add = []
        # for t in range(1, len(tokens), 2):
        #     if tokens[t] == "*":
        #         result = multiply(int(tokens[t-1]), int(tokens[t+1]))
        #         tokens_to_add.append(result)

        total = int(tokens[0])

        for t in range(1, len(tokens), 2):
            if tokens[t] == "+":
                total = add(total, int(tokens[t+1]))
            elif tokens[t] == "-":
                total = subtract(total, int(tokens[t+1]))
            elif tokens[t] == "*":
                total = multiply(total, int(tokens[t+1]))
            elif tokens[t] == "/":
                total = divide(total, float(tokens[t+1]))
            elif tokens[t] == "square":
                total = total + square(int(tokens[t+1]))
            elif tokens[t] == "cube":
                total = total + cube(int(tokens[t+1]))
            elif tokens[t] == "pow":
                total = power(total, int(tokens[t+1]))
            elif tokens[t] == "mod":
                total =  mod(total, int(tokens[t+1]))
            else:
                pass

        print total


            # elif tokens[0] == "*":
            #     print multiply(int(tokens[1]), int(tokens[2]))
            # elif tokens[0] == "/":
            #     print divide(float(tokens[1]), float(tokens[2]))
            # elif tokens[0] == "square":
            #     print square(int(tokens[1]))
            # elif tokens[0] == "cube":
            #     print cube(int(tokens[1]))
            # elif tokens[0] == "pow":
            #     print power(int(tokens[1]), int(tokens[2]))
            # elif tokens[0] == "mod":
            #     print mod(int(tokens[1]), int(tokens[2]))
            # else:
            #     break

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def square(num1):
    return int(pow(num1, 2))

def cube(num1):
    return int(pow(num1, 3))

def power(num1, num2):
    return int(pow(num1, num2))

def mod(num1, num2):
    return num1 % num2

if __name__ == "__main__":
    main()