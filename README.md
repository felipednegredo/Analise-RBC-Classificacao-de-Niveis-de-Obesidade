
# RBC

### Enunciado

Programar um protótipo de RBC para um tema definido pela equipe. Devem ser determinados pela equipe todos os componentes de um RBC até a recuperação do caso.As definições técnicas devem ser justificadas pela equipe, fundamentando com pesquisas na área.O trabalho deve ser entregue e apresentado pelo grupo na data de entrega. Grupos que não apresentarem o trabalho ou não estiverem presente quando chamados ficarão com nota zero.Grupos de até 3 integrantes.

Observação importante:

1- Na aula anterior a entrega todas as equipes deverão mostrar a modelagem do RBC, com a definição de atributos, pesos e métricas de similaridade a serem utilizadas. As equipes que não mostrarem os detalhes do modelo perderão pontos na avaliação do trabalho.

2- A entrega do programa e slides da apresentação devem ser feitos no sistema, até o horário de postagem. 

3- As apresentações iniciarão no horário da aula e todas as equipes devem apresentar neste dia.

4- A participação e empenho nas aulas de desenvolvimento do trabalho serão consideradas na avaliação final.

- -> A saída deve apresentar o caso de entrada, os pesos e uma lista com os casos da base ordenados por similaridade. Maior similaridade primeiro. Preferencialmente mostrar como uma lista com cada caso em uma linha.
- A implementação é em linguagem de programação. Com aquela linguagem que vocês quiserem, pois os procedimentos são simples e podem ser implementados em qualquer linguagem (não é uma planilha de Excel).
- Tem que apresentar a modelagem indicando os atributos, valores possíveis e como eles são comparados (métrica de similaridade local). O programa tem que ter cadastrados numa base os casos (pelo menos 50). Um interface que permita alterar se o usuário quiser os pesos dos atributos e inserir o caso de entrada (que será comparado a todos os casos da base e calculado a similaridade com cada um deles). A saída deve mostrar o caso de entra e todos os casos da base em ordem de similaridade (do mais similar ao menos similar). Todos os atributos do caso devem ser apresentados e o % de similaridade com o caso de entrada.



## Créditos

Este projeto utiliza componentes do tema [Azure-ttk-theme](https://github.com/rdbende/Azure-ttk-theme/tree/main), criado por [Benedek Dévényi (@rdbende)](https://github.com/rdbende), sob a licença MIT. Agradecemos ao autor pelo seu excelente trabalho.


## Rodando o projeto

Para rodar o projeto, rode os seguintes comandos

Clone o projeto

```bash
  git clone https://github.com/felipednegredo/Trabalho_IA_M2.git
```

Entre no diretório do projeto:

```bash
  cd Trabalho_IA_M2
```

Instale as dependências:

```bash
  pip install -r requirements.txt
```

Rode o projeto:

```bash
  python main.py
```

## Link da DataBase usada
Para mais informações e dados sobre os níveis de obesidade, consulte o conjunto de dados de níveis de obesidade disponível no Kaggle.
[Obesity Levels](https://www.kaggle.com/datasets/fatemehmehrparvar/obesity-levels)

## Autores

- [@felipednegredo](https://github.com/felipednegredo)
- [@VanessaBdL](https://github.com/VanessaBdL)
- [@yuri-rodriguesv](https://github.com/yuri-rodriguesv)

## Licença
[![AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

