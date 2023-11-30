DROP TABLE IF EXISTS cohorts CASCADE;
DROP SEQUENCE IF EXISTS cohorts_id_seq;
DROP TABLE IF EXISTS students CASCADE;
DROP SEQUENCE IF EXISTS students_id_seq;

CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  nomnre text,
  starting_date text
);

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  alumno text,
  cohort_id int
  -- constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

INSERT INTO cohorts (nombre, starting_date) VALUES ('March 2023', '01/03/2023');
INSERT INTO cohorts (nombre, starting_date ) VALUES ('July 2023', '01/07/2023');
INSERT INTO cohorts (nombre, starting_date) VALUES ('October 2023', '01/10/2023');

INSERT INTO students (alumno, cohort_id) VALUES ('Bruno', 3);
INSERT INTO students (alumno, cohort_id) VALUES ('Paula' ,2);
INSERT INTO students (alumno, cohort_id) VALUES ('Miguel', 1);
INSERT INTO students (alumno, cohort_id) VALUES ('Laura', 2);
