print("Welcome to thr treasure island. your mission is to find the treasure")
ans = input("first step is go left or right ?")
if ans == "left":
    asn2 = input("want to swim or wait for boat")
    if asn2 == "wait":
        asn3 = input("you are safe\n now pick left or right door")
        if asn3 == "yellow":
            print("GG bruh u find the treasure!")
        else:
            print("you're dead bruh!")
    else:
        print("you're dead bruh!")
else:
    print("you're dead bruh!")