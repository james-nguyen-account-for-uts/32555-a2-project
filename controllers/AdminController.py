from utils.helpers import get_grade, is_student_pass

class AdminController:
  def __init__(self):
    from models.Database import Database
    self.database = Database()

  def clear_student_data(self):
    print("Clear Student Data")
    
    # Confirm before delete
    prompt_confirmation = "Are you sure you want to clear the database? (Y/N) "
    confirmation = input(prompt_confirmation).strip().lower()
    if confirmation == "y":
      self.database.clear_student_data()
  
  def group_students(self, prompt_input):
    grouped_by_grade = "g"
    grouped_by_pass_fail = "p"

    # Print heading and get student_groups based on input
    groups = {}
    if prompt_input == grouped_by_grade:
      print("Grade Grouping")
      groups = {"HD": [], "D": [], "C": [], "P": [], "Z": []}
    elif prompt_input == grouped_by_pass_fail:
      print("PASS/FAIL Partition")
      groups = {"FAIL": [], "PASS": []}

    # Read all student records in database
    students = self.database.read_all()
    for student in students:
      student_name = student["name"]
      student_id = student["id"]

      # Calculate student average mark and grade
      student_marks = [subject["mark"] for subject in student["subjects"]]
      student_avg_mark = round(sum(student_marks) / len(student_marks), 2) if student_marks else 0.0
      student_grade = get_grade(student_avg_mark)

      # Add entry to the grade group if grouped by grade
      # Add entry to PASS or FAIL group if grouped by PASS/FAIL
      entry = f"{student_name} :: {student_id} --> GRADE: {student_grade} - MARK: {student_avg_mark:.2f}"
      if prompt_input == grouped_by_grade:
        groups[student_grade].append(entry)
      elif prompt_input == grouped_by_pass_fail:
        groups[is_student_pass(student_avg_mark)].append(entry)

    # Print only recorded groups if grouped by grade
    # Print both groups if grouped by PASS/FAIL
    for category in groups.keys():
      if groups[category] or prompt_input == grouped_by_pass_fail:
        entries = ", ".join(groups[category])
        print(f"{category} --> [{entries}]")

  def remove_student_by_id(self):
    print("Remove Student")

    # Read all student records in database
    students = self.database.read_all()

    # Find student ID to remove
    prompt_input = input("Enter student ID to remove: ").strip()
    updated_students = [s for s in students if s["id"] != prompt_input]

    if len(updated_students) == len(students):
      # Inform if ID not found
      print(f"No student found with ID: {prompt_input}")
    else:
      # Save updated list back to database
      self.database.write_all(updated_students)
      print(f"Student with ID {prompt_input} has been removed")
  
  def show_all_students(self):
    print("Student List")

    # Read all student records in database
    students = self.database.read_all()

    # Inform if no records found
    if not students:
      print("No record.")
      return

    # Print the student records
    for student in students:
      student_name = student["name"]
      student_id = student["id"]
      student_email = student["email"]
      print(f"{student_name} :: {student_id} --> Email: {student_email}")
