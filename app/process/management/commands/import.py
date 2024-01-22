import csv
from datetime import datetime
from decimal import Decimal, InvalidOperation

import numpy as np
import pandas as pd
from django.core.management.base import BaseCommand

from app.process.models import *


def converter_para_decimal(valor_monetario_str):
    # Remova o símbolo de moeda e substitua a vírgula por ponto
    try:
        valor_sem_simbolo = (
            str(valor_monetario_str)
            .replace("R$", "")
            .replace(".", "")
            .replace(",", ".")
        )
        print(valor_sem_simbolo)
        # Converta a string para um objeto Decimal
        valor_decimal = Decimal(valor_sem_simbolo)

        return valor_decimal
    except InvalidOperation as e:
        # Trate a exceção aqui
        print(f"Erro ao converter para Decimal: {e}")
        return None

    except ValueError:
        return None


def converter_para_formato_iso(data_str):
    # Converta a string para um objeto datetime
    try:
        data_obj = datetime.strptime(str(data_str), "%d/%m/%Y")

        # Converta o objeto datetime para uma string no formato ISO "yyyy-mm-dd"
        data_iso = data_obj.strftime("%Y-%m-%d")

        return data_iso
    except ValueError:
        return None


class Command(BaseCommand):
    help = "Importa dados de um arquivo CSV para o banco de dados"

    def handle(self, *args, **kwargs):
        caminho_arquivo = "planilha.csv"

        Process.objects.all().delete()

        # Abre o arquivo CSV e importa os dados
        with open(caminho_arquivo, newline="", encoding="utf-8") as arquivo_csv:
            # leitor_csv = csv.DictReader(arquivo_csv, delimiter=";")

            dados = pd.read_csv("planilha.csv", delimiter=";")

            for linha in dados.to_dict("records"):
                linha = {
                    chave.strip(): ("VAZIO" if pd.isna(valor) else valor)
                    for chave, valor in linha.items()
                }
                print(linha)
                # Use get_or_create nas chaves estrangeiras
                bank, _ = Bank.objects.get_or_create(name=linha["BANCO"])
                doc_analyst, _ = DocAnalyst.objects.get_or_create(
                    name=linha["ANALISTA"]
                )
                credit_analyst, _ = CreditAnalyst.objects.get_or_create(
                    name=linha["LIMITE"]
                )
                planner, _ = Planner.objects.get_or_create(name=linha["PROJETISTA"])
                bank_manager, _ = BankManager.objects.get_or_create(
                    name=linha["GERENTE"]
                )
                client, _ = Client.objects.get_or_create(name=linha["NOME"])
                business, _ = Business.objects.get_or_create(name=linha["ATIVIDADE"])

                process_instance = Process.objects.create(
                    bank=bank,
                    branch=linha["AGENCIA"],
                    doc_analyst=doc_analyst,
                    credit_analyst=credit_analyst,
                    planner=planner,
                    bank_manager=bank_manager,
                    client=client,
                    business=business,
                    available_credit=converter_para_decimal(linha["VALOR_LIBERADO"]),
                    credit_line=linha["LINHA"],
                    client_status=linha["STATUS"],
                    feedback=linha["RETORNO"],
                    risk_alert=linha["RISCO"],
                    credit_info=linha["DETALHES"],
                    date=linha["DATA"],
                    credit_due_date=converter_para_formato_iso(linha["VENCIMENTO"]),
                    credit_insurance=linha["GARANTIA"],
                    project_info=linha["INFOEXTRA"],
                )

        self.stdout.write(self.style.SUCCESS("Importação concluída com sucesso."))
