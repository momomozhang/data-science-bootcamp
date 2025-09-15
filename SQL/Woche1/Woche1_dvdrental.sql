--------------------------------------------------
-- Aufgabe 1 --
--------------------------------------------------
SELECT *
FROM film
WHERE length > 180
ORDER BY length DESC;

--------------------------------------------------
-- Aufgabe 2 --
--------------------------------------------------
SELECT COUNT(actor_id) AS total_actors
FROM actor;

--------------------------------------------------
-- Aufgabe 3 --
--------------------------------------------------
SELECT COUNT(film_id) AS action_film_count
FROM film_category
INNER JOIN category
ON film_category.category_id = category.category_id
WHERE category.name = 'Action';

--------------------------------------------------
-- Aufgabe 4 --
--------------------------------------------------
SELECT DISTINCT country.country
FROM customer
INNER JOIN address ON customer.address_id = address.address_id
INNER JOIN city ON address.city_id = city.city_id
INNER JOIN country ON city.country_id = country.country_id
WHERE country.country ILIKE 'A%' OR country.country ILIKE '%L'
ORDER BY country.country ASC;
