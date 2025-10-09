CREATE TABLE airports (
	airport_id VARCHAR(10) PRIMARY KEY,
	airport_name VARCHAR(100),
	airport_city VARCHAR(100),
	airport_country VARCHAR(100),
	airport_latitude NUMERIC(10,7),
	airport_longitude NUMERIC(11,7)
);

CREATE TABLE aircraft_types (
	aircraft_type_id SERIAL PRIMARY KEY,
	aircraft_designation VARCHAR(100),
	aircraft_description TEXT
);

CREATE TABLE passengers (
	passenger_id SERIAL PRIMARY KEY,
	passport_number VARCHAR(20) NOT NULL UNIQUE,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL
);

CREATE TABLE passenger_details (
	passenger_id INT PRIMARY KEY REFERENCES passengers(passenger_id),
	birthday DATE,
	gender VARCHAR(50),
	street VARCHAR(100),
	city VARCHAR(100),
	postcode VARCHAR(50),
	country VARCHAR(100),
	email VARCHAR(355) UNIQUE NOT NULL,
	phone_number VARCHAR(20),
	CHECK (birthday < CURRENT_DATE)
);

CREATE TABLE airlines (
	airline_id VARCHAR(3) PRIMARY KEY,
	iata_code CHAR(2) NOT NULL UNIQUE,
	airline_name VARCHAR(100) NOT NULL,
	home_airport_id VARCHAR(10) REFERENCES airports(airport_id)
);

CREATE TABLE aircrafts (
	aircraft_id SERIAL PRIMARY KEY,
	capacity INT NOT NULL CHECK (capacity > 0),
	aircraft_type_id INT REFERENCES aircraft_types(aircraft_type_id) NOT NULL,
	airline_id VARCHAR(3) REFERENCES airlines(airline_id) NOT NULL
);

CREATE TABLE flights (
	flight_id SERIAL PRIMARY KEY,
	flight_number VARCHAR(15) NOT NULL,
	departure_time TIMESTAMPTZ NOT NULL,
	arrival_time TIMESTAMPTZ NOT NULL,
	airline_id VARCHAR(3) REFERENCES airlines(airline_id) NOT NULL,
	aircraft_id INT REFERENCES aircrafts(aircraft_id) NOT NULL,
	departure_airport_id VARCHAR(10) REFERENCES airports(airport_id) NOT NULL,
	arrival_airport_id VARCHAR(10) REFERENCES airports(airport_id) NOT NULL,
	CHECK (departure_time < arrival_time),
	UNIQUE(flight_number, departure_time)
);

CREATE TABLE bookings (
	booking_id SERIAL PRIMARY KEY,
	seat VARCHAR(10),
	price DECIMAL(10, 2) NOT NULL,
	passenger_id INT REFERENCES passengers(passenger_id) NOT NULL,
	flight_id INT REFERENCES flights(flight_id) NOT NULL,
	booking_time TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
	UNIQUE(flight_id, seat),
	CHECK (price >= 0),
	CHECK (seat IS NULL OR seat ~ '^[0-9]{1,3}[A-Z]$')
);

CREATE INDEX idx_airlines_home_airport ON airlines(home_airport_id);
CREATE INDEX idx_aircrafts_aircraft_type ON aircrafts(aircraft_type_id);
CREATE INDEX idx_aircrafts_airline ON aircrafts(airline_id);
CREATE INDEX idx_flights_airline ON flights(airline_id);
CREATE INDEX idx_flights_aircraft ON flights(aircraft_id);
CREATE INDEX idx_flights_departure_airport ON flights(departure_airport_id);
CREATE INDEX idx_flights_arrival_airport ON flights(arrival_airport_id);
CREATE INDEX idx_bookings_passenger ON bookings(passenger_id);
CREATE INDEX idx_bookings_flight ON bookings(flight_id);



