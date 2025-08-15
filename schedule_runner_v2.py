# 2. Criar as classes Python

class Professor:
    """
    Representa um professor na escola.

    Atributos:
        nome (str): O nome do professor.
        disciplinas_que_leciona (list): Uma lista de objetos Disciplina que o professor pode lecionar.
    """
    def __init__(self, nome, disciplinas_que_leciona):
        self.nome = nome
        self.disciplinas_que_leciona = disciplinas_que_leciona # Lista de objetos Disciplina

class Disciplina:
    """
    Representa uma disciplina oferecida pela escola.

    Atributos:
        nome (str): O nome da disciplina.
        requer_laboratorio (bool): Indica se a disciplina requer uma sala de laboratório.
        curso (str, optional): O curso ao qual a disciplina pertence. Defaults to None.
        duracao (int): A duração da aula em slots de horário. Defaults to 1.
    """
    def __init__(self, nome, requer_laboratorio, curso=None, duracao=1):
        self.nome = nome
        self.requer_laboratorio = requer_laboratorio # Booleano
        self.curso = curso # Added course attribute
        self.duracao = duracao # Added duration attribute

class Sala:
    """
    Representa uma sala de aula na escola.

    Atributos:
        nome (str): O nome da sala.
        capacidade (int): A capacidade máxima de alunos na sala.
        eh_laboratorio (bool): Indica se a sala é um laboratório.
        tipo_laboratorio (str, optional): O tipo de laboratório, se for um. Defaults to None.
    """
    def __init__(self, nome, capacidade, eh_laboratorio, tipo_laboratorio=None):
        self.nome = nome
        self.capacidade = capacidade
        self.eh_laboratorio = eh_laboratorio # Booleano
        self.tipo_laboratorio = tipo_laboratorio

class Turma:
    """
    Representa um grupo de alunos (turma).

    Atributos:
        nome (str): O nome da turma.
        numero_de_alunos (int): O número de alunos na turma.
        disciplinas (list): Uma lista de objetos Disciplina que a turma deve cursar.
        turno (str): O turno que a turma frequenta ('Manhã', 'Tarde', 'Noite').
    """
    def __init__(self, nome, numero_de_alunos, disciplinas, turno):
        self.nome = nome
        self.numero_de_alunos = numero_de_alunos
        self.disciplinas = disciplinas # Lista de objetos Disciplina
        self.turno = turno # Added turno attribute

import random

# 3. Criar dados de exemplo (v2 com durações)
disciplina_names = [
    "Matemática I", "Português I", "Química Geral", "Física Básica", "História Antiga",
    "Biologia Celular", "Geografia Física", "Artes Visuais", "Educação Física", "Inglês Básico",
    "Programação Orientada a Objetos", "Estrutura de Dados", "Redes de Computadores", "Sistemas Operacionais", "Banco de Dados Avançado",
    "Circuitos Digitais", "Eletrônica Analógica", "Máquinas de Corrente Contínua", "Instalações Elétricas", "Automação Industrial",
    "Controle de Poluição", "Tratamento de Água", "Gerenciamento de Resíduos", "Legislação Ambiental", "Impacto Ambiental",
    "Cálculo I", "Álgebra Linear", "Probabilidade e Estatística", "Desenho Técnico", "Estatística Aplicada ao Agronegócio",
    "Fundamentos de Administração", "Marketing", "Recursos Humanos", "Logística", "Finanças Corporativas",
    "Desenvolvimento Web I", "Interface Humano-Computador", "Inteligência Artificial Aplicada", "Segurança da Informação", "Computação em Nuvem",
    "Sensores e Atuadores", "Robótica Móvel", "Sistemas Embarcados", "Microcontroladores", "Comunicação Industrial",
    "Manejo de Solo", "Fitopatologia", "Entomologia Agrícola", "Agrometeorologia", "Topografia",
    "Direito Empresarial", "Contabilidade Geral", "Economia", "Sociologia", "Ética Profissional"
]

