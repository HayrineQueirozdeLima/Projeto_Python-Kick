import pandas as pd
import matplotlib.pyplot as plt

planilha = pd.read_excel("casos_obitos_sp.xlsx")

plt.title("Percentual de Casos vs Óbitos de São Paulo, 30. Jan. 2022")

plt.pie(planilha["Casos/Óbitos"], labels = planilha["Total_casos = 986976"], autopct="%1.2f%%")

plt.show()