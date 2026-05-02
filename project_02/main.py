import json
import random
from pathlib import Path

def load_questions():
    file_path = Path(__file__).parent / "questions.json"
    with open(file_path, "r") as file:
        return json.load(file)["questions"]

def next_question(data):
    return data.pop(random.randint(0, len(data) - 1))

def ask_question(question, q_number):
    q_text = question["question"]
    a_list = question["options"]
    correct_answer = question["answer"]
    ind_answer = a_list.index(correct_answer)

    print(f"Question number {q_number + 1}:")
    print(q_text)
    print("Answers:")
    for i in range(len(a_list)):
        print(f"{i + 1}) {a_list[i]}")

    return ind_answer + 1

questions = load_questions()

def main():
    number_of_corrects = 0
    print("This is a Quizz. Prepare yourself.")
    tot_num_questions = int(input("How many questions would you like? (3-10)"))
    for q in range(tot_num_questions):
        question = next_question(questions)
        answer_number = ask_question(question, q)
        user_answer = input("Choose your answer: ")
        if int(user_answer) == answer_number:
            print("You're correct!")
            number_of_corrects += 1
        else:
            print("Not quite.")

    print(f"Your score is {number_of_corrects}/{tot_num_questions}")

if __name__ == "__main__":
    main()
