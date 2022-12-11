question1="Round 1:-\nQuestion 1: The atomic number for lithium is 17.\n(a)True\n(b)False\n"
question2="Round 2:-\nQuestion 2: pinocchio was walt Disney's first animated feature film in full colour.\n(a)True\n(b)False\n"
question3="Round 3:-\nQuestion 3: The national sport of India is Hockey.\n(a)True\n(b)False\n"
question4="Round 4:-\nQuestion 4: Nepal is the only country in the world without the rectangular flag.\n(a)True\n(b)False\n"
question5="Round 5:-\nQuestion 5: The world largest island is Greenland.\n(a)True\n(b)False\n"
dict={question1:"b",question2:"b",question3:"a",question4:"a",question5:"a"}
score=0
for i in dict:
    print(i)
    ans=input("Enter your answer: ")
    if ans==dict[i]:
        print("Congratulations!!! Your answer is correct.👍")
        score=score+1
    else:
        print("Your answer is Incorrect.")
print("Total score obtained:",score)
