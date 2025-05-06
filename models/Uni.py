import sys
import os

# Add the project root (1 level up from current file) to sys.path
# To prevent Python modules from incorrectly imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from controllers.UniController import UniController

# Class: University System
class Uni:
  # System prompt texts
  prompt_session_start = "University System: (A)dmin, (S)tudent, or X : "
  prompt_error_handler = "Available options (a/s/x)."
  prompt_session_end = "Thank You"

  def __init__(self):
    self.controller = UniController()

  def main(self):
    # Choose options within the University System
    prompt_input = input(self.prompt_session_start).strip().lower()
    
    while (prompt_input != "x"):
      match prompt_input:
        case "a":
          # Create admin session to start Admin System
          admin_session = self.controller.create_admin_session()
          admin_session.main()
        case "s":
          # Create student session to start Student System
          student_session = self.controller.create_student_session()
          student_session.main()
        case _:
          print(self.prompt_error_handler)      
      prompt_input = input(self.prompt_session_start).strip().lower()

    print(self.prompt_session_end)

# Run University System as a login session
if __name__ == "__main__":
  login_session = Uni()
  login_session.main()