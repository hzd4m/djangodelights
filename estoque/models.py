from django.db import models

# Representa um ingrediente no Estoque
class Ingrediente(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do Ingrediente")
    quantidade = models.FloatField(default=0.0, verbose_name="Quantidade em Stock")
    unidade = models.CharField(max_length=20, default="unidade", verbose_name="Unidade (ex: kg, l, unidade)")
    preco_por_unidade = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Preço por Unidade")

    def __str__(self):
        return f"{self.nome} ({self.quantidade} {self.unidade})"

# Representa um item no menu do restaurante
class ItemCardapio(models.Model):
    titulo = models.CharField(max_length=100, unique=True, verbose_name="Título do Prato")
    preco_venda = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Preço de Venda")

    def __str__(self):
        return self.titulo
    
    # Função para verificar se há estoque suficiente para preparar o prato
    def pode_ser_feito(self):
        # Percorre todos os ingredientes necessários para este prato
        for requisito in self.requisitos.all():
            if requisito.quantidade > requisito.ingrediente.quantidade:
                return False # Se faltar qualquer ingrediente, retorna False
        return True # Se todos os ingredientes estiverem disponíveis, retorna True

# Tabela intermédia que liga Ingredientes a Itens do Cardápio
class RequisitoReceita(models.Model):
    item_cardapio = models.ForeignKey(ItemCardapio, on_delete=models.CASCADE, related_name="requisitos")
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    quantidade = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.quantidade} de {self.ingrediente.nome} para {self.item_cardapio.titulo}"

# Regista uma compra de um Item do Cardápio
class Compra(models.Model):
    item_cardapio = models.ForeignKey(ItemCardapio, on_delete=models.CASCADE)
    momento_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Formata a data e hora para o fuso horário local de Teresina (UTC-3)
        momento_local = self.momento_compra.astimezone(models.fields.timezone.get_fixed_timezone(-180))
        return f"Compra de {self.item_cardapio.titulo} em {momento_local.strftime('%d/%m/%Y %H:%M')}"
