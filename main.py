from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from quiz_categories import QuizCategories
question_bank = []
category_does_not_exist = True
quiz_categories = QuizCategories()

categories = quiz_categories.get_quiz_categories()

while category_does_not_exist:
    categories = quiz_categories.get_quiz_categories()
    selected_category = input(f"Pick a quiz category. {categories}: ")
    questions = quiz_categories.get_questions(selected_category)
    if questions:
        category_does_not_exist = False

for question in questions:
    text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")