# Processing App

## Start with docker
`docker-compose up`
## Set up manually

 Requirements: PostgreSQL, Python 3.8

 1. Start PostgreSQL Database
 2. Install python modules
	 `pip3 install -r requirements.txt`
3. Set env variable
	`export DATABASE_URL=postgresql://user:password@db:5432/db`
 4. Create tables
    `alembic upgrade head`
4. Start server
	`uvicorn main:app`    

App will run at `localhost:8000`

## Endpoints
 - /
   - GET - Minimal frontend
 - /deals/
   - POST - accept csv file in multipart/form data format
   - GET - return 5 users sorted by spent money with gems bought at least by 2 customers from this list

## CSV File format
|customer|item|total|quantity|date|	 
|--|--|--|--|--|
|user login|item name|deal amount|item count|time|
|bellwether|Цаворит|612|6|2018-12-14 08:29:52.506166|
