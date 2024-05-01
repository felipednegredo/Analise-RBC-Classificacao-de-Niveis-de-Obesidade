import tkinter as tk
import os
from tkinter import messagebox
from tkinter import ttk

from base import ler_base, definir_similaridade

data = {}


def checkbox_value(var):
    return "Sim" if var == 1 else "Não"


# Constantes para os campos
FIELDS = [
    "Idade", "Genero", "Altura (Ex: 1,60)", "Peso (Ex: 55,00)", "Bebe álcool com frequencia?",
    "Você come alimentos com alto teor calórico com frequência?",
    "Quantas vezes costuma comer legumes em suas refeições?",
    "Quantas refeições principais você tem diariamente?",
    "Você monitora as calorias que você come diariamente?", "Você fuma?",
    "Quanta litros de água você bebe diariamente?",
    "Um membro da família sofreu ou sofre de excesso de peso?",
    "Com que frequência você tem atividade física? (por semana)",
    "Você come qualquer alimento entre as refeições?",
    "Qual transporte você costuma usar?"
]

CHECKBOX_FIELDS = [
    "Você come alimentos com alto teor calórico com frequência?",
    "Você monitora as calorias que você come diariamente?",
    "Você fuma?",
    "Um membro da família sofreu ou sofre de excesso de peso?"
]

SELECT_FIELDS = ["Genero",
                 "Bebe álcool com frequencia?",
                 "Você come qualquer alimento entre as refeições?",
                 "Qual transporte você costuma usar?"
                 ]

SELECT_OPTIONS = [
    ["Masculino", "Feminino"],
    ["Não", "As vezes", "Frequentemente", "Sempre"],
    ["Nunca", "As Vezes", "Frequentemente", "Sempre"],
    ["Carro", "Transporte público", "Moto","Bicicleta", "Caminhada"]
]


# Função para registrar os dados
def register(entries, last_register_table, output_table, ATTRIBUTES_WEIGHTS):
    """Função para registrar os dados.
        Args:
            entries: Dicionário com os campos e valores
            last_register_table: Tabela com o último cadastro
            output_table: Tabela de saída
            ATTRIBUTES_WEIGHTS: 
        entries: Dicionário com os campos e valores
        last_register_table: Tabela com o último cadastro
        output_table: Tabela de saída
    """
    data = {}
    for field, entry in entries.items():
        if field in CHECKBOX_FIELDS:
            data[field] = entry.get()
            data[field] = checkbox_value(data[field])
        elif field in SELECT_FIELDS:
            data[field] = entry.get()
        else:
            data[field] = entry.get()

    # Atualiza o label do último cadastro
    data = list(data.values())
    data = [str(value) for value in data]
    # retiro campo altura e peso e calcula o IMC
    altura = float(data[2].replace(",", "."))
    peso = float(data[3].replace(",", "."))
    imc = round(peso / (altura ** 2), 2)
    data.append(imc)

    data_copy = data

    # Pega os índices de 'Altura' e 'Peso'
    altura_index = FIELDS.index("Altura (Ex: 1,60)")
    peso_index = FIELDS.index('Peso (Ex: 55,00)')

    # Remove 'Altura' e 'Peso' de data_copy
    data_copy = [v for i, v in enumerate(data_copy) if i not in [altura_index, peso_index]]

    # Adiciona o último cadastro na tabela
    last_register_table.insert("", "end", values=data_copy)

    messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")

    # Ler a base de dados
    base_data = ler_base()

    # Calcula a similaridade
    similar_data = definir_similaridade(base_data, data, ATTRIBUTES_WEIGHTS)

    # Limpa a tabela de saída
    for i in output_table.get_children():
        output_table.delete(i)

    # Adiciona os dados similares na tabela de saída
    for item in similar_data:
        # Se o item for um dicionário, transforma em uma lista
        if isinstance(item, dict):
            item = list(item.values())
        output_table.insert("", "end", values=item)

    return data

