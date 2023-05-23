from django.test import TestCase


from .models import Image, Category

class ImageModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.image = Image.objects.create(
            title='Test Image',
            image='path/to/image.jpg',
            created_date='2023-05-23',
            age_limit=18
        )
        self.image.categories.add(self.category)

    def test_image_has_category(self):
        self.assertEqual(self.image.categories.count(), 1)
        self.assertEqual(self.image.categories.first(), self.category)
      

    def test_image_str_representation(self):
        self.assertEqual(str(self.image), 'Test Image')

