CREATE TABLE IF NOT EXISTS "clientes"(
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "cpf" TEXT NOT NULL UNIQUE,
    "nome_completo" TEXT NOT NULL,
    "emprego_atual" TEXT NOT NULL,
    "data_nascimento" DATE NOT NULL,
    "situacao_civil" TEXT NOT NULL,
    "endereco" TEXT NOT NULL,
    "cliente_especial" INTEGER NOT NULL CHECK (cliente_especial IN (0, 1))
);