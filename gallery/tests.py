from django.test import TestCase
from gallery.models import Category, Image


class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(category.name, 'Test Category')


class ImageModelTest(TestCase):
    def test_image_creation(self):
        category = Category.objects.create(name='Test Category')
        image = Image.objects.create(
            title='Test Image', image='test.jpg',
            created_date='2023-05-23', age_limit=18)
        image.categories.add(category)

        self.assertEqual(image.title, 'Test Image')
        self.assertEqual(image.image, 'test.jpg')
        self.assertEqual(image.created_date, '2023-05-23')
        self.assertEqual(image.age_limit, 18)
        self.assertEqual(image.categories.count(), 1)
        self.assertIn(category, image.categories.all())
