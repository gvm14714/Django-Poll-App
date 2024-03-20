from django.test import TestCase
from .models import MyModel  # Correctly importing MyModel from models.py

class MyModelTestCase(TestCase):
    def setUp(self):
        # Set up data for the whole TestCase
        MyModel.objects.create(name="Just a test")

    def test_is_named_test(self):
        """Test that the MyModel object has a name attribute"""
        test_object = MyModel.objects.get(name="Just a test")
        self.assertEqual(test_object.name, "Just a test")
        
    def test_mymodel_has_name(self):
        """Test the is_named_test method"""
        test_object = MyModel.objects.get(name="Just a test")
        self.assertTrue(test_object.is_named_test())



