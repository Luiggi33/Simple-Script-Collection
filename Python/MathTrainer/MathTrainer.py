import requests

def doMathTraining():
    r = requests.get('https://x-math.herokuapp.com/api/random')

    print("Math Question Generator")
    print("\n" + r.json()['expression'])

    uAnswer = input("\nYour Answer: ")
    answer = str(r.json()['answer'])

    if uAnswer == answer:
        print("Correct!")
    else:
        print("Incorrect!")
        print("The correct answer is: " + answer)

    print("\n")

loop = True
while loop:
    doMathTraining()