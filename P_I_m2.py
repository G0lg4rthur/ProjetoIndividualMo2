notas = ["e1_t2_p3_a4", "e2_t1_p4_a3", "e3_t3_p2_a1", "e4_t4_p1_a2"]
nomes_candidatos = ["Arthur", "João", "Ágatha", "Fábio"]

def buscar_candidatos(criterios):
    candidatos_encontrados = []
    
    for i in range(len(notas)):
        resultado = notas[i]
        nome = nomes_candidatos[i]

        if any(criterio in resultado for criterio in criterios):
            candidatos_encontrados.append((nome, resultado))
    
    return candidatos_encontrados


crit_e = input("Digite a nota de 'e': ")
crit_t = input("Digite a nota de 't': ")
crit_p = input("Digite a nota de 'p': ")
crit_a = input("Digite a nota de 'a': ")


criterios = [f"e{crit_e}", f"t{crit_t}", f"p{crit_p}", f"a{crit_a}"]
candidatos_encontrados = buscar_candidatos(criterios)


print("Candidatos encontrados:")
for candidato in candidatos_encontrados:
    nome, resultado = candidato
    print("Nome:", nome)
    print("Resultado:", resultado)
    print("------------------")
