-- displays the average temperature (Fahrenheit) by city 
SELECT city, AVG(value) AS avg_temp
  FROM temperatures
  GROUP BY city
  ORDER by city, avg_temp DESC;
