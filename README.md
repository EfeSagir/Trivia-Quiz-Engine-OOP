# Trivia Quiz Engine (OOP) 🧠

This is a dynamic, text-based quiz application that demonstrates advanced **Object-Oriented Programming (OOP)** and **Data Parsing** in Python. The system takes raw, nested dictionary data (JSON style) and transforms it into a functional, interactive trivia game.

## 🚀 Key Features

- **Data-to-Object Modeling**: Automatically converts raw data from `data.py` into a collection of `Question` objects.
- **Centralized Logic (The Engine)**: The `QuizBrain` class manages the entire game state, including question numbering, user input validation, and checking if questions remain.
- **Encapsulation**: Each component (Data, Model, Brain) is strictly separated, making the code maintainable and scalable.
- **Real-time Feedback**: Provides immediate scoring and reveals the correct answer upon incorrect guesses.

## 🛠️ Project Structure

- `main.py`: The entry point that initializes the engine and runs the game loop.
- `quiz_brain.py`: The core logic "engine" that controls the flow of the quiz.
- `question_model.py`: Defines the `Question` class blueprint.
- `data.py`: Contains a large set of trivia questions in a complex dictionary format.

## 🎮 How to Play

1.  Clone the repository.
2.  Run the application:
    ```bash
    python main.py
    ```
3.  Answer the questions with `True` or `False`.
4.  See your final score at the end of the session!

---

_Developed as part of the 100 Days of Code: The Complete Python Pro Bootcamp._
