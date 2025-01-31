## DICIONÁRIOS - CABEÇALHOS ##
# Muito longos. Impossível de manipular no painel.

novos_cabecalhos = {
    'Carimbo de data/hora': 'data/hora',
    '1. Sexo Biológico': '1.sexo',
    '2. Identidade de gênero': '2.gênero',
    '3. Orientação Sexual': '3.orientação_sexual',
    '4. Cor ou raça': '4.cor_raça',
    '5. Portador de necessidades especiais': '5.necessidades_especiais',
    '6. Onde cursou o Ensino Médio?': '6.ensino_medio',
    '7. Nacionalidade': '7.nacionalidade',
    '8. Curso': '8.curso',
    '9. Onde cursou a Graduação?': '9.graduação',
    '10. Você está vinculado(a) a qual Departamento? ': '10.depto',
    '11.  A classificação dos ingressantes para distribuição de bolsas no Programa de Pós-Graduação em Física se baseia nos critérios descritos abaixo. Qual a sua opinião sobre esse sistema de classificação? ': '11.aval_classificação_bolsas',
    '12. Como você avalia o atendimento e apoio da Secretaria de Pós-Graduação aos estudantes (e-mail e presencial)?': '12.aval_secretaria',
    '13. Como você avalia a página (homepage) da Comissão de Pós-Graduação, considerando sua funcionalidade e qualidade da informação disponível?': '13.aval_home_page',
    '14. Como você avalia a recepção aos ingressantes na pós-graduação do IFUSP? ': '14.aval_recepção',
    '15. Como você avalia o conjunto de todas as disciplinas oferecidas pelo Programa de Pós-Graduação? ': '15.aval_disciplinas',
    '16. Como você avalia o conjunto das disciplinas de Pós-Graduação que você já cursou?': '16.aval_disciplinas_cursadas',
    '17. Como você avalia seu interesse nas disciplinas de Pós-Graduação? ': '17.aval_interesse_disciplinas',
    '18. Como você avalia a infraestrutura das salas de aula, incluindo a qualidade predial, móveis, lousas e projetores?': '18.aval_infra_salas',
    '19. Você assistiu a aulas remotas durante a pandemia?': '19.aulas_remotas_bool',
    '20. Caso tenha respondido "sim" à pergunta anterior, como avalia a qualidade das aulas remotas?': '20.aval_aulas_remotas',
    '21. Você tem preferência por aulas de Pós-Graduação em qual formato?': '21.formato_prefe_aulas',
    '22. Como você avalia o número de créditos de disciplinas exigidos no Mestrado?': '22.aval_creditos_me',
    '23. Como você avalia o número de créditos de disciplinas exigidos no Doutorado?': '23.aval_creditos_do',
    '24. Como você avalia o número de créditos de disciplinas exigidos no Doutorado Direto?': '24.aval_creditos_dd',
    '25. O seu projeto de pesquisa melhor se enquadra em qual grande área da Física?': '25.area_física',
    '26. O seu projeto de pesquisa é predominantemente ': '26.predomina_pesquisa',
    '27. Suas atividades de pesquisa utilizam, principalmente:': '27.uso_equip_lab',
    '28. Como você avalia a infraestrutura do(s) laboratório(s) de pesquisa que você mais utiliza?': '28.aval_infra_lab',
    '29. Como você avalia o corpo técnico de apoio e manutenção do(s) laboratório(s) de pesquisa que você mais utiliza?': '29.aval_tecnicos_lab',
    '30. Como você avalia a disponibilidade de recursos e equipamentos de laboratório  importantes para sua pesquisa?': '30.aval_disponibilidade_lab',
    '31. Como você avalia o apoio do seu grupo para realização das atividades de pesquisa ou visitas técnicas nos(s) laboratório(s) que você mais utiliza?': '31.aval_apoio_grupo_lab',
    '32. Suas atividades de pesquisa utilizam, principalmente:': '32.infra_computacional',
    '33. Como você avalia a infraestrutura computacional mais frequentemente utilizada em sua pesquisa?': '33.aval_infra_computacional',
    '34. Como você avalia o corpo técnico de apoio e manutenção dos centros de computação ou clusters que você mais utiliza?': '34.aval_tecnico_computacional',
    '35. Como você avalia a disponibilidade da infraestrutura computacional mais importante para sua pesquisa (disponibilidade de software e hardware, tempo em filas de submissão de jobs, etc.)? ': '35.aval_disponib_computacional',
    '36. Como você avalia o apoio do seu grupo para o desenvolvimento do seu projeto de pesquisa?': '36.aval_apoio_grupo_desenvolvimento',
    '37. Como você avalia o apoio, dentro da colaboração em que você trabalha, para realização de suas atividades de pesquisa e/ou visitas técnicas?': '37.aval_apoio_grupo_atividade',
    '38. Como você avalia a qualidade das discussões científicas em seu grupo de pesquisa considerando reuniões, seminários e journal clubs?': '38.aval_discussões_grupo',
    '39. Como você avalia as condições de trabalho e acomodações disponíveis em seu departamento ou grupo de pesquisa? (Por exemplo, disponibilidade de sala e/ou mobiliário.) ': '39.aval_condições_trabalho',
    '40. Com que frequência você faz empréstimos ou consulta o acervo físico (livros e periódicos) da biblioteca do IFUSP?': '40.freq_biblioteca',
    '41. Como você avalia a importância do acervo físico da biblioteca do IFUSP (livros e periódicos) para sua pós-graduação?': '41.aval_importancia_biblioteca',
    '42. Como você avalia o acesso a periódicos digitais oferecido pelo sistema de bibliotecas da USP?': '42.aval_pedio_dig_biblioteca',
    '43. Qual o seu meio de acesso mais frequente a periódicos digitais?': '43.tipo_acesso_periodicos',
    '44. Como você avalia a importância do acervo de periódicos digitais, contabilizando todas as bases disponíveis, para sua pós-graduação?': '44.aval_impotancia_period_dig',
    '45. Como você avalia o seu interesse pelos Colóquios do IFUSP e seminários departamentais?': '45.aval_coloquios',
    '46. Como você avalia a relevância dos Colóquios e seminários departamentais para sua formação?': '46.aval_import_coloquios_dpto',
    '47. Como você avalia a relevância dos seminários ou journal clubs em seu grupo de pesquisa para sua formação?': '47.aval_import_semi_journal',
    '48. Como você avalia a obrigatoriedade do estágio PAE na pós-graduação?': '48.aval_obrigatoriedade_pae',
    '49. Como você avalia a importância das atividades de monitoria (PAE e outras) para sua formação?': '49.aval_import_monioria',
    '50. Como você avalia a importância das bolsas de monitoria para sua renda pessoal ou familiar?': '50.import_bolsa_monitoria',
    '51. Você tem dependentes financeiros (filhos(as), pai, mãe, cônjuge ou parentes)?  ': '51.dependentes_financ',
    '52. Você realizou ou realiza atividades profissionais paralelas à Pós-Graduação? Considere aulas em qualquer nível, aulas  particulares, atividades voluntárias ou de outra natureza, mas desconsidere monitorias.': '52.ativ_paralela',
    '53. Qual opção melhor descreve suas atividades paralelas?': '53.descrição_atividades_paralela',
    '54. Suas atividades paralelas são (foram) realizadas principalmente em qual turno?': '54.turno_ativid_paralela',
    '55. Em média, quantas horas semanais são (foram) dedicadas às atividades paralelas?': '55.horas_ativid_paralela',
    '56. Considere a soma da mensalidade da sua bolsa de Pós-Graduação com o seu ganho mensal com atividades paralelas. As atividades paralelas correspondem (correspondiam), aproximadamente, a qual percentual dessa soma:': '56.percent_ativi_paralela',
    '57. Qual o principal motivo para ter buscado atividades paralelas?': '57.motivo_ativid_paralela',
    '58. Com qual frequência você vem ao IFUSP? Indique a alternativa que mais se aproxima.': '58.freq_ifusp',
    '59. Quais os principais motivos que levam você a frequentar o IFUSP? Indique todas as opções que julgar relevantes.': '59.motivo_freq_ifusp',
    '60. Como você avalia o ambiente social do IFUSP, considerando o convívio com colegas de pós-graduação, servidores(as) e docentes?': '60.aval_ambiente_ifusp',
    '61. Como você descreveria seu sentimento de pertencimento ao IFUSP?': '61.sent_pertencimento',
    '62. Como você descreveria seu convívio com colegas de pós-graduação?': '62.sent_colegas',
    '63. Caso você seja estrangeiro e tenha ingressado no IFUSP diretamente na pós-graduação (graduação em outra instituição), como avalia sua inserção junto aos colegas? ': '63.aval_estrang_inserção',
    '64. Caso você seja brasileiro, mas não tenha sido aluno de Graduação no IFUSP, como avalia sua inserção junto aos colegas?': '64.aval_insercao_br_externo',
    '65. Como você avalia o ambiente acadêmico entre os estudantes de Pós-Graduação do IFUSP? Considere o respeito, reconhecimento, abertura para discussões científicas, disponibilidade para ajudar, trocar informações e estudar em grupo. Indique todas as alternativas que julgar relevantes.': '65.palavras_ambiente_colegas',
    '66. Como você avalia o ambiente entre professores(as) e estudantes nas disciplinas de pós-graduação? Considere respeito, reconhecimento, incentivo/motivação e o ambiente para aprendizagem e discussão. Indique todas as alternativas que julgar relevantes.': '66.palavras_ambient_prof',
    '67. Como você avalia o ambiente entre orientador(a) e colegas em seu grupo de pesquisa? Considere respeito, reconhecimento, incentivo/motivação e o ambiente para aprendizagem e discussão. Indique todas as alternativas que julgar relevantes.': '67.palavras_ambient_grupo',
    '69. Você tem conhecimento sobre o Acolhimento Integrado do IFUSP, que oferece apoio psicológico dentre outras atividades?': '69.acolhimento_bool',
    '70. Você já procurou o Acolhimento Integrado?': '70.procurou_acolhimento',
    '71. Quais os principais motivos que levaram você a procurar o Acolhimento Integrado? Indique todas as alternativas que julgar relevantes.': '71.motivo_acolhimento',
    '72. Você procurou o Acolhimento Integrado': '72.colhimento_covid',
    '73. Você tem conhecimento sobre a Ouvidoria do IFUSP, que acolhe denúncias de assédio (dentre outras), reclamações e sugestões?': '73.conhece_ouvidoria',
    '74. Você se sente seguro(a) para procurar a Ouvidoria? Indique todas as alternativas que julgar relevantes.': '74.seguro_proc_ouvidoria',
    '75. Você já apresentou denúncia ou reclamação na Ouvidoria do IFUSP?': '75.denuncia_ouvidoria',
    '76. Você entende já ter sido vítima de assédio no IFUSP?': '76.sofreu_assedio',
    '50. Como você avalia a importância das bolsas de monitoria para sua renda pessoal ou familiar?': '50.import_bolsa_monitoria',
    'Unnamed: 76': 'Unnamed: 76',
    '68. Em algum momento você pensou em procurar ajuda de profissionais de saúde mental (psicólogos e/ou psiquiatras) por motivo relacionado à sua pós-graduação?': '68.ajuda_saude_mental',
    'Unnamed: 78': 'Unnamed: 78',
    '75. Você entende que o assédio sofrido no IFUSP se relaciona a qual característica? Indique todas as alternativas que julgar relevantes.': '',
    '76. Você classificaria o assédio sofrido no IFUSP como': '76.tipo_assedio',
    '77. Você entende ter sofrido assédio no IFUSP por parte de quem? Indique todas as alternativas que julgar relevantes.': '77.origem_assedio'
}

