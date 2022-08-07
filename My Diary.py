import textwrap
import os
count = 5
while count != 0:
    pwd = input("Please enter password to access: ")
    if pwd == "your name":
        print("\n===WELCOME TO YOUR OWN DIARY===")
        print("\nHere you can write anything you want, anyway you want, without any interruption whatsoever.")
        print("\nNow, what do you want to do?")
        print("\n*****MAIN MENU*****")
        print("1. Write a new entry")
        print("2. Access a previous entry")
        print("3. Delete a previous entry")
        print("4. Print all entries")
        print("5. Delete all entries")


        def new_entry():
            diary = open("diary.txt", "a")
            diary.write("Your Entry: ")
            entry = input("\nEnter the date and your corresponding entry: ")
            diary.write(entry + '\n')
            diary.write('\n\n')
            diary.close()


        def read_entry():
            diary = open("diary.txt", "r")
            lines = diary.readlines()
            print("\n(Psst. If you cannot remember a certain date or keyword of an entry, "
                  "just type can't remember or don't remember)")
            date = input("\nEnter date of entry you wish to access: ")

            if date == "can't remember" or date == "don't remember":
                key_word = input("\nThat's okay! Enter specific keyword(s) of entry you wish to access: ")
                for line in lines:
                    if key_word in line:
                        output2 = textwrap.fill(line, width=125)
                        print("\n" + output2)
                        break
                else:
                    print("\nSorry, entry not found. Please try again.")
                if key_word == "can't remember" or key_word == "don't remember":
                    print("\nSorry. Entry not found with this keyword. Try again.")

            else:
                for line in lines:
                    if date in line:
                        output = textwrap.fill(line, width=125)
                        print("\n" + output)
                        break
                else:
                    print("\nSorry. Entry not found for this date. Try again!")

            diary.close()


        def del_entry():
            diary = open("diary.txt", "r")
            lines = diary.readlines()
            del_diary = open("diary.txt", "w")
            date = input("\nEnter date of entry you wish to delete: ")
            for line in lines:
                if date not in line.strip():
                    del_diary.write(line)
            print("\nEntry Successfully Deleted.")
            diary.close()


        def all_entry():
            diary = open("diary.txt", "r")
            file_size = os.stat("diary.txt").st_size
            if file_size == 0:
                print("\nNo entries currently present in file. Restart to make a new entry(s)!")
            else:
                lines = diary.readlines()
                for line in lines:
                    output3 = textwrap.fill(line, width=125)
                    print(output3)
            diary.close()


        def clear_entry():
            diary = open("diary.txt", "r+")
            diary.truncate()
            print("\nAll entries successfully deleted. Thank you!")
            diary.close()


        choice = int(input("\nEnter Your Choice: "))
        if choice == 1:
            new_entry()

        elif choice == 2:
            read_entry()

        elif choice == 3:
            del_entry()

        elif choice == 4:
            all_entry()

        elif choice == 5:
            clear_entry()

        break


    elif pwd == "forgot password" or pwd == "forgot":
        print("\nYour password is your name. Try again.")
        break


    else:
        count = count - 1
        if count == 0:
            print("\nWrong password. You are not allowed access to the diary. Please try later.")
        else:
            print("\nWrong password. Access Denied. Try again.")
            print("You have", count, "tries left.")
            print("\n")
