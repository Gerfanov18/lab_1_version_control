# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Помилка: ділення на нуль!"
    return a / b

if __name__ == "__main__":
    print("Калькулятор")
    while True:
        try:
            num1 = float(input("Введіть перше число: "))
            op = input("Введіть операцію (+, -, *, /): ")
            num2 = float(input("Введіть друге число: "))

            if op == "+":
                print("Результат:", add(num1, num2))
            elif op == "-":
                print("Результат:", subtract(num1, num2))
            elif op == "*":
                print("Результат:", multiply(num1, num2))
            elif op == "/":
                print("Результат:", divide(num1, num2))
            else:
                print("Невідома операція!")
        except ValueError:
            print("Будь ласка, введіть число!")

        again = input("\nЩе раз? (y/n): ").lower()
        if again != 'y':
            break
