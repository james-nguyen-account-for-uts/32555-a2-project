class Admin:
  # System prompt texts
  prompt_session_start = "Admin System (c/g/p/r/s/x) : "
  prompt_error_handler = "Available options (c/g/p/r/s/x)."

  def main(self):
    # Choose options within the Admin System
    prompt_input = input(self.prompt_session_start).strip().lower()
    
    while (prompt_input != "x"):
      match prompt_input:
        case _:
          print(self.prompt_error_handler)      
      prompt_input = input(self.prompt_session_start).strip().lower()

# Run Admin System as a login session
if __name__ == "__main__":
  login_session = Admin()
  login_session.main()