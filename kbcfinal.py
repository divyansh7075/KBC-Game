import time
print("\n\033[1mAPKA PAHELA PRASHNA 1000₹ KE LIYE YE RHAA\033[0m\n")
time.sleep(1)
print("प्रश्न १ who is the current prime minister of India \n A. Narendra Modi  \n B.Amit yadav \n C.Rahul Gandhi.      D. Akhilesh Yadav")
Answer= input("उत्तर। if you need helpline press 'E' or 'e'")
if (Answer=="A" or Answer== "a"):
    print("\033[34m Your Answer is correct YOU WON 1000₹\033[0m")
    #lifelines
elif(Answer=="e" or Answer==" E"):
    print("\033[32m YOU HAVE THREE LIFELINES \n 1}50:50 \n2} Audience Poll \n3} Chat with Friend\033[0m")  
    Lifeline=int(input("CHOOSE YOUR LIFELINE: "))
    #lifeline1  
    if(Lifeline== 1):
        time.sleep(1)
        print("\033[1m\033[30mAPKE 2 GALAT ANSWER MIT GAYE HAI\033[0m")
        time.sleep(1)
        print("प्रश्न १ who is the current prime minister of India \n A. Narendra Modi     \nB.Amit yadav")
        Answers=(input("Answer: "))
        time.sleep(1)
        if(Answers=='A'or Answers== 'a'):
            print("\033[34m Your Answer is correct YOU WON 1000₹\033[0m")
        else:
            print("\033[31m Your answer is wrong and YOUR ARE OUT OF THE CONTEST\033[0m")    
            exit()
            
     #lifeline2      
    elif(Lifeline==2):
        print("AUDIENCE POLL 📊📊")
        print("प्रश्न १ who is the current prime minister of India \nA. Narendra Modi (80%)   \nB.Amit yadav(2%) \nC.Rahul Gandhi. (10%)   \nD. Akhilesh Yadav(8%)")   
        Answers=(input("Answer: "))
        time.sleep(1)
        if(Answers=='A'or Answers== 'a'):
            print("\033[34m Your Answer is correct YOU WON 1000₹\033[0m")
        else:
            print("\033[31m Your answer is wrong and YOUR ARE OUT OF THE CONTEST\033[0m")    
            exit()
    #lifeline3        
    elif(Lifeline==3):
        print("\033[1m Chat with friend\033[0m")
        time.sleep(1)
        print("\033[32m CONNECTING....\033[0m")
        time.sleep(1)
        print("\033[44m Displaying Question to your Friend\033[0m")
        time.sleep(1)
        print("Freind's Answer is A 'Narendra Modi'") 
        time.sleep(1)
        your_answer=(input("Answer: "))
        if(your_answer=="A"or your_answer=="a"):
            print("\033[34m Your Answer is correct YOU WON 1000₹\033[0m")
        else:
            print("\033[31m Your answer is wrong and YOUR ARE OUT OF THE CONTEST\033[0m")    
            exit()  
else:
    print ("Your Answer is Wrong , \033 YOU ARE OUT OF THE  CONTEST \033")
    exit()
# Questions 2
print("\n\033[1mAPKA DUSRA PRASHNA 2000₹ KE LIYE YE RHAA\033[0m\n")
print ("QUESTION 2. What is the name of the famous Indian mathematician who made significant contributions to number theory?\n(A) Ramanujan \n(B) Aryabhata\n(C) Brahmagupta\n(D) Bhaskaracharya")
Answer= input("उत्तर। if you need helpline press 'E' or 'e'")
if (Answer=="A" or Answer== "a"):
    print("\033[34m Your Answer is correct YOU WON 2000₹\033[0m")
    #lifelines
elif(Answer=="e" or Answer==" E"):
    print("\033[32m YOU HAVE THREE LIFELINES \n 1}50:50 \n2} Audience Poll \n3} Chat with Friend\033[0m")  
    Lifeline=int(input("CHOOSE YOUR LIFELINE: "))
    #lifeline1  
    if(Lifeline== 1):
        time.sleep(1)
        print("\033[1m\033[30mAPKE 2 GALAT ANSWER MIT GAYE HAI\033[0m")
        time.sleep(1)
        print("What is the name of the famous Indian mathematician who made significant contributions to number theory?\n(A) Ramanujan \n(B) Aryabhata")
        Answers=(input("Answer: "))
        time.sleep(1)
        if(Answers=='A'or Answers== 'a'):
            print("\033[34m Your Answer is correct YOU WON 2000₹\033[0m")
        else:
            print("\033[31m Your answer is wrong and YOUR ARE OUT OF THE CONTEST\033[0m")    
            exit()
            
     #lifeline2      
    elif(Lifeline==2):
        print("AUDIENCE POLL 📊📊")
        print("QUESTION 2. What is the name of the famous Indian mathematician who made significant contributions to number theory?\n(A) Ramanujan(60%) \n(B) Aryabhata(18%)\n(C) Brahmagupta(12%)\n(D) Bhaskaracharya(10%)")
        Answers=(input("Answer: "))
        time.sleep(1)
        if(Answers=='A'or Answers== 'a'):
            print("\033[34m Your Answer is correct YOU WON 2000₹\033[0m")
        else:
            print("\033[31m Your answer is wrong and YOUR ARE OUT OF THE CONTEST\033[0m")    
            exit()
    #lifeline3        
    elif(Lifeline==3):
        print("\033[1m Chat with friend\033[0m")
        time.sleep(1)
        print("\033[32m CONNECTING....\033[0m")
        time.sleep(1)
        print("\033[44m Displaying Question to your Friend\033[0m")
        time.sleep(1)
        print("Freind's Answer is A 'Ramanajun'") 
        time.sleep(1)
        your_answer=(input("Answer: "))
        if(your_answer=="A"or your_answer=="a"):
            print("\033[34m Your Answer is correct YOU WON 2000₹\033[0m")
        else:
            print("\033[31m Your answer is wrong and YOUR ARE OUT OF THE CONTEST\033[0m")    
            exit()  
else:
    print ("Your Answer is Wrong , \033 YOU ARE OUT OF THE  CONTEST \033")
    exit()