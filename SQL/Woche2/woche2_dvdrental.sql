---------------------------
--- Aufgabe 1
---------------------------

SELECT address_id, address
FROM address
FULL JOIN customer
USING (address_id)
WHERE customer_id IS NULL;


---------------------------
--- Aufgabe 2
---------------------------

SELECT film_id, inventory_id, title
FROM inventory
INNER JOIN film USING (film_id)
FULL JOIN rental USING (inventory_id)
WHERE rental_id IS NULL;