disciplinas = []
for i, name in enumerate(disciplina_names):
    requer_laboratorio = "Química" in name or "Programação" in name or "Estrutura de Dados" in name or "Redes" in name or "Sistemas Operacionais" in name or "Banco de Dados" in name or "Circuitos" in name or "Eletrônica" in name or "Máquinas Elétricas" in name or "Instalações Elétricas" in name or "Automação" in name or "Robótica" in name or "Sistemas Embarcados" in name or "Microcontroladores" in name or "Topografia" in name

    curso = None
    if "Informática" in name or "Programação" in name or "Estrutura de Dados" in name or "Redes" in name or "Sistemas Operacionais" in name or "Banco de Dados" in name or "Desenvolvimento Web" in name or "Interface Humano-Computador" in name or "Inteligência Artificial" in name or "Segurança da Informação" in name or "Computação em Nuvem" in name:
        curso = "Informática/ADS"
    elif "Circuitos" in name or "Eletrônica" in name or "Máquinas Elétricas" in name or "Instalações Elétricas" in name or "Automação" in name or "Sensores e Atuadores" in name or "Robótica" in name or "Sistemas Embarcados" in name or "Microcontroladores" in name or "Comunicação Industrial" in name:
        curso = "Automação/Eletrotécnica"
    elif "Ambiental" in name or "Poluição" in name or "Resíduos" in name or "Tratamento de Água" in name:
        curso = "Controle Ambiental"
    elif "Administração" in name or "Marketing" in name or "Recursos Humanos" in name or "Logística" in name or "Finanças" in name or "Direito Empresarial" in name or "Contabilidade" in name or "Economia" in name or "Ética Profissional" in name:
        curso = "Administração"
    elif "Agrocomputação" in name or "Manejo de Solo" in name or "Fitopatologia" in name or "Entomologia Agrícola" in name or "Agrometeorologia" in name:
        curso = "Agrocomputação"
    elif "Cálculo" in name or "Álgebra" in name or "Probabilidade" in name or "Desenho Técnico" in name or "Estatística" in name:
        curso = "Cursos Básicos"

    disciplinas.append(Disciplina(name, requer_laboratorio, curso))

disciplinas_por_curso = {curso: [] for curso in set(d.curso for d in disciplinas if d.curso)}
for disciplina in disciplinas:
    if disciplina.curso:
        disciplinas_por_curso[disciplina.curso].append(disciplina)

# Professores
professores = []
num_professors = 40
for i in range(1, num_professors + 1):
    professores.append(Professor(f"Professor {i}", []))

all_disciplines_copy = list(disciplinas)
random.shuffle(all_disciplines_copy)
for i, disciplina in enumerate(all_disciplines_copy):
    professor_index = i % num_professors
    professores[professor_index].disciplinas_que_leciona.append(disciplina)

# Salas
salas = []
for i in range(1, 26): salas.append(Sala(f"Sala Regular {i}", 35, False))
for i in range(1, 6): salas.append(Sala(f"Laboratório de Informática {i}", 20, True, "Informática"))
for i in range(1, 6): salas.append(Sala(f"Laboratório de Química {i}", 25, True, "Química"))
for i in range(1, 6): salas.append(Sala(f"Laboratório de Robótica/Eletricidade {i}", 20, True, "Robótica/Eletricidade"))

# Turmas
turmas = []

def assign_disciplines_with_duration(course_name, num_disciplines, durations):
    disciplines_pool = list(disciplinas_por_curso.get(course_name, []))
    random.shuffle(disciplines_pool)
    assigned_disciplines = []
    if len(disciplines_pool) < num_disciplines:
        print(f"Aviso: Não há disciplinas suficientes para o curso {course_name}.")
        return []

    disciplines_to_assign = disciplines_pool[:num_disciplines]
    for i in range(num_disciplines):
        disc = disciplines_to_assign[i]
        assigned_disciplines.append(Disciplina(disc.nome, disc.requer_laboratorio, disc.curso, duracao=durations[i]))
    return assigned_disciplines

# Duração para turmas diurnas (4x3, 4x2, 2x1 = 22 slots)
day_durations = [3]*4 + [2]*4 + [1]*2
random.shuffle(day_durations)

# Duração para turmas noturnas (5 disciplinas de 4 slots)
night_durations = [4]*5

