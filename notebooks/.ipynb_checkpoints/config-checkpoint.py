MONTHS = ["jan", "March", "November"]

POSTGRS_CREDENTIALS = {
    "HOST":"pgdatabase",
    "PORT":5432,
    "USER":"root",
    "PASSWORD":"root",
    "db":"airBnB_DWH"
}


DWH_DIMS_FACTS = {
            "dim_host":["host_id", "host_name", "host_url", 
                        "host_since","host_about", "host_response_rate",
                        "host_total_listings_count", "host_verifications",
                        "host_identity_verified", "accommodates", "bathrooms",
                        "bedrooms", "beds"],

            "dim_location": ["host_location", "neighbourhood", "latitude",
                            "longitude", "region_name", "region_parent_name", 
                            "region_parent_parent_name"],

            "dim_property": ["property_type", "room_type"],
            "fact_listings":["price", "maximum_nights","minimum_nights",
                             "number_of_reviews","availability_30",
                             "availability_60", "availability_90","availability_365"]
           }

DATA_COLS = ['id', 'listing_url', 'scrape_id', 'last_searched', 'last_scraped',
       'name', 'description', 'neighborhood_overview', 'picture_url',
       'host_id', 'host_url', 'host_name', 'host_since', 'host_location',
       'host_about', 'host_response_time', 'host_response_rate',
       'host_acceptance_rate', 'host_is_superhost', 'host_thumbnail_url',
       'host_picture_url', 'host_neighbourhood', 'host_listings_count',
       'host_total_listings_count', 'host_verifications',
       'host_has_profile_pic', 'host_identity_verified', 'neighbourhood',
       'latitude', 'longitude', 'property_type', 'room_type', 'accommodates',
       'bathrooms', 'bathrooms_text', 'bedrooms', 'beds', 'amenities', 'price',
       'minimum_nights', 'maximum_nights', 'minimum_minimum_nights',
       'maximum_minimum_nights', 'minimum_maximum_nights',
       'maximum_maximum_nights', 'minimum_nights_avg_ntm',
       'maximum_nights_avg_ntm', 'calendar_updated', 'has_availability',
       'availability_30', 'availability_60', 'availability_90',
       'availability_365', 'calendar_last_scraped', 'number_of_reviews',
       'number_of_reviews_ltm', 'number_of_reviews_l30d', 'first_review',
       'last_review', 'review_scores_rating', 'review_scores_accuracy',
       'review_scores_cleanliness', 'review_scores_checkin',
       'review_scores_communication', 'review_scores_location',
       'review_scores_value', 'requires_license', 'license',
       'instant_bookable', 'calculated_host_listings_count',
       'calculated_host_listings_count_entire_homes',
       'calculated_host_listings_count_private_rooms',
       'calculated_host_listings_count_shared_rooms', 'region_id',
       'region_name', 'region_parent_id', 'region_parent_name',
       'region_parent_parent_id', 'region_parent_parent_name',
       'reviews_per_month']