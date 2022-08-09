import textwrap
count = 5
while count != 0:
    pwd = input("Please enter password to access: ")
    if pwd == "your name":
        print("\n===WELCOME TO YOUR OWN DIARY===")
        print("\nHere you can write anything you want, anyway you want, without any interruption whatsoever.")
        print("\nNow, what do you want to do?")
        print("\n*****MAIN MENU*****")
        print("1. Write a new entry(s)")
        print("2. Access a previous entry")
        print("3. Add an entry to a previous date")
        print("4. Delete a previous entry")
        print("5. Print all entries")
        print("6. Delete all entries")


        def new_entry():
            diary = open("diary.txt", "a")
            n = int(input("\nDo you want to make a single entry or more than one (answer in number): "))
            if n > 1:
                for i in range(n):
                    diary.write("\nYour Entry: ")
                    entry = input("\nEnter the date and your corresponding entry: ")
                    diary.write(entry + '\n')

            else:
                diary.write("\nYour Entry: ")
                entry = input("\nEnter the date and your corresponding entry: ")
                diary.write(entry + '\n')
                diary.close()


        def read_entry():
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


        def add_entry():
            diary = open("diary.txt", "r+")
            lines = diary.readlines()
            entries = []
            print("\n(Psst. If you cannot remember a certain date or keyword of an entry, "
                  "just type can't remember or don't remember)")
            date = input("\nEnter date of entry you wish to modify: ")

            if date == "can't remember" or date == "don't remember":
                key_word = input("\nThat's okay! Enter specific keyword(s) of entry you wish to modify: ")
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
                        output3 = textwrap.fill(entries[i], width=125)
                        print(output3)

                    rep1 = "\nEnter the portion of the entry you want to succeed: "
                    mod1 = "\nEnter your successive entry: "

                    if rep1 in entries[-1]:
                        entries.append(mod1)
                    else:
                        for i, line in enumerate(entries):
                            if rep1 in line and mod1 not in entries[i + 1]:
                                entries.insert(i + 1, mod1)
                                break
                    diary.seek(0)
                    diary.writelines(entries)


            else:
                for line in lines:
                    if date in line:
                        entries.append(line)
                    else:
                        continue

                for i in range(len(entries)):
                    output4 = textwrap.fill(entries[i], width=125)
                    print(output4)

                rep2 = input("\nEnter the portion of the entry you want to succeed: ")
                mod2 = input("\nEnter your successive entry: ")

                if mod2 in lines[-1]:
                    lines.append(mod2)

                else:
                    for i, line in enumerate(lines):
                        if rep2 in line and mod2 not in lines[i + 1]:
                            lines.insert(i + 1, mod2)
                            break

                diary.seek(0)
                diary.writelines(lines)


        def del_entry():
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


        def all_entry():
            diary = open("diary.txt", "r")
            lines = diary.readlines()
            for line in lines:
                read = textwrap.fill(line, width=125)
                print(read)


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
            add_entry()

        elif choice == 4:
            del_entry()

        elif choice == 5:
            all_entry()

        elif choice == 6:
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
        else:
            print("\nWrong password. Access Denied. Try again.")
            print("You have", count, "tries left.")
            print("\n")
