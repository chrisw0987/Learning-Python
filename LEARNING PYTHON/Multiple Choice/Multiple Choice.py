from Question import Question

question_prompts = [
    "What is the multiply symbol in math? \n(a) * \n(b) + \n(c) - \n",
    "What color are Bananas? \n(a) Teal \n(b) Magenta \n(c) Yellow \n",
    "The human arm is comprised of? \n(a) Quadraceps \n(b) Bicep/Tricep \n(c) Latissimus Dorsi \n"
]

questions =[
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You Got " + str(score) + "/" + str(len(questions)) + " correct!")

run_test(questions)