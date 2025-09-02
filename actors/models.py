from django.db import models


NATIONALITY_CHOICES = (
    ('BR', 'Brasil'),
    ('USA', 'Estados Unidos'),
    ('UK', 'Reino Unido'),
    # Adicione mais nacionalidades conforme necessário
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.name