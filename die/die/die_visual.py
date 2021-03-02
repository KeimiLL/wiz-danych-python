from die import Die

#Utworzenie kości typu D6
die = Die()

#Wykonanie pewnej liczby rzutów i umieszczneie wyników na liście
results=[]
for roll in range(100):
    result = die.roll()
    results.append(result)

print(results)
