import sqlite3
import json

def migrar_banco():
    conn = sqlite3.connect("escola.db")
    cursor = conn.cursor()

    # Verificar se a coluna 'disciplinas_turma' já existe
    cursor.execute("PRAGMA table_info(turmas)")
    colunas = [c[1] for c in cursor.fetchall()]
    if "disciplinas_turma" in colunas:
        print("✅ Banco já está na versão mais recente.")
        conn.close()
        return

    print("🔄 Iniciando migração do banco de dados...")

    # Adicionar novas colunas
    try:
        cursor.execute("ALTER TABLE turmas ADD COLUMN disciplinas_turma TEXT DEFAULT '[]'")
        cursor.execute("ALTER TABLE turmas ADD COLUMN regras_neuro TEXT DEFAULT '[]'")
        print("✅ Colunas 'disciplinas_turma' e 'regras_neuro' adicionadas à tabela 'turmas'.")
    except sqlite3.OperationalError:
        print("⚠️ Colunas já existem.")

    try:
        cursor.execute("ALTER TABLE professores ADD COLUMN turmas_permitidas TEXT DEFAULT '[]'")
        print("✅ Coluna 'turmas_permitidas' adicionada à tabela 'professores'.")
    except sqlite3.OperationalError:
        print("⚠️ Coluna 'turmas_permitidas' já existe.")

    # Converter a antiga coluna 'disciplinas' para a nova estrutura (se necessário)
    # Neste caso, não faremos nada, pois o conteúdo antigo será sobrescrito ao salvar

    conn.commit()
    conn.close()
    print("✅ Banco de dados migrado com sucesso!")

if __name__ == "__main__":
    migrar_banco()