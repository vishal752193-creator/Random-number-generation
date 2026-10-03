import random
import streamlit as st

st.title(" NUMBER GUESSING GAME")

# Difficulty
difficulty = st.selectbox(
    "Choose Difficulty",
    [
        "Easy (1-50, 10 chances)",
        "Medium (1-100, 7 chances)",
        "Hard (1-500, 8 chances)"
    ]
)

# Difficulty settings
if difficulty.startswith("Easy"):
    max_number = 50
    max_chances = 10

elif difficulty.startswith("Medium"):
    max_number = 100
    max_chances = 7

else:
    max_number = 500
    max_chances = 8


# Initialize game
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, max_number)
    st.session_state.chances = max_chances
    st.session_state.attempt = 1
    st.session_state.score = 100
    st.session_state.game_over = False
    st.session_state.difficulty = difficulty
    st.session_state.message = ""


# Reset when difficulty changes
if st.session_state.difficulty != difficulty:
    st.session_state.secret_number = random.randint(1, max_number)
    st.session_state.chances = max_chances
    st.session_state.attempt = 1
    st.session_state.score = 100
    st.session_state.game_over = False
    st.session_state.difficulty = difficulty
    st.session_state.message = ""


# Game information
st.write("Number is between 1 and", max_number)
st.write("Chances remaining:", st.session_state.chances)
st.write("Score:", st.session_state.score)


# Show previous hint
if st.session_state.message:
    if st.session_state.message == "low":
        st.warning("TOO LOW! Try a HIGHER number.")

    elif st.session_state.message == "high":
        st.warning("TOO HIGH! Try a LOWER number.")


# Main game
if not st.session_state.game_over:

    guess = st.number_input(
        "Enter your guess",
        min_value=1,
        max_value=max_number,
        step=1
    )

    if st.button(" Submit Guess"):

        # Correct guess
        if guess == st.session_state.secret_number:

            bonus = (st.session_state.chances - 1) * 10

            st.session_state.score += bonus
            st.session_state.game_over = True
            st.session_state.message = ""

            st.success(" CONGRATULATIONS!")

            st.write(
                "You guessed the number in",
                st.session_state.attempt,
                "attempts."
            )

            st.write(
                "Your Final Score:",
                st.session_state.score
            )

        # Wrong guess
        else:

            st.session_state.chances -= 1
            st.session_state.score -= 10

            # Guess is too low
            if guess < st.session_state.secret_number:
                st.session_state.message = "low"

            # Guess is too high
            else:
                st.session_state.message = "high"


            # Game over
            if st.session_state.chances <= 0:

                st.session_state.game_over = True
                st.session_state.message = ""

                st.error(" GAME OVER")

                st.write(
                    "The correct number was:",
                    st.session_state.secret_number
                )

                st.write(
                    "Your Final Score:",
                    st.session_state.score
                )

            else:

                st.session_state.attempt += 1

                # Refresh screen
                st.rerun()


# New Game
if st.session_state.game_over:

    if st.button(" New Game"):

        st.session_state.secret_number = random.randint(
            1,
            max_number
        )

        st.session_state.chances = max_chances
        st.session_state.attempt = 1
        st.session_state.score = 100
        st.session_state.game_over = False
        st.session_state.difficulty = difficulty
        st.session_state.message = ""

        st.rerun()