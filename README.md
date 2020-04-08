# UFPB - Análise E Projeto De Algoritmos

Código do projeto final das disciplina de APA.

## Instancias

- O número de vértices pode ser encontrado no campo `DIMENSION`.
- A capacidade de cada veículo pode ser encontrada no campo `CAPACITY`.
- A matriz de custos pode ser encontrada no campo `EDGE_WEIGHT_SECTION`.
- O vértice 0 é o depósito.
- Considerem que não há limite no número de veículos.

## Utilização

- Clone o Repositório

```bash
git clone https://github.com/bmviniciuss/ufpb-apa
```

- Entrar na pasta

```bash
cd ufpb-apa
```

- Rodar o script selecionando o path para a pasta com as entradas

```bash
python3 main.py -f instancias_teste/P-n50-k10.txt
```

- Se quiser escrever um arquivo de output do teste adicione a flag `-o`

```bash
python3 main.py -f instancias_teste/P-n50-k10.txt -o
```

# Otimizações

## Reinsertion

### Original

`[ 0, 2, 4, 5, 7, 0]`

### Teste

`[ 0, 4, 5, 2, 7, 0]`

### index

`(i, k) = (1, 3)`

### Quebradas

- 0 -> 2 : `M[R[i-1]][R[i]]`
- 2 -> 4 : `M[R[i]][R[k - 1]]`
- 5 -> 7 : `M[R[k]][R[K + 1]]`

### Ligadas

- 0 -> 4 : `M[R[i - 1]][R[k -1]]`
- 5 -> 2 : `M[R[k]][R[i]]`
- 2 -> 7 : `M[R[i]][R[k+1]]`

### Reinsertion - EDGE CASE

### Original

`[ 0, 2, 4, 5, 7, 0]`

### Teste

`[ 0, 4, 2, 5, 7, 0]`

### index

`(i, k) = (1, 2)`

### Quebradas

- 0 -> 2 : `M[R[i-1]][R[i]]`
- 4 -> 5 : `M[R[k]][R[K + 1]]`

### Ligadas

- 0 -> 4 : `M[R[i - 1]][R[k]]`
- 2 -> 5 : `M[R[i]][R[k+1]]`

## Swap

### Original

`[2, 3, 5, 7, 8, 9]`

### Swap

`[2, 8, 5, 7, 3, 9]`

### Index

`(i, k) = (1, 4)`

### Quebradas:

- 2->3: `M[R[i - 1]][R[i]]`
- 3->5: `M[R[i]][R[i + 1]]`
- 7->8: `M[R[k - 1]][R[k]]`
- 8->9: `M[R[k]][R[k + 1]]`

### Conexão:

- 2->8 : `M[R[i - 1]][R[k]]`
- 8->5 : `M[R[k]][R[i + 1]]`
- 7->3 : `M[R[k - 1]][R[i]]`
- 3->9 : `M[R[i]][R[k + 1]]`

## Swap - Edge Case

`[2, 3, 5, 7, 8, 9]`
`[2, 3, 7, 5, 8, 9]`

`(i, k) = (2, 3)`

Quebra

- 3->5 : `M[R[i - 1]][R[i]]`
- 7->8 : `M[R[k]][R[k + 1]]`

Conexao

- 3 -> 7: `M[R[i - 1]][R[k]]`
- 5 -> 8: `M[R[i]][R[k + 1]]`

## 2-Opt

## Original

`0 , 2 , 8` `4 , 12 , 11 , 9` `3 , 0]`
`9, 11, 12, 4`
(i,k) = (3,6)

## Quebrou

- 8 -> 4: `M[R[i-1]][R[i]]`
- 9 -> 3: `M[R[k]][R[k +1]]`

## Conexão

- 8 -> 9: `M[R[i-1]][R[k]]`
- 4 -> 3: `M[R[i]][R[k+1]]`

## Final

1. `[0, 2 , 8]`

2. `[9, 11, 12, 4]`

3. `[3 , 0]`

`[0, 2 , 8, 9, 11, 12, 4, 3 , 0]`

## 2-Opt - EDGE CASE

## Original

`0 , 2 , 8` `4` `, 12 , 11 , 9 , 3 , 0]`
(i,k) = (3,4)

## Quebrou

- 8 -> 4: `M[R[i-1]][R[i]]`
- 9 -> 3: `M[R[k]][R[k +1]]`

## Conexão

- 8 -> 9: `M[R[i-1]][R[k]]`
- 4 -> 3: `M[R[i]][R[k+1]]`

## Final

1. `[0, 2 , 8]`

2. `[9, 11, 12, 4]`

3. `[3 , 0]`

`[0, 2 , 8, 9, 11, 12, 4, 3 , 0]`

## Swap

### Original

`[2, 3, 5, 7, 8, 9]`

`[2, 8, 5, 7, 3, 9]`

### Swap

`(i, k) = (1, 4)`

### Quebradas:

- 2->3: `M[R[i - 1]][R[i]]`
- 3->5: `M[R[i]][R[i + 1]]`
- 7->8: `M[R[k - 1]][R[k]]`
- 8->9: `M[R[k]][R[k + 1]]`

### Conexão:

- 2->8 : `M[R[i - 1]][R[k]]`
- 8->5 : `M[R[k]][R[i + 1]]`
- 7->3 : `M[R[k - 1]][R[i]]`
- 3->9 : `M[R[i]][R[k + 1]]`

## Reinsertion

### Original

`[1 2 3 4 5 6 7 8]`
`[1 2 4 5 6 3 7 8]`

### index

`(i, k) = (2, 5)`

### Quebradas

- 2->3: `M[R[i - 1]][R[i]]`
- 3->4: `M[R[i]][R[i + 1]]`
- 6->7: `M[R[k]][R[k + 1]]`

### Ligadas

- 2->4: `M[R[i - 1]][R[i + 1]]`
- 6->3: `M[R[k]][R[i]]`
- 3->7: `M[R[i]][R[k + 1]]`

## Reinsertion - Edge Case

### Original

`[1 2 3 4 5 6 7 8]`
`[1 2 4 3 5 6 7 8]`

### index

`(i, k) = (2, 7)`

### Quebradas

- 2->3: `M[R[i - 1]][R[i]]`
- 4->5: `M[R[k]][R[K + 1]]`

### Ligadas

- 2->4: `M[R[i - 1]][R[k]]`
- 3->5: `M[R[i]][R[K + 1]]`
