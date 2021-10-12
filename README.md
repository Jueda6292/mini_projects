# mini_projects

* Write your code in `server.py`
* Place your data in `data.csv`


Create a Flask application that allows users to interact with a set of data stored in a csv file.

Minimum Requirements
Decide what kind of data you want the application to manage. Examples include music collections, cars, recipes, investments, budget items, work request tickets, etc.

* Each record should have 3-5 fields of data
* Create a csv file with specific columns and a few rows as "seed" data for use while developing

* This route should accept a POST request with the new data in JSON format
* This route does not require an HTML template

* Be sure to test your route using Insomnia
* Make sure the newly added data is visible when you visit the index route and the show route for that particular new record
* Add a delete route that allows users to delete a certain record (as specified by an id)
* This route should accept a DELETE request
* This route does not require an HTML template
* Make sure that records that don't exist are not deleted!
* Add an update route that allows users to update a certain record (as specified by an id)
* This route should accept a PATCH request with the new data in JSON format
* This route does not require an HTML template
* Make sure that records that don't exist are not updated!
* Add error handling to the create and update routes, so that users cannot create/update records with invalid data
* For example, quantities should be integers, not strings
* The status code typically used to indicate this sort of situation is 422 - Unprocessable Entity

General Hints
We've emphasized the importance of data types and recognizing the type of data you're working with. Be very aware at all times what kind of data you are dealing with at any moment. Is it a string? An integer? A dictionary? A list?
For the delete and update routes, beware that these routes are much more difficult to implement along with synchronizing data to a csv file
csv files are not meant for you to be able to easily access just one specific row -- so don't try to do that
Instead, you'll have to overwrite the entire file!
