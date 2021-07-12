# FireQuest
FireQuest Tasks Solutions


### Task 1 ###
-> I used request package from python to get the data from JSON API. 
-> Further i used json() procedure to convert the string data from API into dictionary named w_data. 
-> Further Exploring into the API, I looked for the data I needed in the given task. So, I found them inside the w_data under key-name "list" with data in form of list-of-dictionary.
-> I stored the list data in another List object named lst. 
-> I prompted user to input choice, as required in the given task, and according to task, asked user to input date, if required. 
-> I traversed through all the dictionaries inside the list "lst" using for loop.
-> Inside loop, I stored dictionary in variable named weather_data and accessed its member with key-name "dt-txt", splitting it using split() method at " ",  to get date and time inside another list named date_time.
-> I compared user-provided date with derived date and if equal, print required data for that date in edited format (for better reading).
