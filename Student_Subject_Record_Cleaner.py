student_records = {
    "STU001": "Mathematics",
    "STU002": "Computer Science",
    "STU003": "Physics",
    "STU004": "Mathematics",  
    "STU005": "Unknown",     
    "STU006": "Chemistry"
}
print("Initial Student Records:")
print(student_records)
print("-" * 50)

search_id = "STU002"
missing_id = "STU099"

print(f"Searching for {search_id}: {student_records.get(search_id, 'Student not found')}")
print(f"Searching for {missing_id}: {student_records.get(missing_id, 'Student not found')}")
print("-" * 50)

student_records["STU007"] = "Biology"

student_records["STU001"] = "Data Science"

print("Records after adding STU007 and updating STU001:")
print(student_records)
print("-" * 50)

cleaned_records = {}
seen_subjects = set()

for student_id, subject in student_records.items():
    if subject == "Unknown":
        continue
    
    if subject in seen_subjects:
        continue
        
    cleaned_records[student_id] = subject
    seen_subjects.add(subject)

print("Cleaned Student Records (No duplicates or 'Unknown'):")
print(cleaned_records)
print("-" * 50)

total_records = len(cleaned_records)
print(f"Total number of valid student records: {total_records}")
print("-" * 50)

print("Final Cleaned Student Directory:")
for student_id, subject in cleaned_records.items():
    print(f"Student ID: {student_id} | Enrolled Subject: {subject}")
