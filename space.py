fuel = int(input("enter fuel level (%):"))
cargo_type = input("enter cargo type: ")
clearance = input("enter security clearance (gold/silver/none): ")

if fuel  < 10:
     print("emergency docking granted: low fuel")
else:
    if cargo_type == "Medication":
        print("access granted: Carrying medication")
    else:
        if clearance == "gold" or clearance == "silver":
            print("access granted: Valid security clearance")
        else:
            print("access denied: low security clearance")