## DICIONÁRIOS - SENTIMENTOS ##

sentimentos = {
    'saudavel': 'positivo',
    'positivamente_competitivo': 'positivo',
    'frio_distante': 'negativo',
    'proximo_caloroso': 'positivo',
    'aberto_acolhedor': 'positivo',
    'toxico': 'negativo',
    'negativamente_competitivo': 'negativo',
    'preconceituoso_discriminatorio': 'negativo',
    'distante': 'negativo',
    'respeitoso': 'positivo',
    'motivador': 'positivo',
    'receptivo': 'positivo',
    'acolhedor': 'positivo',
    'desrespeitoso': 'negativo',
    'rigido': 'negativo',
    'inspirador': 'positivo',
    'opressor': 'negativo',
    'desmotivador': 'negativo',
    'caloroso': 'positivo',
    # '-' é ignorado
    # Repetições de palavras são ignoradas, pois o dicionário não permite chaves duplicadas
}

## DICIONÁRIOS - VALORES ##
# transformação da avaliação por conceito (strings) para números. Dessa forma é possível usar gráficos para comparação 
suficiencia= {"muito insuficiente":-2,
            "insuficiente":-1,
            "razoável":0,
            "suficiente":1,
            "mais que suficiente":2
            }

qualidade={"ótimo": 5,
           "ótima": 5,
           "ótimas":5,
           "boa": 4,
           "boas": 4,
           "bom": 4,
           "razoável": 3,
           "razoáveis":3,
           "regular": 3,
           "ruim": 2,
           "ruins": 2,
           "péssima": 1,
           "péssimas":1,
           "péssimo": 1
        }

