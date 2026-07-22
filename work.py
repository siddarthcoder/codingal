habit_info = ("Read Books", "Productivity", 5)

weekly_completion = (True, False, True, True, False, True, False)

print("--- 1. Habit Tracker Initialized ---")
print(f"Habit Details: {habit_info}")
print(f"Weekly Completion Record: {weekly_completion}\n")


days_tracked = len(weekly_completion)
print("--- 2. Checking Tracking Length ---")
print(f"Number of days tracked this week: {days_tracked} days\n")


print("--- 3. Accessing Data ---")
habit_name = habit_info[0]
print(f"Habit Name: {habit_name}")

monday_status = weekly_completion[0]
print(f"Completed on Monday?: {monday_status}")

weekday_records = weekly_completion[0:5]
print(f"Weekday Records (Mon-Fri): {weekday_records}\n")


print("--- 4. Exploring Immutability ---")
print("Tuples are immutable. Python will raise an error if we try to change them.")

try:
    weekly_completion[0] = False
except TypeError as error:
    print(f"Caught expected error: {error}")
    print("Explanation: You cannot modify a tuple after creation. It prevents accidental data changes.")