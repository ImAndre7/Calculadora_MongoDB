# Calculadora Simples com Persistência de Dados em MongoDB

Este projeto consiste em uma calculadora interativa simples que realiza operações matemáticas básicas (adição, subtração, multiplicação e divisão) e armazena o histórico de cálculos em um banco de dados MongoDB.

## Funcionalidades

* Realiza operações matemáticas básicas: adição, subtração, multiplicação e divisão.
* Armazena o histórico de cálculos em um banco de dados MongoDB.
* Exibe o resultado das operações no console.

## Tecnologias Utilizadas

* **Python:** 
* **PyMongo:** Driver Python para conexão e interação com o MongoDB.
* **MongoDB:** Banco de dados NoSQL 
* **VS Code:** Editor de código utilizado para o desenvolvimento do código.

## Pré-requisitos

* MongoDB instalado e em execução
* PyMongo instalado (`pip install pymongo`)

## Configuração do MongoDB

* Certifique-se de que o MongoDB esteja em execução na porta padrão (27017).
* O script Python se conecta ao banco de dados "calculadora\_db" e à coleção "resultados". Se esses elementos não existirem, o MongoDB os criará automaticamente.