excesso = {"muito insuficiente": -2,
        "insuficiente": -1,
        "adequado": 0,
        "excessivo": 1,
        "muito excessivo": 2
        }

frequencia = {"nunca": 1,
              "raramente": 2,
              "ocasionalmente": 3,
              "frequentemente": 4,
              "continuadamente": 5
              }

interesse = {"muito interessado(a)": 5,
             "medianamente interessado(a)": 4,
             "pouco interessado(a)": 3,
             "interessado(a)": 2,
             "desinteressado(a)": 1
             }

interesse2 = {"não me interesso": 1,
            "me interesso pouco": 2,
            "me interesso medianamente": 3,
            "me interesso": 4,
            "me interesso muito": 5
}

relevancia = {"irrelevante": 1,
            "pouco relevante": 2,
            "razoavelmente relevante": 3,
            "relevante": 4,
            "muito relevante": 5
}

corcorda = {"discordo completamente": 1,
        "discordo parcialmente": 2,
        "indiferente": 3,
        "concordo parcialmente": 4,
        "concordo completamente": 5
}

horas_atividade = {
        "até 4 horas semanais": 4,
        "até 8 horas semanais": 8,
        "até 12 horas semanais": 12,
        "até 16 horas semanais": 16,
        "até 20 horas semanais": 20,
        "mais que 20 horas semanais": 24
}

