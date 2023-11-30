from lib.student import Student
from lib.cohort import Cohort

class CohortRepository:
    
    def __init__(self, connection):
        self.connection = connection


    def find_with_students(self, cohort_id):
        rows = self.connection.execute(
        "SELECT cohorts.id as cohort_id, cohorts.nombre, cohorts.starting_date, students.id AS students_id, students.alumno " \
            "FROM cohorts JOIN students ON cohorts.id = students.cohort_id "\
            "WHERE cohorts.id = %s", [cohort_id])    
        print(rows)
        students = []
        for row in rows:
            student = Student(row["students_id"], row["alumno"], row["cohort_id"])
            students.append(student)
        return Cohort(rows[0]["cohort_id"], rows[0]["nombre"], rows[0]["starting_date"], students)
