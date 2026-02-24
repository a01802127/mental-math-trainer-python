import random

def multiplication_quiz(min_a, max_a, min_b, max_b):

    user_answers = []
    correct_answers = []

    question_number = 1

    correct_count = 0
    incorrect_count = 0

    for _ in range(20):

        num_a = random.randint(min_a, max_a)
        num_b = random.randint(min_b, max_b)

        correct_result = num_a * num_b

        correct_answers.append(correct_result)

        while True:
            try:
                user_input = int(input(f"\n{question_number}) {num_a} x {num_b} = "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        user_answers.append(user_input)

        if user_input == correct_result:

            print("Correct answer.")
            correct_count += 1

        else:

            print(f"Incorrect answer. The correct result is {correct_result}.")
            incorrect_count += 1

        question_number += 1

    score = (correct_count * 100) / 20

    with open("results.txt", "w", encoding="utf-8") as results_file:

        results_file.write(f"Final score: {score}%\n")

        if correct_count >= 14:

            results_file.write(
                f"\nStatus: Passed\nCorrect answers: {correct_count}\nIncorrect answers: {incorrect_count}\n"
            )

        else:

            results_file.write(
                f"\nStatus: Failed\nCorrect answers: {correct_count}\nIncorrect answers: {incorrect_count}\n"
            )

        results_file.write(f"\nYour answers: {user_answers}\n")
        results_file.write(f"Correct answers: {correct_answers}\n")

    print("\nResults saved in 'results.txt'.")

    while True:

        retry = input("\nDo you want to try again? (y/n): ").strip().lower()

        if retry == "y":
            print()
            select_level()
            break

        elif retry == "n":
            print("\nThank you for using the program.")
            break

        else:
            print("Please enter 'y' or 'n'.")


def elementary_level():

    print("\nBeginner Level: Basic multiplication (1-digit numbers).")

    multiplication_quiz(1, 10, 1, 10)


def intermediate_level():

    print("\nIntermediate Level: Multiplication with 2-digit numbers.")

    multiplication_quiz(10, 99, 10, 99)


def advanced_level():

    print("\nAdvanced Level: Multiplication with a 3-digit number and a 2-digit number.")

    multiplication_quiz(100, 999, 10, 99)


def select_level():

    print("Select a difficulty level:")
    print("1) Beginner")
    print("2) Intermediate")
    print("3) Advanced")

    while True:
        try:
            level = int(input("Enter level (1–3): "))
            if level in [1, 2, 3]:
                break
            else:
                print("Invalid level. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if level == 1:
        elementary_level()

    elif level == 2:
        intermediate_level()

    else:
        advanced_level()


def welcome():

    print("MENTAL MATH TRAINER")
    print("Practice multiplication with different difficulty levels.")

    select_level()


welcome()