percent_ativid = {  
    "0% (trabalho voluntário)": 0,
    "até 25%": 0.25,
    "até 50%": 0.5,
    "até 75%": 0.75,
    "entre 75% e 100%": 1.0,
    "100% (não tenho/tinha bolsa quando realizei as atividades)": np.nan
}


# Descartar valores nulos que "sujam" os vetores númericos
nulos = {"não se aplica a minha pesquisa":None,
         "ainda não sei avaliar":None,
         "não tenho opInião":None,
         "não tenho opinião formada":None,
         "não se aplica (pesquisa não inserida em colaboração)":None,
         "não utilizo o suficiente para opinar":None,
         "ainda não realizei atividades de monitoria":None,
         "não utilizo o suficiente para opinar": None
}

# Respostas muito longas. Atrapalham na visualização dos gráficos

ensino_medio = {
    'Todo em escola particular': 'particular total',
    'Parte ou todo em escolas técnicas Federais ou Estaduais': 'tec fed estadual',
    'Todo em escola pública (não técnica)': 'publica total',
    'Parte ou todo em escolas técnicas privadas (e.g. Liceu de Artes e Ofícios, Senai)': 'tec privada',
    'Parte em escola pública parte em particular': 'publica particular'
}

uso_equip_lab = {
    'equipamentos externos à USP (outras universidades, Sirius, CERN, etc)': 'equip ext USP',
    'nan': None,
    'equipamentos disponíveis no laboratório do seu grupo de pesquisa no IFUSP': 'equip lab grupo IFUSP',
    'equipamentos multiusuários disponíveis no IFUSP': 'equip multi IFUSP',
    'equipamentos disponíveis em laboratórios de outras unidades da USP': 'equip outros lab USP',
    'equipamentos multiusuários disponíveis em outras unidades da USP': 'equip multi outros USP'
}

infra_computacional = {
    'infraestrutura computacional do seu grupo de pesquisa no IFUSP': 'infra grupo IFUSP',
    'nan': None,
    'infraestrutura computacional multiusuário da USP (por exemplo, USP Cloud, cluster AGUIA)': 'infra multi USP',
    'infraestrutura computacional multiusuário externa à USP (por exemplo, CENAPAD, Santos Dumont ou similar no exterior)': 'infra multi ext USP',
    'infraestrutura computacional de grupos de pesquisa externos ao IFUSP (colaboradores no país ou exterior)': 'infra grupos ext IFUSP'
}

tipo_acesso_periodicos = {
    'base de periódicos do sistema de bibliotecas da USP': 'periodicos USP',
    'periódicos com acesso aberto': 'acesso aberto',
    'base de periódicos da CAPES': 'periodicos CAPES',
    'outros': 'outros'
}

