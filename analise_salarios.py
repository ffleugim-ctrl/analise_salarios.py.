# analise_salarios.py.# Lista de colaboradores (Simulando uma base de dados real)
base_rh = [
    {"nome": "Miguel", "depto": "Logística", "salario": 3500},
    {"nome": "Ana", "depto": "RH", "salario": 4200},
    {"nome": "Carlos", "depto": "Logística", "salario": 2800},
    {"nome": "Beatriz", "depto": "Logística", "salario": 3100},
    {"nome": "Marcos", "depto": "TI", "salario": 5000}
]

print("--- RELATÓRIO DE SALÁRIOS: LOGÍSTICA ---")

# Filtrando apenas quem é da Logística e ganha acima de 3000
for funcionario in base_rh:
    if funcionario["depto"] == "Logística" and funcionario["salario"] > 3000:
        print(f"Funcionário: {funcionario['nome']} | Salário: R$ {funcionario['salario']}")

print("---------------------------------------")
