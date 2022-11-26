questions = ['what is the full form of DBMS ?','Who is the founder gec ?','What is the easy language in programming ?']
answers = ['Data base management system','Seshadri rao','Python']
options = [ ['Data biller management sys','Data basic management system','Data base management system','Dealing base management system'],['chintu','Seshadri rao','Hitesh','Jaswanth'],['Java','Python','C','R']]
def play_game(username,questions,options,answers):
    score = 0
    print("Hello "+username+" to enter into the KBC game")
    for i in range(len(questions)):
        current_question = questions[i]
        current_answers = answers[i]
        current_option = options[i]
        print(i+1,"Question:\n",current_question)
        for index,each_option in enumerate(current_option):
            print(index+1,") ",each_option,sep='')
        user_answer_index= int(input("Enter your options numbers : "))
        user_answer=current_option[user_answer_index-1]
        if user_answer == current_answers:
            print("Right answer")
            score+=100
        else:
            print("Wrong answer")
            break
    print("Your final score is :",score)
    return username,score
def view_score(names_score):
    for names,score in names_score.items():
        print(names,"has scored ",score)
    

def kbc(questions,options,answers):
    names_score={}
    while True:
        print("Welcome to the kbc game")
        print("1) Play Game\n2) View Score\n3) Exit")
        choice=int(input("Enter your choice : "))
        if choice == 1:
            username=input("Enter your name : ")
            username,score=play_game(username,questions,options,answers)
            names_score[username] = score
        elif choice == 2:
            view_score(names_score)
        elif choice == 3:
            break
        else:
            print("Please enter correct number")
kbc(questions,options,answers)