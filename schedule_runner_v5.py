# Horario de Professores v5
# This notebook implements a multi-file CSV data loading system.

# 1. Instalar bibliotecas
# !pip install ortools pandas

# 2. Definições de Classes
import random
import pandas as pd
from datetime import datetime, timedelta
from ortools.sat.python import cp_model
import os # Para verificar a existência de arquivos

class Professor:
    def __init__(self, nome, disciplinas_que_leciona, horarios_indisponiveis=None):
        self.nome = nome
        self.disciplinas_que_leciona = disciplinas_que_leciona
        self.horarios_indisponiveis = horarios_indisponiveis if horarios_indisponiveis is not None else []

class Disciplina:
    def __init__(self, nome, curso=None, duracao=1, tipo_sala_requerida='comum'):
        self.nome = nome
        self.curso = curso
        self.duracao = duracao
        self.tipo_sala_requerida = tipo_sala_requerida
        self.requer_laboratorio = 'lab' in self.tipo_sala_requerida

class Sala:
    def __init__(self, nome, capacidade, eh_laboratorio, tipo_sala='comum'):
        self.nome = nome
        self.capacidade = capacidade
        self.eh_laboratorio = eh_laboratorio
        self.tipo_sala = tipo_sala

class Turma:
    def __init__(self, nome, numero_de_alunos, disciplinas, turno):
        self.nome = nome
        self.numero_de_alunos = numero_de_alunos
        self.disciplinas = disciplinas
        self.turno = turno

# 3. Lógica de Carregamento de Dados (v5)

def generate_example_data():
    print("Gerando dados de exemplo...")
    restricoes_globais = []
    disciplina_names = [
        "Matemática I", "Português I", "Química Geral", "Física Básica", "História Antiga",
        "Biologia Celular", "Geografia Física", "Artes Visuais", "Educação Física", "Inglês Básico",
        "Programação Orientada a Objetos", "Estrutura de Dados", "Redes de Computadores", "Sistemas Operacionais", "Banco de Dados Avançado",
        "Circuitos Digitais", "Eletrônica Analógica", "Máquinas de Corrente Contínua", "Instalações Elétricas", "Automação Industrial",
        "Controle de Poluição", "Tratamento de Água", "Gerenciamento de Resíduos", "Legislação Ambiental", "Impacto Ambiental"
    ]
    disciplinas = []
    for name in disciplina_names:
        tipo_sala = 'comum'
        curso = 'Geral'
        if "Química" in name or "Biologia" in name:
            tipo_sala = 'lab_quimica'
            curso = 'Química/Biologia'
        elif "Programação" in name or "Redes" in name or "Sistemas" in name or "Banco de Dados" in name:
            tipo_sala = 'lab_informatica'
            curso = 'Informática/ADS'
        elif "Circuitos" in name or "Eletrônica" in name or "Automação" in name or "Robótica" in name:
            tipo_sala = 'lab_eletrica_robotica'
            curso = 'Automação/Eletrotécnica'
        disciplinas.append(Disciplina(name, curso=curso, tipo_sala_requerida=tipo_sala))

    professores = []
    for i in range(1, 41):
        professores.append(Professor(f"Professor {i}", [], horarios_indisponiveis=[]))
    disciplinas_disponiveis = list(disciplinas)
    for prof in professores:
        num_disciplinas_prof = random.randint(2, 5)
        prof.disciplinas_que_leciona = random.sample(disciplinas_disponiveis, min(num_disciplinas_prof, len(disciplinas_disponiveis)))

    salas = []
    for i in range(1, 26): salas.append(Sala(f"Sala Comum {i}", 35, False, tipo_sala='comum'))
    for i in range(1, 6): salas.append(Sala(f"Lab Info {i}", 20, True, tipo_sala='lab_informatica'))
    for i in range(1, 6): salas.append(Sala(f"Lab Quim {i}", 25, True, tipo_sala='lab_quimica'))
    for i in range(1, 6): salas.append(Sala(f"Lab Eletro/Robo {i}", 20, True, tipo_sala='lab_eletrica_robotica'))

    turmas = []
    day_durations = [3]*4 + [2]*4 + [1]*2
    night_durations_map = { 5: [4]*5, 6: [4]*3 + [2]*3, 7: [3]*7, 8: [3]*5 + [2]*3 }
    def assign_disciplines_to_turma(num_disciplines, durations, all_disciplines_pool):
        disciplines_pool = list(all_disciplines_pool)
        random.shuffle(disciplines_pool)
        assigned = []
        disciplines_to_assign = disciplines_pool[:num_disciplines]
        for i in range(num_disciplines):
            disc = disciplines_to_assign[i]
            dur = durations[i % len(durations)]
            assigned.append(Disciplina(disc.nome, curso=disc.curso, duracao=dur, tipo_sala_requerida=disc.tipo_sala_requerida))
        return assigned

    nomes_turmas_diurnas = ["Informática Manhã", "Automação Manhã", "Controle Ambiental Manhã", "Informática Tarde", "Automação Tarde", "Controle Ambiental Tarde", "Administração Tarde"]
    nomes_turmas_noturnas = ["Eletrotécnica Noite", "ADS Noite", "Agrocomputação Noite"]
    for nome_base in nomes_turmas_diurnas:
        num_disciplinas = random.randint(10, 15)
        random.shuffle(day_durations)
        turno = "Manhã" if "Manhã" in nome_base else "Tarde"
        turmas.append(Turma(nome_base + " 1", 30, assign_disciplines_to_turma(num_disciplinas, day_durations, disciplinas), turno))
    for nome_base in nomes_turmas_noturnas:
        num_disciplinas = random.randint(5, 8)
        durations = night_durations_map[num_disciplinas]
        random.shuffle(durations)
        turmas.append(Turma(nome_base + " 1", 25, assign_disciplines_to_turma(num_disciplinas, durations, disciplinas), "Noite"))

    return turmas, professores, salas, restricoes_globais


