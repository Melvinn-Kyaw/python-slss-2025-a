import math

def main():
    print("What are two sides of a square?")
    a = int(input("Side 1: "))
    b = int(input("Side 2: "))

    hyp = math.sqrt(a ** 2 + b ** 2)

    print(f"Area: {area}")


if __name__ == "__main__":
    main()
