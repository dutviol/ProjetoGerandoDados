import csv

from matplotlib import pyplot as plt
from datetime import datetime

file_name = "arquivos/death_valley_2014.csv"

with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            alta = int(row[1])
            baixa = int(row[3])
            data = datetime.strptime(row[0], '%Y-%m-%d')           
        except:
            pass
        else:  
            highs.append(alta)
            lows.append(baixa)
            dates.append(data)

# Faz a plotagem dos dados
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(dates, highs, c='red', alpha = 1)

plt.plot(dates, lows, c='blue', alpha = 1)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha = 0.1)

#Formatar gráfico
plt.title("Daily higth and low temperatures - 2014", fontsize = 24)
plt.xlabel("", fontsize = 6)
fig.autofmt_xdate()
plt.ylabel("TEMPERATURE(F)", fontsize = 16)
plt.tick_params(axis= 'both', which='major', labelsize=6)

plt.show()

# print(header_row)
# print(highs)    