# Manhã
for i in range(1, 3): turmas.append(Turma(f"Informática Manhã {i}", 20, assign_disciplines_with_duration("Informática/ADS", 10, day_durations), "Manhã"))
for i in range(1, 3): turmas.append(Turma(f"Automação Manhã {i}", 25, assign_disciplines_with_duration("Automação/Eletrotécnica", 10, day_durations), "Manhã"))
for i in range(1, 5): turmas.append(Turma(f"Controle Ambiental Manhã {i}", 30, assign_disciplines_with_duration("Controle Ambiental", 10, day_durations), "Manhã"))

# Tarde
for i in range(1, 3): turmas.append(Turma(f"Informática Tarde {i}", 20, assign_disciplines_with_duration("Informática/ADS", 10, day_durations), "Tarde"))
for i in range(1, 3): turmas.append(Turma(f"Automação Tarde {i}", 25, assign_disciplines_with_duration("Automação/Eletrotécnica", 10, day_durations), "Tarde"))
for i in range(1, 5): turmas.append(Turma(f"Controle Ambiental Tarde {i}", 30, assign_disciplines_with_duration("Controle Ambiental", 10, day_durations), "Tarde"))
turmas.append(Turma("Administração Tarde 1", 35, assign_disciplines_with_duration("Administração", 10, day_durations), "Tarde"))

# Noite
for i in range(1, 4): turmas.append(Turma(f"Eletrotécnica Noite {i}", 20, assign_disciplines_with_duration("Automação/Eletrotécnica", 5, night_durations), "Noite"))
for i in range(1, 4): turmas.append(Turma(f"ADS Noite {i}", 30, assign_disciplines_with_duration("Informática/ADS", 5, night_durations), "Noite"))
turmas.append(Turma("Agrocomputação Noite 1", 25, assign_disciplines_with_duration("Agrocomputação", 5, night_durations), "Noite"))

print("Dados de exemplo (v2 com durações) criados com sucesso!")

# 4. Mapear horários para inteiros e definir o modelo
from datetime import datetime, timedelta
from ortools.sat.python import cp_model

days_of_week = ["Segunda", "Terca", "Quarta", "Quinta", "Sexta"]
morning_start_time = datetime.strptime('07:30', '%H:%M')
afternoon_start_time = datetime.strptime('13:30', '%H:%M')
night_start_time = datetime.strptime('19:00', '%H:%M')
class_duration_minutes = 45
morning_afternoon_classes_before_break = 3
morning_afternoon_classes_after_break = 3
night_classes_before_break = 2
night_classes_after_break = 2
break_duration_minutes = 15

horarios_por_turno = {"Manhã": [], "Tarde": [], "Noite": []}
for day in days_of_week:
    current_time = morning_start_time
    for i in range(morning_afternoon_classes_before_break):
        horarios_por_turno["Manhã"].append(f"{day}_{current_time.strftime('%Hh%M')}")
        current_time += timedelta(minutes=class_duration_minutes)
    current_time += timedelta(minutes=break_duration_minutes)
    for i in range(morning_afternoon_classes_after_break):
        horarios_por_turno["Manhã"].append(f"{day}_{current_time.strftime('%Hh%M')}")
        current_time += timedelta(minutes=class_duration_minutes)
    current_time = afternoon_start_time
    for i in range(morning_afternoon_classes_before_break):
        horarios_por_turno["Tarde"].append(f"{day}_{current_time.strftime('%Hh%M')}")
        current_time += timedelta(minutes=class_duration_minutes)
    current_time += timedelta(minutes=break_duration_minutes)
    for i in range(morning_afternoon_classes_after_break):
        horarios_por_turno["Tarde"].append(f"{day}_{current_time.strftime('%Hh%M')}")
        current_time += timedelta(minutes=class_duration_minutes)
    current_time = night_start_time
    for i in range(night_classes_before_break):
        horarios_por_turno["Noite"].append(f"{day}_{current_time.strftime('%Hh%M')}")
        current_time += timedelta(minutes=class_duration_minutes)
    current_time += timedelta(minutes=break_duration_minutes)
    for i in range(night_classes_after_break):
        horarios_por_turno["Noite"].append(f"{day}_{current_time.strftime('%Hh%M')}")
        current_time += timedelta(minutes=class_duration_minutes)

horarios_flat = sorted(list(set(horarios_por_turno["Manhã"] + horarios_por_turno["Tarde"] + horarios_por_turno["Noite"])))
horario_to_int = {horario: i for i, horario in enumerate(horarios_flat)}
int_to_horario = {i: horario for i, horario in enumerate(horarios_flat)}
horizon = len(horarios_flat)

