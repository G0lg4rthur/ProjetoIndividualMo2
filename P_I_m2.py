notas = ["e1_t2_p3_a4", "e2_t1_p4_a3", "e3_t3_p2_a1", "e4_t4_p1_a2"]
nomes_candidatos = ["Arthur", "João", "Ágatha", "Fábio"]

def buscar_candidatos(criterios):
    candidatos_encontrados = []
     #Percorre notas e nomes 
    for i in range(len(notas)):
        resultado = notas[i]
        nome = nomes_candidatos[i]
         #Verifica os critérios
        if any(criterio in resultado for criterio in criterios):
            candidatos_encontrados.append((nome, resultado))
    
    return candidatos_encontrados


while True:
    crit_e = input("Digite a nota de 'e': ")
    crit_t = input("Digite a nota de 't': ")
    crit_p = input("Digite a nota de 'p': ")
    crit_a = input("Digite a nota de 'a': ")

    if (
        not crit_e.isdigit() or
        not crit_t.isdigit() or
        not crit_p.isdigit() or
        not crit_a.isdigit() or
        int(crit_e) < 0 or
        int(crit_e) > 10 or
        int(crit_t) < 0 or
        int(crit_t) > 10 or
        int(crit_p) < 0 or
        int(crit_p) > 10 or
        int(crit_a) < 0 or
        int(crit_a) > 10
    ):
        print("Entrada inválida. As notas devem ser números inteiros entre 0 e 10.")
    else:
        break


#Lista com input do usuário
criterios = [f"e{crit_e}", f"t{crit_t}", f"p{crit_p}", f"a{crit_a}"]
#Chama a def
candidatos_encontrados = buscar_candidatos(criterios)


print("Candidatos encontrados:")
for candidato in candidatos_encontrados:
    nome, resultado = candidato
    print("Nome:", nome)
    print("Resultado:", resultado)
    print("------------------")
