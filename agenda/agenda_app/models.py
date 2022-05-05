from django.db import models

STATUS = (
    ('agendado', 'Agendado'),
    ('realizado', 'Realizado'),
    ('cancelado', 'Cancelado')
)

class Compromisso(models.Model):
    titulo = models.CharField(max_length=120)
    observacoes = models.TextField(blank=True)
    data = models.DateField(blank=False)
    hora_Inicio = models.TimeField(auto_now_add=False, blank=False)
    hora_Fim = models.TimeField(auto_now_add=False, blank=False)
    local = models.CharField(max_length=120)
    status = models.CharField(
        max_length=10,
        choices=STATUS,
    )

    def __str__(self):
        return self.titulo