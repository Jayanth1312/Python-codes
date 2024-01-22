import json
from difflib import get_close_matches
from typing import List


# load the data from the JSON file (knowledge.json)
def load_data(filename: str) -> dict:
    with open(filename, 'r') as file:
        data: dict = json.load(file)
    return data


# Dumping the data into the JSON file (knowledge.json)
def saving_knowledge(filename: str, data: dict):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)


# Finds the best match for the user question with the accuracy of upto 80% from the JSON file
def find_best_matches(user_question: str, questions: List[str]) -> str:
    matches: List[str] = get_close_matches(user_question, questions, n=1, cutoff=0.8)
    return matches[0] if matches else None


# Answers the question, which is present in the JSON file
def answer_from_question(user_question: str, knowledge: dict) -> str:
    return next(
        (
            q["answer"]
            for q in knowledge["questions"]
            if q["question"] == user_question
        ),
        None,
    )


# Takes input from the user and answers the question from the database JSON file
def ChatBot():
    knowledge: dict = load_data('knowledge.json')

    while True:
        user_question: str = input("You: ")
        if user_question == 'quit':
            break
        if best_match := find_best_matches(
                user_question, [q["question"] for q in knowledge["questions"]]
        ):
            print(f'Bot: {answer_from_question(best_match, knowledge)}')
        else:
            print("Bot: I dont know the answer. Can you teach me??: ")
            new_answer: str = input("Teach the bot: ")

            if new_answer != 'skip':
                knowledge["questions"].append({"question": user_question, "answer": new_answer})
                saving_knowledge('knowledge.json', knowledge)
                print("Bot: Thank you for teaching me!")


# The Main Function
if __name__ == '__main__':
    ChatBot()
