# Tminus0-Tours-N-Travel
## Team Members
- Harsh Mahajan 
- Aditya Raj
- B Chetan Rao
- Hitika Rajesh Kumar



## About

> We have developed an on-line tour and travel web application for the people. Online tour and > travels system provides many services to the people.

## Software Requirements
- Microsoft Visual Studio Code - Download link (optional)
- PostgreSQL (fully configured) - Download link
-	Python3 - Download link
-	Pgadmin4 - Download link
-	Django (django will be installed when you run pip install -r requirements.txt)



## How to run this project


```sh
git clone https://github.com/harsh-8989/Tminus0-Tours-N-Travel.git
cd Tminus0-Tours-N-Travels
pip3 or pip install -r requirements.txt

```
# For setting up the Database

- First create a database in postgreSQL named as ‘ToursNTravel’.

- We have created a backup of our own database (which includes the information about travel destinations and flights, trains and hotels schedules we are providing for this project) that you can restore .
- 
![postgres](https://github.com/harsh-8989/Tminus0-Tours-N-Travel/blob/main/images%20readme/Web%20capture_11-5-2021_23840_docs.google.com.jpeg)
![postgres](https://github.com/harsh-8989/Tminus0-Tours-N-Travel/blob/main/images%20readme/Web%20capture_11-5-2021_23859_docs.google.com.jpeg)

- Then open settings.py in the code editor and change the database information, particularly username and password which you have set in your postgres.
![settings.py](https://github.com/harsh-8989/Tminus0-Tours-N-Travel/blob/main/images%20readme/Web%20capture_11-5-2021_23918_docs.google.com.jpeg)
- Now run the following commands - 
 

```
cd .\tminus0\
python or python3 manage.py migrate
python or python3 manage.py runserver
```
Now, open localhost:8000 or 127.0.0.1:8000 at the browser of your choice.
Voila, now you must have landed at the homepage of our website Tours & Travels.

> NOTE-
To book any flight, train or hotel you must be logged in. Flights, trains, and hotels are limited to the destinations and dates we have picked. So please use the dummy data provided below.
**All the fields are case sensitive.

Destinations added - 
1.	Tokyo
2.	New York
3.	Sydney
4.	Ladakh
5.	Seoul

Flights-
| Source |	Destination |	Departure Date |
|----------|:-------------:|------:|
| New York | 	Tokyo |	1-5-2021 | 
| Ladakh |	Seoul |	1-5-2021 | 
| Tokyo |	Sydney |	1-5-2021 |
| Sydney |	Ladakh |	1-5-2021 |


Trains -
| Source |	Destination |	Departure Date |
|----------|:-------------:|------:|
| New York |	Tokyo |	2021-05-01 |
| Ladakh	| Seoul	 | 2021-05-01 |
| Tokyo	| Sydney |	2021-05-01 |
| Seoul	| New York |	2021-05-01 |
| Sydney	| Ladakh	| 2021-05-01 |

Hotels - 
| Company Name	| City |	Address |
|----------|:-------------:|------:|
| TMinus0	| Tokyo |	TokyoCity|
| TMinus0	| Seoul	| SeoulCity |
| TMinus0	| Sydney	| SydneyCity |
| TMinus0	| New York	| NewYorkCity |
| TMinus0	| Ladakh	| Ladakh |





 
