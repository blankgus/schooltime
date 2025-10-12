from models import Aula, DIAS_SEMANA
from collections import defaultdict
import random

class SimpleGradeHoraria:
    def __init__(self, turmas, professores, disciplinas):
        self.turmas = turmas
        self.professores = {p.nome: p for p in professores}
        self.disciplinas = {d.nome: d for d in disciplinas}
        self.dias = ["seg", "ter", "qua", "qui", "sex"]
        self.horarios = [1, 2, 3, 4, 5, 6, 7]
        self.carga_turma = defaultdict(lambda: defaultdict(int))
        # Agora, usa a lista de DisciplinaTurma de cada turma
        for turma in turmas:
            for dt in turma.disciplinas_turma:
                self.carga_turma[turma.nome][dt.nome] = dt.carga_semanal

    def gerar_grade(self):
        aulas = []
        prof_aulas = defaultdict(list)
        turma_aulas = defaultdict(list)
        pendentes = []
        for turma_nome in self.carga_turma:
            for disc, carga in self.carga_turma[turma_nome].items():
                for _ in range(carga):
                    pendentes.append((turma_nome, disc))
        random.shuffle(pendentes)
        for turma_nome, disc_nome in pendentes:
            atribuido = False
            # Aqui, filtramos professores com base na turma
            turma = next((t for t in self.turmas if t.nome == turma_nome), None)
            if turma:
                dt = next((dt for dt in turma.disciplinas_turma if dt.nome == disc_nome), None)
                if dt and dt.professor_fixo:
                    profs_possiveis = [p for p in self.professores.values() if p.nome == dt.professor and disc_nome in p.disciplinas]
                else:
                    profs_possiveis = [p for p in self.professores.values() if disc_nome in p.disciplinas]
            else:
                profs_possiveis = [p for p in self.professores.values() if disc_nome in p.disciplinas]

            random.shuffle(profs_possiveis)
            for prof in profs_possiveis:
                # Verificar se o professor pode lecionar para esta turma
                if prof.turmas_permitidas and turma_nome not in prof.turmas_permitidas:
                    continue
                combinacoes = [(dia, h) for dia in self.dias for h in self.horarios]
                random.shuffle(combinacoes)
                for dia, horario in combinacoes:
                    # Verificar indisponibilidade de dia e horário
                    if dia in prof.dias_indisponiveis or horario in prof.horarios_indisponiveis:
                        continue
                    # Verificar restrições específicas
                    if f"{dia}_{horario}" in prof.restricoes:
                        continue
                    conflito = False
                    for a in prof_aulas[prof.nome]:
                        if a.dia == dia and a.horario == horario:
                            conflito = True
                            break
                    for a in turma_aulas[turma_nome]:
                        if a.dia == dia and a.horario == horario:
                            conflito = True
                            break
                    if not conflito:
                        sala_nome = "Sala 1"
                        aula = Aula(turma_nome, disc_nome, prof.nome, dia, horario, sala_nome)
                        aulas.append(aula)
                        prof_aulas[prof.nome].append(aula)
                        turma_aulas[turma_nome].append(aula)
                        atribuido = True
                        break
                if atribuido:
                    break
        return aulas