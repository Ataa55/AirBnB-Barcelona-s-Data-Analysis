-- dim_host

CREATE TABLE dim_host (
    host_sk SERIAL PRIMARY KEY,
    host_id VARCHAR(500),
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
    beds DECIMAL
);


CREATE TABLE dim_location (
    location_sk SERIAL PRIMARY KEY,
    host_location VARCHAR(500),
    neighbourhood VARCHAR(500),
    latitude DECIMAL,
    longitude DECIMAL,
    region_name VARCHAR(500),
    region_parent_name VARCHAR(500),
    region_parent_parent_name VARCHAR(500)
);

CREATE TABLE dim_property (
    property_sk SERIAL PRIMARY KEY,
    property_type VARCHAR(500),
    room_type VARCHAR(500)
);
