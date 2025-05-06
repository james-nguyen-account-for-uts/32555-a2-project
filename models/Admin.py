from collections import defaultdict
from controllers.AdminController import AdminController

class Admin:
  # System prompt texts
  prompt_session_start = "Admin System (c/g/p/r/s/x) : "
  prompt_error_handler = "Available options (c/g/p/r/s/x)."

  def __init__(self):
    self.controller = AdminController()

  def main(self):
    # Choose options within the Admin System
    prompt_input = input(self.prompt_session_start).strip().lower()
    
    while (prompt_input != "x"):
      match prompt_input:
        case "c":
          # (C)lear all student data
          self.controller.clear_student_data()
        case "g":
          # (G)roup students by grade
          self.controller.group_students(prompt_input)
        case "p":
          # (P)artition students by PASS/FAIL
          self.controller.group_students(prompt_input)
        case "r":
          # (R)emove student by ID
          self.controller.remove_student_by_id()
        case "s":
          # (S)how all students
          self.controller.show_all_students()
        case _:
          print(self.prompt_error_handler)
      print("")   # New line
      prompt_input = input(self.prompt_session_start).strip().lower()

# Run Admin System as a login session
if __name__ == "__main__":
  login_session = Admin()
  login_session.main()