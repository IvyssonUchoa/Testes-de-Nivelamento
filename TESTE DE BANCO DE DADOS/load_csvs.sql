-- Executar atraves do Terminal

-- Importa o conteúdo do Relatorio de Dados cadastrais das Operadoras Ativas para a tabela "cadop"
\COPY cadop("Registro_ANS", "CNPJ", "Razao_Social", "Nome_Fantasia", "Modalidade", "Logradouro","Numero", "Complemento", "Bairro", "Cidade", "UF", "CEP", "DDD", "Telefone", "Fax", "Endereco_eletronico", "Representante","Cargo_Representante", "Regiao_de_Comercializacao", "Data_Registro_ANS") FROM 'C:\Users\Ivysson\Downloads\Relatorio_cadop.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';

-- Importa os conteúdo dos Relatorios de Demonstrações Contábeis para a tabela "demo_contabeis"
\COPY demo_contabeis("Data", "Reg_Ans", "Cd_Conta_Contabil", "Descricao_Conta", "Vl_Saldo_Inicial", "Vl_Saldo_Final") FROM 'C:\Users\Ivysson\Downloads\demo_contabeis\1T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\COPY demo_contabeis("Data", "Reg_Ans", "Cd_Conta_Contabil", "Descricao_Conta", "Vl_Saldo_Inicial", "Vl_Saldo_Final") FROM 'C:\Users\Ivysson\Downloads\demo_contabeis\2t2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\COPY demo_contabeis("Data", "Reg_Ans", "Cd_Conta_Contabil", "Descricao_Conta", "Vl_Saldo_Inicial", "Vl_Saldo_Final") FROM 'C:\Users\Ivysson\Downloads\demo_contabeis\3T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\COPY demo_contabeis("Data", "Reg_Ans", "Cd_Conta_Contabil", "Descricao_Conta", "Vl_Saldo_Inicial", "Vl_Saldo_Final") FROM 'C:\Users\Ivysson\Downloads\demo_contabeis\4T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\COPY demo_contabeis("Data", "Reg_Ans", "Cd_Conta_Contabil", "Descricao_Conta", "Vl_Saldo_Inicial", "Vl_Saldo_Final") FROM 'C:\Users\Ivysson\Downloads\demo_contabeis\1T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\COPY demo_contabeis("Data", "Reg_Ans", "Cd_Conta_Contabil", "Descricao_Conta", "Vl_Saldo_Inicial", "Vl_Saldo_Final") FROM 'C:\Users\Ivysson\Downloads\demo_contabeis\2T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\COPY demo_contabeis("Data", "Reg_Ans", "Cd_Conta_Contabil", "Descricao_Conta", "Vl_Saldo_Inicial", "Vl_Saldo_Final") FROM 'C:\Users\Ivysson\Downloads\demo_contabeis\3T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
\COPY demo_contabeis("Data", "Reg_Ans", "Cd_Conta_Contabil", "Descricao_Conta", "Vl_Saldo_Inicial", "Vl_Saldo_Final") FROM 'C:\Users\Ivysson\Downloads\demo_contabeis\4T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';
