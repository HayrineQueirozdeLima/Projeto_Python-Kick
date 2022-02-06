import os
from fpdf import FPDF


pdf = FPDF("P", "mm", "A4")
pdf.add_page()



def texto():
    pdf.set_text_color(0,0,0)
    pdf.set_font('Arial','',12)

def negrito():
    pdf.set_font('Arial','B',12)
def sublinhado():
    pdf.set_font('Arial','U',12)
def italico():
    pdf.set_font('Arial','I',12)

def titulo(titulo):
    pdf.ln()
    pdf.set_font('Arial','B',16)
    pdf.cell(190,5,txt=titulo, align='C')
    pdf.ln(10)
def subtitulo(subtitulo):
    pdf.ln()
    pdf.set_font('Arial','B',14)
    pdf.cell(190,5,txt=subtitulo, align='C')
    pdf.ln()
def p(paragrafo):
    texto()
    pdf.multi_cell(190,5,txt=paragrafo)
    pdf.ln(h=3)
def descricao(descricao):
    pdf.set_font('Arial','',10)
    pdf.multi_cell(190,5,txt=descricao)
    pdf.ln(h=3)
    

texto()
pdf.multi_cell(w=0,h=5, txt='Hayrine Queiroz de Lima\nPorto Velho - RO\n2022\n', align='J')
pdf.image(name="kick.png", w=25, h=10, y=5, x=180)
pdf.line(5, 15, 205, 15)

titulo('Saúde Mental Na Pandemia')

p('     Em janeiro de 2020, a Organização Mundial da Saúde (OMS) declarou o surgimento de uma nova doença provocada por um vírus do tipo coronavírus - a Covid -19. Foi considerada uma emergência de saúde pública de interesse internacional, com alto risco de se espalhar para outros países ao redor do mundo. Em março de 2020, a OMS avaliou que a Covid-19 caracterizava-se como uma pandemia.')

p('     A agenda de saúde frente à pandemia engloba uma gama enorme de áreas que devem ser cobertas, mas é preciso chamar a atenção da comunidade médica e, também, da população para o risco de uma epidemia paralela, que já dá indícios preocupantes: o aumento do sofrimento psicológico, dos sintomas psíquicos e dos transtornos mentais. Embora o impacto da disseminação do coronavírus para as doenças psíquicas ainda esteja sendo mensurado, as implicações para a saúde mental em situações como a que estamos vivendo já foram relatadas na literatura científica.')

subtitulo('Saúde Mental')

pdf.image(name="img1.png", w=170, y=115, x=15)
pdf.ln(80)

descricao('     Na média global, 45 por cento dos cerca de 21 mil entrevistados pelo Ipsos afirmaram que sua saúde mental piorou pouco ou muito no último ano, sob a pandemia')

negrito()
pdf.multi_cell(190,5,txt='     Mais da metade dos brasileiros entrevistados por uma pesquisa declararam que sua saúde emocional e mental piorou desde o início da pandemia, em índice superior à média dos 30 países e territórios pesquisados.')
pdf.ln(h=3)

p('     Outros estudos sobre o mesmo tema também trazem dados preocupantes.')

p('     Um deles, publicado pela Fiocruz com outras seis universidades em meados do ano passado, dizia que "sentimentos frequentes de tristeza e depressão afetavam 40 por cento da população adulta brasileira, e sensação frequente de ansiedade e nervosismo foi relatada por mais de 50 por cento das pessoas".')

p('     Um relatório de 2017 da Organização Mundial da Saúde (OMS) apontava o Brasil como o país com a maior prevalência de transtornos de ansiedade nas Américas: o problema afetava 9,3 por cento da população, o equivalente a 18,6 milhões de pessoas.')

p('     Transtornos depressivos foram relatados por 5,8 por cento dos brasileiros, ou 11,5 milhões de pessoas.')

p('     De fato, vemos como isso é um problema aqui no Brasil (com as pesquisas), e a situação atual da pandemia tem pesado muito. As notícias são muito tristes, e (com o isolamento social e a perda de redes de apoio) as pessoas têm perdido as estratégias para lidar com isso.')

negrito()
pdf.multi_cell(190,5,txt='Gráficos que representam o número de casos e óbitos por dia no estado de São Paulo, desde 26 de fevereiro de 2020 até 30 de janeiro de 2022', align='C')
pdf.ln(h=3)

