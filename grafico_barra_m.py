import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

covid = pd.read_csv('Dados-covid-19-municipios.csv', sep = ';', encoding='latin-1')

covid.head()

municipios = covid.query('Município == "São Paulo" | Município == "Guarulhos" | Município == "Campinas" | Município == "Santo André" | Município == "Ribeirão Preto" | Município == "Sorocaba" | Município == "Jundiaí" | Município == "Piracicaba" | Município == "Santos" | Município == "Osasco"')

fig, (axis1) = plt.subplots(1, 1, figsize=(15, 5))
axis1 = sns.barplot(x = 'Município', y = 'Mun_Total de casos', data = municipios, ax = axis1, palette = 'mako')
axis1.set_title('Casos de Covid-19 em 10 municípios de São Paulo', fontsize=25, pad=25)
axis1.set_ylabel("Casos", fontsize=18)
axis1.set_xlabel("Municípios", fontsize=12)

fig, (axis1) = plt.subplots(1, 1, figsize=(15, 5))
axis1 = sns.barplot(x = 'Município', y = 'Mun_Total de óbitos', data = municipios, ax = axis1, palette = 'mako')
axis1.set_title('Óbitos ocasionados pela Covid-19 em 10 municípios de São Paulo', fontsize=25, pad=25)
axis1.set_ylabel("Óbitos", fontsize=18)
axis1.set_xlabel("Municípios", fontsize=12)

plt.show()