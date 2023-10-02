# from functions import lis_todo,write_lis
import functions
import time

now=time.strftime("%d-%b-%Y %H:%M:%S")
print("It is",now)
while True:
    print("what you want add or show or edit or or remove or exit:")
    user_act=input("enter your choice: ")
    user_act=user_act.strip()

    
    if user_act.startswith("add"):
        ad=user_act[4:]+"\n"

        lis=functions.lis_todo("lis.txt")

        lis.append(ad)

        functions.write_lis("lisi.txt",lis)

    elif user_act.startswith("show"):
        
        lis=functions.lis_todo("lis.txt")

        new_lis=[item.strip("\n") for item in lis]

        for index,a in enumerate(new_lis):
            print(f"{index+1}-{a}")

    elif user_act.startswith("exit"):
        break

    elif user_act.startswith("edit"):
        try:
            number=int(user_act[5:])
            number-=1

            lis=functions.lis_todo("lis.txt")

            todo=input("enter the item: ")
            lis[number]=todo+"\n"

            functions.write_lis("lis.txt",lis)
        except ValueError:
            print("you entered invalid command")

    elif user_act.startswith("remove"):
        try:
            lis=functions.lis_todo("lis.txt")

            number=int(user_act[7:])
            index=number-1

            lis_to_remove=lis[index].strip("\n")
            message=f"removed item is {lis_to_remove}"
            print(message)
            
            lis.pop(index)

            functions.write_lis("lis.txt",lis)
        except ValueError:
            print("tou entered an invalid command")
        except IndexError:
            print("Yor index value is high")
    else:
        print("you entered an unknown command")
print("bye!")