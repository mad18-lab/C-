print("WELCOME TO INDIGO THEATRES!", "\n")

movies = ["Licorice Pizza", "Top Gun: Maverick", "The Batman", "RRR", "Brahmastra: Part One - Shiva"]
print("Now Showing: ")
for i in movies:
    print(i)

movie = input("\nEnter the movie you want to watch. You can either enter the numeric choice or the name of the movie: ")

if movie == movies[0] or movie == "licorice pizza" or movie == "Licorice pizza" or movie == "1":
    print("\nThank you for choosing", movies[0], "as your movie!")
    time_lp = {
        "2:50 PM": "Audi 2",
        "4:20 PM": "Audi 1"
    }
    print("\nTimings for", movies[0], ": ")
    for x, y in time_lp.items():
        print(x, y)
    time = input("\nEnter your preferred timings in proper format (with AM/PM): ")
    num = int(input("How many seats would you like? "))
    seats = ""
    seat = ""
    if num > 1:
        seats = input("Enter your preferred seating arrangement(s) with row and seat no. (separated by a comma): ")
        seat = seats.split(",")
    else:
        seat = input("Enter your preferred seating arrangement with row and seat no.: ")
    name = str(input("Enter your name: "))

    print("\nThank you for booking with us", name, "!")
    print("\nYour ticket: ", "\n")
    print(movies[0])
    for a, b in time_lp.items():
        if a == time:
            print(a, ":", b)
    print(seat)
    print("\nHappy Viewing! Enjoy your time with us here at Indigo Theatres.")

elif movie == movies[1] or movie == "top gun maverick" or movie == "top gun" or movie == "2":
    print("\nThank you for choosing", movies[1], "as your movie!")
    time_mvk = {
        "8:45 AM": "Audi 1",
        "2:25 PM": "Audi 4",
        "9:00 PM": "Audi 3"
    }
    print("\nTimings for", movies[1], ": ")
    for a, b in time_mvk.items():
        print(a, b)
    time = input("\nEnter your preferred timings in proper format (with AM/PM): ")
    num = int(input("How many seats would you like? "))
    seats = ""
    seat = ""
    if num > 1:
        seats = input("Enter your preferred seating arrangement(s) with row and seat no. (separated by a comma): ")
        seat = seats.split(",")
    else:
        seat = input("Enter your preferred seating arrangement with row and seat no.: ")
    name = str(input("Enter your name: "))

    print("\nThank you for booking with us", name, "!")
    print("\nYour ticket: ", "\n")
    print(movies[1])
    for x, y in time_mvk.items():
        if x == time:
            print(x, ":", y)
    print(seat)
    print("\nHappy Viewing! Enjoy your time with us here at Indigo Theatres.")

elif movie == movies[2] or movie == "the batman" or movie == "batman" or movie == 3:
    print("\nThank you for choosing", movies[2], "as your movie!")
    time_btm = {
        "11:35 AM": "Audi 3",
        "5:30 PM": "Audi 5",
        "8:45 PM": "Audi 1"
    }
    print("Timings for", movies[2], ": ")
    for c, d in time_btm.items():
        print(c, d)
    time = input("\nEnter your preferred timings in proper format (with AM/PM): ")
    num = int(input("How many seats would you like? "))
    seats = ""
    seat = ""
    if num > 1:
        seats = input("Enter your preferred seating arrangement(s) with row and seat no. (separated by a comma): ")
        seat = seats.split(",")
    else:
        seat = input("Enter your preferred seating arrangement with row and seat no.: ")
    name = str(input("Enter your name: "))

    print("\nThank you for booking with us", name, "!")
    print("\nYour ticket: ", "\n")
    print(movies[2])
    for a, b in time_btm.items():
        if a == time:
            print(a, ":", b)
    print(seat)
    print("\nHappy Viewing! Enjoy your time with us here at Indigo Theatres.")

elif movie == movies[3] or movie == "rrr" or movie == "4":
    print("\nThank you for choosing", movies[3], "as your movie!")
    time_rrr = {
        "2:00 PM": "Audi 5",
        "5:00 PM": "Audi 1"
    }
    print("\nTimings for", movies[3], ": ")
    for x, y in time_rrr.items():
        print(x, y)
    time = input("\nEnter your preferred timings in proper format (with AM/PM): ")
    num = int(input("How many seats would you like? "))
    seats = ""
    seat = ""
    if num > 1:
        seats = input("Enter your preferred seating arrangement(s) with row and seat no. (separated by a comma): ")
        seat = seats.split(",")
    else:
        seat = input("Enter your preferred seating arrangement with row and seat no.: ")
    name = str(input("Enter your name: "))

    print("\nThank you for booking with us", name, "!")
    print("\nYour ticket: ", "\n")
    print(movies[3])
    for a, b in time_rrr.items():
        if a == time:
            print(a, ":", b)
    print(seat)
    print("\nHappy Viewing! Enjoy your time with us here at Indigo Theatres.")

elif movie == movies[4] or movie == "brahmastra" or movie == "brahmastra part 1 shiva" or movie == "brahmastra part one" or movie == "5":
    print("\nThank you for choosing", movies[4], "as your movie!")
    time_bms = {
        "11:00 AM": "Audi 1",
        "11:30 AM": "Audi 2",
        "11:45 AM": "Audi 4",
        "3:15 PM": "Audi 3",
        "5:30 PM": "Audi 2",
        "9:00 PM": "Audi 5"
    }
    print("\nTimings for", movies[4], ": ")
    for x, y in time_bms.items():
        print(x, y)
    time = input("\nEnter your preferred timings in proper format (with AM/PM): ")
    num = int(input("How many seats would you like? "))
    seats = ""
    seat = ""
    if num > 1:
        seats = input("Enter your preferred seating arrangement(s) with row and seat no. (separated by a comma): ")
        seat = seats.split(",")
    else:
        seat = input("Enter your preferred seating arrangement with row and seat no.: ")
    name = str(input("Enter your name: "))

    print("\nThank you for booking with us", name, "!")
    print("\nYour ticket: ", "\n")
    print(movies[4])
    for a, b in time_bms.items():
        if a == time:
            print(a, ":", b)
    print(seat)
    print("\nHappy Viewing! Enjoy your time with us here at Indigo Theatres.")
