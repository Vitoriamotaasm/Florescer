from datetime import datetime, timedelta

def calcular_ciclo(data_ultima_menstruacao: str, duracao_ciclo: int = 28):
    """
    Calcula os próximos 3 ciclos menstruais com base na data da última menstruação.

    Args:
        data_ultima_menstruacao (str): Data no formato dd/mm/aaaa
        duracao_ciclo (int): Duração média do ciclo menstrual (padrão 28 dias)

    Returns:
        list[dict]: Lista com as previsões de menstruação, ovulação e TPM
    """
    try:
        data_inicial = datetime.strptime(data_ultima_menstruacao, "%d/%m/%Y")
    except ValueError:
        raise ValueError("Formato de data inválido. Use dd/mm/aaaa.")

    resultados = []
    for i in range(1, 4):
        proximo_ciclo = data_inicial + timedelta(days=duracao_ciclo * i)
        ovulacao = proximo_ciclo - timedelta(days=14)
        tpm_inicio = proximo_ciclo - timedelta(days=7)

        resultados.append({
            "Ciclo": i,
            "Próxima Menstruação": proximo_ciclo.strftime("%d/%m/%Y"),
            "Ovulação Estimada": ovulacao.strftime("%d/%m/%Y"),
            "Início da TPM": tpm_inicio.strftime("%d/%m/%Y")
        })

    return resultados


def exibir_resultados(resultados):
    """
    Exibe os resultados de forma formatada no terminal.
    """
    print("\n📅 Previsão dos próximos ciclos:\n")
    for r in resultados:
        print(f"Ciclo {r['Ciclo']}:")
        print(f"  Próxima Menstruação: {r['Próxima Menstruação']}")
        print(f"  Ovulação Estimada : {r['Ovulação Estimada']}")
        print(f"  Início da TPM      : {r['Início da TPM']}\n")


def main():
    """
    Função principal que executa a aplicação.
    """
    print("\n🌸 Bem-vinda ao Florescer! Sua calculadora de ciclo menstrual ✨\n")
    data = input("📌 Digite a data da sua última menstruação (dd/mm/aaaa): ")
    duracao = input("⏱️ Quantos dias dura seu ciclo? (Pressione Enter para padrão de 28 dias): ")

    duracao = int(duracao) if duracao.strip() else 28

    try:
        resultados = calcular_ciclo(data, duracao)
        exibir_resultados(resultados)
    except ValueError as e:
        print(f"\n⚠️ Erro: {e}")


if __name__ == "__main__":
    main()