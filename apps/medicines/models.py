from django.db import models
from django.urls import reverse_lazy


# Create your models here.

class BaseName(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Symptoms(BaseName):
   
    class Meta:
        verbose_name = 'Sintoma'
        verbose_name_plural = 'Sintomas'

    def get_edit_url(self):
        return reverse_lazy('medicines:symptoms-edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('medicines:symptoms-delete', kwargs={'pk': self.pk})

    def get_detail_url(self):
        return reverse_lazy('medicines:symptoms-detail', kwargs={'pk': self.pk})



class Medicines(BaseName):
    description = models.CharField(max_length=256, verbose_name='Descripcion del medicamento')
    brand = models.CharField(max_length=10, verbose_name='Marca')
    laboratory = models.CharField(max_length=10, verbose_name='Laboratorio')
    image = models.ImageField(upload_to='medicines', verbose_name='Imagen', blank=True)
    symptom = models.ManyToManyField(Symptoms, verbose_name='Sintoma')

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'

    def get_edit_url(self):
        return reverse_lazy('medicines:medicines-edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('medicines:medicines-delete', kwargs={'pk': self.pk})

    def get_detail_url(self):
        return reverse_lazy('medicines:medicines-detail', kwargs={'pk': self.pk})
