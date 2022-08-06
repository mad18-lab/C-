import textwrap
import os
print("===WELCOME TO YOUR OWN DIARY===")
print("\nHere you can write anything you want, anyway you want, without interruption.")
print("\nNow, what do you want to do?")
print("\n=====MAIN MENU=====")
print("1. Write a new entry")
print("2. Access a previous entry")
print("3. Delete a previous entry")
print("4. Print all entries")
print("5. Delete all entries")
choice = int(input("\nEnter Your Choice: "))

if choice == 1:
    diary = open("diary.txt", "a")
    diary.write("Your Entry: ")
    entry = input("Enter date in DD/MM/YYYY and your entry: ")
    diary.write(entry+'\n')
    diary.write('\n\n')
    diary.close()


elif choice == 2:
    diary = open("diary.txt", "r")
    date = input("Enter date of entry you wish to access in DD/MM/YYYY: ")
    lines = diary.readlines()

    for line in lines:
        if date in line:
            output = textwrap.fill(line, width=125)
            print(output)

    diary.close()


elif choice == 3:
    diary = open("diary.txt", "r")
    lines = diary.readlines()
    del_diary = open("diary.txt", "w")
    date = input("Enter date of entry you wish to delete: ")
    for line in lines:
        if date not in line.strip():
            del_diary.write(line)
    print("Entry Successfully Deleted.")


elif choice == 4:
    diary = open("diary.txt", "r")
    file_size = os.stat("diary.txt").st_size
    if file_size == 0:
        print("No entries present in file. Restart to make a new entry(s)!")
    else:
        print(diary.read())
    diary.close()


elif choice == 5:
    diary = open("diary.txt", "r+")
    diary.truncate()
    print("All entries successfully deleted. Thank you!")
    diary.close()