pdf.image(name="Gráfico-Total_de_casos_por_dia_no_estado_de_São_Paulo.png", w=100, y=45, x=9)
pdf.image(name="Gráfico - Total de óbitos por dia no estado de São Paulo.png", w=100, y=45, x=110)
pdf.ln(75)

negrito()
pdf.multi_cell(190,5,txt='Gráficos que representam o número de casos e óbitos em alguns municípios de São Paulo, atualizado dia 25 de Janeiro de 2022', align='C')
pdf.ln(h=3)

pdf.image(name="grafico_barras_casos_10m.png", w=200, y=135, x=7)
pdf.image(name="grafico_barras_obitos_10m.png", w=200, y=215, x=7)
pdf.ln(150)

p('     Uma das consequências da pandemia é o aumento de transtornos mentais e do trauma psicológico provocados diretamente pela infecção ou por seus desdobramentos secundários.')

p('     As pessoas reagem de maneira diferente a situações estressantes. Como cada um responde à pandemia pode depender de sua formação, da sua história de vida, das suas características particulares e da comunidade em que vive. Os grupos que podem responder mais intensamente ao estresse de uma crise incluem: Pessoas idosas ou com doenças crônicas que apresentam maior risco se tiverem Covid-19; Profissionais de saúde que trabalham no atendimento à Covid-19; Pessoas que têm transtornos mentais, incluindo problemas relacionados ao uso de substâncias.')
pdf.ln(90)

pdf.image(name="casos_confirmados_31_jan_2022.png", w=190, y=55, x=9)

pdf.set_font('Arial','',10)
pdf.multi_cell(190,5,txt='Atializado em 31.Jan.2022', align='C')
pdf.ln(70)

pdf.image(name="imgseade.png", w=190, y=155, x=9)

pdf.set_font('Arial','',10)
pdf.multi_cell(190,5,txt='Atializado em 31.Jan.2022', align='C')
pdf.ln(h=3)

p('     O aumento dos sintomas psíquicos e dos transtornos mentais durante a pandemia pode ocorrer por diversas causas. Dentre elas, pode-se destacar a ação direta do vírus da Covid-19 no sistema nervoso central, as experiências traumáticas associadas à infeção ou à morte de pessoas próximas, o estresse induzido pela mudança na rotina devido às medidas de distanciamento social ou pelas consequências econômicas, na rotina de trabalho ou nas relações afetivas e, por fim, a interrupção de tratamento por dificuldades de acesso.')

p('     Esses cenários não são independentes. Ou seja, uma pessoa pode ter sido exposta a várias destas situações ao mesmo tempo, o que eleva o risco para desenvolver ou para agravar transtornos mentais já existentes.')

p('     O distanciamento social alterou os padrões de comportamento da sociedade, com o fechamento de escolas, a mudança dos métodos e da logística de trabalho e de diversão, minando o contato próximo entre as pessoas, algo tão importante para a saúde mental.')

p('     O convívio prolongado dentro de casa aumentou o risco de desajustes na dinâmica familiar. Somam-se a isso as reduções de renda e o desemprego, que pioram ainda mais a tensão sobre as famílias. E, ainda, as mortes de entes queridos em um curto espaço de tempo, juntamente à dificuldade para realizar os rituais de despedida, dificultando a experiência de luto e impedindo a adequada ressignificação das perdas, aumentando o estresse.')

negrito()
pdf.multi_cell(190,5,txt='Algumas reações comuns são: ', align='C')
pdf.ln(h=3)

p('_O medo de ficar doente e morrer;')
p('_Evitar de procurar um serviço de saúde por outros motivos, por receio de se contaminar; medo de perder a fonte de renda, por não poder trabalhar, ou ser demitido; ')
p('_Alterações do sono, da concentração nas tarefas diárias, ou aparecimento de pensamentos intrusivos; ')
p('_Sentimentos de desesperança, tédio, solidão e depressão devido ao isolamento; ')
p('_Raiva, frustração ou irritabilidade pela perda de autonomia e liberdade pessoal; ')
p('_Medo de ser socialmente excluído ou estigmatizado por ter ficado doente; ')
p('_Sentir-se impotente em proteger as pessoas próximas, ou medo de ser separado de familiares por motivo de quarentena/isolamento; ')
p('_Preocupação com a possibilidade de o indivíduo ou de membros de sua família contraírem a Covid-19 ou a transmitirem a outros;risco de deterioração de doenças clínicas e de transtornos mentais prévios ou, ainda, do desencadeamento de transtornos mentais; ')
p('_Risco de adoecimento de profissionais de saúde sem ter substituição adequada; ')
p('_Medo, ansiedade ou outras reações de estresse ligadas a notícias falsas, alarmistas ou sensacionalistas, e mesmo ao grande volume de informações circulando.')

