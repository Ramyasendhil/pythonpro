def sports():
    print("==========================================")
    print("         SPORTS                           ")
    print("==========================================")
    print(int(input("enter the phone number :")))
    print(str(input("address of customer :")))
    print("\t\t\t 1.football\n\t\t\t 2.handball\n\t\t\t 3.basketball\n\t\t\t 4.tennies ball")
    choice=str(input("enter your choice : "))
    if(choice=="football"):
        print("\t\t\t1.small\n\t\t\t2.meidium\n\t\t\t3.large")
        size=str(input("enter the size of football:"))
        if(size=="small"):
            stock=40
            cost=350
            need=int(input("enter the need of small size football :"))
            remaining_balance = stock = need
            print("cost of single piece=",cost)
            print("cost of the football=",need*cost)
            print("remaining_balnce=",remaining_balance)
            print("if you want to chack more sports of ours")
            print("\t\t 'yes'\n\n\t\t 'no'")
            question=input("enter 'yes'or 'no'")
            if(question=="yes"):
                sports()
            elif(question=="no"):
                print("===================================================================")
                print("thank you so much for your order :i hope you enjoy with our product  ")
                print("===================================================================")
        if(size=="medium"):
            stock=45
            cost=780
            need=int(input("enter the need of mwdium size football :"))
            remaining_balance = stock = need
            print("cost of single piece=",cost)
            print("cost of the football=",need*cost)
            print("remaining_balnce=",remaining_balance)
            print("if you want to chack more sports of ours")
            print("\t\t 'yes'\n\n\t\t 'no'")
            question=input("enter 'yes'or 'no'")
            if(question=="yes"):
                sports()
            elif(question=="no"):
                print("===================================================================")
                print("thank you so much for your order :i hope you enjoy with our product  ")
                print("===================================================================")
        if(size=="large"):
            stock=43
            cost=320
            need=int(input("enter the need of large size football :"))
            remaining_balance = stock = need
            print("cost of single piece=",cost)
            print("cost of the football=",need*cost)
            print("remaining_balnce=",remaining_balance)
            print("if you want to chack more sports of ours")
            print("\t\t 'yes'\n\n\t\t 'no'")
            question=input("enter 'yes'or 'no'")
            if(question=="yes"):
                sports()
            elif(question=="no"):
                print("===================================================================")
                print("thank you so much for your order :i hope you enjoy with our product  ")
                print("===================================================================")
    if(choice=="handball"):
        print("\t\t\t 1.small\n\t\t 2.meidium\n\t\t 3.large")
        size=str(input("enter the size of handball:"))
        if(size=="small"):
            stock=67
            cost=450
            need=int(input("enter the need of small size handball :"))
            remaining_balance = stock = need
            print("cost of single piece=",cost)
            print("cost of the handball=",need*cost)
            print("remaining_balnce=",remaining_balance)
            print("if you want to chack more sports of ours")
            print("\t\t 'yes'\n\n\t\t 'no'")
            question=input("enter 'yes'or 'no'")
            if(question=="yes"):
                sports()
            elif(question=="no"):
                print("===================================================================")
                print("thank you so much for your order :i hope you enjoy with our product  ")
                print("===================================================================")
        if(size=="medium"):
            stock=89
            cost=390
            need=int(input("enter the need of medium size handball :"))
            remaining_balance = stock = need
            print("cost of single piece=",cost)
            print("cost of the handball=",need*cost)
            print("remaining_balnce=",remaining_balance)
            print("if you want to chack more sports of ours")
            print("\t\t 'yes'\n\n\t\t 'no'")
            question=input("enter 'yes'or 'no'")
            if(question=="yes"):
                sports()
            elif(question=="no"):
                print("===================================================================")
                print("thank you so much for your order :i hope you enjoy with our product  ")
                print("===================================================================")
        if(size=="large"):
            stock=45
            cost=789
            need=int(input("enter the need of large size handball :"))
            remaining_balance = stock = need
            print("cost of single piece=",cost)
            print("cost of the handball=",need*cost)
            print("remaining_balnce=",remaining_balance)
            print("if you want to chack more sports of ours")
            print("\t\t 'yes'\n\n\t\t 'no'")
            question=input("enter 'yes'or 'no'")
            if(question=="yes"):
                sports()
            elif(question=="no"):
                print("===================================================================")
                print("thank you so much for your order :i hope you enjoy with our product  ")
                print("===================================================================")
    if(choice=="basketball"):
        print("\t\t\t1.small\n\t\t\t2.meidium\n\t\t\t3.large")
        size=str(input("enter the size of basketball:"))
        if(size=="small"):
            stock=87
            cost=876
            need=int(input("enter the need of small size basketball :"))
            remaining_balance = stock = need
            print("cost of single piece=",cost)
            print("cost of the basketball=",need*cost)
            print("remaining_balnce=",remaining_balance)
            print("if you want to chack more sports of ours")
            print("\t\t 'yes'\n\n\t\t 'no'")
            question=input("enter 'yes'or 'no'")
            if(question=="yes"):
                sports()
            elif(question=="no"):
                print("===================================================================")
                print("thank you so much for your order :i hope you enjoy with our product  ")
                print("===================================================================")
        if(size=="medium"):
            stock=40
            cost=370
            need=int(input("enter the need of mwdium size basketball :"))
            remaining_balance = stock = need
            print("cost of single piece=",cost)
            print("cost of the basketball=",need*cost)
            print("remaining_balnce=",remaining_balance)
            print("if you want to chack more sports of ours")
            print("\t\t 'yes'\n\n\t\t 'no'")
            question=input("enter 'yes'or 'no'")
            if(question=="yes"):
                sports()
            elif(question=="no"):
                print("===================================================================")
                print("thank you so much for your order :i hope you enjoy with our product  ")
                print("===================================================================")
        if(size=="large"):
            stock=42
            cost=390
            need=int(input("enter the need of large size basketball :"))
            remaining_balance = stock = need
            print("cost of single piece=",cost)
            print("cost of the basketball=",need*cost)
            print("remaining_balnce=",remaining_balance)
            print("if you want to chack more sports of ours")
            print("\t\t 'yes'\n\n\t\t 'no'")
            question=input("enter 'yes'or 'no'")
            if(question=="yes"):
                sports()
            elif(question=="no"):
                print("===================================================================")
                print("thank you so much for your order :i hope you enjoy with our product  ")
                print("===================================================================")
    if(choice=="tennies ball"):
        print("\t\t\t1.small\n\t\t\t2.meidium\n\t\t\t3.large")
        size=str(input("enter the size of tennies ball:"))
        if(size=="small"):
            stock=23
            cost=100
            need=int(input("enter the need of small size tennies ball :"))
            remaining_balance = stock = need
            print("cost of single piece=",cost)
            print("cost of the tennies ball=",need*cost)
            print("remaining_balnce=",remaining_balance)
            print("if you want to chack more sports of ours")
            print("\t\t 'yes'\n\n\t\t 'no'")
            question=input("enter 'yes'or 'no'")
            if(question=="yes"):
                sports()
            elif(question=="no"):
                print("===================================================================")
                print("thank you so much for your order :i hope you enjoy with our product  ")
                print("===================================================================")
        if(size=="medium"):
            stock=30
            cost=80
            need=int(input("enter the need of medium size tennies ball :"))
            remaining_balance = stock = need
            print("cost of single piece=",cost)
            print("cost of the tennies ball=",need*cost)
            print("remaining_balnce=",remaining_balance)
            print("if you want to chack more sports of ours")
            print("\t\t 'yes'\n\n\t\t 'no'")
            question=input("enter 'yes'or 'no'")
            if(question=="yes"):
                sports()
            elif(question=="no"):
                print("===================================================================")
                print("thank you so much for your order :i hope you enjoy with our product  ")
                print("===================================================================")
        if(size=="large"):
            stock=40
            cost=120
            need=int(input("enter the need of large size tennies ball:"))
            remaining_balance = stock = need
            print("cost of single piece=",cost)
            print("cost of the tennies ball =",need*cost)
            print("remaining_balnce=",remaining_balance)
            print("if you want to chack more sports of ours")
            print("\t\t 'yes'\n\n\t\t 'no'")
            question=input("enter 'yes'or 'no'")
            if(question=="yes"):
                sports()
            elif(question=="no"):
                print("===================================================================")
                print("thank you so much for your order :i hope you enjoy with our product  ")
                print("===================================================================")
                

                
sports()


