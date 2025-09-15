--------------------------------------------------
-- Aufgabe 1 --
--------------------------------------------------
SELECT COUNT(salary)
FROM salaries
WHERE emp_no = '100001'
GROUP BY emp_no;

--------------------------------------------------
-- Aufgabe 2 --
--------------------------------------------------
SELECT COUNT(DISTINCT title)
FROM titles;

--------------------------------------------------
-- Aufgabe 3 --
--------------------------------------------------
SELECT COUNT(birth_date)
FROM employees
WHERE birth_date::text LIKE '%-08-17';

SELECT COUNT(birth_date)
FROM employees
WHERE date_part('month', birth_date) = 08
AND date_part('day', birth_date) = 17;

--------------------------------------------------
-- Aufgabe 4 --
--------------------------------------------------
SELECT last_name
FROM employees
WHERE emp_no < 20000
AND first_name = 'Uri'
AND gender = 'F'
AND
((birth_date BETWEEN '1957-05-23' AND '1958-01-01') OR
(hire_date BETWEEN '1989-02-10' AND '1990-01-01'));


--------------------------------------------------
-- Aufgabe 5 --
--------------------------------------------------
SELECT first_name, last_name
FROM employees
WHERE emp_no < 20000
AND first_name LIKE 'U__'
AND first_name != 'Uri'
AND gender = 'F'
AND
((birth_date BETWEEN '1957-05-23' AND '1958-01-01') OR
(hire_date BETWEEN '1989-02-10' AND '1990-01-01'))
ORDER BY first_name ASC;
