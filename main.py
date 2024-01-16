import os
from post import session


def PrintArt(artName: str):
    if artName == "Logo":
        print("\n\n\n\n\n\n\n--------------------------------------------------------")
        print("|                _          _____           _          |")
        print("|     /\        | |        |_   _|         | |         |")
        print("|    /  \  _   _| |_ ___     | |  _ __  ___| |_ __ _   |")
        print("|   / /\ \| | | | __/ _ \    | | | '_ \/ __| __/ _` |  |")
        print("|  / ____ \ |_| | || (_) |  _| |_| | | \__ \ || (_| |  |")
        print("| /_/    \_\__,_|\__\___/  |_____|_| |_|___/\__\__,_|  |")
        print("--------------------------------------------------------\n")

    elif artName == "Bye":
        print("\n\n\n\n\n--------------------------------------------------------")
        print("|   _____                           /\//\/|            |")
        print("|  / ____|                         |/\//\/             |")
        print("| | (___   ___  ___   _   _  __ _                      |")
        print("|  \___ \ / _ \/ _ \ | | | |/ _` |                     |")
        print("|  ____) |  __/  __/ | |_| | (_| |                     |")
        print("| |_____/ \___|\___|  \__, |\__,_|                     |")
        print("|                      __/ |                           |")
        print("                     |___ /                            |")
        print("--------------------------------------------------------\n")


#iniciando
if __name__ == "__main__":
    PrintArt("Logo")
    print("\nWELCOME!!!\n\nPlease, log in with your instagram account\n")
    
    login = session()
    
    while(True):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("|------------------------|")
        print("|        MAIN MENU       |")
        print("|------------------------|")
        
        id = login.cl.user_id
        print("Hello {}!  =)".format(login.cl.user_info(id).full_name))
        
        
        print("\n\n Select an option: \n1) Basic Post \n2) Schedule Post \n3) Exit")
        option = input()
        
        #basic ost
        if(option == "1"):
            login.imageUpload(login.postBuilder())

        #schedule post
        elif(option == "2"):
            login.SchedulePost(login.postBuilder())

        #exit
        elif(option == "3"):
            PrintArt("Bye")
            break
        