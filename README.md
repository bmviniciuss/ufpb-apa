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
- 2 -> 4 : `M[R[i]][R[i + 1]]`
- 5 -> 7 : `M[R[k]][R[K + 1]]`

### Ligadas

- 0 -> 4 : `M[R[i - 1]][R[i + 1]]`
- 5 -> 2 : `M[R[k]][R[i]]`
- 2 -> 7 : `M[R[i]][R[k+1]]`

## Swap

### Original

`[2, 3, 5, 7, 8, 2]`

### Swap

`[2, 8, 5, 7, 3, 2]`

### Index

`(i, k) = (1, 4)`

### Quebradas:

- 2->3: `M[R[i-1]][R[i]]`
- 3->5: `M[R[i]][R[i+1]]`
- 7->8: `M[R[k-1]][R[k]]`
- 8->2: `M[R[k]][R[k+1]]`

conexão:

- 2->8 : `M[R[i - 1]][R[k]]`
- 8->5 : `M[R[k]][R[i+1]]`
- 7->3 : `M[R[k-1]][R[i]]`
- 3->2 : `M[R[i]][R[i-1]]`
