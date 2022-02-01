import pandas as pd
import matplotlib.pyplot as plt

planilha = pd.read_excel("Dados-covid-19-estado.xlsx")

plt.title("Óbitos por dia no estado de São Paulo")

plt.xlabel("Dias, 26. Fev. 2020 - 30. Jan. 2022")
plt.ylabel("Óbitos")

plt.plot(planilha["Óbitos por dia"])

plt.grid()
plt.show()