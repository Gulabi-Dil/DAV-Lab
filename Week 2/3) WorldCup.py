## Write a Python code block to create a dictionary of cricket World Cup winners. Let the key be the year; the value is the country that won the World Cup that year. Print the name of the best-performing country. Display the unique list of countries that have won the World Cup.
winners={
1975:"West Indies",
1979:"West Indies",
1983:"India",
1987:"Australia",
1991:"Pakistan",
1995:"Sri Lanka",
1999:"Australia",
2003:"Australia",
2007:"Australia",
2011:"India",
2015:"Australia",
2019:"England"
}
record={}
for country in winners.values():
  if country in record: record[country]+=1
  else: record[country]=1
W=max(record.values())
best=[x for x,y in record.items() if W==y]
print(f"Best performing country is: {best[0]}\nUnique list of countries that won the World cup: ")
for i in set(winners.values()): print(i)
