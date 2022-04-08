import itertools

if __name__ == '__main__':
    email = input("Input your email (no periods): ")
    lhs, rhs = email.split("@")
    arr = [char for char in lhs]
    max_number_possible_periods = len(lhs) - 1
    matrix = list(itertools.product([False, True], repeat=max_number_possible_periods))
    print(f"Given email was {email}")
    print("The following emails are all equivalent:")

    for iteration in matrix:
        lhs = ""

        for i in range(0, len(arr) - 1):
            lhs += arr[i]

            if iteration[i]:
                lhs += '.'

        lhs += arr[len(arr) - 1]
        print(f"{lhs}@{rhs}")

    print("Done")
