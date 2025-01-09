# TDEO: Algoritmo de Otimização de Throughput e Eficiência Energética

Bem-vindo ao repositório do TDEO (Throughput and Energy Optimization Algorithm), um projeto de pesquisa que utiliza aprendizado por reforço profundo para otimizar redes IoT densas e sem bateria, com foco em retroespalhamento ambiente.

## 🎯 Objetivo

O TDEO ajusta dinamicamente a potência de transmissão em dispositivos IoT para maximizar o throughput e a eficiência energética. Este repositório fornece todos os recursos necessários para simular, treinar e validar o algoritmo, permitindo que pesquisadores e desenvolvedores repliquem e testem o trabalho.

---

## 🗂 Estrutura do Repositório

- **`/simulations`**: Scripts e configurações para o OMNeT++.
- **`/training`**: Implementação do algoritmo DDPG no Google Colab.
- **`/results`**: Dados coletados e análises comparativas.
- **`/docs`**: Documentação técnica e artigos relacionados.
- **`README.md`**: Este arquivo!

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos

Certifique-se de ter os seguintes softwares instalados:

- [OMNeT++](https://omnetpp.org/) (versão usada: 5.6.2 ou superior)
- Python 3.8 ou superior, com as bibliotecas:
  - `tensorflow`
  - `numpy`
  - `pandas`
  - `gym`
- Google Colab (opcional, para treinar o modelo de aprendizado por reforço)

### 2. Executar Simulações no OMNeT++

1. Navegue até a pasta `/simulations` e copie o conteúdo para o diretório de projetos do OMNeT++.
2. Abra o OMNeT++ e importe o projeto.
3. Configure o arquivo `omnetpp.ini` para ajustar os parâmetros da rede.
4. Execute as simulações e salve os resultados na pasta `/results`.

### 3. Treinar o Modelo no Google Colab

1. Abra o arquivo `training/tdeo_ddpg.ipynb` no Google Colab.
2. Carregue os dados gerados pelo OMNeT++ na pasta `/results`.
3. Execute o notebook passo a passo para treinar o modelo e gerar os resultados otimizados.

### 4. Visualizar os Resultados

1. Acesse a pasta `/results` para encontrar os gráficos e tabelas comparativas.
2. Use os scripts da pasta `/analysis` para personalizar análises ou gerar novos gráficos.

---

## 📊 Resultados e Validação

Os principais resultados obtidos com o TDEO incluem:
- **Melhoria de até 15% no throughput**.
- **Aumento de 20% na eficiência energética**.
- Desempenho estável em cenários densos, com até 50 dispositivos IoT.

---

## 📚 Documentação

Para detalhes técnicos, consulte:
- O artigo na pasta `/docs`.
- As explicações completas no arquivo `tdeo_algorithm.md`.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Se você deseja colaborar, por favor:
1. Faça um fork do repositório.
2. Crie uma nova branch para suas alterações: `git checkout -b minha-branch`.
3. Envie um pull request detalhado.

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## 📬 Contato

Dúvidas ou sugestões? Entre em contato:

- Autor: **[Edwardes A. Galhardo]**
- E-mail: [edwardes.galhardo@ifto.edu.br]
- LinkedIn: [seu-linkedin](https://www.linkedin.com/in/edwards-amaro-0278bb120)

