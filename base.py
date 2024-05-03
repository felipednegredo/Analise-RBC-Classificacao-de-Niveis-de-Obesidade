import pandas as pd
import os

# Valores de peso_base de IMC (Índice de Massa Corporal)
IMC_VALORES = [[1.00, 0.50, 0.25], [0.50, 1.00, 0.50], [0.25, 0.50, 1.00]]

# Valores de peso_base de BQLDAD (Quantos litros de água você bebe diariamente?)
BQLDAD_VALORES = [[1.00, 0.60, 0.10],
                  [0.60, 1.00, 0.60],
                  [0.10, 0.60, 1.00]]

# Valores de peso_base de BACDF (Bebe álcool com frequencia?)
BACDF_VALORES = [[1.00, 0.80, 0.50, 0.00],
                 [0.80, 1.00, 0.50, 0.30],
                 [0.50, 0.50, 1.00, 0.80],
                 [0.00, 0.30, 0.80, 1.00]]

# Valores de peso_base de QVZCLESR (Quantas vezes costuma comer legumes nas suas refeições?)
QVZCLESR_VALORES = [[1.00, 0.80, 0.40, 0.00],
                    [0.80, 1.00, 0.80, 0.40],
                    [0.40, 0.80, 1.00, 0.80],
                    [0.00, 0.40, 0.80, 1.00]]

# Valores de peso_base de QRTND (Quantas refeições principais tem diariamente?)
QRTND_VALORES = [[1.00, 0.80, 0.40, 0.20],
                 [0.80, 1.00, 0.80, 0.40],
                 [0.40, 0.80, 1.00, 0.80],
                 [0.20, 0.40, 0.80, 1.00]]

# Valores de peso_base de CQFPAF (Com que frequência tem atividade física?)
CQFPAF_VALORES = [[1.00, 0.00, 0.00],
                  [0.00, 1.00, 0.50],
                  [0.00, 0.50, 1.00]]

# Valores de peso_base de VCQAEAR (Come qualquer alimento entre as refeições?)
VCQAEAR_VALORES = [[1.00, 0.20, 0.20, 0.00],
                   [0.20, 1.00, 0.50, 0.50],
                   [0.20, 0.50, 1.00, 0.80],
                   [0.00, 0.50, 0.80, 1.00]]

# Valores de peso_base de QTCU (Qual transporte costuma usar?)
QTCU_VALORES = [[1.00, 0.90, 0.00, 0.00, 0.00],
                [0.90, 1.00, 0.00, 0.00, 0.00],
                [0.00, 0.00, 1.00, 1.00, 1.00],
                [0.00, 0.00, 1.00, 1.00, 1.00],
                [0.00, 0.00, 1.00, 1.00, 1.00]]

'''
PESOS_POR_ATRIBUTO = [
    0.2, # Idade
    0.4, # Genero
    0.9, # Bebe álcool com frequencia?
    0.5, # Você come alimentos com alto teor calórico com frequência?
    0.6, # Quantas vezes costuma comer legumes em suas refeições?
    0.7, # Quantas refeições principais você tem diariamente?
    0.5, # Você monitora as calorias que você come diariamente?
    0.3, # Você fuma?
    0.5, # Quanta litros de água você bebe diariamente?
    0.8, # Um membro da família sofreu ou sofre de excesso de peso?
    0.7, # Com que frequência você tem atividade física?
    0.6, # Você come qualquer alimento entre as refeições?
    0.5, # Qual transporte você costuma usar?
    1, # IMC
    Peso total = 8,2
]
'''


