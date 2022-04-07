# FastAPI JellySmack test

## Structure
The backend is a RESTful API built in FastAPI and a PostgreSQL database.

### conceptual data model
You can see the CDM [here](images/MCD.png "MCD DOC")

## Usage
### docker-compose
Create a file `.env` to create the environment variables like in `.env_example`

```bash
source .env
```

To run the application we need to have `Docker` and `docker-compose` installed. 
The execute from the root directory named 'jelly_project':
```bash
sudo -E docker-compose up
```

### Tests


## Interactive API docs
[API ROUTES](images/routes.png "API DOC")
You can see the interactive API documentation (provided by <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a> )

Now go to <a href="http://127.0.0.1:5000/docs" class="external-link" target="_blank">http://127.0.0.1:5000/docs</a>.

## Alternative API docs
And now, go to <a href="http://127.0.0.1:5000/redoc" class="external-link" target="_blank">http://127.0.0.1:5000/redoc</a>.

You will see the alternative automatic documentation (provided by <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>):

## Examples
### Populate database 
To populate database :
http://127.0.0.1:5000/populate-db

### Filters EXAMPLE

`http://127.0.0.1:5000/characters?search=[{"id":[{"operator":"IN", "value":[1,2,3]}]}]`
is equivalent to:
```bash
SELECT * FROM characters WHERE id IN (1,2,3);
```

`http://127.0.0.1:5000/characters?search=[{"name":[{"operator":"LIKE", "value":"Rick%"}]}]`
is equivalent to:
```bash
SELECT * FROM characters WHERE name LIKE "Rick%";
```

`http://127.0.0.1:5000/characters?search=[{"id":[{"operator":"IN", "value":[1,2,3]}]},{"name":[{"operator":"LIKE", "value":"Rick%"}]}]`
is equivalent to:
```bash
SELECT * FROM characters WHERE id IN (1,2,3) OR name LIKE "Rick%";
```

`http://127.0.0.1:5000/characters?search=[{"id":[{"operator":"IN", "value":[1,2,3]}],"name":[{"operator":"LIKE", "value":"Rick%"}]}] `
is equivalent to:
```bash
SELECT * FROM characters WHERE id IN (1,2,3) AND name LIKE "Rick%";
```


## Time spent :
### Environnement, Architecture
Around 6h

### Feature 1 
1. Import data from JSON to PostgreSQL : < 30 min
2. To expose two API routes : =~ 1h

### Feature 2
To create comment table + API CRUD on comment : =~ 1h30

### Feature 3
1. Pagination =~ 1h
2. Filters =~ 4h

### Feature 5 
Export comments to csv or xls : >15 min 

## Commits
I made a mistake on the commits and realized it later. So you will find my local commits here :
[Commits](images/git.png "commit")


## Difficulties
1. I had difficulties for the tests, I will explain to you during the interview (I will try if I can to implement it in the meantime).
2. In a rush, I misused git.
3. The environment took a long time because I had some "bugs" at the beginning. (I started with a ubuntu 18.04 with nothing installed)