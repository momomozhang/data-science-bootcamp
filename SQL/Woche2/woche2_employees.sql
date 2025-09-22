
CREATE VIEW basic_info AS
SELECT
    gender AS "Geschlecht",
    dept_name AS "Abteilung",
    AVG(salary) AS "Durch. Gehalt",
	COUNT(*) AS "Anzahl MAs"
FROM employees
INNER JOIN dept_emp USING (emp_no)
INNER JOIN salaries USING (emp_no)
INNER JOIN departments USING (dept_no)
WHERE dept_emp.to_date = '9999-01-01' AND salaries.to_date = '9999-01-01'
GROUP BY dept_name, gender;

------------------------
--- Aufgabe 1(a)
------------------------

SELECT "Geschlecht", "Abteilung", "Durch. Gehalt"
FROM basic_info
ORDER BY "Abteilung", "Geschlecht";

------------------------
--- Aufgabe 1(b)
------------------------

SELECT "Geschlecht", "Abteilung", "Durch. Gehalt"
FROM basic_info
ORDER BY "Durch. Gehalt" DESC, "Geschlecht";

------------------------
--- Aufgabe 1(c)
------------------------

SELECT *
FROM basic_info
WHERE "Anzahl MAs" > 10000;


------------------------
--- Aufgabe 2
------------------------

SELECT * FROM employees AS e1
JOIN employees AS e2 ON
	e1.gender = e2.gender
	AND EXTRACT(YEAR FROM e1.birth_date) = 1965
	AND EXTRACT(YEAR FROM e2.birth_date) = 1965
	AND e1.emp_no > e2.emp_no;