def setup_data(grade_path, salas_path, restricoes_path):
    if not os.path.exists(grade_path):
        print(f"Arquivo '{grade_path}' não encontrado.")
        return generate_example_data()

    print(f"Carregando dados de '{grade_path}'...")
    try:
        df_grade = pd.read_csv(grade_path)
        required_cols = ['turma_nome', 'professor_nome', 'disciplina_nome', 'sala_requerida']
        if not all(col in df_grade.columns for col in required_cols):
            print("Erro: Colunas essenciais faltando em grade_curricular.csv.")
            return None, None, None, None
    except Exception as e:
        print(f"Erro ao ler '{grade_path}': {e}")
        return None, None, None, None

    professores_map = {name: Professor(name, []) for name in df_grade['professor_nome'].unique()}
    turmas_map = {name: Turma(name, 0, [], '') for name in df_grade['turma_nome'].unique()}

    for _, row in df_grade.iterrows():
        p = professores_map[row['professor_nome']]
        d = Disciplina(row['disciplina_nome'], row['curso_nome'], row['disciplina_duracao'], row['sala_requerida'])
        if not any(disc.nome == d.nome for disc in p.disciplinas_que_leciona):
            p.disciplinas_que_leciona.append(d)

        t = turmas_map[row['turma_nome']]
        t.disciplinas.append(d)
        t.numero_de_alunos = int(row['turma_alunos'])
        t.turno = row['turma_turno']

    salas_map = {}
    tipos_sala_unicos = df_grade['sala_requerida'].unique()
    for tipo in tipos_sala_unicos:
        for i in range(1, 6): salas_map[f"{tipo}_{i}"] = Sala(f"{tipo}_{i}", 30, 'lab' in tipo, tipo)

    if os.path.exists(salas_path):
        print(f"Carregando dados de '{salas_path}'...")
        try:
            df_salas = pd.read_csv(salas_path)
            for _, row in df_salas.iterrows():
                if row['sala_nome'] in salas_map:
                    salas_map[row['sala_nome']].capacidade = int(row['capacidade'])
                else:
                    salas_map[row['sala_nome']] = Sala(row['sala_nome'], int(row['capacidade']), 'lab' in row['tipo_sala'], row['tipo_sala'])
        except Exception as e:
            print(f"Aviso: Não foi possível carregar '{salas_path}'. Usando capacidades padrão. Erro: {e}")
    else:
        print(f"Aviso: '{salas_path}' não encontrado. Usando salas e capacidades padrão.")

    restricoes_globais = []
    if os.path.exists(restricoes_path):
        print(f"Carregando dados de '{restricoes_path}'...")
        try:
            df_restricoes = pd.read_csv(restricoes_path)
            for _, row in df_restricoes.iterrows():
                horario_str = f"{row['dia_semana']}_{row['horario']}"
                if row['tipo_restricao'] == 'ESCOLA' and row['nome_entidade'] == 'GLOBAL':
                    restricoes_globais.append(horario_str)
                elif row['tipo_restricao'] == 'PROFESSOR' and row['nome_entidade'] in professores_map:
                    professores_map[row['nome_entidade']].horarios_indisponiveis.append(horario_str)
        except Exception as e:
            print(f"Aviso: Não foi possível carregar '{restricoes_path}'. Nenhuma restrição de tempo será aplicada. Erro: {e}")
    else:
        print(f"Aviso: '{restricoes_path}' não encontrado. Nenhuma restrição de tempo será aplicada.")

    print("\n--- Resumo dos Dados Finais ---")
    print(f"Total de Turmas: {len(turmas_map)}, Professores: {len(professores_map)}, Salas: {len(salas_map)}")

    return list(turmas_map.values()), list(professores_map.values()), list(salas_map.values()), restricoes_globais

