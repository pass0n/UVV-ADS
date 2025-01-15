# Sistema de Avaliação - UVVON

Este projeto é um algoritmo em Python desenvolvido para calcular e analisar as notas de alunos de um curso EAD da UVVON. O objetivo é determinar o status de aprovação dos estudantes com base nas notas obtidas em atividades online e provas.

## Descrição do Problema

O sistema lê as notas de 100 alunos e calcula as seguintes métricas:

- **Atividade Online Pontuada 1 (AOP1)**: Nota de 0 a 1.
- **Atividade Online Pontuada 2 (AOP2)**: Nota de 0 a 2.
- **Atividade Online Pontuada 3 (AOP3)**: Nota de 0 a 1.
- **Prova Regular**: Nota de 0 a 6.
- **Prova de Recuperação**: Nota de 0 a 10 (apenas se a soma inicial das atividades e da prova regular for menor que 7).

### Cálculos

O sistema realiza os seguintes cálculos para determinar o status do aluno:

1. **Soma do Módulo (SM)** = AOP1 + AOP2 + AOP3 + Prova Regular
2. **Média do Módulo (MM)** = (AOP1 + AOP2 + AOP3 + Prova Regular + Prova de Recuperação) / 2

### Status do Aluno

Com base nos cálculos acima, o status do aluno pode ser:

- **Aprovado**:
  - Soma do Módulo (SM) >= 7.0 ou
  - Média do Módulo (MM) >= 5.0
- **Prova de Recuperação**:
  - Soma do Módulo (SM) < 7.0
- **Reprovado após a prova de recuperação**:
  - Média do Módulo (MM) < 5.0
- **Reprovado Direto**:
  - Soma do Módulo (SM) < 3.0

O programa também calcula a porcentagem de alunos aprovados e reprovados.

## Funcionalidades

- **Leitura de notas** com validação: impede a inserção de valores fora dos intervalos definidos para cada atividade/prova.
- **Cálculo automático** do status de aprovação de cada aluno.
- **Exibição dos resultados** de forma clara e objetiva, incluindo a porcentagem de aprovação e reprovação.