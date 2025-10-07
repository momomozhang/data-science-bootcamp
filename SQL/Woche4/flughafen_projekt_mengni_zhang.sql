CREATE TABLE passengers (
	passenger_id SERIAL PRIMARY KEY,
	passport_number INT NOT NULL,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL
);

CREATE TABLE passenger_details (
	passenger_id SERIAL PRIMARY KEY,
	birthday DATE,
	gender VARCHAR(50),
	street VARCHAR(100),
	city VARCHAR(100),
	postcode VARCHAR(50),
	country VARCHAR(100),
	email VARCHAR(355) UNIQUE NOT NULL,
	phone_number VARCHAR(20)
);

CREATE TABLE bookings (
	booking_id SERIAL PRIMARY KEY,
	seat VARCHAR(100),
	price DECIMAL(10, 2) NOT NULL,
	passenger_id INT REFERENCES passengers(passenger_id) NOT NULL,
	flight_id INT REFERENCES flights(flight_id) NOT NULL,
	booking_time TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE flights (
	flight_id SERIAL PRIMARY KEY,
	flight_number VARCHAR(15) NOT NULL,
	departure_time TIMESTAMPTZ NOT NULL,
	arrival_time TIMESTAMPTZ NOT NULL,
	airline_id VARCHAR(3) REFERENCES airlines(airline_id) NOT NULL,
	aircraft_id VARCHAR(10) REFERENCES aircrafts(aircraft_id) NOT NULL,
	departure_airport_id VARCHAR(10) NOT NULL,
	arrival_airport_id VARCHAR(10) NOT NULL
);

CREATE TABLE airlines (
	airline_id SERIAL PRIMARY KEY,
	iata_code CHAR(2) NOT NULL UNIQUE,
	airline_name VARCHAR(100) NOT NULL,
	home_airport_id VARCHAR(100)
);

CREATE TABLE aircrafts (
	aircraft_id SERIAL PRIMARY KEY,
	capacity INT NOT NULL CHECK (capacity > 0),
	aircraft_type_id INT NOT NULL,
	airline_id VARCHAR(3) REFERENCES airlines(airline_id) NOT NULL
);

CREATE TABLE aircraft_types (
	aircraft_type_id SERIAL PRIMARY KEY,
	aircraft_designation VARCHAR(100),
	aircraft_description TEXT
);

CREATE TABLE airports (
	airport_id SERIAL PRIMARY KEY,
	airport_name VARCHAR(100),
	airport_city VARCHAR(100),
	airport_country VARCHAR(100),
	airport_latitude VARCHAR(100),
	airport_longitude VARCHAR(100)
)
