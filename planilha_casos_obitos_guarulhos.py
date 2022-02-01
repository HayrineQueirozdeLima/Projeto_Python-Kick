import openpyxl
from openpyxl.styles import Border, Side, Alignment

planilha = openpyxl.Workbook()

estilo = Side(border_style="thin", color="000000")

borda = Border(top=estilo, bottom=estilo, left=estilo, right=estilo)


planilha["Sheet"].title = "Guarulhos"
p2 = planilha["Guarulhos"]

p2.append(["Total_casos = 66560", "Casos/Óbitos"])
p2.append(["Casos", 61483])
p2.append(["Óbitos", 5077])

p2.column_dimensions["A"].width = 20
p2.column_dimensions["B"].width = 15

def borda_style_p2(column, qtd):
    for x in range(1,qtd):
        p2[column+str(x)].border = borda
        p2[column+str(x)].alignment = Alignment(horizontal="distributed")

borda_style_p2("A", 4)
borda_style_p2("B", 4)

planilha.save("casos_obitos_guarulhos.xlsx")