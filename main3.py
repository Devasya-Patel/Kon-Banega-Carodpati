ques = [  [ '\n1. Which language P using ?' , 'Python' , 'HTML' , 'MERN'
               , 'SQL'] , 

               [ '\n2. Which language H using ?' , 'HTML' , 'Python' ,  'MERN'
               , 'SQL'] ,

               [ '\n3. Which language M using ?' , 'HTML' , 'MERN'
               ,'Python' , 'SQL'] ,

               [ '\n4. Which language I S using ?' , 'HTML' , 'MERN'
               , 'SQL', 'Python' ] 
            ]
levels = [1000,2000,3000,5000,10000,20000,50000,1200000,3200000]
a=0 
while True : 
    # options = [ques[a][1] ,ques[a][2] ,ques[a][3] ,ques[a][4] ] 
    questions = ques[a][0]
    print(questions , "\n" ,ques[a][1] ,ques[a][2] ,ques[a][3] ,ques[a][4] )
    ans_no = input("Enter your choice : ")

    if ans_no == 'a':
        ans_no = ques[a][1]
    elif ans_no == 'b':
        ans_no = ques[a][2]
    elif ans_no == 'c':
        ans_no = ques[a][3]
    elif ans_no == 'd':
        ans_no = ques[a][4]

    # level 1
    if a == 0 :
        jayu = ques[a][1]
        if jayu == ans_no :
            print("Correct answer")
            print(f"you take Rs. {levels[0] }")

        else:
            print("Wrong answer ")
            break

    elif a == 1 :
        jayu = ques[a][1]
        if jayu == ans_no :
            print("Correct answer")
            print(f"you take Rs. {levels[1] }")

        else:
            print("Wrong answer ")
            break

    elif a == 2 :
        jayu = ques[a][2]
        if jayu == ans_no :
            print("Correct answer")
            print(f"you take Rs. {levels[2] }")

        else:
            print("Wrong answer ")
            break

    elif a == 3 :
        jayu = ques[a][3]
        if jayu == ans_no :
            print("Correct answer")
            print(f"you take Rs. {levels[3] }")

        else:
            print("Wrong answer ")
            break

    if a == 3:
        break

    a+=1


print("Thanks for playing")


