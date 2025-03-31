# Quiz_game
Welcome to the Computer Quiz Game project! This is a simple Python-based quiz game where users can test their knowledge by answering multiple-choice questions.
Features:
•	Multiple-choice quiz questions with predefined options.
•	Scoring system based on correct answers.
•	Personalized greeting and feedback based on performance.
How It Works:
1.	The game starts with a greeting and asks for your name.
2.	It then presents a series of multiple-choice questions.
3.	You choose an option (A, B, or C).
4.	After each answer, the game tells you whether you're correct or not.
5.	At the end, the game displays your score and gives personalized feedback based on your performance.
Technologies Used:
•	Python (Programming Language)
Code Structure:
1.	Quiz Questions: The quiz questions are stored in a list of dictionaries, where each dictionary contains:
o	ques: The question text.
o	options: The possible answers.
o	Ans: The correct answer.
2.	quizgame() Function: This function runs the entire quiz:
o	Greets the user.
o	Loops through the questions and options.
o	Accepts user input and checks it against the correct answer.
o	Scores the user and provides feedback at the end.
