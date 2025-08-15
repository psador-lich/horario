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
    """
    def __init__(self, nome, requer_laboratorio, curso=None):
        self.nome = nome
        self.requer_laboratorio = requer_laboratorio # Booleano
        self.curso = curso # Added course attribute

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

# 3. Criar dados de exemplo
# Estas são as instâncias específicas das classes usadas neste problema de agendamento.

# Disciplinas (Added course attribute)
# Assuming 10 disciplines per turma for example purposes and some laboratory requirements
disciplinas = []
disciplina_names = [
    "Matemática I", "Português I", "Química Geral", "Física Básica", "História Antiga",
    "Biologia Celular", "Geografia Física", "Artes Visuais", "Educação Física", "Inglês Básico", # Common disciplines
    "Programação Orientada a Objetos", "Estrutura de Dados", "Redes de Computadores", "Sistemas Operacionais", "Banco de Dados Avançado", # Informatics/ADS
    "Circuitos Digitais", "Eletrônica Analógica", "Máquinas de Corrente Contínua", "Instalações Elétricas", "Automação Industrial", # Automação/Eletrotécnica
    "Controle de Poluição", "Tratamento de Água", "Gerenciamento de Resíduos", "Legislação Ambiental", "Impacto Ambiental", # Controle Ambiental
    "Cálculo I", "Álgebra Linear", "Probabilidade e Estatística", "Desenho Técnico", "Estatística Aplicada ao Agronegócio", # More general/Agrocomputação
    "Fundamentos de Administração", "Marketing", "Recursos Humanos", "Logística", "Finanças Corporativas", # Administração
    "Desenvolvimento Web I", "Interface Humano-Computador", "Inteligência Artificial Aplicada", "Segurança da Informação", "Computação em Nuvem", # More Informatics/ADS
    "Sensores e Atuadores", "Robótica Móvel", "Sistemas Embarcados", "Microcontroladores", "Comunicação Industrial", # More Automação/Eletrotécnica
    "Manejo de Solo", "Fitopatologia", "Entomologia Agrícola", "Agrometeorologia", "Topografia", # More Agrocomputação
    "Direito Empresarial", "Contabilidade Geral", "Economia", "Sociologia", "Ética Profissional" # More general/Administração
]

for i, name in enumerate(disciplina_names):
    requer_laboratorio = False
    curso = None
    if "Química" in name or "Informática" in name or "Programação" in name or "Estrutura de Dados" in name or "Redes" in name or "Sistemas Operacionais" in name or "Banco de Dados" in name or "Circuitos" in name or "Eletrônica" in name or "Máquinas Elétricas" in name or "Instalações Elétricas" in name or "Automação" in name or "Robótica" in name or "Sistemas Embarcados" in name or "Microcontroladores" in name or "Fundamentos de Agrocomputação" in name or "Topografia" in name: # Simplified laboratory requirement logic
         requer_laboratorio = True

    # Assign courses (simplified example)
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
        curso = "Cursos Básicos" # Example for basic science disciplines

    disciplinas.append(Disciplina(name, requer_laboratorio, curso))

# Map disciplines by course (re-generated)
disciplinas_por_curso = {}
for disciplina in disciplinas:
    if disciplina.curso not in disciplinas_por_curso:
        disciplinas_por_curso[disciplina.curso] = []
    disciplinas_por_curso[disciplina.curso].append(disciplina)


# Professores (Create 40 professors and distribute disciplines)
professores = []
num_professors = 40
for i in range(1, num_professors + 1):
    professores.append(Professor(f"Professor {i}", [])) # Initialize with empty discipline list

# Distribute disciplines among professors (simple round-robin)
all_disciplines = list(disciplinas) # Create a copy
for i, disciplina in enumerate(all_disciplines):
    professor_index = i % num_professors
    professores[professor_index].disciplinas_que_leciona.append(disciplina)


# Salas (Keep the current 40 rooms configuration)
salas = []
# 25 salas de aula regulares
for i in range(1, 26):
    salas.append(Sala(f"Sala Regular {i}", capacidade=35, eh_laboratorio=False)) # Assuming capacity 35

# 5 laboratórios de informática
for i in range(1, 6):
    salas.append(Sala(f"Laboratório de Informática {i}", capacidade=20, eh_laboratorio=True, tipo_laboratorio="Informática")) # Assuming capacity 20

# 5 laboratórios de química
for i in range(1, 6):
    salas.append(Sala(f"Laboratório de Química {i}", capacidade=25, eh_laboratorio=True, tipo_laboratorio="Química")) # Assuming capacity 25

# 5 laboratórios de eletricidade/robótica
for i in range(1, 6):
    salas.append(Sala(f"Laboratório de Robótica/Eletricidade {i}", capacidade=20, eh_laboratorio=True, tipo_laboratorio="Robótica/Eletricidade")) # Assuming capacity 20


# Turmas (Updated based on the new request and disciplines)
turmas = []
# Curso de Informática (4 turmas - 2 Manhã, 2 Tarde)
# Assign 10 disciplines from Informatics/ADS to each turma (simplified - need to ensure enough disciplines exist)
informatica_ads_disciplines = disciplinas_por_curso.get("Informática/ADS", [])
for i in range(1, 3):
    turmas.append(Turma(f"Informática Manhã {i}", numero_de_alunos=20, disciplinas=informatica_ads_disciplines[:10], turno="Manhã")) # Assign first 10
    turmas.append(Turma(f"Informática Tarde {i}", numero_de_alunos=20, disciplinas=informatica_ads_disciplines[10:20] if len(informatica_ads_disciplines) >= 20 else informatica_ads_disciplines, turno="Tarde")) # Assign next 10 or remaining

# Curso de Automação (4 turmas - 2 Manhã, 2 Tarde)
automacao_eletrotecnica_disciplines = disciplinas_por_curso.get("Automação/Eletrotécnica", [])
for i in range(1, 3):
     turmas.append(Turma(f"Automação Manhã {i}", numero_de_alunos=25, disciplinas=automacao_eletrotecnica_disciplines[:10], turno="Manhã")) # Assign first 10
     turmas.append(Turma(f"Automação Tarde {i}", numero_de_alunos=25, disciplinas=automacao_eletrotecnica_disciplines[10:20] if len(automacao_eletrotecnica_disciplines) >= 20 else automacao_eletrotecnica_disciplines, turno="Tarde")) # Assign next 10 or remaining

# Curso de Controle Ambiental (8 turmas - 4 Manhã, 4 Tarde)
controle_ambiental_disciplines = disciplinas_por_curso.get("Controle Ambiental", [])
disciplines_per_ambiental_turma = len(controle_ambiental_disciplines) // 8 if len(controle_ambiental_disciplines) >= 80 else 10 # Ensure at least 10 if possible

current_discipline_index = 0
for i in range(1, 5):
    turmas.append(Turma(f"Controle Ambiental Manhã {i}", numero_de_alunos=30, disciplinas=controle_ambiental_disciplines[current_discipline_index:current_discipline_index + disciplines_per_ambiental_turma], turno="Manhã"))
    current_discipline_index += disciplines_per_ambiental_turma
    turmas.append(Turma(f"Controle Ambiental Tarde {i}", numero_de_alunos=30, disciplinas=controle_ambiental_disciplines[current_discipline_index:current_discipline_index + disciplines_per_ambiental_turma], turno="Tarde"))
    current_discipline_index += disciplines_per_ambiental_turma


# Curso de Administração (1 turma - Tarde)
administracao_disciplines = disciplinas_por_curso.get("Administração", [])
turmas.append(Turma("Administração Tarde 1", numero_de_alunos=35, disciplinas=administracao_disciplines[:10], turno="Tarde"))

# Curso de Eletrotécnica (3 turmas - Noite)
eletrotecnica_disciplines = disciplinas_por_curso.get("Automação/Eletrotécnica", []) # Using same pool for simplicity
disciplines_per_eletrotecnica_turma = len(eletrotecnica_disciplines) // 3 if len(eletrotecnica_disciplines) >= 15 else 5 # Ensure at least 5 if possible

current_discipline_index = 0
for i in range(1, 4):
     turmas.append(Turma(f"Eletrotécnica Noite {i}", numero_de_alunos=20, disciplinas=eletrotecnica_disciplines[current_discipline_index:current_discipline_index + disciplines_per_eletrotecnica_turma], turno="Noite"))
     current_discipline_index += disciplines_per_eletrotecnica_turma


# Curso de Análise e Desenvolvimento de Sistemas (3 turmas - Noite)
ads_disciplines = disciplinas_por_curso.get("Informática/ADS", []) # Using same pool for simplicity
disciplines_per_ads_turma = len(ads_disciplines) // 3 if len(ads_disciplines) >= 15 else 5 # Ensure at least 5 if possible

current_discipline_index = 0
for i in range(1, 4):
    turmas.append(Turma(f"ADS Noite {i}", numero_de_alunos=30, disciplinas=ads_disciplines[current_discipline_index:current_discipline_index + disciplines_per_ads_turma], turno="Noite"))
    current_discipline_index += disciplines_per_ads_turma


# Curso de Agrocomputação (1 turma - Noite)
agrocomputacao_disciplines = disciplinas_por_curso.get("Agrocomputação", [])
turmas.append(Turma("Agrocomputação Noite 1", numero_de_alunos=25, disciplinas=agrocomputacao_disciplines[:5], turno="Noite")) # Assign first 5


# Horários (Morning, Afternoon, Night shifts)
from datetime import datetime, timedelta

# Define the start time and class duration
morning_start_time = datetime.strptime('07:30', '%H:%M')
afternoon_start_time = datetime.strptime('13:30', '%H:%M')
night_start_time = datetime.strptime('19:00', '%H:%M') # Night shift start time
class_duration = timedelta(minutes=45)
break_duration = timedelta(minutes=15)
morning_afternoon_classes_before_break = 3
morning_afternoon_classes_after_break = 3
night_classes_before_break = 2 # Number of classes before break at night
night_classes_after_break = 2 # Number of classes after break at night
days_of_week = ["Segunda", "Terca", "Quarta", "Quinta", "Sexta"]

# Generate the schedule for all shifts
horarios_por_turno = {
    "Manhã": [],
    "Tarde": [],
    "Noite": []
}

# Generate time slots and assign them to the correct shift
for day in days_of_week:
    # Morning schedule
    current_time = morning_start_time
    for i in range(morning_afternoon_classes_before_break):
        horarios_por_turno["Manhã"].append(f"{day}_{current_time.strftime('%Hh%M')}")
        current_time += class_duration
    current_time += break_duration # Morning break
    for i in range(morning_afternoon_classes_after_break):
        horarios_por_turno["Manhã"].append(f"{day}_{current_time.strftime('%Hh%M')}")
        current_time += class_duration

    # Afternoon schedule
    current_time = afternoon_start_time
    for i in range(morning_afternoon_classes_before_break):
        horarios_por_turno["Tarde"].append(f"{day}_{current_time.strftime('%Hh%M')}")
        current_time += class_duration
    current_time += break_duration # Afternoon break
    for i in range(morning_afternoon_classes_after_break):
        horarios_por_turno["Tarde"].append(f"{day}_{current_time.strftime('%Hh%M')}")
        current_time += class_duration

    # Night schedule
    current_time = night_start_time
    for i in range(night_classes_before_break):
        horarios_por_turno["Noite"].append(f"{day}_{current_time.strftime('%Hh%M')}")
        current_time += class_duration
    current_time += break_duration # Night break
    for i in range(night_classes_after_break):
        horarios_por_turno["Noite"].append(f"{day}_{current_time.strftime('%Hh%M')}")
        current_time += class_duration

# Create a single flat list of all unique time slots for the solver
horarios = sorted(list(set(
    horarios_por_turno["Manhã"] +
    horarios_por_turno["Tarde"] +
    horarios_por_turno["Noite"]
)))


print("Dados de exemplo (incluindo salas atualizadas, turmas e professores) criados com sucesso!")

# Import the necessary module from ortools
# cp_model is the module for Constraint Programming.
from ortools.sat.python import cp_model

# Initialize the solver model
# This creates an instance of the CpModel, which will hold all variables and constraints.
model = cp_model.CpModel()

# Mapear dados para o modelo
# Create convenient mapping dictionaries for easier access to data during constraint definition.

# 1. Crie um dicionário chamado aulas
# Maps (turma_name, disciplina_name) to the corresponding turma and disciplina objects.
# This should be done *after* turmas and their disciplines are defined.
aulas = {}
for turma in turmas:
    for disciplina in turma.disciplinas:
        aulas[(turma.nome, disciplina.nome)] = {
            'turma': turma,
            'disciplina': disciplina
        }

# Define the decision variables
# aulas_vars is a dictionary storing boolean variables.
# aulas_vars[turma][disciplina][professor][sala][horario] = True if this specific combination is scheduled.
aulas_vars = {}
# 2. Crie um dicionário chamado professores_por_disciplina
# Maps disciplina_name to a list of Professor objects who can teach that discipline.
professores_por_disciplina = {}
for disciplina in disciplinas:
    professores_por_disciplina[disciplina.nome] = []
for professor in professores:
    for disciplina in professor.disciplinas_que_leciona:
        professores_por_disciplina[disciplina.nome].append(professor)

# 3. Crie um dicionário chamado disciplinas_por_professor
# Maps professor_name to a list of Disciplina objects they can teach.
disciplinas_por_professor = {}
for professor in professores:
    disciplinas_por_professor[professor.nome] = professor.disciplinas_que_leciona

for turma_name, disciplina_name in aulas.keys():
    turma = aulas[(turma_name, disciplina_name)]['turma']
    disciplina = aulas[(turma_name, disciplina_name)]['disciplina']

    if turma_name not in aulas_vars:
        aulas_vars[turma_name] = {}
    if disciplina_name not in aulas_vars[turma_name]:
        aulas_vars[turma_name][disciplina_name] = {}

    # Iterate through professors who can teach this discipline
    for professor in professores_por_disciplina.get(disciplina_name, []):
        if professor.nome not in aulas_vars[turma_name][disciplina_name]:
            aulas_vars[turma_name][disciplina_name][professor.nome] = {}

        # Iterate through all rooms and times
        for sala in salas:
            if sala.nome not in aulas_vars[turma_name][disciplina_name][professor.nome]:
                aulas_vars[turma_name][disciplina_name][professor.nome][sala.nome] = {}
            for horario in horarios:
                var_name = f"{turma_name}_{disciplina_name}_{professor.nome}_{sala.nome}_{horario}"
                aulas_vars[turma_name][disciplina_name][professor.nome][sala.nome][horario] = model.NewBoolVar(var_name)

print("Variáveis booleanas (com professor) criadas com sucesso!")

# 4. Crie um dicionário chamado salas_por_tipo
# Separates rooms into 'laboratorio' and 'normal' types, and by laboratory type.
salas_por_tipo = {
    'laboratorio': {
        'Informática': [],
        'Química': [],
        'Robótica/Eletricidade': []
    },
    'normal': []
}
for sala in salas:
    if sala.eh_laboratorio:
        if sala.tipo_laboratorio in salas_por_tipo['laboratorio']:
             salas_por_tipo['laboratorio'][sala.tipo_laboratorio].append(sala)
        # Handle potential laboratories without a specified type if necessary
    else:
        salas_por_tipo['normal'].append(sala)

print("Mapeamentos criados com sucesso!")

# The objective is to schedule as many classes as possible, with some preferences.
objective = []

# Add hard constraints
# These are constraints that MUST be satisfied for a solution to be valid.

# 1. Professor can only be in one place at a time
for professor in professores:
    for horario in horarios:
        model.AddAtMostOne(
            aulas_vars[t_name][d_name][professor.nome][s_name][horario]
            for t_name, d_name_map in aulas_vars.items()
            for d_name, p_name_map in d_name_map.items()
            if professor.nome in p_name_map
            for s_name in p_name_map[professor.nome]
        )

# 2. Turma can only have one class at a time
for turma_name, disciplina_dict in aulas_vars.items():
    for horario in horarios:
        model.AddAtMostOne(
            aulas_vars[turma_name][d_name][p_name][s_name][horario]
            for d_name, p_name_map in disciplina_dict.items()
            for p_name, s_name_map in p_name_map.items()
            for s_name in s_name_map
        )

# 3. Room can only be used by one class at a time
for sala in salas:
    for horario in horarios:
        model.AddAtMostOne(
            aulas_vars[t_name][d_name][p_name][sala.nome][horario]
            for t_name, d_name_map in aulas_vars.items()
            for d_name, p_name_map in d_name_map.items()
            for p_name, s_name_map in p_name_map.items()
            if sala.nome in s_name_map
        )

# 4. Each aula (turma, disciplina) should be assigned to at most one professor, room, and time.
# We will try to schedule as many as possible.
for turma_name, disciplina_name in aulas.keys():
    assignment_vars = []
    if turma_name in aulas_vars and disciplina_name in aulas_vars[turma_name]:
        assignment_vars = [
            var
            for p_name, s_name_map in aulas_vars[turma_name][disciplina_name].items()
            for s_name, h_name_map in s_name_map.items()
            for h_name, var in h_name_map.items()
        ]
    if assignment_vars:
        # Relax the constraint to allow classes to be unscheduled
        model.AddAtMostOne(assignment_vars)
        # Add scheduling the class to the objective function. The solver will try to maximize this.
        objective.extend(assignment_vars)
    else:
        print(f"Warning: No variables created for Aula: Turma {turma_name}, Disciplina {disciplina_name}. This aula cannot be scheduled.")

# 5. Room capacity must be respected
for turma_name, disciplina_name, professor_name, sala_name, horario in (
    (t, d, p, s, h)
    for t, d_map in aulas_vars.items()
    for d, p_map in d_map.items()
    for p, s_map in p_map.items()
    for s, h_map in s_map.items()
    for h in h_map
):
    turma = aulas[(turma_name, disciplina_name)]['turma']
    # Find the sala object from its name
    sala_obj = next((s for s in salas if s.nome == sala_name), None)
    if sala_obj and sala_obj.capacidade < turma.numero_de_alunos:
        model.Add(aulas_vars[turma_name][disciplina_name][professor_name][sala_name][horario] == 0)

# 6. Lab disciplines must be in corresponding labs (Generalized)
lab_map = {
    "Informática": ["Informática/ADS"],
    "Química": ["Controle Ambiental"], # Example mapping, adjust course names if needed
    "Robótica/Eletricidade": ["Automação/Eletrotécnica"]
}

for lab_type, courses in lab_map.items():
    # Get all disciplines for the specified courses
    disciplines_for_lab = [
        d.nome for d in disciplinas if d.curso in courses and d.requer_laboratorio
    ]
    # Get all rooms of this lab type
    lab_rooms = [s.nome for s in salas_por_tipo['laboratorio'].get(lab_type, [])]

    if not disciplines_for_lab or not lab_rooms:
        continue # Skip if no such disciplines or labs

    for turma_name, d_name, p_name, s_name, horario_var in (
        (t, d, p, s, var)
        for t, d_map in aulas_vars.items()
        for d, p_map in d_map.items() if d in disciplines_for_lab
        for p, s_map in p_map.items()
        for s, h_map in s_map.items()
        for h, var in h_map.items()
    ):
        # If a discipline requires a lab, it must be in a room of that lab type
        if s_name not in lab_rooms:
            model.Add(horario_var == 0)

print("Restrições rígidas (refatoradas) adicionadas com sucesso!")

# Add soft constraints (preferences)
# These are not strictly required but contribute to the optimization objective.
# The objective will be to maximize the number of satisfied preferences.

# Example 1: Professor 1 prefers to teach Matemática I.
# We can add the assignment variable for this professor teaching this class to the objective.
# The solver will get a "point" for making this assignment.
professor_1_name = "Professor 1"
matematica_i_name = "Matemática I"

if professor_1_name in disciplinas_por_professor and matematica_i_name in [d.nome for d in disciplinas_por_professor[professor_1_name]]:
    for t_name, d_name, p_name, s_name, h_name, var in (
        (t, d, p, s, h, v)
        for t, d_map in aulas_vars.items()
        for d, p_map in d_map.items() if d == matematica_i_name
        for p, s_map in p_map.items() if p == professor_1_name
        for s, h_map in s_map.items()
        for h, v in h_map.items()
    ):
        objective.append(var)

# Example 2: Turma "Informática Manhã 1" prefers to have "Programação Orientada a Objetos" on Mondays.
turma_pref_name = "Informática Manhã 1"
disc_pref_name = "Programação Orientada a Objetos"

if turma_pref_name in aulas_vars and disc_pref_name in aulas_vars[turma_pref_name]:
    for p_name, s_name, h_name, var in (
        (p, s, h, v)
        for p, s_map in aulas_vars[turma_pref_name][disc_pref_name].items()
        for s, h_map in s_map.items()
        for h, v in h_map.items()
        if h.startswith("Segunda")
    ):
        objective.append(var)


# Define the optimization objective: Maximize the sum of preference variables
if objective:
    model.Maximize(sum(objective))
    print("Objetivo de otimização (com preferências) definido com sucesso!")
else:
    print("Nenhum objetivo de otimização foi definido.")


# Solve the model with optimization
# Create a CpSolver instance and solve the model.
solver = cp_model.CpSolver()
status = solver.Solve(model)

# Process and display the optimized solution
# Check the status of the solution and print the results.
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print('Solution found.')
    if objective:
        print(f'Optimal objective value: {solver.ObjectiveValue()}')
    else:
        print('No optimization objective was set.')

    # (Step 2) Restructure data to be organized by turma
    schedule_by_turma = {turma.nome: {} for turma in turmas}
    for (turma_name, d_map) in aulas_vars.items():
        for (disciplina_name, p_map) in d_map.items():
            for (professor_name, s_map) in p_map.items():
                for (sala_name, h_map) in s_map.items():
                    for (horario_name, var) in h_map.items():
                        if solver.Value(var) == 1:
                            schedule_by_turma[turma_name][horario_name] = f"{disciplina_name}\n({professor_name})\n@{sala_name}"

    # (Step 3) Print a separate text-based schedule for each turma
    print("\n--- Grade de Horários por Turma (Texto) ---")
    for turma in turmas:
        print("\n" + "="*80)
        print(f"Horário para: {turma.nome} (Turno: {turma.turno})")
        print("="*80)

        turma_horarios = horarios_por_turno[turma.turno]
        time_slots = sorted(list(set(h.split('_')[1] for h in turma_horarios)))

        header = ["Dia"] + time_slots
        # Adjust the width based on the number of time slots
        col_width = 35
        row_format = "{:<10}" + "{:<{width}}" * len(time_slots)

        print(row_format.format(*header, width=col_width))
        print("-" * (10 + col_width * len(time_slots)))

        for day in days_of_week:
            row_data = [day]
            for slot in time_slots:
                horario_key = f"{day}_{slot}"
                row_data.append(schedule_by_turma[turma.nome].get(horario_key, "---"))
            print(row_format.format(*row_data, width=col_width))

    # (Step 4) Create a separate plot for each turma's schedule
    import matplotlib.pyplot as plt
    import numpy as np

    print("\n--- Gerando Grades Visuais por Turma ---")
    for turma in turmas:
        fig, ax = plt.subplots(figsize=(16, 4)) # New figure for each turma
        ax.axis('off') # Hide axes

        turma_horarios = horarios_por_turno[turma.turno]
        time_slots = sorted(list(set(h.split('_')[1] for h in turma_horarios)))

        cell_text = []
        for day in days_of_week:
            row_data = []
            for slot in time_slots:
                horario_key = f"{day}_{slot}"
                cell_text.append(schedule_by_turma[turma.nome].get(horario_key, "---"))

        # Reshape data for the table
        if not cell_text:
            print(f"Nenhuma aula agendada para {turma.nome} para exibir na grade visual.")
            plt.close(fig) # Close the empty figure
            continue

        cell_text = np.array(cell_text).reshape(len(days_of_week), len(time_slots))

        table = ax.table(cellText=cell_text,
                         rowLabels=days_of_week,
                         colLabels=time_slots,
                         loc='center',
                         cellLoc='center')

        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table.scale(1, 2.5) # Adjust scale for better layout

        ax.set_title(f"Horário: {turma.nome} (Turno: {turma.turno})", fontsize=14, pad=20)
        fig.tight_layout()

    # plt.show()

else:
    print('No solution found.')
