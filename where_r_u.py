#where r u

day = input("Day: ")
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))

print("\n")

if day == "mon":
    if hours == 8:
        print("Tom: Art 8:30 - 10:00")
        print("Dan: FREE (not started)")
    elif hours == 9:
        print("Tom: Art 8:30 - 10:00")
        print("Dan: FREE (not started)")
    elif hours == 10:
        if minutes == 0:
            print("Tom: Art 8:30 - 10:00")
            print("Dan: FREE (not started)")
        else:
            print("Tom: History 10:15 - 11:45")
            print("Dan: Maths 10:15 - 11:45")
    elif hours == 11:
        print("Tom: History 10:15 - 11:45")
        print("Dan: Maths 10:15 - 11:45")
    elif hours == 12:
        print("Tom: FREE (finished)")
        print("Dan: FREE (finished)")
    elif hours == 13:
        print("Tom: FREE (finished)")
        print("Dan: FREE (finished)")
    elif hours == 14:
        if minutes == 0:
            print("Tom: FREE (finished)")
            print("Dan: FREE (finished)")
        else:
            print("Tom: FREE (finished)")
            print("Dan: FREE (finished)")
    elif hours == 15:
        print("Tom: FREE (finished)")
        print("Dan: FREE (finished)")
       
elif day == "tue":
    if hours == 8:
        print("Tom: FREE (not started)")
        print("Dan: Biology 8:30 - 10:00")
    elif hours == 9:
        print("Tom: FREE (not started)")
        print("Dan: Biology 8:30 - 10:00")
    elif hours == 10:
        if minutes == 0:
            print("Tom: FREE (not started)")
            print("Dan: Biology 8:30 - 10:00")
        else:
            print("Tom: FREE (not started)")
            print("Dan: Psychology 10:15 - 11:45")
    elif hours == 11:
        print("Tom: Form 11:00 - 11:45")
        print("Dan: Psychology 10:15 - 11:45")
    elif hours == 12:
        print("Tom: Psychology 12:30 - 14:00")
        print("Dan: Support 12:30 - 14:00")
    elif hours == 13:
        print("Tom: Psychology 12:30 - 14:00")
        print("Dan: Support 12:30 - 14:00")
    elif hours == 14:
        if minutes == 0:
            print("Tom: Psychology 12:30 - 14:00")
            print("Dan: Support 12:30 - 14:00")
        else:
            print("Tom: Art 14:15 - 15:45")
            print("Dan: FREE")
    elif hours == 15:
        if minutes <= 45:
            print("Tom: Art 14:15 - 15:45")
            print("Dan: FREE")
        else:
            print("Tom: History 15:50 - 17:20")
            print("Dan: Maths 15:50 - 17:20")
    elif hours == 16:
        print("Tom: History 15:50 - 17:20")
        print("Dan: Maths 15:50 - 17:20")
    elif hours == 17:
        print("Tom: History 15:50 - 17:20")
        print("Dan: Maths 15:50 - 17:20")

elif day == "wed":
    if hours == 8:
        print("Tom: FREE (not started)")
        print("Dan: FREE (not started)")
    elif hours == 9:
        print("Tom: FREE (not started)")
        print("Dan: FREE (not started)")
    elif hours == 10:
        if minutes == 0:
            print("Tom: FREE (not started)")
            print("Dan: FREE (not started)")
        else:
            print("Tom: FREE (not started)")
            print("Dan: FREE (not started)")
    elif hours == 11:
        print("Tom: FREE (not started)")
        print("Dan: FREE (not started)")
    elif hours == 12:
        print("Tom: History 12:30 - 14:00")
        print("Dan: Maths 12:30 - 14:00")
    elif hours == 13:
        print("Tom: History 12:30 - 14:00")
        print("Dan: Maths 12:30 - 14:00")
    elif hours == 14:
        if minutes == 0:
            print("Tom: History 12:30 - 14:00")
            print("Dan: Maths 12:30 - 14:00")
        else:
            print("Tom: FREE (finished)")
            print("Dan: Biology 14:15 - 15:45")
    elif hours == 15:
        print("Tom: FREE (finished)")
        print("Dan: Biology 14:15 - 15:45")

elif day == "thu":
    if hours == 8:
        print("Tom: FREE (not started)")
        print("Dan: Psychology 8:30 - 10:00")
    elif hours == 9:
        print("Tom: FREE (not started)")
        print("Dan: Psychology 8:30 - 10:00")
    elif hours == 10:
        if minutes == 0:
            print("Tom: FREE (not started)")
            print("Dan: Psychology 8:30 - 10:00")
        else:
            print("Tom: Psychology 10:15 - 11:45")
            print("Dan: FREE")
    elif hours == 11:
        print("Tom: Psychology 10:15 - 11:45")
        print("Dan: FREE")
    elif hours == 12:
        print("Tom: Support 12:30 - 14:00")
        print("Dan: Biology 12:30 - 14:00")
    elif hours == 13:
        print("Tom: Support 12:30 - 14:00")
        print("Dan: Biology 12:30 - 14:00")
    elif hours == 14:
        if minutes == 0:
            print("Tom: Support 12:30 - 14:00")
            print("Dan: Biology 12:30 - 14:00")
        else:
            print("Tom: Art 14:15 - 15:45")
            print("Dan: Form 14:15 - 15:00")
    elif hours == 15:
        print("Tom: Art 14:15 - 15:45")
        print("Dan: FREE (finished)")

elif day == "fri":
    if hours == 8:
        print("Tom: FREE (not started)")
        print("Dan: FREE (not started)")
    elif hours == 9:
        print("Tom: FREE (not started)")
        print("Dan: FREE (not started)")
    elif hours == 10:
        if minutes == 0:
            print("Tom: FREE (not started)")
            print("Dan: FREE (not started)")
        else:
            print("Tom: FREE (not started)")
            print("Dan: FREE (not started)")
    elif hours == 11:
        print("Tom: FREE (not started)")
        print("Dan: FREE (not started)")
    elif hours == 12:
        print("Tom: FREE (not started)")
        print("Dan: Psychology 12:30 - 14:00")
    elif hours == 13:
        print("Tom: FREE (not started)")
        print("Dan: Psychology 12:30 - 14:00")
    elif hours == 14:
        if minutes == 0:
            print("Tom: FREE (not started)")
            print("Dan: Psychology 12:30 - 14:00")
        else:
            print("Tom: Psychology 14:15 - 15:45")
            print("Dan: FREE (finished)")
    elif hours == 15:
        print("Tom: Psychology 14:15 - 15:45")
        print("Dan: FREE (finished)")
