# DWH modelling Approach

- Applyin Kimpall 4 steps Design:
 
 1. what is the Buisnees process?
    
    - here we asking what is this organization doing?
      
      - for airBnB, it's a company that book hotels, appartments and provide hosting services for any country visiors, 
        not only for hotels, anyone can introduce his place and present hoting services fro visitore throug airBnB   

 2. what is the grain?
    - here we asking how we can descripe a single row at the fact table?
        
        - here i decided my grain to be one row per listing for one host, so i have the data at it's atomic level, 
            then i can summary it freely according to the buiesness requirements. 
            
 3. what are the dimnensions?
    - here we asking quetions like [how, what, why and when].
        - host is straightforward dims we can extract formn the grain, 
        - also they are other context we can notice from the data: property, location, and date dimensions
 
 4. what are the facts?
    - here we asking questions like, what is this buseness process measuring? 
      and also all the facts must be proper to the grain we already choose before.
      
        - price of the room is really very obvious and important fact.
        - also another facts like, minimum_nights, maximum_nights, number_of_reviews,
          availability_30, availability_60, availability_90, availability_365 
