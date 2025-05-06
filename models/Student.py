class Student:
  # System prompt texts
  prompt_session_start = "Student System (l/r/x) : "
  prompt_error_handler = "Available options (l/r/x)."

  def main(self):
    # Choose options within the Student System
    prompt_input = input(self.prompt_session_start).strip().lower()
    
    while (prompt_input != "x"):
      match prompt_input:
        case _:
          print(self.prompt_error_handler)      
      prompt_input = input(self.prompt_session_start).strip().lower()

# Run Student System as a login session
if __name__ == "__main__":
  login_session = Student()
  login_session.main()