from dataclasses import dataclass, field
from typing import List, Set
import uuid

DIAS_SEMANA = ["dom", "seg", "ter", "qua", "qui", "sex", "sab"]

@dataclass
class Disciplina:
    nome: str
    carga_semanal: int
    tipo: str
    series: List[str]
    cor_fundo: str = "#4A90E2"
    cor_fonte: str = "#FFFFFF"
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

@dataclass
class Professor:
    nome: str
    disciplinas: List[str]
    disponibilidade_dias: Set[str]
    disponibilidade_horarios: Set[int]
    restricoes: Set[str] = field(default_factory=set)
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

@dataclass
class Turma:
    nome: str
    serie: str
    turno: str
    tipo: str = "regular"  # "pcd", "inclusao", "regular"
    disciplinas_turma: List[str] = field(default_factory=list)  # Ex: ["Matemática", "Português"]
    regras_neuro: List[str] = field(default_factory=list)  # Ex: ["max_2_pesadas", "sem_aula_pos_intervalo"]
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

@dataclass
class Sala:
    nome: str
    capacidade: int = 30
    tipo: str = "normal"
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

@dataclass
class Aula:
    turma: str
    disciplina: str
    professor: str
    dia: str
    horario: int
    sala: str = "Sala 1"
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

@dataclass
class Feriado:
    str
    motivo: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
