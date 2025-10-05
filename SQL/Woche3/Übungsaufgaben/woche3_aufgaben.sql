-----------------------------------------------------------------------------------------------------
----- Aufgabe 1
----- Erstelle eine Abfrage, die die Namen aller Mitarbeiter und ihre jeweiligen Titel ausgibt.
-----------------------------------------------------------------------------------------------------
SELECT firstName AS first_name,
	lastName AS last_name,
	jobTitle AS job_title
FROM employees;


-----------------------------------------------------------------------------------------------------
----- Aufgabe 2
----- Gib alle Informationen zu Produkten aus der Produktlinie "Motorcycles" aus.
-----------------------------------------------------------------------------------------------------
SELECT *
FROM
	products
WHERE
	productLine = 'Motorcycles';


-----------------------------------------------------------------------------------------------------
----- Aufgabe 3
----- Ermittle, wie viele Motorräder aktuell auf Lager sind.
-----------------------------------------------------------------------------------------------------
SELECT
	SUM(quantityInStock) AS inventory_number_motorcycles
FROM
	products
WHERE
	productLine = 'Motorcycles';


-----------------------------------------------------------------------------------------------------
----- Aufgabe 4
----- Berechne das günstigste, das teuerste und den durchschnittlichen Preis der Motorräder.
-----------------------------------------------------------------------------------------------------
SELECT
	MIN(buyPrice) AS motorcycle_cheapest,
	MAX(buyPrice) AS motorcycle_most_expensive,
	AVG(buyPrice) AS motorcycle_avarage_price
FROM
	products
WHERE
	productLine = 'Motorcycles';


-----------------------------------------------------------------------------------------------------
----- Aufgabe 5
----- Finde heraus, ob es Bestellungen gibt, die später versandt wurden, als ursprünglich gefordert.
-----------------------------------------------------------------------------------------------------
SELECT *
FROM
	orders
WHERE
	shippedDate > requiredDate;


-----------------------------------------------------------------------------------------------------
----- Aufgabe 6
----- Identifiziere die drei häufigsten Kommentare zu Bestellungen.
-----------------------------------------------------------------------------------------------------
SELECT
	comments,
	COUNT(*) AS frequency
FROM
	orders
WHERE
	comments IS NOT NULL
GROUP BY
	comments
ORDER BY
	frequency DESC
LIMIT 3;


-----------------------------------------------------------------------------------------------------
----- Aufgabe 7
----- Berechne die durchschnittliche Zeit von der Auftragserteilung bis zur Auslieferung.
-----------------------------------------------------------------------------------------------------
SELECT
	AVG(shippedDate - orderDate) AS average_shipment_time
FROM
	orders;

-----------------------------------------------------------------------------------------------------
----- Aufgabe 8
----- Ermittle das Sales-Mitglied, das den höchsten Zahlungsbetrag gemäß `pm.amount` generiert.
-----------------------------------------------------------------------------------------------------
SELECT
	e.employeeNumber AS employee_number,
	e.lastName AS last_name,
	e.firstName AS first_name,
	SUM(amount) AS pm_amount
FROM
	employees AS e
	LEFT JOIN customers AS c
		ON e.employeeNumber = c.salesRepEmployeeNumber
	LEFT JOIN payments AS p
		ON c.customerNumber = p.customerNumber
GROUP BY
	employee_number,
	last_name,
	first_name
HAVING
	SUM(amount) > 0
ORDER BY
	pm_amount DESC
LIMIT 1;


-----------------------------------------------------------------------------------------------------
----- Aufgabe 9
----- Finde Produkte, die noch von keinem Kunden bestellt wurden.
-----------------------------------------------------------------------------------------------------
SELECT
	p.productCode AS product_code,
	p.productName AS product_name
FROM
	products AS p
	LEFT JOIN orderdetails AS od
		ON p.productCode = od.productCode
WHERE
	od.orderNumber IS NULL;


-----------------------------------------------------------------------------------------------------
----- Aufgabe 10
----- Liste für alle unterschiedlichen Porsches folgende Informationen:
----- Die Verkaufsmenge
----- Den erwarteten Gewinn basierend auf dem MSRP (p.MSRP - p.buyPrice) * od.quantityOrdered
----- Den tatsächlichen Gewinn basierend auf dem Verkaufspreis (od.priceEach - p.buyPrice) * od.quantityOrdered
-----------------------------------------------------------------------------------------------------
SELECT
	p.productName AS product_name,
	SUM(od.quantityOrdered) AS quantity_ordered,
	SUM((p.MSRP - p.buyPrice) * od.quantityOrdered) AS profits_expexted,
	SUM((od.priceEach - p.buyPrice) * od.quantityOrdered) AS profits_actual
FROM
	products AS p
	LEFT JOIN orderdetails AS od
		ON p.productCode = od.productCode
WHERE
	p.productName ILIKE '%porsche%'
GROUP BY
	p.productName
ORDER BY
	p.productName


-----------------------------------------------------------------------------------------------------
----- Aufgabe 11
----- Ermittle den Gesamtumsatz pro Kunde und den prozentualen Anteil am Gesamtumsatz.
-----------------------------------------------------------------------------------------------------
SELECT
	c.customerNumber AS customer,
	SUM(od.quantityOrdered * od.priceEach) AS revenue_per_customer,
	total.revenue_total,
	ROUND((SUM(od.quantityOrdered * od.priceEach) / total.revenue_total) * 100, 2) AS revenue_percentage
