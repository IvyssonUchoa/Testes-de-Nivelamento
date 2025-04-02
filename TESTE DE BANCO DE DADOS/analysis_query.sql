-- Operadoras com as maiores despesas do ultimo trimestre na categoria "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR"
SELECT
    cadop."CNPJ",
	cadop."Razao_Social",
    cadop."Nome_Fantasia",
    demo_contabeis."Descricao_Conta",
    (REPLACE(demo_contabeis."Vl_Saldo_Inicial", ',', '.')::NUMERIC) "Saldo Inicial",
    (REPLACE(demo_contabeis."Vl_Saldo_Final", ',', '.')::NUMERIC) "Saldo Final",
	(REPLACE(demo_contabeis."Vl_Saldo_Inicial", ',', '.')::NUMERIC) - (REPLACE(demo_contabeis."Vl_Saldo_Final", ',', '.')::NUMERIC) "Despesa"
FROM
	cadop 
    LEFT JOIN DEMO_CONTABEIS on demo_contabeis."Reg_Ans" = cadop."Registro_ANS"
WHERE
	DEMO_CONTABEIS."Descricao_Conta" = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
	AND DEMO_CONTABEIS."Data" >= '2024-07-01' -- Data de Inicio do Ultimo trimestre
	AND DEMO_CONTABEIS."Data" < '2024-10-01' -- Data de Fim do Ultimo trimestre
ORDER BY 
    "Despesa" DESC
LIMIT 
	10;

    
-- Operadoras com as maiores despesas do ultimo ano na categoria "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR"
SELECT
    cadop."CNPJ",
	cadop."Razao_Social",
    cadop."Nome_Fantasia",
    demo_contabeis."Descricao_Conta",
    (REPLACE(demo_contabeis."Vl_Saldo_Inicial", ',', '.')::NUMERIC) "Saldo Inicial",
    (REPLACE(demo_contabeis."Vl_Saldo_Final", ',', '.')::NUMERIC) "Saldo Final",
	(REPLACE(demo_contabeis."Vl_Saldo_Inicial", ',', '.')::NUMERIC) - (REPLACE(demo_contabeis."Vl_Saldo_Final", ',', '.')::NUMERIC) "Despesa"
FROM
	cadop 
    LEFT JOIN DEMO_CONTABEIS on demo_contabeis."Reg_Ans" = cadop."Registro_ANS"
WHERE
	DEMO_CONTABEIS."Descricao_Conta" = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
	AND EXTRACT(YEAR FROM DEMO_CONTABEIS."Data") = 2023 --Dados do ultimo ano
ORDER BY 
    "Despesa" DESC
LIMIT 
	10;