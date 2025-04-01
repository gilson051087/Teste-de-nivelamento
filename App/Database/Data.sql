CREATE TABLE operadoras_ativas (
    id SERIAL PRIMARY KEY,
    registro_ans VARCHAR(20) UNIQUE NOT NULL,
    cnpj VARCHAR(18) NOT NULL,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    uf VARCHAR(2),
    data_registro DATE
);

CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    registro_ans VARCHAR(20) REFERENCES operadoras_ativas(registro_ans),
    ano INT NOT NULL,
    receita DECIMAL(15,2),
    despesa DECIMAL(15,2),
    resultado DECIMAL(15,2)
);

LOAD DATA LOCAL INFILE '/Teste-de-nivelamento/src/Banco de Dados/Operadoras_ativas.csv'
INTO TABLE operadoras_ativas
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, uf, @data_registro)
SET data_registro = STR_TO_DATE(@data_registro, '%d/%m/%Y');

LOAD DATA LOCAL INFILE 'Teste-de-nivelamento/src/Banco de Dados/demonstracoes_contabeis'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(registro_ans, ano, receita, despesa, resultado);
