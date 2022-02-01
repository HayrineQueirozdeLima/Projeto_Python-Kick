import os
from fpdf import FPDF

# cria um PDF
# Tipo de documento (P - Vetical, L - Horizontal)
# Unidade de medida (mm, cm, in)
# Formato do documento (A3, A4, A5, Latter e Legal)
pdf = FPDF("p", "mm", "A4")

# cria uma página para o PDF
pdf.add_page()

# Nome da fonte, formato (B, U, I ou '') e o tamanho
pdf.set_font('Arial', '', 12)

pdf.image(name="kick.png", w=25, h=10, y=5, x=180)

pdf.line(5, 15, 205, 15)

pdf.image(name="Gráfico-Total_de_casos_por_dia_no_estado_de_São_Paulo.png", w=100, y=125, x=9)
pdf.image(name="Gráfico - Total de óbitos por dia no estado de São Paulo.png", w=100, y=125, x=110)
# pdf.image(name="grafico_barras_casos_10m.png", w=200, y=165, x=9)
# pdf.image(name="grafico_barras_obitos_10m.png", w=200, y=360, x=9)

p = 'Hayrine Queiroz de Lima\nPorto Velho - RO\n2022\n\n\n                                                             SAÚDE MENTAL NA PANDEMIA\n\n\n     Em janeiro de 2020, a Organização Mundial da Saúde (OMS) declarou o surgimento de uma nova doença provocada por um vírus do tipo coronavírus - a Covid-19. Foi considerada uma emergência de saúde pública de interesse internacional, com alto risco de se espalhar para outros países ao redor do mundo. Em março de 2020, a OMS avaliou que a Covid-19 caracterizava-se como uma pandemia.\n\n     A agenda de saúde frente à pandemia engloba uma gama enorme de áreas que devem ser cobertas, mas é preciso chamar a atenção da comunidade médica e, também, da população para o risco de uma epidemia paralela, que já dá indícios preocupantes: o aumento do sofrimento psicológico, dos sintomas psíquicos e dos transtornos mentais. Embora o impacto da disseminação do coronavírus para as doenças psíquicas ainda esteja sendo mensurado, as implicações para a saúde mental em situações como a que estamos vivendo já foram relatadas na literatura científica.\n\n\n SAÚDE MENTAL\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNa média global, 45 por cento dos cerca de 21 mil entrevistados pelo Ipsos afirmaram que sua saúde mental piorou pouco ou muito no último ano, sob a pandemia.\n\n        Mais da metade dos brasileiros entrevistados por uma pesquisa declararam que sua saúde emocional e mental piorou desde o início da pandemia, em índice superior à média dos 30 países e territórios pesquisados.\n\n       Outros estudos sobre o mesmo tema também trazem dados preocupantes.\n\n       Um deles, publicado pela Fiocruz com outras seis universidades em meados do ano passado, dizia que "sentimentos frequentes de tristeza e depressão afetavam 40 por cento da população adulta brasileira, e sensação frequente de ansiedade e nervosismo foi relatada por mais de 50 por cento das pessoas".\n\n       Um relatório de 2017 da Organização Mundial da Saúde (OMS) apontava o Brasil como o país com a maior prevalência de transtornos de ansiedade nas Américas: o problema afetava 9,3 por cento da população, o equivalente a 18,6 milhões de pessoas.\n\n        Transtornos depressivos foram relatados por 5,8 por cento dos brasileiros, ou 11,5 milhões de pessoas.\n\n     De fato, vemos como isso é um problema aqui no Brasil (com as pesquisas), e a situação atual da pandemia tem pesado muito. As notícias são muito tristes, e (com o isolamento social e a perda de redes de apoio) as pessoas têm perdido as estratégias para lidar com isso.\n\n        Uma das consequências da pandemia é o aumento de transtornos mentais e do trauma psicológico provocados diretamente pela infecção ou por seus desdobramentos secundários.\n\n      As pessoas reagem de maneira diferente a situações estressantes. Como cada um responde à pandemia pode depender de sua formação, da sua história de vida, das suas características particulares e da comunidade em que vive. Os grupos que podem responder mais intensamente ao estresse de uma crise incluem: Pessoas idosas ou com doenças crônicas que apresentam maior risco se tiverem Covid-19; Profissionais de saúde que trabalham no atendimento à Covid-19; Pessoas que têm transtornos mentais, incluindo problemas relacionados ao uso de substâncias.\n\n       O aumento dos sintomas psíquicos e dos transtornos mentais durante a pandemia pode ocorrer por diversas causas. Dentre elas, pode-se destacar a ação direta do vírus da Covid-19 no sistema nervoso central, as experiências traumáticas associadas à infeção ou à morte de pessoas próximas, o estresse induzido pela mudança na rotina devido às medidas de distanciamento social ou pelas consequências econômicas, na rotina de trabalho ou nas relações afetivas e, por fim, a interrupção de tratamento por dificuldades de acesso.\n\n     Esses cenários não são independentes. Ou seja, uma pessoa pode ter sido exposta a várias destas situações ao mesmo tempo, o que eleva o risco para desenvolver ou para agravar transtornos mentais já existentes.\n\n       O distanciamento social alterou os padrões de comportamento da sociedade, com o fechamento de escolas, a mudança dos métodos e da logística de trabalho e de diversão, minando o contato próximo entre as pessoas, algo tão importante para a saúde mental.\n\n       O convívio prolongado dentro de casa aumentou o risco de desajustes na dinâmica familiar. Somam-se a isso as reduções de renda e o desemprego, que pioram ainda mais a tensão sobre as famílias. E, ainda, as mortes de entes queridos em um curto espaço de tempo, juntamente à dificuldade para realizar os rituais de despedida, dificultando a experiência de luto e impedindo a adequada ressignificação das perdas, aumentando o estresse.\n\n\n        Algumas reações comuns são:\n\n    ->O medo de ficar doente e morrer;\n   ->Evitação de procurar um serviço de saúde por outros motivos, por receio de se contaminar; medo de perder a fonte de renda, por não poder trabalhar, ou ser demitido;\n  ->Alterações do sono, da concentração nas tarefas diárias, ou aparecimento de pensamentos intrusivos;\n  ->Sentimentos de desesperança, tédio, solidão e depressão devido ao isolamento;\n    ->Raiva, frustração ou irritabilidade pela perda de autonomia e liberdade pessoal;\n   ->Medo de ser socialmente excluído ou estigmatizado por ter ficado doente;\n  ->Sentir-se impotente em proteger as pessoas próximas, ou medo de ser separado de familiares por motivo de quarentena/isolamento;\n  ->Preocupação com a possibilidade de o indivíduo ou de membros de sua família contraírem a Covid-19 ou a transmitirem a outros;risco de deterioração de doenças clínicas e de transtornos mentais prévios ou, ainda, do desencadeamento de transtornos mentais;\n    ->Risco de adoecimento de profissionais de saúde sem ter substituição adequada;\n  ->Medo, ansiedade ou outras reações de estresse ligadas a notícias falsas, alarmistas ou sensacionalistas, e mesmo ao grande volume de informações circulando.\n\n\nMais pesquisas sobre o caso:\n\n      Uma pesquisa da Workana (2020) mostra que 43,7 por cento dos trabalhadores sentiram algum sintoma de prejuízo mental durante a pandemia. Entre os pesquisados, 24 por cento sentiram dificuldade de se concentrar. 13,2 por cento sentiram ansiedade. 5,8 por cento sentiram solidão e 0,8 por cento sentiram depressão ou claustrofobia.\n\n       Para compreender  algumas das diversas mudanças que a pandemia trouxe para o cotidiano dos brasileiros nos últimos meses, a Mastercard realizou uma pesquisa em 13 países, incluindo Brasil, México, Chile, Colômbia, Argentina e Peru.\n\n        O levantamento analisou dados do dia a dia dos entrevistados e os que se destacam mostram como as pessoas têm novas prioridades no Brasil, incluindo começar a cuidar da saúde mental.\n\n       Apesar de ser reconhecido pelas suas vantagens, o home office pode ser uma das causas de transtornos de ansiedade e de excesso de trabalho. Um levantamento feito por uma empresa de dados verificou que os comentários das pessoas nas redes sociais foram menos favoráveis ao trabalho remoto conforme os meses passaram neste ano.\n\n       Outro dado alarmante descoberto no mês de novembro de 2020 pela empresa de consultoria Falconi foi o aumento de doenças psiquiátricas como depressão ou distúrbios emocionais como burnout. Taxas maiores foram registradas por 37 por cento das empresas.\n\n      A Organização Pan-Americana de Saúde (Opas) alertou, nesta quinta-feira, 5, que os efeitos da pandemia de covid-19 na saúde mental das pessoas provavelmente "persistirão" depois que o vírus for controlado e alertou sobre dados "preocupantes" entre os profissionais de saúde.\n\n\nAlgumas dicas para lidar com a situação\n\n__Tenha pequenos momentos de lazer, que te tragam satisfação\n__Cuidado com o uso de substâncias tóxicas, como álcool, tabaco e outras drogas\n__Cuidado com as cobranças digitais\n__Separe o lazer do trabalho e não fique online o tempo inteiro\n__Cuide do sono e escolha ambientes escuros para dormir\n__Identificar os sinais de que saúde mental não vai bem é o primeiro (e fundamental) passo. Alguns deles são: perda de prazer em atividades que você gosta, alterações no sono e no apetite e grande dificuldade de concentração\n__Procure ajuda médica sempre que necessário, e não tente resolver tudo sozinho(a). Todo sofrimento pode e deve ser aliviado, e o SUS oferece atendimento nas UBS, nos CAPS e nos ambulatórios de saúde mental\n__Reconhecer e acolher seus receios e medos, procurando pessoas de confiança para conversar;\n__Reenquadrar os planos e estratégias de vida, de forma a seguir produzindo planos de forma adaptada às condições associadas à pandemia.\n__Buscar fontes confiáveis de informação, como o site da Organização Mundial da Saúde\n__Reduzir o tempo que passa assistindo ou ouvindo coberturas midiáticas.\n__Manter ativa a rede socioafetiva, estabelecendo contato, mesmo que virtual, com familiares, amigos e colegas;\n__Retomar estratégias e ferramentas de cuidado que tenha usado em momentos de crise ou sofrimento e ações que trouxeram sensação de maior estabilidade emocional;\n__Investir em exercícios e ações que auxiliem na redução do nível de estresse agudo (meditação, leitura, exercícios de respiração, entre outros mecanismos que auxiliem a situar o pensamento no momento presente), bem como estimular a retomada de experiências e habilidades usadas em tempos difíceis do passado para gerenciar emoções durante a epidemia.\n\n\n\nFalar sobre saúde mental nunca foi tão importante quanto em tempos de pandemia.'
pdf.multi_cell(w=0,h=5, txt=p, align='J')

pdf.image(name="img1.png", w=115, y=90, x=9)
pdf.image(name="img2.png", w=125, y=125, x=85)
pdf.image(name="img3.png", w=120, y=230, x=15)

pdf.output("Relatório.pdf")

print("O PDF foi criado com sucesso!")
os.system("pause")