SELECT countries.name, languages.language, languages.percentage
From countries 
JOIN languages 
ON languages.country_id=countries.id
WHERE languages.language='Slovene'
ORDER BY languages.percentage DESC;

SELECT countries.name, count(*) 
From cities
left JOIN countries  
ON cities.country_id=countries.id;
SELECT cities.name, cities.population
From cities
join countries on 
cities.country_id= countries.id
WHERE countries.name ='Mexico' and cities.population >500000;
SELECT countries.name, langauges.language, languages.percentage 
From languages
left join countries on 
languages.country_id= countries.id
WHERE languages.percentage > '89%';









 