import streamlit as st
from models import Turma, Professor, Disciplina, Sala, DisciplinaTurma
import database

def init_session_state():
    database.init_db()
    if "turmas" not in st.session_state:
        st.session_state.turmas = database.carregar_turmas() or [
            Turma("6anoA", "6ano", "manha", "pcd", [
                DisciplinaTurma("Matemática", 3, "Ana A"),
                DisciplinaTurma("Português", 3, "Bruno A"),
                DisciplinaTurma("Ciências", 2, "Diego A"),
            ]),
            Turma("6anoB", "6ano", "manha", "inclusao", [
                DisciplinaTurma("Matemática", 4, "Ana B"),
                DisciplinaTurma("Português", 4, "Bruno B"),
                DisciplinaTurma("Ciências", 2, "Diego B"),
            ]),
            # Adicione mais turmas A e B para 7ano, 8ano, 9ano, 1em, 2em, 3em
            # ...
        ]
    if "professores" not in st.session_state:
        st.session_state.professores = database.carregar_professores() or [
            Professor("Ana A", ["Matemática"], set(), set()),
            Professor("Ana B", ["Matemática"], set(), set()),
            Professor("Bruno A", ["Português"], set(), set()),
            Professor("Bruno B", ["Português"], set(), set()),
            Professor("Diego A", ["Ciências", "Biologia"], set(), set()),
            Professor("Diego B", ["Ciências", "Biologia"], set(), set()),
            # Adicione mais professores
            # ...
        ]
    if "disciplinas" not in st.session_state:
        st.session_state.disciplinas = database.carregar_disciplinas() or [
            Disciplina("Matemática", 4, "pesada", ["6ano", "7ano", "8ano", "9ano"], "#4A90E2", "#FFFFFF"),
            Disciplina("Português", 4, "pesada", ["6ano", "7ano", "8ano", "9ano"], "#D35400", "#FFFFFF"),
            # Adicione mais disciplinas
            # ...
        ]
    if "salas" not in st.session_state:
        st.session_state.salas = database.carregar_salas() or [
            Sala("Sala 1", 30, "normal"),
            Sala("Sala 2", 30, "normal"),
            # Adicione mais salas
            # ...
        ]