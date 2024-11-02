-- dim_host

CREATE TABLE fact_listings (
    source_uid INT PRIMARY KEY,
	listing_url TEXT,
    price DECIMAL,
    maximum_nights DECIMAL,
    minimum_nights DECIMAL,
    number_of_reviews DECIMAL,
    availability_30 DECIMAL,
    availability_60 DECIMAL,
    availability_90 DECIMAL,
    availability_365 DECIMAL,
	last_scraped date
);

CREATE TABLE dim_host (
    host_sk SERIAL PRIMARY KEY,
    listing_uid int,
    host_id int,
    host_name VARCHAR(500),
    host_url VARCHAR(500),
    host_since DATE,
    host_about TEXT,
    host_response_rate VARCHAR(500),
    host_total_listings_count DECIMAL,
    host_verifications TEXT,
    host_identity_verified VARCHAR(500),
    accommodates DECIMAL,
    bathrooms DECIMAL,
    bedrooms DECIMAL,
    beds DECIMAL,
    FOREIGN KEY (listing_uid) REFERENCES fact_listings(source_uid)
);

CREATE TABLE dim_location (
    location_sk SERIAL PRIMARY KEY,
    listing_uid int,
    host_location VARCHAR(500),
    neighbourhood VARCHAR(500),
    latitude DECIMAL,
    longitude DECIMAL,
    region_name VARCHAR(500),
    region_parent_name VARCHAR(500),
    region_parent_parent_name VARCHAR(500),
    FOREIGN KEY (listing_uid) REFERENCES fact_listings(source_uid)
);

CREATE TABLE dim_property (
    property_sk SERIAL PRIMARY KEY,
    listing_uid int,
    property_type VARCHAR(500),
    FOREIGN KEY (listing_uid) REFERENCES fact_listings(source_uid)
);

CREATE TABLE dim_room (
    room_sk SERIAL PRIMARY KEY,
    listing_uid int,
    room_type VARCHAR(500),
    FOREIGN KEY (listing_uid) REFERENCES fact_listings(source_uid)
);