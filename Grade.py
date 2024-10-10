Physics = float(input(" Enter mark for physics"))
chemistry =float(input(" Enter mark for chemistry"))
biology =float(input(" Enter mark for biology"))
maths= float(input(" Enter mark for maths"))
computer = float(input(" Enter mark for computer"))

total = Physics+chemistry+biology+maths+computer

print("### STUDENT DETAILS ###")

print("Total Mark",total)

percentage = (total/500)*100

print("Percentage :",percentage)

if percentage>=90:
    print("A Grade ")
elif percentage>=80:
    print(" B Grade")
elif percentage>=70:
    print(" C Grade")
elif percentage>=60:
    print("D Grade ")
else:

    print("Failed...!")

print("Hiahhhhhhhh")