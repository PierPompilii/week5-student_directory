from lib.cohort_repository import CohortRepository  
from lib.cohort import Cohort
from lib.student import Student


def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)
    result = repository.find_with_students(2)
    assert result == Cohort(2, 'July 2023', '01/07/2023', [
        Student (2, 'Paula', 2),
        Student (4, 'Laura', 2)
    ])
    