subtitulo('Mais Pesquisas Sobre O Caso:')

p('     Uma pesquisa da Workana (2020) mostra que 43,7 por cento dos trabalhadores sentiram algum sintoma de prejuízo mental durante a pandemia. Entre os pesquisados, 24 por cento sentiram dificuldade de se concentrar. 13,2 por cento sentiram ansiedade. 5,8 por cento sentiram solidão e 0,8 por cento sentiram depressão ou claustrofobia.')

p('     Para compreender  algumas das diversas mudanças que a pandemia trouxe para o cotidiano dos brasileiros nos últimos meses, a Mastercard realizou uma pesquisa em 13 países, incluindo Brasil, México, Chile, Colômbia, Argentina e Peru.')

p('     O levantamento analisou dados do dia a dia dos entrevistados e os que se destacam mostram como as pessoas têm novas prioridades no Brasil, incluindo começar a cuidar da saúde mental.')

p('     Apesar de ser reconhecido pelas suas vantagens, o home office pode ser uma das causas de transtornos de ansiedade e de excesso de trabalho. Um levantamento feito por uma empresa de dados verificou que os comentários das pessoas nas redes sociais foram menos favoráveis ao trabalho remoto conforme os meses passaram neste ano. ')

pdf.add_page()
pdf.ln(160)

pdf.image(name="img2.png", w=190, y=15, x=9)

p('     Outro dado alarmante descoberto no mês de novembro de 2020 pela empresa de consultoria Falconi foi o aumento de doenças psiquiátricas como depressão ou distúrbios emocionais como burnout. Taxas maiores foram registradas por 37 por cento das empresas.')

pdf.image(name="img3.png", w=180, y=190, x=15)

pdf.add_page()

p('     A Organização Pan-Americana de Saúde (Opas) alertou, nesta quinta-feira, 5, que os efeitos da pandemia de covid-19 na saúde mental das pessoas provavelmente "persistirão" depois que o vírus for controlado e alertou sobre dados "preocupantes" entre os profissionais de saúde.')

subtitulo('Algumas dicas para lidar com a situação')

p('_Tenha pequenos momentos de lazer, que te tragam satisfação.')
p('_Cuidado com o uso de substâncias tóxicas, como álcool, tabaco e outras drogas')
p('_Cuidado com as cobranças digitais')
p('_Separe o lazer do trabalho e não fique online o tempo inteiro')
p('_Cuide do sono e escolha ambientes escuros para dormir')
p('_Identificar os sinais de que saúde mental não vai bem é o primeiro (e fundamental) passo. Alguns deles são: perda de prazer em atividades que você gosta, alterações no sono e no apetite e grande dificuldade de concentração')
p('_Procure ajuda médica sempre que necessário, e não tente resolver tudo sozinho(a). Todo sofrimento pode e deve ser aliviado, e o SUS oferece atendimento nas UBS, nos CAPS e nos ambulatórios de saúde mental')
p('_Reconhecer e acolher seus receios e medos, procurando pessoas de confiança para conversar')
p('_Reenquadrar os planos e estratégias de vida, de forma a seguir produzindo planos de forma adaptada às condições associadas à pandemia')
p('_Buscar fontes confiáveis de informação, como o site da Organização Mundial da Saúde')
p('_Reduzir o tempo que passa assistindo ou ouvindo coberturas midiáticas')
p('_Manter ativa a rede socioafetiva, estabelecendo contato, mesmo que virtual, com familiares, amigos e colegas')
p('_Retomar estratégias e ferramentas de cuidado que tenha usado em momentos de crise ou sofrimento e ações que trouxeram sensação de maior estabilidade emocional')
p('_Investir em exercícios e ações que auxiliem na redução do nível de estresse agudo (meditação, leitura, exercícios de respiração, entre outros mecanismos que auxiliem a situar o pensamento no momento presente), bem como estimular a retomada de experiências e habilidades usadas em tempos difíceis do passado para gerenciar emoções durante a epidemia')


