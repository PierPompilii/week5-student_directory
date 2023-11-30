from lib.cohort import Cohort

def test_cohort_construct():
    cohort = Cohort(1,"July 2023", "01/07/2023")
    assert cohort.id == 1
    assert cohort.nombre == "July 2023"
    assert cohort.starting_date == "01/07/2023"