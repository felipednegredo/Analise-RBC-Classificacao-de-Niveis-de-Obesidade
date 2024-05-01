import pandas as pd
import os

# Valores de similaridade de IMC (Índice de Massa Corporal)
IMC_VALORES = [[1, 0.5, 0.25], [0.5, 1, 0.5], [0.25, 0.5, 1]]

# Valores de similaridade de BQLDAD (Quantos litros de água você bebe diariamente?)
BQLDAD_VALORES = [[1.0, 0.6, 0.1],
                  [0.6, 1.0, 0.6],
                  [0.1, 0.6, 1.0]]

# Valores de similaridade de BACDF (Bebe álcool com frequencia?)
BACDF_VALORES = [[1.0, 0.8, 0.5, 0.0],
                 [0.8, 1.0, 0.5, 0.3],
                 [0.5, 0.5, 1.0, 0.8],
                 [0.0, 0.3, 0.8, 1.0]]

# Valores de similaridade de QVZCLESR (Quantas vezes costuma comer legumes em suas refeições?)
QVZCLESR_VALORES = [[1.0, 0.8, 0.4, 0.0],
                    [0.8, 1.0, 0.8, 0.4],
                    [0.4, 0.8, 1.0, 0.8],
                    [0.0, 0.4, 0.8, 1.0]]

# Valores de similaridade de QRTND (Quantas refeições principais você tem diariamente?)
QRTND_VALORES = [[1.0, 0.8, 0.4, 0.2],
                 [0.8, 1.0, 0.8, 0.4],
                 [0.4, 0.8, 1.0, 0.8],
                 [0.2, 0.4, 0.8, 1.0]]

# Valores de similaridade de CQFPAF (Com que frequência você tem atividade física?)
CQFPAF_VALORES = [[1.0, 0.0, 0.0],
                  [0.0, 1.0, 0.5],
                  [0.0, 0.5, 1.0]]

# Valores de similaridade de VCQAEAR (Você come qualquer alimento entre as refeições?)
VCQAEAR_VALORES = [[1.0, 0.2, 0.2, 0.0],
                   [0.2, 1.0, 0.5, 0.5],
                   [0.2, 0.5, 1.0, 0.8],
                   [0.0, 0.5, 0.8, 1.0]]

# Valores de similaridade de QTCU (Qual transporte você costuma usar?)
QTCU_VALORES = [[1.0, 0.9, 0.0, 0.0, 0.0],
                [0.9, 1.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 1.0, 1.0],
                [0.0, 0.0, 1.0, 1.0, 1.0],
                [0.0, 0.0, 1.0, 1.0, 1.0]]

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
            [i,idade, genero, BACDF, CACATCCF, QVZCLESR, QRTND, MACQCD, FUMA, BQLDAD, AMDFSOSCEDP, CQFPAF, VCQAEAR, QTCU,
             IMC, NO])

    # Transformar os dados em um DataFrame
    df = pd.DataFrame(casos_base, columns=['Index','Idade', 'Genero', 'Bebe álcool com frequencia?',
                                           'Você come alimentos com alto teor calórico com frequência?',
                                           'Quantas vezes costuma comer legumes em suas refeições?',
                                           'Quantas refeições principais você tem diariamente?',
                                           'Você monitora as calorias que você come diariamente?', 'Você fuma?',
                                           'Quanta litros de água você bebe diariamente?',
                                           'Um membro da família sofreu ou sofre de excesso de peso?',
                                           'Com que frequência você tem atividade física?',
                                           'Você come qualquer alimento entre as refeições?',
                                           'Qual transporte você costuma usar?', 'IMC', 'Nível de obesidade'])

    # Convert the DataFrame to a list of dictionaries
    data = df.to_dict('records')

    return data


