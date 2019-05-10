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
        
class ImageTestClass(TestCase):
    def setUp(self):
        self.wanjiku = Editor(name='Wanjiku',email='sheekokariuki@gmail.com')
        self.wanjiku.save_editor()

        self.new_category = Category(category ='testing')
        self.new_category.save()

        self.new_location = Location(location ='tested')
        self.new_location.save()

        self.new_image = Image(caption = 'Test Image',description = 'This is a post tester', category = self.new_category,editor = self.wanjiku,location=self.new_location)
        self.new_image.save()
        # self.new_image.category.add(self.new_category)

    def tearDown(self):
        Editor.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

    def test_get_photos(self):
        today_photos = Image.today_photos()
        self.assertTrue(len(today_photos)>0)