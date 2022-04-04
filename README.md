# jellysmack_rick

source .env
sudo -E docker-compose up

To populate database :
/populate-db

Route :
List all episodes
/episodes
List all episodes
/characters


[{"id":[{"operator":"IN", "value":[1,2,3]}]}]
SELECT * FROM [table] WHERE id IN (1,2,3)

[{"name":[{"operator":"LIKE", "value":"Rick%"}]}]
SELECT * FROM [table] WHERE name LIKE "Rick%"

[{"id":[{"operator":"IN", "value":[1,2,3]}]},
{"name":[{"operator":"LIKE", "value":"Rick%"}]}] 
SELECT * FROM [table] WHERE id IN (1,2,3) OR name LIKE "Rick%"

[{"id":[{"operator":"IN", "value":[1,2,3]}],
"name":[{"operator":"LIKE", "value":"Rick%"}]}] 
SELECT * FROM [table] WHERE id IN (1,2,3) AND name LIKE "Rick%"