FROM
	customers AS c
	LEFT JOIN orders AS o
		ON c.customerNumber = o.customerNumber
	LEFT JOIN orderdetails AS od
		ON o.orderNumber = od.orderNumber
	CROSS JOIN (
		SELECT SUM(quantityOrdered * priceEach) AS revenue_total
		FROM orderdetails
	) AS total
GROUP BY
	c.customerNumber,
	total.revenue_total
HAVING
	SUM(od.quantityOrdered * od.priceEach) > 0
ORDER BY c.customerNumber


-----------------------------------------------------------------------------------------------------
----- Aufgabe 12
----- Berechne den durchschnittlichen Zahlungsbetrag pro Verkaufsperson für jeden Standort.
-----------------------------------------------------------------------------------------------------
SELECT
	offices.city,
	offices.country,
	COUNT (DISTINCT e.employeeNumber) AS sales_rep_number,
	SUM(p.amount) AS amount,
	ROUND((SUM(p.amount) / COUNT (DISTINCT e.employeeNumber)), 2) AS amount_per_sales_rep
FROM
	offices
	INNER JOIN employees AS e
		ON offices.officeCode = e.officeCode
	INNER JOIN customers AS C
		ON e.employeeNumber = c.salesRepEmployeeNumber
	INNER JOIN payments AS p
		on c.customerNumber = p.customerNumber
WHERE
	e.jobTitle = 'Sales Rep'
GROUP BY
	offices.city,
	offices.country
ORDER BY
	offices.city,
	offices.country;


-----------------------------------------------------------------------------------------------------
----- Aufgabe 13
----- Vergleiche den monatlichen Umsatz von 2003 mit dem von 2004 und berechne die Differenz.
-----------------------------------------------------------------------------------------------------
CREATE TEMPORARY TABLE monthly_revenue AS
SELECT
	EXTRACT(MONTH from o.orderDate) AS order_month,
	EXTRACT(YEAR from o.orderDate) AS order_year,
	SUM(od.quantityOrdered * od.priceEach) AS revenue
FROM
	orders AS o
	INNER JOIN orderdetails AS od
		ON o.orderNumber = od.orderNumber
WHERE
	EXTRACT(YEAR from o.orderDate) IN (2003, 2004)
GROUP BY
	order_month,
	order_year;

SELECT
    order_month,
    SUM(CASE WHEN order_year = 2003 THEN revenue ELSE 0 END) AS revenue_2003,
    SUM(CASE WHEN order_year = 2004 THEN revenue ELSE 0 END) AS revenue_2004,
    SUM(CASE WHEN order_year = 2004 THEN revenue ELSE 0 END) -
    SUM(CASE WHEN order_year = 2003 THEN revenue ELSE 0 END) AS difference
FROM monthly_revenue
GROUP BY order_month
ORDER BY order_month;


-----------------------------------------------------------------------------------------------------
----- Aufgabe 14
----- Identifiziere Paare von Produkten, die häufig zusammen gekauft werden.
-----------------------------------------------------------------------------------------------------
SELECT
	od1.productCode AS item1,
	od2.productCode AS item2,
	COUNT(*) AS bought_together
FROM
	orderdetails AS od1
	INNER JOIN orderdetails AS od2
		ON od1.orderNumber = od2.orderNumber
WHERE
	od1.productCode < od2.productCode
GROUP BY
	od1.productCode,
	od2.productCode
ORDER BY
	bought_together DESC


-----------------------------------------------------------------------------------------------------
----- Aufgabe 15
----- Finde Produkte, die im Dezember 2003 verkauft wurden, aber nicht im Dezember 2004.
-----------------------------------------------------------------------------------------------------
SELECT
	DISTINCT od.productCode
FROM
	orderdetails od
	INNER JOIN orders o
		ON od.orderNumber = o.orderNumber
WHERE
	EXTRACT(YEAR from o.orderDate) = 2003 AND
	EXTRACT(MONTH from o.orderDate) = 12

EXCEPT

SELECT
	DISTINCT od.productCode
FROM
	orderdetails od
	INNER JOIN orders o
		ON od.orderNumber = o.orderNumber
WHERE
	EXTRACT(YEAR from o.orderDate) = 2004 AND
	EXTRACT(MONTH from o.orderDate) = 12


-----------------------------------------------------------------------------------------------------
----- Aufgabe 16
----- Berechne den durchschnittlichen Wert aller Bestellungen in 2004.
-----------------------------------------------------------------------------------------------------
CREATE VIEW order_value_2004 AS
SELECT
	od.orderNumber,
	SUM(od.quantityOrdered * od.priceEach) AS order_value
FROM
	orderdetails od
	INNER JOIN orders o
		on od.orderNumber = o.orderNumber
WHERE
	EXTRACT(YEAR from orderDate) = 2004
GROUP BY
	od.orderNumber;


CREATE VIEW average_order_value_2004 AS
SELECT
	ROUND(AVG(order_value), 2) AS average_order_value_2004
FROM
	order_value_2004;


SELECT * FROM average_order_value_2004

-----------------------------------------------------------------------------------------------------
----- Aufgabe 17
----- Ermittle Bestellungen aus 2004,
----- deren Bestellwert höher als der in Aufgabe 16 berechnete durchschnittliche Bestellwert ist.
-----------------------------------------------------------------------------------------------------
SELECT
	ov.orderNumber,
	ov.order_value
FROM
	order_value_2004 ov
WHERE
	ov.order_value > (SELECT * FROM average_order_value_2004)
ORDER BY
	order_value DESC
