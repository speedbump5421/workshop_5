import random
# Task 1
'''    

def guess_random_number(tries, start, stop):
    target_number = random.randint(start, stop)

    while tries > 0:
        print(f"You have {tries} tries remaining.")

        try:
            guess = int(input(f"Guess a number between {start} and {stop}: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess == target_number:
            print(
                f"Congratulations! You guessed the correct number: {target_number}")
            return
        elif guess < target_number:
            print("Guess higher!")
        else:
            print("Guess lower!")

        tries -= 1

    print(f"Sorry, you're out of tries. The number was {target_number}.")


if __name__ == "__main__":
   # guess_random_number(tries=5, start=0, stop=10)
    # Task 1

 '''


# Task 2
'''

def guess_random_num_linear(tries, start, stop):
    target_number = random.randint(start, stop)
    print(f"The target number is {target_number}")

    for guess in range(start, stop + 1):
        print(f"Computer guesses: {guess}")

        tries -= 1

        if guess == target_number:
            print(
                f"Success! The computer guessed the correct number: {target_number}")
            return

        if tries == 0:
            print(
                f"Failure! The computer ran out of tries. The correct number was {target_number}.")
            return


if __name__ == "__main__":
    guess_random_num_linear(tries=5, start=0, stop=10)

    Task 2
    '''


# Task 3


def guess_random_num_binary(tries, start, stop):
    target_number = random.randint(start, stop)
    print(f"The target number is {target_number}")

    low = start
    high = stop

    while tries > 0:
        guess = (low + high) // 2
        print(f"Computer guesses: {guess}")

        tries -= 1

        if guess == target_number:
            print(
                f"Success! The computer guessed the correct number: {target_number}")
            return

        elif guess < target_number:
            print("Guess higher!")
            low = guess + 1

        else:
            print("Guess lower!")
            high = guess - 1

        if tries == 0:
            print(
                f"Failure! The computer ran out of tries. The correct number was {target_number}.")
            return


if __name__ == "__main__":

    guess_random_num_binary(tries=5, start=0, stop=100)