def limpar_campos(entries):
    """Função para limpar os campos. Args: entries: Dicionário com os campos e valores

    Args:
        entries: Dicionário com os campos e valores

    Returns:
        object: retorna os campos limpos
    """
    for entry in entries.values():
        if isinstance(entry, tk.Entry):
            entry.delete(0, "end")
        elif isinstance(entry, tk.StringVar):
            entry.set("")
        elif isinstance(entry, tk.IntVar):
            entry.set(0)
    return entries


# Função para classificar a tabela
def sortby(tree, col, descending):
    """Função para classificar os itens da tabela. Args: tree: tabela col: coluna descending: ordem de classificação

    Args:
        tree:
        col:
        descending:

    Returns:
        object:
    """
    data = [(tree.set(child, col), child) for child in tree.get_children('')]
    data.sort(reverse=descending)

    for indx, item in enumerate(data):
        tree.move(item[1], '', indx)

    tree.heading(col, command=lambda col=col: sortby(tree, col, int(not descending)))


def save_weights(ATTRIBUTES_WEIGHTS, frame):
    """Função para salvar os pesos. Args: ATTRIBUTES_WEIGHTS: Dicionário com os pesos frame: Frame com os pesos

    Args:
        ATTRIBUTES_WEIGHTS: Dicionário com os pesos
        frame: Frame com os pesos

    Returns:
        object: retorna os pesos
    """
    for i, (attribute, weight) in enumerate(ATTRIBUTES_WEIGHTS.items()):
        entry = frame.grid_slaves(row=i + 1, column=1)[0]
        ATTRIBUTES_WEIGHTS[attribute] = float(entry.get())
    messagebox.showinfo("Pesos", "Pesos salvos com sucesso!")

    print(ATTRIBUTES_WEIGHTS)

    return ATTRIBUTES_WEIGHTS


