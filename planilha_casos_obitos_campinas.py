import openpyxl
from openpyxl.styles import Border, Side, Alignment

planilha = openpyxl.Workbook()

estilo = Side(border_style="thin", color="000000")

borda = Border(top=estilo, bottom=estilo, left=estilo, right=estilo)

planilha["Sheet"].title = "Campinas"

p3 = planilha["Campinas"]

p3.append(["Total_casos = 119868", "Casos/Óbitos"])
p3.append(["Casos", 115213])
p3.append(["Óbitos", 4655])

p3.column_dimensions["A"].width = 20
p3.column_dimensions["B"].width = 15

def borda_style_p3(column, qtd):
    for x in range(1,qtd):
        p3[column+str(x)].border = borda
        p3[column+str(x)].alignment = Alignment(horizontal="distributed")

borda_style_p3("A", 4)
borda_style_p3("B", 4)

planilha.save("casos_obitos_campinas.xlsx")