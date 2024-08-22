-- Mostra os Bancos de Dados (SGBD - mySQL)--
SHOW DATABASES;
SHOW SCHEMAS;

-- selecionando o BD--
USE sakila;

-- Exibe as tabelas do BD escolhido--
SHOW TABLES;

-- É comando de Consulta aos dados do BD (tabela) --
SELECT* FROM sakila.payment;

-- consulta os dados de duas colunas --
SELECT title, description FROM sakila.film;

-- Exibe a estrutura da tabela--
DESCRIBE sakila.payment;

-- contar os itens encontrados --
-- COUNT () - função que conta os itens encontrados --
SELECT COUNT(title) FROM sakila.film;