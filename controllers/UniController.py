class UniController:
  def create_admin_session(self):
    from models.Admin import Admin
    return Admin()

  def create_student_session(self):
    from models.Student import Student
    return Student()
