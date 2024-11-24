notas = {}
alunos = 2
alunos_aprovados = 0

try:
    for i in range(alunos):

        nota_AOP1 = float(input(f"Aluno{i} - Nota [0 - 1] na AOP1: "))
        if nota_AOP1 < 0 or nota_AOP1 > 1:
            raise ValueError("A nota da AOP1 deve ser entre 0 ou 1.")

        nota_AOP2 = float(input(f"Aluno{i} - Nota [0 - 2] na AOP2: "))
        if nota_AOP2 < 0 or nota_AOP2 > 2:
            raise ValueError("A nota da AOP2 deve ser entre 0 ou 1.")

        nota_AOP3 = float(input(f"Aluno{i} - Nota [0 - 1] na AOP3 "))
        if nota_AOP3 < 0 or nota_AOP3 > 1:
            raise ValueError("A nota da AOP3 deve ser entre 0 ou 1.")

        nota_prova_regular = float(input(f"Aluno{i} - Nota [0 - 6] da PROVA REGULAR: "))
        if nota_prova_regular < 0 or nota_prova_regular > 6:
            raise ValueError("A nota da Prova regular deve ser entre 0 ou 6.")

        sm = nota_AOP1 + nota_AOP2 + nota_AOP3 + nota_prova_regular
        mm = sm
        status = ""

        if sm < 3:
            status = "Reprovado direto"
        elif sm < 7:
            nota_recuperacao = int(input("Nota [0 - 10] da PROVA DE RECUPERAÇÃO"))
            if nota_recuperacao < 0 or nota_recuperacao > 10:
                raise ValueError(
                    "A nota da Prova de recuperação deve ser entre 0 ou 10."
                )

            mm = (sm + nota_recuperacao) / 2
            status = "Prova de Recuperação"

            if mm < 5:
                status = "Reprovado"

        if sm >= 7 and mm >= 5:
            alunos_aprovados += 1
            status = "Aprovado"

        notas[f"Aluno{i}"] = {
            "Soma dos Módulos": sm,
            "Média dos Módulos": mm,
            "Status do Aluno": status,
        }

    for i in notas.items():
        print(i)

    porcentagem_aprovados = (alunos_aprovados / alunos) * 100
    print(f"Total de alunos aprovados: {alunos_aprovados} ({porcentagem_aprovados}%)")

except ValueError as e:
    print("Erro:", e)