def ler_base():
    """Função para ler a base de dados.
        Returns:
        data: Lista de dicionários com os dados
    """

    diretorio_atual = os.path.dirname(os.path.realpath(__file__))
    # Construa o caminho para o arquivo "azure.tcl" usando o diretório atual
    caminho_base_xlsx = os.path.join(diretorio_atual, "..", "Trabalho_IA_M2", "Obesidade_V2.xlsx")

    # Ler o arquivo Excel
    dataframe = pd.read_excel(caminho_base_xlsx, 'Obesidade - Tratado')

    casos_base = []

    # Carregar os dados
    for i, r in dataframe.iterrows():
        idade = (r['Idade'])
        genero = (r['Genero'])
        BACDF = (r['Bebe álcool com frequencia?'])
        CACATCCF = (r['Você come alimentos com alto teor calórico com frequência?'])
        QVZCLESR = (r['Quantas vezes costuma comer legumes em suas refeições?'])
        QRTND = (r['Quantas refeições principais você tem diariamente?'])
        MACQCD = (r['Você monitora as calorias que você come diariamente?'])
        FUMA = (r['Você fuma?'])
        BQLDAD = (r['Quanta litros de água você bebe diariamente?'])
        AMDFSOSCEDP = (r['Um membro da família sofreu ou sofre de excesso de peso?'])
        CQFPAF = (r['Com que frequência você tem atividade física?'])
        VCQAEAR = (r['Você come qualquer alimento entre as refeições?'])
        QTCU = (r['Qual transporte você costuma usar?'])
        IMC = (r['IMC'])
        NO = (r['Nível de obesidade'])
        casos_base.append(
            [i, idade, genero, BACDF, CACATCCF, QVZCLESR, QRTND, MACQCD, FUMA, BQLDAD, AMDFSOSCEDP, CQFPAF, VCQAEAR,
             QTCU,
             IMC, NO])

    # Transformar os dados em um DataFrame
    df = pd.DataFrame(casos_base, columns=['Index', 'Idade', 'Genero', 'Bebe álcool com frequencia?',
                                           'Você come alimentos com alto teor calórico com frequência?',
                                           'Quantas vezes costuma comer legumes em suas refeições?',
                                           'Quantas refeições principais você tem diariamente?',
                                           'Você monitora as calorias que você come diariamente?', 'Você fuma?',
                                           'Quanta litros de água você bebe diariamente?',
                                           'Um membro da família sofreu ou sofre de excesso de peso?',
                                           'Com que frequência você tem atividade física?',
                                           'Você come qualquer alimento entre as refeições?',
                                           'Qual transporte você costuma usar?', 'IMC', 'Nível de obesidade',
                                           ])

    # Convert the DataFrame to a list of dictionaries
    data = df.to_dict('records')

    return data


