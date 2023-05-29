# Readme - Busca de Candidatos por Critérios de Notas

Este código em Python permite buscar candidatos com base em critérios de notas. É possível definir os critérios de busca para cada uma das notas "e" (exercício), "t" (trabalho), "p" (prova) e "a" (apresentação), e o programa retornará os candidatos que atendem a esses critérios.

## Funcionamento do Código

O código utiliza duas listas para armazenar as notas e os nomes dos candidatos:

```python
notas = ["e1_t2_p3_a4", "e2_t1_p4_a3", "e3_t3_p2_a1", "e4_t4_p1_a2"]
nomes_candidatos = ["Arthur", "João", "Ágatha", "Fábio"]
```

A função `buscar_candidatos(criterios)` é responsável por realizar a busca com base nos critérios informados. Ela percorre as notas e nomes dos candidatos, verificando se algum dos critérios está presente na nota correspondente. Caso um critério seja encontrado, o candidato é adicionado a uma lista de candidatos encontrados. Ao final, a função retorna essa lista.

Os critérios são informados pelo usuário por meio de inputs, sendo solicitado o valor de cada uma das notas "e", "t", "p" e "a":

```python
crit_e = input("Digite a nota de 'e': ")
crit_t = input("Digite a nota de 't': ")
crit_p = input("Digite a nota de 'p': ")
crit_a = input("Digite a nota de 'a': ")
```

Em seguida, os critérios são utilizados para formar uma lista chamada `criterios`, que contém as strings correspondentes aos critérios informados pelo usuário.

Por fim, o código realiza a busca de candidatos chamando a função `buscar_candidatos(criterios)` e imprime na tela os candidatos encontrados:

```python
print("Candidatos encontrados:")
for candidato in candidatos_encontrados:
    nome, resultado = candidato
    print("Nome:", nome)
    print("Resultado:", resultado)
    print("------------------")
```


## Observações

- Certifique-se de fornecer os critérios de busca no formato adequado, por exemplo, "1" para uma nota específica ou "1,2" para buscar candidatos com uma das duas notas.
- O programa considera que a ordem das notas na lista `notas` corresponde à ordem dos nomes na lista `nomes_candidatos`. Portanto, é importante manter a consistência entre as listas.

