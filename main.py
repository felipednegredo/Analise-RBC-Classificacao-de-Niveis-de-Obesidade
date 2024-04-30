import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from base import ler_base, definir_similaridade

data = {}

def checkbox_value(var):
    return "Sim" if var.get() == 1 else "Não"

# Constantes para os campos
FIELDS = [
    "Idade", "Genero", "Altura", "Peso", "Bebe álcool com frequencia?",
    "Você come alimentos com alto teor calórico com frequência?",
    "Quantas vezes costuma comer legumes em suas refeições?",
    "Quantas refeições principais você tem diariamente?",
    "Você monitora as calorias que você come diariamente?", "Você fuma?",
    "Quanta litros de água você bebe diariamente?",
    "Um membro da família sofreu ou sofre de excesso de peso?",
    "Com que frequência você tem atividade física?",
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
    ["Não","As vezes","Frequentemente","Sempre"],
    ["Nunca","As Vezes","Frequente","Sempre"],
    ["Carro", "Transporte público", "Bicicleta", "Caminhada"]
]

# Função para registrar os dados
def register(entries, last_register_table, output_table,PESOS):
    """Função para registrar os dados.
        Args:
        entries: Dicionário com os campos e valores
        last_register_table: Tabela com o último cadastro
        output_table: Tabela de saída
    """
    data = {}
    for field, entry in entries.items():
        if field in CHECKBOX_FIELDS:
            data[field] = entry.get()
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
    imc = round(peso / (altura ** 2),2)
    data.append(imc)

    data_copy = data

    # Get the indices of 'Altura' and 'Peso' in FIELDS
    altura_index = FIELDS.index('Altura')
    peso_index = FIELDS.index('Peso')

    # Remove 'Altura' and 'Peso' from data_copy
    data_copy = [v for i, v in enumerate(data_copy) if i not in [altura_index, peso_index]]

    # Adiciona o último cadastro na tabela
    last_register_table.insert("", "end", values=data_copy)

    messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")

    # Read base data
    base_data = ler_base()

    # Calculate similarity
    similar_data = definir_similaridade(base_data, data, PESOS)

    print(similar_data)

    # Clear existing data in output_table
    for i in output_table.get_children():
        output_table.delete(i)

    # Insert new data into output_table
    for item in similar_data:
        # Convert the item to a list if it's a dictionary
        if isinstance(item, dict):
            item = list(item.values())
        output_table.insert("", "end", values=item)

    return data

# Função para classificar a tabela
def sortby(tree, col, descending):
        """Função para classificar os itens da tabela. Args: tree: tabela col: coluna descending: ordem de classificação """
        data = [(tree.set(child, col), child) for child in tree.get_children('')]
        data.sort(reverse=descending)

        for indx, item in enumerate(data):
            tree.move(item[1], '', indx)

        tree.heading(col, command=lambda col=col: sortby(tree, col, int(not descending)))

def save_edit(edit_entry, row_id, column_id, weights_table):
    """Function to save the edited value in the table. Args: edit_entry: Entry widget containing the edited value row_id: ID of the row being edited column_id: ID of the column being edited"""
    new_value = edit_entry.get()
    row_values = weights_table.item(row_id)['values']
    column_index = int(column_id[1]) - 1
    row_values[column_index] = new_value
    weights_table.item(row_id, values=row_values)
    edit_entry.destroy()


# Chama a função para criar a interface gráfica
def create_interface():
    """Função para criar a interface gráfica. Args: None. Returns: None."""
    root = tk.Tk()
    root.title("Interface de Cadastro")
    root.tk.call("source", "azure.tcl")
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

    ATRIBUTOS = ["Idade", "Gênero", "Bebe álcool com frequência?", "Alimentos com alto teor calórico", "Quantidade de legumes", "Refeições diárias", "Monitora calorias", "Fumante", "Consumo de água", "Histórico familiar de excesso de peso", "Atividade física", "Alimentos entre refeições", "Transporte utilizado", "IMC", "Similaridade"]

    PESOS = [
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


    # Campos para a tabela de pesos
    for i, atributo in enumerate(ATRIBUTOS):
        label = ttk.Label(tab3, text=atributo)
        label.grid(row=i, column=0, padx=20, pady=10, sticky="w")
        entry = ttk.Entry(tab3)
        entry.grid(row=i, column=1, padx=20, pady=10, sticky="w")
        PESOS[atributo] = entry


    # Label para mostrar o último cadastro
    last_register_table = ttk.Treeview(tab2, height=1)
    last_register_table['columns'] = ("Idade", "Gênero", "Bebe álcool com frequência?", "Alimentos com alto teor calórico", "Quantidade de legumes", "Refeições diárias", "Monitora calorias", "Fumante", "Consumo de água", "Histórico familiar de excesso de peso", "Atividade física", "Alimentos entre refeições", "Transporte utilizado", "IMC")

    for column in last_register_table['columns']:
        last_register_table.column(column, width=75, minwidth=20)
        last_register_table.heading(column, text=column)

    last_register_table['show'] = 'headings'
    last_register_table.pack(padx=10, pady=10)

    # Faça uma tabela de saída com os campos
    # Cria a tabela de saída
    output_table = ttk.Treeview(tab2, height=10)  # Define a altura da tabela

    # Define as colunas
    output_table['columns'] = ("Idade", "Gênero", "Bebe álcool com frequência?", "Alimentos com alto teor calórico", "Quantidade de legumes", "Refeições diárias", "Monitora calorias", "Fumante", "Consumo de água", "Histórico familiar de excesso de peso", "Atividade física", "Alimentos entre refeições", "Transporte utilizado", "IMC", "Similaridade")

    # Formata as colunas
    for column in output_table['columns']:
        output_table.column(column, width=75, minwidth=20)
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
            checkbox = ttk.Checkbutton(tab1, variable=var,command=lambda var=var : checkbox_value(var))
            checkbox.grid(row=i // 2, column=i % 2 * 2 + 1, padx=20, pady=10, sticky="w")
            entries[field] = var
        elif field in SELECT_FIELDS:
            var = tk.StringVar()
            select = ttk.Combobox(tab1, textvariable=var, state="readonly")
            select['values'] = SELECT_OPTIONS[SELECT_FIELDS.index(field)]
            select.grid(row=i//2, column=i%2*2+1, padx=20, pady=10, sticky="w")
            entries[field] = var
        else:
            entry = ttk.Entry(tab1)  # Add to tab1 instead of root
            entry.grid(row=i//2, column=i%2*2+1, padx=20, pady=10, sticky="w")
            entries[field] = entry

    register_button = ttk.Button(tab1, text="Cadastrar", command=lambda: register(entries, last_register_table, output_table,PESOS))
    register_button.grid(row=len(FIELDS)//2+1, column=0, columnspan=4, padx=20, pady=20)
    root.mainloop()


create_interface()