def definir_similaridade(casos_base, novo_caso, PESOS_POR_ATRIBUTO):
    """Função para definir a peso_base entre os casos da base e o novo caso.
        Args:
        casos_base: Lista de dicionários com os casos da base
        novo_caso: Lista com os valores do novo caso
        Returns:
            object:
        casos_base: Lista de dicionários com os casos da base e a peso_base
    """
    peso_total = 0

    for peso in PESOS_POR_ATRIBUTO:
        peso_total += float(PESOS_POR_ATRIBUTO[peso])

    print(f"O Peso Total é de: {peso_total}")
    for caso in casos_base:
        peso_base = 0
        idade = caso["Idade"]
        genero = caso["Genero"]
        BACDF = caso["Bebe álcool com frequencia?"]
        CACATCCF = caso["Você come alimentos com alto teor calórico com frequência?"]
        QVZCLESR = caso["Quantas vezes costuma comer legumes em suas refeições?"]
        QRTND = caso["Quantas refeições principais você tem diariamente?"]
        MACQCD = caso["Você monitora as calorias que você come diariamente?"]
        FUMA = caso["Você fuma?"]
        BQLDAD = caso["Quanta litros de água você bebe diariamente?"]
        AMDFSOSCEDP = caso["Um membro da família sofreu ou sofre de excesso de peso?"]
        CQFPAF = caso["Com que frequência você tem atividade física?"]  # ARRUMAR
        VCQAEAR = caso["Você come qualquer alimento entre as refeições?"]
        QTCU = caso["Qual transporte você costuma usar?"]
        IMC = round(caso["IMC"], 2)
        max_idade = max([int(caso["Idade"]) for caso in casos_base])
        max_imc = max([float(abs(caso["IMC"])) for caso in casos_base])

        peso_base += PESOS_POR_ATRIBUTO["Idade"] * (1 - abs((idade - int(novo_caso[0])) / max_idade))
        novo_caso[2] = novo_caso[2].replace(',', '.')
        novo_caso[3] = novo_caso[3].replace(',', '.')
        IMC_casoNovo = float(novo_caso[3]) / (float(novo_caso[2]) ** 2)

        peso_base += PESOS_POR_ATRIBUTO["IMC"] * (1 - abs(IMC - float(IMC_casoNovo)) / max_imc)

        if genero == novo_caso[1]:  # Genero
            peso_base += 1 * PESOS_POR_ATRIBUTO["Genero"]

        if CACATCCF == novo_caso[5]:  # Come alimentos com alto teor calórico com frequência?
            peso_base += 1 * PESOS_POR_ATRIBUTO["Você come alimentos com alto teor calórico com frequência?"]

        if MACQCD == novo_caso[8]:  # Você monitora as calorias que você come diariamente? if novo_caso[8] == "Sim":
            peso_base += 1 * PESOS_POR_ATRIBUTO["Você monitora as calorias que você come diariamente?"]

        if FUMA == novo_caso[9]:  # Você fuma?if novo_caso[9] == 'Sim':
            peso_base += 1 * PESOS_POR_ATRIBUTO["Você fuma?"]

        if AMDFSOSCEDP == novo_caso[11]:  # Um membro da família sofreu ou sofre de excesso de peso?
            peso_base += 1 * PESOS_POR_ATRIBUTO["Um membro da família sofreu ou sofre de excesso de peso?"]

        ''' Com que frequência você tem atividade física? '''

        if novo_caso[12] == '0':
            CQFPAF_pos = 0
        elif novo_caso[12] == '1' or novo_caso[12] == '2':
            CQFPAF_pos = 1
        else:
            CQFPAF_pos = 2

        if CQFPAF == 0:  # Com que frequência tem atividade física?
            peso_base += CQFPAF_VALORES[CQFPAF_pos][0] * PESOS_POR_ATRIBUTO[
                "Com que frequência você tem atividade física?"]
        elif CQFPAF == 1 or CQFPAF == 2:
            peso_base += CQFPAF_VALORES[CQFPAF_pos][1] * PESOS_POR_ATRIBUTO[
                "Com que frequência você tem atividade física?"]
        else:
            peso_base += CQFPAF_VALORES[CQFPAF_pos][2] * PESOS_POR_ATRIBUTO[
                "Com que frequência você tem atividade física?"]

        ''' Você come qualquer alimento entre as refeições? '''

        if VCQAEAR == "Nunca":
            VCQAEAR_pos = 0
        elif VCQAEAR == "As Vezes":
            VCQAEAR_pos = 1
        elif VCQAEAR == "Frequente":
            VCQAEAR_pos = 2
        elif VCQAEAR == "Sempre":
            VCQAEAR_pos = 3

        if novo_caso[13] == "Nunca":  # Come qualquer alimento entre as refeições?
            peso_base += VCQAEAR_VALORES[VCQAEAR_pos][0] * PESOS_POR_ATRIBUTO[
                "Você come qualquer alimento entre as refeições?"]
        elif novo_caso[13] == "As Vezes":
            peso_base += VCQAEAR_VALORES[VCQAEAR_pos][1] * PESOS_POR_ATRIBUTO[
                "Você come qualquer alimento entre as refeições?"]
        elif novo_caso[13] == "Frequente":
            peso_base += VCQAEAR_VALORES[VCQAEAR_pos][2] * PESOS_POR_ATRIBUTO[
                "Você come qualquer alimento entre as refeições?"]
        elif novo_caso[13] == "Sempre":
            peso_base += VCQAEAR_VALORES[VCQAEAR_pos][3] * PESOS_POR_ATRIBUTO[
                "Você come qualquer alimento entre as refeições?"]

        ''' Bebe álcool com frequencia? '''

        if BACDF == "Não":  # Bebe álcool com frequencia?
            BACDF_pos = 0
        elif BACDF == "As vezes":
            BACDF_pos = 1
        elif BACDF == "Frequentemente":
            BACDF_pos = 2
        elif BACDF == "Sempre":
            BACDF_pos = 3

        if novo_caso[4] == "Não":
            peso_base += BACDF_VALORES[BACDF_pos][0] * PESOS_POR_ATRIBUTO["Bebe álcool com frequencia?"]
        elif novo_caso[4] == "As vezes":
            peso_base += BACDF_VALORES[BACDF_pos][1] * PESOS_POR_ATRIBUTO["Bebe álcool com frequencia?"]
        elif novo_caso[4] == "Frequentemente":
            peso_base += BACDF_VALORES[BACDF_pos][2] * PESOS_POR_ATRIBUTO["Bebe álcool com frequencia?"]
        elif novo_caso[4] == "Sempre":
            peso_base += BACDF_VALORES[BACDF_pos][3] * PESOS_POR_ATRIBUTO["Bebe álcool com frequencia?"]

        ''' Quantas vezes costuma comer legumes em suas refeições? '''

        if QVZCLESR == 0:  # Quantas vezes costuma comer legumes nas suas refeições?
            QVZCLESR_pos = 0
        elif QVZCLESR == 1:
            QVZCLESR_pos = 1
        elif QVZCLESR == 2:
            QVZCLESR_pos = 2
        else:
            QVZCLESR_pos = 3

        if novo_caso[6] == '0':
            peso_base += QVZCLESR_VALORES[QVZCLESR_pos][0] * PESOS_POR_ATRIBUTO[
                "Quantas vezes costuma comer legumes em suas refeições?"]
        elif novo_caso[6] == '1':
            peso_base += QVZCLESR_VALORES[QVZCLESR_pos][1] * PESOS_POR_ATRIBUTO[
                "Quantas vezes costuma comer legumes em suas refeições?"]
        elif novo_caso[6] == '2':
            peso_base += QVZCLESR_VALORES[QVZCLESR_pos][2] * PESOS_POR_ATRIBUTO[
                "Quantas vezes costuma comer legumes em suas refeições?"]
        else:
            peso_base += QVZCLESR_VALORES[QVZCLESR_pos][3] * PESOS_POR_ATRIBUTO[
                "Quantas vezes costuma comer legumes em suas refeições?"]

        ''' Quantas refeições principais você tem diariamente? '''

        if QRTND == 1:  # Quantas refeições principais tem diariamente?
            QRTND_pos = 0
        elif QRTND == 2:
            QRTND_pos = 1
        elif QRTND == 3:
            QRTND_pos = 2
        else:
            QRTND_pos = 3

        if novo_caso[7] == '1':
            peso_base += QRTND_VALORES[QRTND_pos][0] * PESOS_POR_ATRIBUTO[
                "Quantas refeições principais você tem diariamente?"]
        elif novo_caso[7] == '2':
            peso_base += QRTND_VALORES[QRTND_pos][1] * PESOS_POR_ATRIBUTO[
                "Quantas refeições principais você tem diariamente?"]
        elif novo_caso[7] == '3':
            peso_base += QRTND_VALORES[QRTND_pos][2] * PESOS_POR_ATRIBUTO[
                "Quantas refeições principais você tem diariamente?"]
        else:
            peso_base += QRTND_VALORES[QRTND_pos][3] * PESOS_POR_ATRIBUTO[
                "Quantas refeições principais você tem diariamente?"]

        ''' Quanta litros de água você bebe diariamente? '''

        if BQLDAD == 1:  # Quanta litros de água você bebe diariamente?
            BQLDAD_pos = 0
        elif BQLDAD == 2:
            BQLDAD_pos = 1
        else:
            BQLDAD_pos = 2

        if novo_caso[10] == '1':
            peso_base += BQLDAD_VALORES[BQLDAD_pos][0] * PESOS_POR_ATRIBUTO[
                "Quanta litros de água você bebe diariamente?"]
        elif novo_caso[10] == 2:
            peso_base += BQLDAD_VALORES[BQLDAD_pos][1] * PESOS_POR_ATRIBUTO[
                "Quanta litros de água você bebe diariamente?"]
        else:
            peso_base += BQLDAD_VALORES[BQLDAD_pos][2] * PESOS_POR_ATRIBUTO[
                "Quanta litros de água você bebe diariamente?"]

        ''' Qual transporte você costuma usar? '''

        if QTCU == "Carro" or QTCU == "Moto":  # Qual transporte costuma usar?
            QTCU_pos = 0
        elif QTCU == "Transporte público":
            QTCU_pos = 1
        elif QTCU == "Bicicleta":
            QTCU_pos = 2
        elif QTCU == "Caminhada":
            QTCU_pos = 3
        else:
            QTCU_pos = 4

        if novo_caso[14] == "Carro" or novo_caso[14] == "Moto":
            peso_base += QTCU_VALORES[QTCU_pos][0] * PESOS_POR_ATRIBUTO["Qual transporte você costuma usar?"]
        elif novo_caso[14] == "Transporte Público":
            peso_base += QTCU_VALORES[QTCU_pos][1] * PESOS_POR_ATRIBUTO["Qual transporte você costuma usar?"]
        elif novo_caso[14] == "Bicicleta":
            peso_base += QTCU_VALORES[QTCU_pos][2] * PESOS_POR_ATRIBUTO["Qual transporte você costuma usar?"]
        elif novo_caso[14] == "Caminhada":
            peso_base += QTCU_VALORES[QTCU_pos][3] * PESOS_POR_ATRIBUTO["Qual transporte você costuma usar?"]
        else:
            peso_base += QTCU_VALORES[QTCU_pos][4] * PESOS_POR_ATRIBUTO["Qual transporte você costuma usar?"]

        peso_base = round(peso_base, 1)
        caso['Similaridade'] = (peso_base / peso_total) * 100
        caso['IMC'] = round(IMC, 2)

    casos_base = sorted(casos_base, key=lambda x: x['Similaridade'], reverse=True)
    print(
        f"O valor final da peso_base é {peso_base}, com o caso com maior representando {round(casos_base[0]['Similaridade'], 2)}% de similaridade.")
    print(f"Tendo como grau de obesidade: {casos_base[0]['Nível de obesidade']}")
    return casos_base
