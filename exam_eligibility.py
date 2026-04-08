# 1) Ask the student if they had a medical cause and store the answer in `medical_cause`.
#    (Also clean the input so it becomes either 'Y' or 'N'.)

# 2) If `medical_cause` is 'Y':
#    - Print that the student is allowed to attend the exam.

# 3) Otherwise (medical_cause is 'N'):
#    a) Ask for the student’s attendance percentage and store it in `atten`.
#    b) If `atten` is 75 or more:
#       - Print "Allowed"
#    c) Else:
#       - Print "Not allowed"

print("answer in Y or N")
medical_cause = input("did you have a medical cause:")

if medical_cause == "Y":
    print("that student is allowed to attend the exam:")
elif medical_cause == "N":
    atten = int(input("what is your attendence percentage:"))
    if atten >=75:
        print("allowed:")
    else:
        print("Not allowed:")
