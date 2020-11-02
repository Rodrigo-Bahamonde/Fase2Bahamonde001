from django.test import TestCase
from peliculas.models import ComentarioDolittle

class ComentarioModelTest(TestCase):

    
    @classmethod
    def setUpTestData(cls):
        ComentarioDolittle.objects.create( descripcion='Esto es una prueba', comentario='Esto es un comentario de prueba', fecha= '2020-02-11')
    
    def test_descripcion_label(self):
        descripcion= ComentarioDolittle.objects.get(id=1)
        field_label = descripcion._meta.get_field('descripcion').verbose_name
        self.assertEquals(field_label,'descripcion')