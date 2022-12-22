#create our nominees for the votining system


nomniee1 = input("Enter the name of the first nominiee: ")
nomniee2 = input("Enter the name of the Second nominiee: ")

nm1_votees = 0
nm2_votees = 0

voters_id = list(range(1,11))

no_ofvoters = len(voters_id)

while True:
    if voters_id ==[]:
        print("All votes has been passed voting session has ended")
        if nm1_votees > nm2_votees:
            percent = (nm1_votees/no_ofvoters)*100
            print(nomniee1, "has won the election with ", percent, "%")
            break

        elif nm2_votees > nm1_votees:
            percent = (nm2_votees/no_ofvoters)*100
            print(nomniee2, "has won the election with ", percent, "%")
            break

        else:
            print("Both has equal votes its a TIE!!")
            break




    voter = int(input("Enter your voter Id: "))
    if voter in voters_id:
        print("Your a voter  ")
        voters_id.remove(voter)
        print("======================================")
        print("To vote for ",nomniee1,"Press 1")
        print("To vote for ",nomniee2,"Press 2")
        print("======================================")

        vote = int(input("Enter your vote: "))
        if vote == 1:
            nm1_votees+=1
            print(nomniee1, "Thanks you for considering him worth of your vote")
        elif vote ==2:
            nm2_votees+=1
            print(nomniee1, "Thanks you for considering him worth of your vote")
        elif vote > 2:
            print("Check your pressed key!!")

        else:
            print("You're not eligible to vote OR your vote has already been passed !!!")