import _sqlite3

DATABASE = "escola.db"

def conectar_banco():
    conexao = _sqlite3.connect("escola.db")
    conexao.row_factory = _sqlite3.Row

    return conexao

def criar_tabelas():
    conexao = conectar_banco()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS alunos ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        idade INTEGER NOT NULL 
        )
        CREATE TABLE IF NOT EXISTS turmas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ano_letivo INTEGER NOT NULL,
        periodo TEXT NOT NULL,
        ativo INTEGER NOT NULL DEFAULT 1,
        criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        CREATE TABLE IF NOT EXISTS disciplinas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        codigo TEXT NOT NULL UNIQUE,
        carga_horaria INTEGER NOT NULL,
        ativo INTEGER NOT NULL DEFAULT 1,
        criado_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        CREATE TABLE IF NOT EXISTS alunos_turma(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER NOT NULL,
        turma_id INTEGER NOT NULL,
        data_matricula DATE NOT NULL DEFAULT CURRENT_DATE
        )
        CREATE TABLE IF NOT EXISTS notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER NOT NULL,
        turma_id INTEGER NOT NULL,
        data_matricula DATE NOT NULL DEFAULT CURRENT_DATE
        )
        CREATE TABLE IF NOT EXISTS frequencias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER NOT NULL,
        turma_id INTEGER NOT NULL,
        data_matricula DATE NOT NULL DEFAULT CURRENT_DATE
        )
    """)
