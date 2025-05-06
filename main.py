import subprocess
import sys

class App:
  # File paths for different modes
  filepath_cmd = "models/Uni.py"
  filename_gui = "UniGuiApp.py"

  def __init__(self):
    # Ask user to select mode: CMD or GUI
    print("Please select mode:")
    print("   1 - Command line (CMD)")
    print("   2 - GUI")
    prompt_input = input("Enter 1 or 2: ").strip()

    match prompt_input:
      case "1":
        # Run app in command line
        subprocess.run([sys.executable, self.filepath_cmd])
        sys.exit()
      case "2":
        # Run app in GUI
        subprocess.run([sys.executable, self.filename_gui])
        sys.exit()
      case _:
        # Ask the prompt again if input is invalid
        print("Invalid input. Please enter 1 or 2.")

if __name__ == "__main__":
  app = App()
  app.__init__()
