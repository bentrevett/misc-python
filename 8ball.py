import random
import time

list = ["Yes, most definitely!", "The chances are high!", "Not likely!", "May the odds be ever in your favor.",
                        "You got no shot, kid.", "Try it out and see!", "23% of working", "99.9% success rate",
                        "Congratulations, yes!", "Ask a probably question", "Ask again later", "Better not tell you now",
           "Cannot predict now", "Concentrate and ask again", "Don't count on it"]

def question():
    print("Ask me a question")
    question=raw_input()
    print("Thinking...")
    time.sleep(1)
    print(random.choice(list))
    again()

def again():
    reply=raw_input("Would you like to ask another question? ")
    if reply.lower()=="yes":
        question()
    
question()