def definir_similaridade(casos_base, novo_caso, PESOS_POR_ATRIBUTO):
    """Função para definir a similaridade entre os casos da base e o novo caso.
        Args:
        casos_base: Lista de dicionários com os casos da base
        novo_caso: Lista com os valores do novo caso
        Returns:
            object: 
        casos_base: Lista de dicionários com os casos da base e a similaridade
    """
    similaridade = 0
    for caso in casos_base:
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
        CQFPAF = caso["Com que frequência você tem atividade física?"]
        VCQAEAR = caso["Você come qualquer alimento entre as refeições?"]
        QTCU = caso["Qual transporte você costuma usar?"]
        IMC = round(caso["IMC"],2)
        NO = caso["Nível de obesidade"]

        max_idade = max([int(caso["Idade"]) for caso in casos_base])
        max_imc = max([float(caso["IMC"]) for caso in casos_base])

        print(PESOS_POR_ATRIBUTO)

        similaridade += PESOS_POR_ATRIBUTO["Idade"] * (1 - abs((idade - int(novo_caso[0])) / (max_idade)))
        novo_caso[2] = novo_caso[2].replace(',', '.')
        novo_caso[3] = novo_caso[3].replace(',', '.')
        IMC_casoNovo = float(novo_caso[2]) / (float(novo_caso[3]) ** 2)
        similaridade += PESOS_POR_ATRIBUTO["IMC"] * (1 - abs(IMC - float(IMC_casoNovo)) / (max_imc))

        if genero == novo_caso[1]:  # Genero
            similaridade += 1 * PESOS_POR_ATRIBUTO["Gênero"]

        if CACATCCF == novo_caso[3]:  # Você come alimentos com alto teor calórico com frequência?
            similaridade += 1 * PESOS_POR_ATRIBUTO["Você come alimentos com alto teor calórico com frequência?"]

        if MACQCD == novo_caso[6]:  # Você monitora as calorias que você come diariamente?
            similaridade += 1 * PESOS_POR_ATRIBUTO["Você monitora as calorias que você come diariamente?"]

        if FUMA == novo_caso[7]:  # Você fuma?
            similaridade += 1 * PESOS_POR_ATRIBUTO["Você fuma?"]

        if AMDFSOSCEDP == novo_caso[9]:  # Um membro da família sofreu ou sofre de excesso de peso?
            similaridade += 1 * PESOS_POR_ATRIBUTO["Histórico familiar de excesso de peso"]

        ''' Com que frequência você tem atividade física? '''

        if novo_caso[10] == "Não":
            CQFPAF_pos = 0
        elif novo_caso[10] == "As vezes":
            CQFPAF_pos = 1
        elif novo_caso[10] == "Frequentemente":
            CQFPAF_pos = 2
        elif novo_caso[10] == "Sempre":
            CQFPAF_pos = 3

        if CQFPAF == "Não":  # Com que frequência você tem atividade física?
            similaridade += CQFPAF_VALORES[CQFPAF_pos][0] * PESOS_POR_ATRIBUTO[
                "Com que frequência você tem atividade física?"]
        elif CQFPAF == "As vezes":
            similaridade += CQFPAF_VALORES[CQFPAF_pos][1] * PESOS_POR_ATRIBUTO[
                "Com que frequência você tem atividade física?"]
        elif CQFPAF == "Frequentemente":
            similaridade += CQFPAF_VALORES[CQFPAF_pos][2] * PESOS_POR_ATRIBUTO[
                "Com que frequência você tem atividade física?"]
        elif CQFPAF == "Sempre":
            similaridade += CQFPAF_VALORES[CQFPAF_pos][3] * PESOS_POR_ATRIBUTO[
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

        if novo_caso[11] == "Nunca":  # Você come qualquer alimento entre as refeições?
            similaridade += VCQAEAR_VALORES[VCQAEAR_pos][0] * PESOS_POR_ATRIBUTO[
                "Você come qualquer alimento entre as refeições?"]
        elif novo_caso[11] == "As Vezes":
            similaridade += VCQAEAR_VALORES[VCQAEAR_pos][1] * PESOS_POR_ATRIBUTO[
                "Você come qualquer alimento entre as refeições?"]
        elif novo_caso[11] == "Frequente":
            similaridade += VCQAEAR_VALORES[VCQAEAR_pos][2] * PESOS_POR_ATRIBUTO[
                "Você come qualquer alimento entre as refeições?"]
        elif novo_caso[11] == "Sempre":
            similaridade += VCQAEAR_VALORES[VCQAEAR_pos][3] * PESOS_POR_ATRIBUTO[
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

        if novo_caso[2] == "Não":
            similaridade += BACDF_VALORES[BACDF_pos][0] * PESOS_POR_ATRIBUTO["Bebe álcool com frequencia?"]
        elif novo_caso[2] == "As vezes":
            similaridade += BACDF_VALORES[BACDF_pos][1] * PESOS_POR_ATRIBUTO["Bebe álcool com frequencia?"]
        elif novo_caso[2] == "Frequentemente":
            similaridade += BACDF_VALORES[BACDF_pos][2] * PESOS_POR_ATRIBUTO["Bebe álcool com frequencia?"]
        elif novo_caso[2] == "Sempre":
            similaridade += BACDF_VALORES[BACDF_pos][3] * PESOS_POR_ATRIBUTO["Bebe álcool com frequencia?"]

        ''' Quantas vezes costuma comer legumes em suas refeições? '''

        if QVZCLESR == "0":  # Quantas vezes costuma comer legumes em suas refeições?
            QVZCLESR_pos = 0
        elif QVZCLESR == "1":
            QVZCLESR_pos = 1
        elif QVZCLESR == "2":
            QVZCLESR_pos = 2
        else:
            QVZCLESR_pos = 3

        if novo_caso[4] == "0":
            similaridade += QVZCLESR_VALORES[QVZCLESR_pos][0] * PESOS_POR_ATRIBUTO["Quantidade de legumes"]
        elif novo_caso[4] == "1":
            similaridade += QVZCLESR_VALORES[QVZCLESR_pos][1] * PESOS_POR_ATRIBUTO["Quantidade de legumes"]
        elif novo_caso[4] == "2":
            similaridade += QVZCLESR_VALORES[QVZCLESR_pos][2] * PESOS_POR_ATRIBUTO["Quantidade de legumes"]
        else:
            similaridade += QVZCLESR_VALORES[QVZCLESR_pos][3] * PESOS_POR_ATRIBUTO["Quantidade de legumes"]

        ''' Quantas refeições principais você tem diariamente? '''

        if QRTND == "1":  # Quantas refeições principais você tem diariamente?
            QRTND_pos = 0
        elif QRTND == "2":
            QRTND_pos = 1
        elif QRTND == "3":
            QRTND_pos = 2
        else:
            QRTND_pos = 3

        if novo_caso[5] == "1":
            similaridade += QRTND_VALORES[QRTND_pos][0] * PESOS_POR_ATRIBUTO["Refeições diárias"]
        elif novo_caso[5] == "2":
            similaridade += QRTND_VALORES[QRTND_pos][1] * PESOS_POR_ATRIBUTO["Refeições diárias"]
        elif novo_caso[5] == "3":
            similaridade += QRTND_VALORES[QRTND_pos][2] * PESOS_POR_ATRIBUTO["Refeições diárias"]
        else:
            similaridade += QRTND_VALORES[QRTND_pos][3] * PESOS_POR_ATRIBUTO["Refeições diárias"]

        ''' Quanta litros de água você bebe diariamente? '''

        if BQLDAD == "1":  # Quanta litros de água você bebe diariamente?
            BQLDAD_pos = 0
        elif BQLDAD == "2":
            BQLDAD_pos = 1
        else:
            BQLDAD_pos = 2

        if novo_caso[8] == "1":
            similaridade += BQLDAD_VALORES[BQLDAD_pos][0] * PESOS_POR_ATRIBUTO["Consumo de água"]
        elif novo_caso[8] == "2":
            similaridade += BQLDAD_VALORES[BQLDAD_pos][1] * PESOS_POR_ATRIBUTO["Consumo de água"]
        else:
            similaridade += BQLDAD_VALORES[BQLDAD_pos][2] * PESOS_POR_ATRIBUTO["Consumo de água"]

        ''' Qual transporte você costuma usar? '''

        if QTCU == "Carro" or QTCU == "Moto":  # Qual transporte você costuma usar?
            QTCU_pos = 0
        elif QTCU == "Transporte público":
            QTCU_pos = 1
        elif QTCU == "Bicicleta":
            QTCU_pos = 2
        elif QTCU == "Caminhada":
            QTCU_pos = 3
        else:
            QTCU_pos = 4

        if novo_caso[12] == "Carro" or novo_caso[12] == "Moto":
            similaridade += QTCU_VALORES[QTCU_pos][0] * PESOS_POR_ATRIBUTO["Transporte utilizado"]
        elif novo_caso[12] == "Transporte público":
            similaridade += QTCU_VALORES[QTCU_pos][1] * PESOS_POR_ATRIBUTO["Transporte utilizado"]
        elif novo_caso[12] == "Bicicleta":
            similaridade += QTCU_VALORES[QTCU_pos][2] * PESOS_POR_ATRIBUTO["Transporte utilizado"]
        elif novo_caso[12] == "Caminhada":
            similaridade += QTCU_VALORES[QTCU_pos][3] * PESOS_POR_ATRIBUTO["Transporte utilizado"]
        else:
            similaridade += QTCU_VALORES[QTCU_pos][4] * PESOS_POR_ATRIBUTO["Transporte utilizado"]

        ''' Bebe álcool com frequencia? '''

        if BACDF == 'Não':
            BACDF_pos = 0
        elif BACDF == 'As vezes':
            BACDF_pos = 1
        elif BACDF == 'Frequentemente':
            BACDF_pos = 2
        else:
            BACDF_pos = 3

        if novo_caso[2] == 'Não':
            similaridade += BACDF_VALORES[BACDF_pos][0] * PESOS_POR_ATRIBUTO["Bebe álcool com frequência?"]
        elif novo_caso[2] == 'As vezes':
            similaridade += BACDF_VALORES[BACDF_pos][1] * PESOS_POR_ATRIBUTO["Bebe álcool com frequência?"]
        elif novo_caso[2] == 'Frequentemente':
            similaridade += BACDF_VALORES[BACDF_pos][2] * PESOS_POR_ATRIBUTO["Bebe álcool com frequência?"]
        else:
            similaridade += BACDF_VALORES[BACDF_pos][3] * PESOS_POR_ATRIBUTO["Bebe álcool com frequência?"]

        caso['Similaridade'] = round(similaridade/100, 2)

        caso['IMC'] = round(IMC, 2)

    casos_base = sorted(casos_base, key=lambda x: x['Similaridade'], reverse=True)

    return casos_base
