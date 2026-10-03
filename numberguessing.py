import random

print("=" * 40)
print("  NUMBER GUESSING GAME")
print("=" * 40)

print("\nChoose Difficulty:")
print("1. Easy   (1-50, 10 chances)")
print("2. Medium (1-100, 7 chances)")
print("3. Hard   (1-500, 8 chances)")

choice = input("\nEnter your choice (1/2/3): ")

if choice == "1":
    max_number = 50
    chances = 10
elif choice == "2":
    max_number = 100
    chances = 7
elif choice == "3":
    max_number = 500
    chances = 8
else:
    print("Invalid choice! Medium difficulty selected.")
    max_number = 100
    chances = 7

secret_number = random.randint(1, max_number)

print(f"\nI have selected a number between 1 and {max_number}.")
print(f"You have {chances} chances to guess it.")
print("Let's start! \n")

score = 100

for attempt in range(1, chances + 1):

    try:
        guess = int(input(f"Attempt {attempt}/{chances} - Enter your guess: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    if guess < 1 or guess > max_number:
        print(f" Enter a number between 1 and {max_number}.")
        continue

    if guess == secret_number:
        bonus = (chances - attempt) * 10
        score += bonus

        print("\n CONGRATULATIONS!")
        print(f"You guessed the number in {attempt} attempts.")
        print(f" Your Score: {score}")
        break

    elif guess < secret_number:
        print(" Too low! Try a higher number.")
    else:
        print(" Too high! Try a lower number.")

    score -= 10

else:
    print("\n GAME OVER!")
    print(f"The correct number was: {secret_number}")
    print("Better luck next time! ")

print("\n" + "=" * 40)
print("          THANK YOU FOR PLAYING")
print("=" * 40)
