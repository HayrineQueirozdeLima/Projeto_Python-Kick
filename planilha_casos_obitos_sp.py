import openpyxl
from openpyxl.styles import Border, Side, Alignment

planilha = openpyxl.Workbook()

estilo = Side(border_style="thin", color="000000")

borda = Border(top=estilo, bottom=estilo, left=estilo, right=estilo)

planilha["Sheet"].title = "Sao_Paulo"
p1 = planilha["Sao_Paulo"]

p1.append(["Total_casos = 986976", "Casos/Óbitos"])
p1.append(["Casos", 947169])
p1.append(["Óbitos", 39807])

p1.column_dimensions["A"].width = 20
p1.column_dimensions["B"].width = 15

def borda_style_p1(column, qtd):
    for x in range(1,qtd):
        p1[column+str(x)].border = borda
        p1[column+str(x)].alignment = Alignment(horizontal="distributed")

borda_style_p1("A", 4)
borda_style_p1("B", 4)

planilha.save("casos_obitos_sp.xlsx")