print(f"Horizonte de tempo: {horizon} slots.")

model = cp_model.CpModel()

# 5. Criar variáveis de intervalo para o modelo

# Dicionário para guardar todas as informações das tarefas (aulas)
all_tasks = {}

for turma in turmas:
    for disciplina in turma.disciplinas:
        # Encontrar professores que podem lecionar a disciplina
        professores_validos = [
            p for p in professores if disciplina.nome in [d.nome for d in p.disciplinas_que_leciona]
        ]
        if not professores_validos:
            print(f"Aviso: Nenhum professor encontrado para a disciplina {disciplina.nome}")
            continue

        # Encontrar salas que atendem aos requisitos de laboratório e capacidade
        salas_validas = []
        if disciplina.requer_laboratorio:
            lab_type_needed = None
            if "Informática" in disciplina.curso or "ADS" in disciplina.curso:
                lab_type_needed = "Informática"
            elif "Química" in disciplina.curso or "Ambiental" in disciplina.curso:
                lab_type_needed = "Química"
            elif "Automação" in disciplina.curso or "Eletrotécnica" in disciplina.curso:
                lab_type_needed = "Robótica/Eletricidade"

            if lab_type_needed:
                salas_validas = [s for s in salas if s.eh_laboratorio and s.tipo_laboratorio == lab_type_needed and s.capacidade >= turma.numero_de_alunos]
        else:
            salas_validas = [s for s in salas if not s.eh_laboratorio and s.capacidade >= turma.numero_de_alunos]

        if not salas_validas:
            print(f"Aviso: Nenhuma sala válida encontrada para a disciplina {disciplina.nome} na turma {turma.nome}")
            continue

        task_key = (turma.nome, disciplina.nome)
        all_tasks[task_key] = {
            "turma": turma,
            "disciplina": disciplina,
            "professores": professores_validos,
            "salas": salas_validas,
            "assignments": [] # Para guardar as variáveis de agendamento
        }

# Criar as variáveis de intervalo para cada combinação válida
for task_key, task_data in all_tasks.items():
    turma = task_data["turma"]
    disciplina = task_data["disciplina"]
    duration = disciplina.duracao

    for professor in task_data["professores"]:
        for sala in task_data["salas"]:
            is_scheduled = model.NewBoolVar(f"is_scheduled_{turma.nome}_{disciplina.nome}_{professor.nome}_{sala.nome}")
            start_var = model.NewIntVar(0, horizon - duration, f"start_{turma.nome}_{disciplina.nome}")
            end_var = model.NewIntVar(0, horizon, f"end_{turma.nome}_{disciplina.nome}")

            interval_var = model.NewOptionalIntervalVar(
                start_var, duration, end_var, is_scheduled,
                f"interval_{turma.nome}_{disciplina.nome}_{professor.nome}_{sala.nome}"
            )

            task_data["assignments"].append({
                "is_scheduled": is_scheduled,
                "interval": interval_var,
                "professor": professor,
                "sala": sala
            })

print("Variáveis de intervalo criadas com sucesso!")

# 6. Adicionar restrições ao modelo

# Restrição: Não sobrepor aulas para o mesmo recurso (turma, professor, sala)
for turma in turmas:
    model.AddNoOverlap([
        assignment["interval"]
        for task_key, task_data in all_tasks.items()
        if task_data["turma"] == turma
        for assignment in task_data["assignments"]
    ])

for professor in professores:
    model.AddNoOverlap([
        assignment["interval"]
        for task_key, task_data in all_tasks.items()
        for assignment in task_data["assignments"]
        if assignment["professor"] == professor
    ])

for sala in salas:
    model.AddNoOverlap([
        assignment["interval"]
        for task_key, task_data in all_tasks.items()
        for assignment in task_data["assignments"]
        if assignment["sala"] == sala
    ])

# Restrição: Cada aula (turma, disciplina) deve ser agendada no máximo uma vez
for task_key, task_data in all_tasks.items():
    model.AddAtMostOne([
        assignment["is_scheduled"] for assignment in task_data["assignments"]
    ])

