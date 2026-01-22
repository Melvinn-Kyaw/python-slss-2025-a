def age_in_2030():
    cur_age = int(input("How old are you? "))
    print(f"In 2030, you will be {2030-2025 + cur_age} years old!")

def boxing_judging(num_judges: int):
    total = 0

    for n in range(num_judges):
        cur_score = float(input(f"Judge {n+1}: "))

        total += cur_score

    print(f"Boxing Score: is {total/num_judges}")

def burger king(tax: float):
    """
    Params:
        tax - tax as a percentage e.g. 14% -> 14"""
    burger = input("Would you like a burger for $4? (Yes/No)\n").lower().strip(",.?! ")
    fries = input("Would you like fries for $2? (Yes/No)\n").lower().strip(",.?! ")

    total = 0

    if burger == "yes":
        total += 4 * (1 + tax/100)
    if fries == "yes":
        total += 2 * (1 + tax/100)

    print(f"Your total is ${round(total, 2):.2f}")


def main():
    age_in_2030()
    boxing_score(5)
    mcdonalds(14)



if __name__ == "__main__":
    main()
