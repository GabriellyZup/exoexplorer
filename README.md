# ExoExplorer - Sistema de Controle de Robôs Planetários

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Pytest](https://img.shields.io/badge/Testes-100%25%20cobertura-success)

 **🚨 Importante**  
> 🚀 **Missão Cumprida!**  
> Sistema completo para gerenciamento de robôs exploradores e análise de dados coletados em missões interplanetárias.  
> Controle missões robóticas em outros planetas com registro automático de leituras ambientais e monitoramento de energia.
---

## Índice

- [🚀 Introdução](#🚀-introdução)
- [📋 Pré-requisitos](#📋-pré-requisitos)
- [🧑‍💻 Conceitos Utilizados](#🧑‍💻-conceitos-utilizados)
- [▶️ Execução do Sistema](#-execução-do-sistema)
- [🛠️ Instalação](#🛠️-instalação)
- [🪐 Como Usar](#🪐-como-usar)
- [📌 Funcionalidades Chave](#📌-funcionalidades-chave)
- [🔍 Validações Automáticas](#🔍-validações-automáticas)
- [🧪 Executando Testes](#🧪-executando-testes)
- [❓ Perguntas Frequentes](#❓-perguntas-frequentes)
- [🧠 Estrutura do Código](#🧠-estrutura-do-código)

---

## 🚀 Introdução

O **ExoExplorer** é um sistema para controle e monitoramento de robôs exploradores em missões planetárias. Permite criar robôs, registrar leituras ambientais e gerar relatórios automáticos, facilitando a análise de dados científicos em ambientes extremos.

---

## 📋 Pré-requisitos

- Python 3.9 ou superior (`python --version`)
- Gerenciador de pacotes PIP atualizado (`pip --version`)
- Instale as dependências do projeto (`pip install -r requirements.txt`)

---
## 🧑‍💻 Conceitos Utilizados

- **Herança em Python:**  
  O projeto utiliza herança de classes, onde `RelatorioDeMissao` herda de `RoboExplorador`. Isso permite que o relatório tenha todos os atributos e métodos do robô, além de funcionalidades próprias.

- **Tuplas:**  
  As leituras coletadas são armazenadas em tuplas, uma estrutura imutável do Python. Isso garante que os dados das leituras não sejam alterados após a coleta, mantendo a integridade dos registros científicos.

---

## ▶️ Execução do Sistema

Para executar o sistema e ver um exemplo prático de uso das classes, rode o arquivo principal:

```bash
A saída esperada será semelhante a:

  - Robô Curiosity - Destino: Marte - Energia: 90%
  - Resumo das leituras:
  - temperatura: -60
  - radiação: 3.2
  - pressão: 0.7
  - Total de leituras: 3
```

## 🛠️ Instalação

### 1. Configurar Ambiente Virtual

```bash
python -m venv .venv

# Ative o ambiente virtual:
# Windows
.\.venv\Scripts\Activate.ps1

# Linux/macOS
source .venv/bin/activate
```

### 2. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

---

## 🪐 Como Usar

### 1. Criar Robô Explorador
```python
from robo_explorador import RoboExplorador

robo = RoboExplorador("Curiosity", "Marte", 90)
print(robo)
# Saída: Robô Curiosity - Destino: Marte - Energia: 90%
```

### 2. Gerar Relatório de Missão
```python

from relatorio_de_missao import RelatorioDeMissao

leituras = (
    ("temperatura", -60),
    ("radiação", 3.2),
    ("pressão", 0.7)
)

relatorio = RelatorioDeMissao("Curiosity", "Marte", 90, leituras)

print("\n📊 Resumo das Leituras:")
for linha in relatorio.resumo():
    print(f" - {linha}")

print(f"\n🔢 Total de leituras: {relatorio.contagem_leituras()}")

```
**Saída Esperada:**  
Robô Curiosity - Destino: Marte - Energia: 90%

📊 Resumo das Leituras:

- temperatura: -60

- radiação: 3.2

- pressão: 0.7

🔢 Total de leituras: 3



## 📌 Funcionalidades Chave



| Funcionalidade          | Como Acessar            | Exemplo de Uso                          |
|-------------------------|-------------------------|------------------------------------------|
| Criar robô explorador    | `RoboExplorador()`      | `RoboExplorador("R2D2", "Marte", 80)`    |
| Gerar relatório          | `RelatorioDeMissao()`   | `RelatorioDeMissao(..., leituras)`       |
| Listar leituras          | `.resumo()`             | `relatorio.resumo()`                     |
| Contagem de dados        | `.contagem_leituras()`  | `relatorio.contagem_leituras()`          |


## 🔍 Validações Automáticas
***Teste 1: Energia Fora do Intervalo***

```
try:
    RoboExplorador("R2D2", "Marte", 150)
except ValueError as erro:
    print(erro)  # "Energia deve estar entre 0 e 100"
```

***Teste 2: Formato do Relatório***

```
leituras = (("vento", 20), ("umidade", 5.5))
relatorio = RelatorioDeMissao("R2D2", "Marte", 80, leituras)
assert relatorio.contagem_leituras() == 2
assert "vento: 20" in relatorio.resumo()
```

## 🧪 Executando Testes

Para executar todos os testes automatizados:

```
pytest test_exoexplorer.py -v

```

## ❓ Perguntas Frequentes


**Como adicionar novos tipos de leitura?** 
```

# Basta incluir na tupla de leituras:
novas_leituras = (
    ("vento", 45),
    ("pH do solo", 7.8)
)
```

**Por que usar tuplas para as leituras?**
```
- Garantia que os dados não serão modificados após a coleta

- Estrutura imutável para registros científicos

```

**Como aumentar a energia do robô?**

```
- robo.energia = 75  # Valor entre 0-100
```

## 🧠 Estrutura do Código
```plaintext
exoexplorer/
├── main.py                 - Demonstração das funcionalidades
├── robo_explorador.py      - Classe base do robô
├── relatorio_de_missao.py  - Sistema de relatórios (herança)
└── test_exoexplorer.py     - Testes automatizados
