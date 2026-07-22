marks = [85, 92, 78, 90, 64, 88, 95, 72]
print(f"Original Marks List: {marks}")

num_students = len(marks)
print(f"Total number of students: {num_students}")

first_mark = marks[0]
last_mark = marks[-1]
print(f"First student's mark (indexing): {first_mark}")
print(f"Last student's mark (indexing): {last_mark}")

top_three = marks[0:3]
print(f"First three marks (slicing): {top_three}")

print("\nIterating through marks:")
for index, mark in enumerate(marks):
    print(f" Student {index + 1}: {mark}")

total_marks = sum(marks)
average_mark = total_marks / num_students
smallest_mark = min(marks)
largest_mark = max(marks)

print("\n" + "="*30)
print(" STUDENT MARKS SUMMARY REPORT ")
print("="*30)
print(f" Total Marks Scored : {total_marks}")
print(f" Average Mark       : {average_mark:.2f}")
print(f" Smallest Mark      : {smallest_mark}")
print(f" Largest Mark       : {largest_mark}")
print("="*30)
