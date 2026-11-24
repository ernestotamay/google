from django.db import models

class Contact(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Detail(models.Model):
    contacto = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='detalles')
    empresa = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return f"Detalle de {self.contacto.nombre}"