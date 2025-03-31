questions = [
    {
        "ques":"What is the capital of Tamilnadu",
        "options":["A.Chennai","B.Trichy","C.Madurai"],
        "Ans":"A"
    },
    {
        "ques":"What is the national flower of Tamilnadu",
        "options":["A.Lilly","B.Lotus","C.Jasmine"],
        "Ans":"B"
    },
    {
        "ques":"When did India Got Independence",
        "options":["A.1950","B.1947","C.1951"],
        "Ans":"B"
    },
    {
        "ques":"Which is the Prime number",
        "options":["A.1","B.3","C.2"],
        "Ans":"C"
    },
    {
        "ques":"What is the former name of Tamilnadu",
        "options":["A.Madrasi","B.Chennai","C.Madras"],
        "Ans":"C"
    }
]
def quizgame(questions):
    score=0
    print("WELCOME TO COMPUTER QUIZ GAME")
    name=input("How can I call you-")
    print(f"Hello! {name}.\nAll the best!\n")

    
    for question in questions:
        print(question["ques"])
        for opt in question["options"]:
            print(opt)
        answer=input("Choose your option(A,B,C,D)").upper()
        if answer==question["Ans"]:
            print(f"You are correct.\n")
            score+=1
        else:
            print(f"Oops! The correct answer is {question["Ans"]}.\n")
    print(f"You scored {score} out of 5 questions.\n")
    if score==5:
        print("Hey Champ!All the best for you future.\nThank you for your participation")
    elif score==3 or score==4:
        print("A great score!\nThank you for your participation")
    elif score==2 or score==1:
        print("Nothing to worry!Better luck next time\nThank you for your participation")
    elif score==0:
        print("Let be cool!\nThank you for your participation")
        

game=quizgame(questions)