# Restrição para garantir que as aulas ocorram nos turnos corretos
for turno in ["Manhã", "Tarde", "Noite"]:
    allowed_indices = [horario_to_int[h] for h in horarios_por_turno[turno] if h in horario_to_int]
    if not allowed_indices: continue

    for task_key, task_data in all_tasks.items():
        if task_data["turma"].turno == turno:
            for assignment in task_data["assignments"]:
                start_var = assignment["interval"].StartExpr()
                # Forçar a variável de início a pertencer ao conjunto de índices permitidos para o turno
                model.AddAllowedAssignments([start_var], [(i,) for i in allowed_indices])

# 7. Definir o objetivo e resolver o modelo
# Objetivo: Maximizar o número de aulas agendadas
objective_vars = [
    assignment["is_scheduled"]
    for task_key, task_data in all_tasks.items()
    for assignment in task_data["assignments"]
]
model.Maximize(sum(objective_vars))

# Resolver o modelo
solver = cp_model.CpSolver()
solver.parameters.max_time_in_seconds = 120.0 # Adicionar um tempo limite
status = solver.Solve(model)

print("Restrições e objetivo definidos. Resolvendo...")

# 8. Processar e exibir a solução
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f"\nSolução encontrada com status {solver.StatusName(status)}.")
    print(f"Total de aulas agendadas: {solver.ObjectiveValue()}")

    # Estrutura para guardar o horário por turma
    schedule_by_turma = {turma.nome: {} for turma in turmas}

    # Extrair os resultados do solver
    for task_key, task_data in all_tasks.items():
        for assignment in task_data["assignments"]:
            if solver.Value(assignment["is_scheduled"]):
                turma_nome = task_data["turma"].nome
                start_index = solver.Value(assignment["interval"].StartExpr())
                duration = task_data["disciplina"].duracao

                details = (
                    f"{task_data['disciplina'].nome}\n"
                    f"({assignment['professor'].nome})\n"
                    f"@{assignment['sala'].nome}"
                )

                # Preencher todos os slots de horário para a aula
                for i in range(duration):
                    horario_str = int_to_horario.get(start_index + i)
                    if horario_str:
                        schedule_by_turma[turma_nome][horario_str] = details

    # Exibir o horário invertido para cada turma
    print("\n--- Horário Final por Turma ---")
    import pandas as pd

    for turma in turmas:
        print("\n" + "="*100)
        print(f"Horário para: {turma.nome} (Turno: {turma.turno})")
        print("="*100)

        turma_horarios_str = horarios_por_turno[turma.turno]
        time_slots = sorted(list(set(h.split('_')[1] for h in turma_horarios_str)))

        # Criar um DataFrame para fácil formatação
        df_data = {day: [] for day in days_of_week}
        for slot in time_slots:
            for day in days_of_week:
                horario_key = f"{day}_{slot}"
                aula = schedule_by_turma[turma.nome].get(horario_key, "---")
                df_data[day].append(aula)

        df = pd.DataFrame(df_data, index=time_slots)
        print(df.to_string())


    # Visualização com Matplotlib
    import matplotlib.pyplot as plt
    import numpy as np

    for turma in turmas:
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.axis('off')

        turma_horarios_str = horarios_por_turno[turma.turno]
        time_slots = sorted(list(set(h.split('_')[1] for h in turma_horarios_str)))

        cell_text = []
        for slot in time_slots:
            row_data = []
            for day in days_of_week:
                horario_key = f"{day}_{slot}"
                row_data.append(schedule_by_turma[turma.nome].get(horario_key, "---"))
            cell_text.append(row_data)

        if not any(any(cell != "---" for cell in row) for row in cell_text):
            print(f"\nNenhuma aula agendada para {turma.nome}, pulando grade visual.")
            plt.close(fig)
            continue

        table = ax.table(cellText=cell_text,
                         rowLabels=time_slots,
                         colLabels=days_of_week,
                         loc='center',
                         cellLoc='center')

        table.auto_set_font_size(False)
        table.set_fontsize(9)
        table.scale(1, 2.5)

        ax.set_title(f"Horário: {turma.nome} (Turno: {turma.turno})", fontsize=16, pad=20)
        fig.tight_layout()

    # plt.show()

else:
    print("\nNenhuma solução encontrada.")
