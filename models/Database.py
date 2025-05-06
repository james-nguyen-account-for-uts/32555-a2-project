import os
import json

class Database:
  def __init__(self, filename="data/student.data"):
    self.filename = filename
    if not os.path.exists(self.filename):
      with open(self.filename, 'w') as f:
        json.dump([], f)

  def read_all(self):
    # Read all student data in student.data
    with open(self.filename, 'r') as f:
      return json.load(f)

  def write_all(self, students):
    # Overwrite student data in student.data
    with open(self.filename, 'w') as f:
      json.dump(students, f, indent=3)

  def clear_student_data(self):
    # Clear all data from student.data
    with open(self.filename, 'w') as f:
      json.dump([], f)

# Run Database
if __name__ == "__main__":
  db = Database()