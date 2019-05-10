from django.test import TestCase
from .models import Editor,Image,Category,Location

class EditorTestClass(TestCase):
    def setUp(self):
        self.wanjiku = Editor(name='Wanjiku',email='sheekokariuki@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.wanjiku,Editor))

    def test_save(self):
        self.wanjiku.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)
        