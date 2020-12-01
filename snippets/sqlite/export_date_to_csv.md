Export data from the SQLite database to a CSV file
``` 
sqlite3 PATH_TO_DATABASE

# in SQLite prompt (sqlite> )
.headers on
.mode csv
.output OUTPUT_FILE.csv
QUERY;
.quit
```
