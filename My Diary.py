import textwrap             # module-to-display-output-as-paragraph
count = 5                   # number-of-tries-to-guess-password
while count != 0:
    pwd = input("Please enter password to access: ")
    if pwd == "your name":
        print("\n===WELCOME TO YOUR OWN DIARY===")
        print("\nHere you can write anything you want, anyway you want, without any interruption whatsoever.")
        print("\nNow, what do you want to do?")
        print("\n*****MAIN MENU*****")
        print("1. Write a new entry(s)")
        print("2. Access a previous entry")
        print("3. Delete a previous entry")
        print("4. Print all entries")
        print("5. Delete all entries")


        def new_entry():        # function-to-write-new-entries
            num = int(input("\nDo you want to make a single entry or multiple entries: "))
            if num > 1:
                for i in range(num):
                    diary = open("diary.txt", "a")
                    diary.write("\nYour Entry: ")
                    date = input("\nEnter your date: ")
                    entry = input("\nEnter your entry: ")
                    diary.write(date + " - " + entry + "\n")
            else:
                diary = open("diary.txt", "a")
                diary.write("\nYour Entry: ")
                date = input("\nEnter your date: ")
                entry = input("\nEnter your entry: ")
                diary.write(date + " - " + entry + "\n")


        def read_entry():       # function-to-read-a-specific-entry
            diary = open("diary.txt", "r")
            lines = diary.readlines()
            entries = []
            print("\n(Psst. If you cannot remember a certain date or keyword of an entry, "
                  "just type can't remember or don't remember)")
            date = input("\nEnter date of entry you wish to access: ")

            if date == "can't remember" or date == "don't remember":
                key_word = input("\nThat's okay! Enter specific keyword(s) of entry you wish to access: ")
                if key_word == "can't remember" or key_word == "don't remember":
                    print("\nHere are all your entries to alleviate your confusion: ")
                    all_entry()
                else:
                    for line in lines:
                        if key_word in line:
                            entries.append(line)
                        else:
                            continue

                    for i in range(len(entries)):
                        output = textwrap.fill(entries[i], width=125)
                        print(output)

            else:
                for line in lines:
                    if date in line:
                        entries.append(line)
                    else:
                        continue

                for i in range(len(entries)):
                    output2 = textwrap.fill(entries[i], width=125)
                    print(output2)

            diary.close()


        def del_entry():        # function-to-delete-a-specific-entry
            diary = open("diary.txt", "r")
            lines = diary.readlines()
            entries = []
            print("\n(Psst. If you cannot remember a certain date or keyword of an entry, "
                  "just type can't remember or don't remember)")
            date = input("\nEnter date of entry you wish to delete: ")

            if date == "can't remember" or date == "don't remember":
                key_word = input("\nThat's okay! Enter specific keyword(s) of entry you wish to access: ")
                if key_word == "can't remember" or key_word == "don't remember":
                    print("\nHere are all your entries to alleviate your confusion: ")
                    all_entry()
                else:
                    for line in lines:
                        if key_word in line:
                            entries.append(line)
                        else:
                            continue

                    for i in range(len(entries)):
                        output7 = textwrap.fill(entries[i], width=125)
                        print(output7)

                    key_word = input("\nEnter key word(s) of the previous entry that you wish to delete: ")
                    del_diary = open("diary.txt", "w")
                    for line in lines:
                        if key_word not in line.rstrip():
                            del_diary.write(line)
                        else:
                            print("\nEntry Successfully Deleted.")
                    del_diary.close()

            else:
                for line in lines:
                    if date in line:
                        entries.append(line)
                    else:
                        continue

                for i in range(len(entries)):
                    output8 = textwrap.fill(entries[i], width=125)
                    print(output8)

                key_word = input("\nEnter key word(s) of the entry you wish to delete: ")
                del_diary = open("diary.txt", "w")
                for line in lines:
                    if key_word not in line.rstrip():
                        del_diary.write(line)
                    else:
                        print("\nEntry Successfully Deleted.")
                del_diary.close()


        def all_entry():        # function-to-print-all-entries
            diary = open("diary.txt", "r")
            lines = diary.readlines()
            for line in lines:
                read = textwrap.fill(line, width=125)
                print(read)


        def clear_entry():      # function-to-delete-all-entries
            diary = open("diary.txt", "r+")
            diary.truncate()
            print("\nAll entries successfully deleted. Thank you!")
            diary.close()


        choice = int(input("\nEnter Your Choice: "))        # choice-for-main-menu
        if choice == 1:                                     # calling-functions
            new_entry()

        elif choice == 2:
            read_entry()

        elif choice == 3:
            del_entry()

        elif choice == 4:
            all_entry()

        elif choice == 5:
            clear_entry()

        else:
            print("\nSorry. Choice invalid.")

        break


    elif pwd == "forgot password" or pwd == "forgot":
        print("\nYour password is your name. Try again.")
        break


    else:
        count = count - 1
        if count == 0:
            print("\nWrong password. You are not allowed access to the diary. Please try later.")
            print("\nA hint: your password is your name.")
        else:
            print("\nWrong password. Access Denied. Try again.")
            print("You have", count, "tries left.")
            print("\n")