pdf.add_page()
pdf.ln(125)
pdf.set_font('Arial','B',16)
pdf.multi_cell(190,5,txt='Falar sobre saúde mental nunca foi tão importante quanto em tempos de pandemia.', align='C')

pdf.add_page()

titulo('REFERÊNCIAS')

pdf.set_text_color(93,216,240)
sublinhado()

pdf.multi_cell(190,5,txt='BBC NEWS Brasil. Covid: saúde mental piorou para 53 por cento dos brasileiros sob pandemia', link='https://www.bbc.com/portuguese/geral-56726583')
pdf.ln(h=3)

pdf.multi_cell(190,5,txt='Biblioteca Virtual em Saúde - MINISTÉRIO DA SAÚDE. Saúde mental e a pandemia de Covid-19.', link='https://bvsms.saude.gov.br/saude-mental-e-a-pandemia-de-covid-19/')
pdf.ln(h=3)

pdf.multi_cell(190,5,txt='Conselho Federal de Enfermagem. Guia de saúde mental pós-pandemia no Brasil.', link='http://biblioteca.cofen.gov.br/wp-content/uploads/2020/12/Guia-de-saude-mental-pos-pandemia-no-Brasil.pdf')
pdf.ln(h=3)

pdf.multi_cell(190,5,txt='COSTA, Fernanda Benquerer. A saúde mental em meio à pandemia de Covid-19.', link='http://www.saude.df.gov.br/wp-conteudo/uploads/2018/03/Nota-Informativa-A-Sa%C3%BAde-Mental-e-a-Pandemia-de-COVID19-poss%C3%ADveis-impactos-e-dicas-de-gerenciamento-para-a-popula%C3%A7%C3%A3o-geral.pdf')
pdf.ln(h=3)

pdf.multi_cell(190,5,txt='Exame. Efeitos da covid-19 na saúde mental persistirão no pós-pandemia, diz Opas.', link='https://exame.com/ciencia/efeitos-da-covid-19-na-saude-mental-persistirao-no-pos-pandemia-diz-opas/')
pdf.ln(h=3)

pdf.multi_cell(190,5,txt='Exame. Estes gráficos mostram como a saúde mental virou prioridade na pandemia.', link='https://exame.com/carreira/estes-graficos-mostram-como-a-saude-mental-virou-prioridade-na-pandemia/')
pdf.ln(h=3)

pdf.multi_cell(190,5,txt='FIOCRUZ Brasília. Coronavírus e saúde mental. Tire suas dúvidas aqui!', link='https://www.fiocruzbrasilia.fiocruz.br/coronavirus-e-saude-mental-tire-suas-duvidas-aqui/')
pdf.ln(h=3)

pdf.multi_cell(190,5,txt='G1. Covid: saúde mental piorou para 53 por cento dos brasileiros sob pandemia, aponta pesquisa. ', link='https://g1.globo.com/bemestar/coronavirus/noticia/2021/04/14/covid-saude-mental-piorou-para-53percent-dos-brasileiros-sob-pandemia-aponta-pesquisa.ghtml')
pdf.ln(h=3)

pdf.multi_cell(190,5,txt='Organização Panamericana da Saúde. Pandemia de COVID-19 aumenta fatores de risco para suicídio.', link='https://www.paho.org/pt/noticias/10-9-2020-pandemia-covid-19-aumenta-fatores-risco-para-suicidio')
pdf.ln(h=3)

pdf.multi_cell(190,5,txt='Realidade imposta pela pandemia pode gerar transtornos mentais e agravar quadros existentes.', link='https://www.gov.br/saude/pt-br/assuntos/noticias/2021-1/outubro/realidade-imposta-pela-pandemia-pode-gerar-transtornos-mentais-e-agravar-quadros-existentes')
pdf.ln(h=3)

pdf.multi_cell(190,5,txt='SP CONTRA O NOVO CORONAVÍRUS - Boletim Completo.', link='https://www.seade.gov.br/coronavirus/')
pdf.ln(h=3)

pdf.multi_cell(190,5,txt='World Health Organization.', link='https://www.who.int/docs/default-source/coronaviruse/mental-health-considerations.pdf')
pdf.ln(h=3)

pdf.output("Relatório.pdf")

print("O PDF foi criado com sucesso!")
os.system("pause")