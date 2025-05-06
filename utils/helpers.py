def get_grade(mark):
  if mark < 50:
    return "Z"    # Fail
  elif mark < 65:
    return "P"    # Pass
  elif mark < 75:
    return "C"    # Credit
  elif mark < 85:
    return "D"    # Distinction
  else:
    return "HD"   # High Distinction
  
def is_student_pass(mark):
  return "PASS" if mark >= 50 else "FAIL"