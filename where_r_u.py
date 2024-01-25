#where is everyone

print("What day is it?\n[1] Monday\n[2] Tuesday\n[3] Wednesday\n[4] Thursday\n[5] Friday")
day = int(input("Option: "))
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
#hours, minutes = input("Enter time: ").split()
#hours = int(hours)
#minutes = int(minutes)

print("")

if day == 1:
    if hours == 8:
        print("Tom: Art 8:30 - 10:00")
        print("Dan: FREE (not started)")
        print("Harisson: FREE (not started)")
        print("Cesare: CompSci 8:30 - 10:00")
    elif hours == 9:
        print("Tom: Art 8:30 - 10:00")
        print("Dan: FREE (not started)")
        print("Harisson: FREE (not started)")
        print("Cesare: CompSci 8:30 - 10:00")
    elif hours == 10:
        if minutes == 0:
            print("Tom: Art 8:30 - 10:00")
            print("Dan: FREE (not started)")
            print("Harisson: FREE (not started)")
            print("Cesare: CompSci 8:30 - 10:00")
        else:
            print("Tom: History 10:15 - 11:45")
            print("Dan: Maths 10:15 - 11:45")
            print("Harisson: FREE (not started)")
            print("Cesare: Maths 10:15 - 11:45")
    elif hours == 11:
        print("Tom: History 10:15 - 11:45")
        print("Dan: Maths 10:15 - 11:45")
        print("Harisson: FREE (not started)")
        print("Cesare: Maths 10:15 - 11:45")
    elif hours == 12:
        print("Tom: FREE (finished)")
        print("Dan: FREE (finished)")
        print("Harisson: Drama 12:30 - 14:00")
        print("Cesare: FREE")
    elif hours == 13:
        print("Tom: FREE (finished)")
        print("Dan: FREE (finished)")
        print("Harisson: Drama 12:30 - 14:00")
        print("Cesare: FREE")
    elif hours == 14:
        if minutes == 0:
            print("Tom: FREE (finished)")
            print("Dan: FREE (finished)")
            print("Harisson: Drama 12:30 - 14:00")
            print("Cesare: FREE")
        else:
            print("Tom: FREE (finished)")
            print("Dan: FREE (finished)")
            print("Harisson: Drama 14:15 - 15:45")
            print("Cesare: Form 14:15 - 15:00")
    elif hours == 15:
        if minutes == 0:
            print("Cesare: Form 14:15 - 15:00")
        else:
            print("Cesare: FREE (finished)")
        print("Tom: FREE (finished)")
        print("Dan: FREE (finished)")
        print("Harisson: Drama 14:15 - 15:45")
       
