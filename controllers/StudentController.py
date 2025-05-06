class StudentController:
  def __init__(self):
    from models.Database import Database
    self.database = Database()
  
  def register(self):
    print("Student Sign Up")

  def login(self):
    print("Student Sign In")