motivo_ativid_paralela = {
    'nan': None,
    'tenho interesse pessoal ou profissional nas atividades profissionais que realizo(zei) paralelamente': 'interesse pessoal profissional',
    'complemento de renda, pois o valor da bolsa é/era insuficiente': 'complemento renda',
    'outro': 'outro',
    'não tenho/tinha bolsa': 'sem bolsa',
    'meu principal interesse ou ocupação são/foram as atividades paralelas': 'interesse principal atividades paralelas'
}

aval_estrang_inserção = {
    'não se aplica (sou brasileiro ou cursei Graduação no IFUSP)': 'nao aplica brasileiro IFUSP',
    'muito entrosado com colegas brasileiros e estrangeiros, a nacionalidade não foi uma barreira': 'entrosado sem barreira',
    'restrita a colegas de mesma nacionalidade': 'restrita mesma nacionalidade',
    'restrita a outros(as) colegas estrangeiros': 'restrita estrangeiros',
    'entrosado com colegas brasileiros e estrangeiros, a nacionalidade foi uma barreira fácil de superar': 'entrosado barreira facil',
    'restrita a colegas de mesma língua nativa': 'restrita mesma lingua'
}

aval_insercao_br_externo = {
    'não se aplica (sou estrangeiro ou fui aluno de graduação no IFUSP)': 'nao aplica estrangeiro IFUSP',
    'muito ampla, não considero a Instituição ou localidade de origem uma barreira': 'ampla sem barreira',
    'restrita a colegas que cursaram a graduação na minha Instituição de origem': 'restrita mesma instituicao',
    'ampla, a Instituição ou localidade de origem não constitui barreira importante': 'ampla sem barreira',
    'restrita a colegas oriundos da minha cidade ou estado de origem': 'restrita mesma cidade estado',
    'restrita a colegas que também não cursaram graduação no IFUSP': 'restrita nao IFUSP'
}

procurou_acolhimento = {
    'ainda não procurei por falta de tempo, mas gostaria': 'nao procurei falta tempo',
    'não, pois nunca senti necessidade': 'nao necessidade',
    'não, pois desconhecia': 'nao desconhecia',
    'sim, já procurei': 'sim procurei',
    'ainda não procurei por me sentir constrangido(a) ou inseguro(a), mas gostaria': 'nao procurei constrangido inseguro'
}

ajuda_saude_mental = {
    'Sim, mas sem urgência. Há questões relacionadas à pós-graduação, mas sem prejuízo significativo.': 'sim sem urgencia',
    'Não, sem pretensão de procurar ajuda de profissionais de saúde mental.': 'nao sem pretensao',
    'Sim, com urgência, devido a sintomas, vontade de desistir/trancar o curso ou dificuldades com a rotina.': 'sim com urgencia',
    'Não, mas com pretensão de buscar ajuda caso vivencie alguma situação paralisante ou estressora.': 'nao com pretensao',
    'Não, pois já estava em acompanhamento com profissional antes de ingressar na pós-graduação.': 'nao ja acompanhamento'
}

trocas_respostas = {
"convívio com amigos(as) ou colegas de pós-graduação": "convívio com amigos e colegas",
"me sentir excessivamente pressionado por meu orientador (minha orientadora)": "senti pressão do orientador(a)",
"reuniões ou seminários do grupo de pesquisa": "reuniões do grupo de pesquisa",
"problemas pessoais ou relacionais externos ao IFUSP": "problemas pessoais",
"colóquios ou seminários departamentais": "colóquios e seminários",
"não, pois tenho medo de exposição no ambiente do IFUSP": "não, medo de exposição",
"não, pois não entendo como funciona a Ouvidoria": "não, desconheço funcionamento da Ouvidoria",
"não, pois tenho dúvidas quanto ao apoio institucional": "não, desconheço Apoio Inst.",
"não, pois tenho medo de perder minha bolsa":"não, medo de perder a bolsa",
"pois tenho medo de exposição em redes sociais": "não, medo de exposição em redes sociais",
"não, pois tenho medo de retaliações": "não, medo de retaliações",
"me sentir excessivamente pressionado por professores(as)":"senti pressão do prof.(a)",
"monitoria (PAE": 'monitoria PAE',
"etc)":None
}