elif day == 2:
    if hours == 8:
        print("Tom: FREE (not started)")
        print("Dan: Biology 8:30 - 10:00")
        print("Harisson: Physics 8:30 - 10:00")
        print("Cesare: Physics 8:30 - 10:00")
    elif hours == 9:
        print("Tom: FREE (not started)")
        print("Dan: Biology 8:30 - 10:00")
        print("Harisson: Physics 8:30 - 10:00")
        print("Cesare: Physics 8:30 - 10:00")
    elif hours == 10:
        if minutes == 0:
            print("Tom: FREE (not started)")
            print("Dan: Biology 8:30 - 10:00")
            print("Harisson: Physics 8:30 - 10:00")
            print("Cesare: Physics 8:30 - 10:00")
        else:
            print("Tom: FREE (not started)")
            print("Dan: Psychology 10:15 - 11:45")
            print("Harisson: FREE")
            print("Cesare: FREE")
    elif hours == 11:
        print("Tom: Form 11:00 - 11:45")
        print("Dan: Psychology 10:15 - 11:45")
        print("Harisson: FREE")
        print("Cesare: FREE")
    elif hours == 12:
        print("Tom: Psychology 12:30 - 14:00")
        print("Dan: Support 12:30 - 14:00")
        print("Harisson: Maths 12:30 - 14:00")
        print("Cesare: Maths 12:30 - 14:00")
    elif hours == 13:
        print("Tom: Psychology 12:30 - 14:00")
        print("Dan: Support 12:30 - 14:00")
        print("Harisson: Maths 12:30 - 14:00")
        print("Cesare: Maths 12:30 - 14:00")
    elif hours == 14:
        if minutes == 0:
            print("Tom: Psychology 12:30 - 14:00")
            print("Dan: Support 12:30 - 14:00")
            print("Harisson: Maths 12:30 - 14:00")
            print("Cesare: Maths 12:30 - 14:00")
        else:
            print("Tom: Art 14:15 - 15:45")
            print("Dan: FREE")
            print("Harisson: FREE (finished)")
            print("Cesare: CompSci 14:15 - 15:45")
    elif hours == 15:
        if minutes <= 45:
            print("Tom: Art 14:15 - 15:45")
            print("Dan: FREE")
            print("Harisson: FREE (finished)")
            print("Cesare: CompSci 14:15 - 15:45")
        else:
            print("Tom: History 15:50 - 17:20")
            print("Dan: Maths 15:50 - 17:20")
            print("Harisson: FREE (finished)")
            print("Cesare: Maths 15:50 - 17:20")
    elif hours == 16:
        print("Tom: History 15:50 - 17:20")
        print("Dan: Maths 15:50 - 17:20")
        print("Harisson: FREE (finished)")
        print("Cesare: Maths 15:50 - 17:20")
    elif hours == 17:
        print("Tom: History 15:50 - 17:20")
        print("Dan: Maths 15:50 - 17:20")
        print("Harisson: FREE (finished)")
        print("Cesare: Maths 15:50 - 17:20")

elif day == 3:
    if hours == 8:
        print("Tom: FREE (not started)")
        print("Dan: FREE (not started)")
        print("Harisson: Drama 8:30 - 10:00")
        print("Cesare: FREE (not started)")
    elif hours == 9:
        print("Tom: FREE (not started)")
        print("Dan: FREE (not started)")
        print("Harisson: Drama 8:30 - 10:00")
        print("Cesare: FREE (not started)")
    elif hours == 10:
        if minutes == 0:
            print("Tom: FREE (not started)")
            print("Dan: FREE (not started)")
            print("Harisson: Drama 8:30 - 10:00")
            print("Cesare: FREE (not started)")
        else:
            print("Tom: FREE (not started)")
            print("Dan: FREE (not started)")
            print("Harisson: FREE")
            print("Cesare: FREE (not started)")
    elif hours == 11:
        print("Tom: FREE (not started)")
        print("Dan: FREE (not started)")
        print("Harisson: FREE")
        print("Cesare: FREE (not started)")
    elif hours == 12:
        print("Tom: History 12:30 - 14:00")
        print("Dan: Maths 12:30 - 14:00")
        print("Harisson: FREE")
        print("Cesare: Maths 12:30 - 14:00")
    elif hours == 13:
        print("Tom: History 12:30 - 14:00")
        print("Dan: Maths 12:30 - 14:00")
        print("Harisson: FREE")
        print("Cesare: Maths 12:30 - 14:00")
    elif hours == 14:
        if minutes == 0:
            print("Tom: History 12:30 - 14:00")
            print("Dan: Maths 12:30 - 14:00")
            print("Harisson: FREE")
            print("Cesare: Maths 12:30 - 14:00")
        else:
            print("Tom: FREE (finished)")
            print("Dan: Biology 14:15 - 15:45")
            print("Harisson: 14:15 - 15:45")
            print("Cesare: Physics 14:15 - 15:45")
    elif hours == 15:
        print("Tom: FREE (finished)")
        print("Dan: Biology 14:15 - 15:45")
        print("Harisson: 14:15 - 15:45")
        print("Cesare: Physics 14:15 - 15:45")

