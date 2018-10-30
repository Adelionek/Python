from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(pytania):
    score = 0
    for question in pytania:
        anwser = input(question.prompt)
        if anwser == question.answer:
            score += 1

    print("Hey, you got " + str(score) + " / " + str(len(pytania)))


run_test(questions)