# --- Bloco de Execução Principal ---
csv_grade_path = "grade_curricular.csv"
csv_salas_path = "salas.csv"
csv_restricoes_path = "restricoes.csv"

turmas, professores, salas, restricoes_globais = setup_data(csv_grade_path, csv_salas_path, csv_restricoes_path)

if turmas:
    horarios_por_turno = {"Manhã": [], "Tarde": [], "Noite": []}
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
    print(f"\nHorizonte de tempo: {horizon} slots.")

    model = cp_model.CpModel()

    all_tasks = {}
    for turma in turmas:
        for disciplina in turma.disciplinas:
            professores_validos = [p for p in professores if any(d.nome == disciplina.nome for d in p.disciplinas_que_leciona)]
            salas_validas = [s for s in salas if s.capacidade >= turma.numero_de_alunos]

            if not professores_validos or not salas_validas:
                continue

            task_key = (turma.nome, disciplina.nome)
            all_tasks[task_key] = {
                "turma": turma, "disciplina": disciplina, "professores": professores_validos,
                "salas": salas_validas, "assignments": []
            }

    for task_key, task_data in all_tasks.items():
        turma, disciplina = task_data["turma"], task_data["disciplina"]
        duration = disciplina.duracao
        for professor in task_data["professores"]:
            for sala in task_data["salas"]:
                is_scheduled = model.NewBoolVar(f"is_scheduled_{turma.nome}_{disciplina.nome}_{professor.nome}_{sala.nome}")
                start_var = model.NewIntVar(0, horizon - duration, f"start_{turma.nome}_{disciplina.nome}")
                end_var = model.NewIntVar(0, horizon, f"end_{turma.nome}_{disciplina.nome}")
                interval_var = model.NewOptionalIntervalVar(start_var, duration, end_var, is_scheduled, f"interval_{turma.nome}_{disciplina.nome}_{professor.nome}_{sala.nome}")
                task_data["assignments"].append({"is_scheduled": is_scheduled, "interval": interval_var, "professor": professor, "sala": sala})
    print("Variáveis de intervalo criadas com sucesso!")

    for task_key, task_data in all_tasks.items():
        task_data["assignments"] = [assign for assign in task_data["assignments"] if assign["sala"].tipo_sala == task_data["disciplina"].tipo_sala_requerida]

    for prof in professores:
        prof.dummy_intervals = [model.NewFixedSizeIntervalVar(horario_to_int[h], 1, f"dummy_{prof.nome}_{h}") for h in prof.horarios_indisponiveis if h in horario_to_int]
    global_dummy_intervals = [model.NewFixedSizeIntervalVar(horario_to_int[h], 1, f"dummy_global_{h}") for h in restricoes_globais if h in horario_to_int]

    for turma in turmas:
        model.AddNoOverlap([assign["interval"] for task_data in all_tasks.values() if task_data["turma"] == turma for assign in task_data["assignments"]])
    for professor in professores:
        model.AddNoOverlap(professor.dummy_intervals + [assign["interval"] for task_data in all_tasks.values() for assign in task_data["assignments"] if assign["professor"] == professor])
    for sala in salas:
        model.AddNoOverlap(global_dummy_intervals + [assign["interval"] for task_data in all_tasks.values() for assign in task_data["assignments"] if assign["sala"] == sala])

    for task_key, task_data in all_tasks.items():
        model.AddAtMostOne([assign["is_scheduled"] for assign in task_data["assignments"]])

    for turno in ["Manhã", "Tarde", "Noite"]:
        allowed_indices = [horario_to_int[h] for h in horarios_por_turno[turno] if h in horario_to_int]
        if not allowed_indices: continue
        for task_data in all_tasks.values():
            if task_data["turma"].turno == turno:
                for assignment in task_data["assignments"]:
                    model.AddAllowedAssignments([assignment["interval"].StartExpr()], [(i,) for i in allowed_indices])
    print("Restrições do modelo v5 adicionadas.")

    objective_vars = [assign["is_scheduled"] for task_data in all_tasks.values() for assign in task_data["assignments"]]
    model.Maximize(sum(objective_vars))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 180.0
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"\nSolução encontrada com status {solver.StatusName(status)}.")
        print(f"Total de aulas agendadas: {solver.ObjectiveValue()}")
        schedule_by_turma = {turma.nome: {} for turma in turmas}
        for task_data in all_tasks.values():
            for assignment in task_data["assignments"]:
                if solver.Value(assignment["is_scheduled"]):
                    start_index = solver.Value(assignment["interval"].StartExpr())
                    duration = task_data["disciplina"].duracao
                    details = f"{task_data['disciplina'].nome}\n({assignment['professor'].nome})\n@{assignment['sala'].nome}"
                    for i in range(duration):
                        horario_str = int_to_horario.get(start_index + i)
                        if horario_str:
                            schedule_by_turma[task_data["turma"].nome][horario_str] = details

        print("\n--- Horário Final por Turma ---")
        for turma in turmas:
            print(f"\n{'='*100}\nHorário para: {turma.nome} (Turno: {turma.turno})\n{'='*100}")
            time_slots = sorted(list(set(h.split('_')[1] for h in horarios_por_turno[turma.turno])))
            df_data = {day: [schedule_by_turma[turma.nome].get(f"{day}_{slot}", "---") for slot in time_slots] for day in days_of_week}
            df = pd.DataFrame(df_data, index=time_slots)
            print(df.to_string())

        import matplotlib.pyplot as plt
        import numpy as np
        for turma in turmas:
            fig, ax = plt.subplots(figsize=(12, 8))
            ax.axis('off')
            time_slots = sorted(list(set(h.split('_')[1] for h in horarios_por_turno[turma.turno])))
            cell_text = [[schedule_by_turma[turma.nome].get(f"{day}_{slot}", "---") for day in days_of_week] for slot in time_slots]
            if not any(any(cell != "---" for cell in row) for row in cell_text):
                plt.close(fig)
                continue
            table = ax.table(cellText=cell_text, rowLabels=time_slots, colLabels=days_of_week, loc='center', cellLoc='center')
            table.auto_set_font_size(False); table.set_fontsize(9); table.scale(1, 2.5)
            ax.set_title(f"Horário: {turma.nome} (Turno: {turma.turno})", fontsize=16, pad=20)
            fig.tight_layout()
        # plt.show()
    else:
        print("\nNenhuma solução encontrada.")
else:
    print("\nNenhum dado para processar. Verifique o caminho do arquivo CSV ou a lógica de geração de dados de exemplo.")
