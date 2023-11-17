# Big-Data
## Grupo DATA TOWN 
### Trabalho - Eficácia da Vacinação da COVID-19
- Extraindo dados
    - Extrai o banco de dados compactado para um diretório
    - [Link](https://github.com/matheusBraga10/Big-Data/blob/main/trabalho_covid/extract_01.ipynb)
- Concatenando arquivos
    - Recebe uma lista de todos os arquivos extraídos, unindo os mesmos e posteriormente salvando em só um arquivo
    - [Link](https://github.com/matheusBraga10/Big-Data/blob/main/trabalho_covid/concatenando_arquivos_covid_02.ipynb)
- Análise exploratória
    - Lê o arquivo concatenado, utilizando variados métodos de vizualização e manipulação, com intuito de definir uma lista de conjunto dados a serem tratados e quais as melhores maneiras para tratar esses dados
    - [Link](https://github.com/matheusBraga10/Big-Data/blob/main/trabalho_covid/analise_exploratoria_03.ipynb)
- Tratamento de dados
    - Divisão do arquivo após filtragem em duas partes (País e municípos)
    - Brasil
        - Junção de banco de dados com dados de vacinação nacional
        - Exclusão de colunas nulas
        - Tratamento de linhas nulas
        - Arquivo filtrado e tratado salvo a parte
        - [Link](https://github.com/matheusBraga10/Big-Data/blob/main/trabalho_covid/tratando_dados_brasil_04.ipynb)
    - Municípios
        - Filtragem de dados para melhor compreenção dos dados nulos
        - Exclusão de linhas e colunas nulas
        - Tratamento de linhas nulas
        - Arquivo filtrado e tratado salvo a parte
        - [Link](https://github.com/matheusBraga10/Big-Data/blob/main/trabalho_covid/tratando_dados_covid_05.ipynb)
- Arquivo Principal de trabalho (já tratado)
    - Após o tratamento dos arquivos, foi feita uma serie de agrupamentos, seleções e filtragens para geração de gráficos para possibilitar entendimento vizual sobre a eficácia da vacinação
    - Os dados se mostraram satisfatórios para a comprovação da eficácia
    - [Link](https://github.com/matheusBraga10/Big-Data/blob/main/trabalho_covid/principal_06.ipynb)