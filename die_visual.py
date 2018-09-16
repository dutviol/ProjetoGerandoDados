import pygal
from die import Die


die_1 = Die()
die_2 = Die(10)

# faz alguns lançamentos e armazena os resultados em uma lista

results = []

null_rolls = 50000

for roll_num in range(null_rolls):
    results.append(die_1.roll()+die_2.roll())

frequencies = []

for value in range(2, die_1.num_size+die_2.num_size+1):
    frequencies.append(results.count(value))
    
# print(frequencies)


# Montar grafico de barras com as frequencias

# Vizualizar os resultados
hist = pygal.Bar()

hist.title = "Results of rolling one D6 "+ str(null_rolls) +" times."
hist.x_labels = range(2, die_1.num_size+die_2.num_size+1)
hist._x_title = "Results"
hist.y_title = "Frequency of Results"
hist.add("D6", frequencies)
hist.render_in_browser()



    