from django.db import models

from app.core.models import BaseModel


def formatar_valor_monetario(valor):
    # Converte o valor para string
    valor_str = str(valor)

    # Separa a parte inteira da parte decimal
    parte_inteira, parte_decimal = valor_str.split(".")

    # Adiciona pontos para separar milhares na parte inteira
    parte_inteira_formatada = "{:,}".format(int(parte_inteira)).replace(",", ".")

    # Adiciona zeros à parte decimal, se necessário
    parte_decimal_formatada = parte_decimal.ljust(2, "0")

    # Formata o valor completo
    valor_formatado = f"R$ {parte_inteira_formatada},{parte_decimal_formatada}"

    return valor_formatado


# Create your models here.
class Bank(BaseModel):
    name = models.CharField(verbose_name="Nome", max_length=300)

    class Meta:
        verbose_name = "Banco"
        verbose_name_plural = "Bancos"

    def __str__(self):
        return f"{self.name}"


class DocAnalyst(BaseModel):
    name = models.CharField(verbose_name="Nome", max_length=300)

    class Meta:
        verbose_name = "Analista Documental"
        verbose_name_plural = "Analistas Documentais"

    def __str__(self):
        return f"{self.name}"


class CreditAnalyst(BaseModel):
    name = models.CharField(verbose_name="Nome", max_length=300)

    class Meta:
        verbose_name = "Analista de Crédito"
        verbose_name_plural = "Analistas de Crédito"

    def __str__(self):
        return f"{self.name}"


class Planner(BaseModel):
    name = models.CharField(verbose_name="Nome", max_length=300)

    class Meta:
        verbose_name = "Planejador"
        verbose_name_plural = "Planejadores"

    def __str__(self):
        return f"{self.name}"


class BankManager(BaseModel):
    name = models.CharField(verbose_name="Nome", max_length=300)

    class Meta:
        verbose_name = "Gerente de Banco"
        verbose_name_plural = "Gerentes de Banco"

    def __str__(self):
        return f"{self.name}"


class Client(BaseModel):
    name = models.CharField(verbose_name="Nome", max_length=300)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.name}"


class Business(BaseModel):
    name = models.CharField(verbose_name="Nome", max_length=300)

    class Meta:
        verbose_name = "Negócio"
        verbose_name_plural = "Negócios"

    def __str__(self):
        return f"{self.name}"


class Status(models.TextChoices):
    ANALISE_NEGATIVA = "analise-negativa", "Análise Negativa"
    ATUALIZADO = "atualizado", "Atualizado"
    COBRAR_GN = "cobrar-gn", "Cobrar GN"
    CONSULTAR_RATING = "consultar-rating", "Consultar Rating"
    CREDITO_APROVADO = "credito-aprovado", "Crédito Aprovado"
    DESISTIU = "desistiu", "Desistiu"
    FALECEU = "faleceu", "Faleceu"
    FALTA_DOC = "falta-doc", "Falta Doc"
    FAZER_LIMITE = "fazer-limite", "Fazer Limite"
    FAZER_PROJETO = "fazer-projeto", "Fazer Projeto"
    INATIVO = "inativo", "Inativo"
    OPERACAO_CONCLUIDA = "operacao-concluida", "Operação Concluída"
    PROCESSO_NO_BANCO = "processo-no-banco", "Processo no Banco"
    PROCESSO_PARADO = "processo-parado", "Processo Parado"
    PROSPECT = "prospect", "Prospect"
    SEM_INTERESSE = "sem-interesse", "Sem Interesse"


class Process(BaseModel):
    bank = models.ForeignKey(
        Bank,
        on_delete=models.PROTECT,
        verbose_name="Banco",
    )
    branch = models.CharField(verbose_name="Agência", max_length=300)
    doc_analyst = models.ForeignKey(
        DocAnalyst,
        on_delete=models.PROTECT,
        verbose_name="Analista",
    )
    credit_analyst = models.ForeignKey(
        CreditAnalyst,
        on_delete=models.PROTECT,
        verbose_name="Analista de Limite",
    )
    planner = models.ForeignKey(
        Planner,
        on_delete=models.PROTECT,
        verbose_name="Projetista",
    )
    bank_manager = models.ForeignKey(
        BankManager,
        on_delete=models.PROTECT,
        verbose_name="Gerente de Banco",
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        verbose_name="Cliente",
    )
    business = models.ForeignKey(
        Business,
        on_delete=models.PROTECT,
        verbose_name="Atividade",
    )
    available_credit = models.DecimalField(
        verbose_name="Crédito Disponível",
        max_digits=11,
        decimal_places=2,
        blank=True,
        null=True,
    )
    credit_line = models.CharField(
        verbose_name="Linha de Crédito", max_length=300, blank=True, null=True
    )
    client_status = models.CharField(
        verbose_name="Status",
        max_length=300,
        # choices=Status.choices,
        blank=True,
        null=True,
    )
    feedback = models.TextField(verbose_name="Feedback", blank=True, null=True)
    risk_alert = models.TextField(verbose_name="Alerta de Risco", blank=True, null=True)
    credit_info = models.TextField(
        verbose_name="Informações de Crédito", blank=True, null=True
    )
    date = models.CharField(verbose_name="Data", blank=True, null=True)
    credit_due_date = models.DateField(
        verbose_name="Data de Vencimento do Crédito", blank=True, null=True
    )
    credit_insurance = models.CharField(
        verbose_name="Seguro de Crédito", max_length=300, blank=True, null=True
    )
    project_info = models.TextField(
        verbose_name="Informações do Projeto", blank=True, null=True
    )

    class Meta:
        verbose_name = "Processo"
        verbose_name_plural = "Processos"

    def __str__(self):
        return f"{self.client}"

    def save(self, *args, **kwargs):
        self.client_status = self.client_status.strip().capitalize()
        super(Process, self).save(*args, **kwargs)

    @property
    def available_credit_f(self):
        if not self.available_credit:
            return None
        return formatar_valor_monetario(self.available_credit)
