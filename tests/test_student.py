from lib.student import Student

def test_student_construct():
    student = Student (1, "Bruno", 3)
    assert student.id == 1
    assert student.alumno == "Bruno"
    assert student.cohort_id == 3