elif day == 4:
    if hours == 8:
        print("Tom: FREE (not started)")
        print("Dan: Psychology 8:30 - 10:00")
        print("Harisson: FREE (not started)")
        print("Cesare: FREE (not started)")
    elif hours == 9:
        print("Tom: FREE (not started)")
        print("Dan: Psychology 8:30 - 10:00")
        print("Harisson: FREE (not started)")
        print("Cesare: FREE (not started)")
    elif hours == 10:
        if minutes == 0:
            print("Tom: FREE (not started)")
            print("Dan: Psychology 8:30 - 10:00")
            print("Harisson: FREE (not started)")
            print("Cesare: FREE (not started)")
        else:
            print("Tom: Psychology 10:15 - 11:45")
            print("Dan: FREE")
            print("Harisson: Maths 10:15 - 11:45")
            print("Cesare: Maths 10:15 - 11:45")
    elif hours == 11:
        print("Tom: Psychology 10:15 - 11:45")
        print("Dan: FREE")
        print("Harisson: Maths 10:15 - 11:45")
        print("Cesare: Maths 10:15 - 11:45")
    elif hours == 12:
        print("Tom: Support 12:30 - 14:00")
        print("Dan: Biology 12:30 - 14:00")
        print("Harisson: physics 12:30 - 14:00")
        print("Cesare: Physics 12:30 - 14:00")
    elif hours == 13:
        print("Tom: Support 12:30 - 14:00")
        print("Dan: Biology 12:30 - 14:00")
        print("Harisson: physics 12:30 - 14:00")
        print("Cesare: Physics 12:30 - 14:00")
    elif hours == 14:
        if minutes == 0:
            print("Tom: Support 12:30 - 14:00")
            print("Dan: Biology 12:30 - 14:00")
            print("Harisson: physics 12:30 - 14:00")
            print("Cesare: Physics 12:30 - 14:00")
        else:
            print("Tom: Art 14:15 - 15:45")
            print("Dan: Form 14:15 - 15:00")
            print("Harisson: FREE (finished)")
            print("Cesare: CompSci 14:15 - 15:45")
    elif hours == 15:
        print("Tom: Art 14:15 - 15:45")
        print("Dan: FREE (finished)")
        print("Harisson: FREE (finished)")
        print("Cesare: CompSci 14:15 - 15:45")

elif day == 5:
    if hours == 8:
        print("Tom: FREE (not started)")
        print("Dan: FREE (not started)")
        print("Harisson: Form 8:30 - 9:15")
        print("Cesare: FREE (not started)")
    elif hours == 9:
        if minutes <= 15:
            print("Form 8:30 - 9:15")
        else:
            print("Harisson: FREE")
        print("Tom: FREE (not started)")
        print("Dan: FREE (not started)")
        print("Cesare: FREE (not started)")
    elif hours == 10:
        if minutes == 0:
            print("Tom: FREE (not started)")
            print("Dan: FREE (not started)")
            print("Harisson: FREE")
            print("Cesare: FREE (not started)")
        else:
            print("Tom: FREE (not started)")
            print("Dan: FREE (not started)")
            print("Harisson: Drama 10:15 - 11:45")
            print("Cesare: FREE (not started)")
    elif hours == 11:
        print("Tom: FREE (not started)")
        print("Dan: FREE (not started)")
        print("Harisson: Drama 10:15 - 11:45")
        print("Cesare: FREE (not started)")
    elif hours == 12:
        print("Tom: FREE (not started)")
        print("Dan: Psychology 12:30 - 14:00")
        print("Harisson: FREE")
        print("Cesare: FREE (not started)")
    elif hours == 13:
        print("Tom: FREE (not started)")
        print("Dan: Psychology 12:30 - 14:00")
        print("Harisson: FREE")
        print("Cesare: FREE (not started)")
    elif hours == 14:
        if minutes == 0:
            print("Tom: FREE (not started)")
            print("Dan: Psychology 12:30 - 14:00")
            print("Harisson: FREE")
            print("Cesare: FREE (not started)")
        else:
            print("Tom: Psychology 14:15 - 15:45")
            print("Dan: FREE (finished)")
            print("Harisson: Maths 14:15 - 15:45")
            print("Cesare: Maths 14:15 - 15:45")
    elif hours == 15:
        print("Tom: Psychology 14:15 - 15:45")
        print("Dan: FREE (finished)")
        print("Harisson: Maths 14:15 - 15:45")
        print("Cesare: Maths 14:15 - 15:45")
