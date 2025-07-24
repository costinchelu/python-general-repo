from data import question_bank
from quiz_brain import QuizBrain
from ui import QuizzInterface


quiz = QuizBrain(question_bank)
quiz_ui = QuizzInterface(quiz)