# Chama a função para criar a interface gráfica
def create_interface():
    """Função para criar a interface gráfica. Args: None. Returns: None.

    Returns:
        object: 
    """
    root = tk.Tk()
    root.title("Interface de Cadastro")
    diretorio_atual = os.path.dirname(os.path.realpath(__file__))
    # Construa o caminho para o arquivo "azure.tcl" usando o diretório atual
    caminho_azure_tcl = os.path.join(diretorio_atual, "..", "Trabalho_IA_M2", "azure.tcl")
    root.tk.call("source", caminho_azure_tcl)
    root.tk.call("set_theme", "dark")

    style = ttk.Style()
    style.configure("TEntry", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 12))
    style.configure("TCheckbutton", font=("Arial", 12))
    style.configure("TCombobox", font=("Arial", 12))

    # Cria o notebook (abas)
    notebook = ttk.Notebook(root)
    notebook.grid(sticky='nsew')  # Use grid instead of pack

    # Cria a primeira aba
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text='Cadastro')

    # Cria a segunda aba
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text='Tabela de Similaridade')

    tab3 = ttk.Frame(notebook)
    notebook.add(tab3, text='Tabela de Pesos')

    notebook.pack(expand=True, fill='both')

    # Create a frame for the grid layout
    frame = ttk.Frame(tab3)
    frame.pack(fill="both", expand=True)

    # Configure the grid
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)

    # Create a dictionary for the attributes and weights
    ATTRIBUTES_WEIGHTS = {
        "Idade": 0.2,
        "Gênero": 0.4,
        "Bebe álcool com frequência?": 0.9,
        "Alimentos com alto teor calórico": 0.5,
        "Quantidade de legumes": 0.6,
        "Refeições diárias": 0.7,
        "Monitora calorias": 0.5,
        "Fumante": 0.3,
        "Consumo de água": 0.5,
        "Histórico familiar de excesso de peso": 0.8,
        "Atividade física": 0.7,
        "Alimentos entre refeições": 0.6,
        "Transporte utilizado": 0.5,
        "IMC": 1,
    }

    # Fields for the weights table
    for i, (attribute, weight) in enumerate(ATTRIBUTES_WEIGHTS.items()):
        label = ttk.Label(frame, text=attribute)
        label.grid(row=i + 1, column=0, padx=5, pady=5, sticky="w")
        entry = ttk.Entry(frame)
        entry.insert(0, weight)
        entry.grid(row=i + 1, column=1, padx=5, pady=5, sticky="w")

    save_weights_button = ttk.Button(frame, text="Salvar Pesos",
                                     command=lambda: ATTRIBUTES_WEIGHTS.update(save_weights(ATTRIBUTES_WEIGHTS, frame)))
    save_weights_button.grid(row=len(ATTRIBUTES_WEIGHTS) + 1, column=0, columnspan=2, padx=5, pady=5)

    # Label para mostrar o último cadastro
    last_register_table = ttk.Treeview(tab2, height=1)
    last_register_table['columns'] = (
        "Idade", "Gênero", "Bebe álcool com frequência?", "Alimentos com alto teor calórico", "Quantidade de legumes",
        "Refeições diárias", "Monitora calorias", "Fumante", "Consumo de água", "Histórico familiar de excesso de peso",
        "Atividade física", "Alimentos entre refeições", "Transporte utilizado", "IMC")

    for column in last_register_table['columns']:
        last_register_table.column(column, width=85, minwidth=20)
        last_register_table.heading(column, text=column)

    last_register_table['show'] = 'headings'
    last_register_table.pack(padx=10, pady=10)

    # Faça uma tabela de saída com os campos
    # Cria a tabela de saída
    output_table = ttk.Treeview(tab2, height=10)  # Define a altura da tabela

    # Define as colunas
    output_table['columns'] = ("Index",
    "Idade", "Gênero", "Bebe álcool com frequência?", "Alimentos com alto teor calórico", "Quantidade de legumes",
    "Refeições diárias", "Monitora calorias", "Fumante", "Consumo de água", "Histórico familiar de excesso de peso",
    "Atividade física", "Alimentos entre refeições", "Transporte utilizado", "IMC", "Obesidade", "Similaridade")

    # Formata as colunas
    for column in output_table['columns']:
        output_table.column(column, width=85, minwidth=20)
        output_table.heading(column, text=column)

    # Oculta a coluna '#0'
    output_table['show'] = 'headings'

    # Adiciona a tabela à tab2
    output_table.pack(padx=10, pady=10)

    entries = {}
    for i, field in enumerate(FIELDS):
        label = ttk.Label(tab1, text=field)
        label.grid(row=i // 2, column=i % 2 * 2, padx=20, pady=10, sticky="w")
        if field in CHECKBOX_FIELDS:
            var = tk.IntVar()
            checkbox = ttk.Checkbutton(tab1, variable=var, command=lambda var=var: checkbox_value(var))
            checkbox.grid(row=i // 2, column=i % 2 * 2 + 1, padx=20, pady=10, sticky="w")
            entries[field] = var
        elif field in SELECT_FIELDS:
            var = tk.StringVar()
            select = ttk.Combobox(tab1, textvariable=var, state="readonly")
            select['values'] = SELECT_OPTIONS[SELECT_FIELDS.index(field)]
            select.grid(row=i // 2, column=i % 2 * 2 + 1, padx=20, pady=10, sticky="w")
            entries[field] = var
        else:
            entry = ttk.Entry(tab1)  # Add to tab1 instead of root
            entry.grid(row=i // 2, column=i % 2 * 2 + 1, padx=20, pady=10, sticky="w")
            entries[field] = entry

    register_button = ttk.Button(tab1, text="Cadastrar",
                                 command=lambda: register(entries, last_register_table, output_table,
                                                          ATTRIBUTES_WEIGHTS))
    reset_button = ttk.Button(tab1, text="Limpar Campos", command=lambda: limpar_campos(entries))
    reset_button.grid(row=len(FIELDS) // 2 + 1, column=2, columnspan=2, padx=20, pady=20)
    register_button.grid(row=len(FIELDS) // 2 + 1, column=0, columnspan=4, padx=20, pady=20)
    root.mainloop()


create_interface()
