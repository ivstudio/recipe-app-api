from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTest(TestCase):
    def test_create_user_with_email_successful(self):
        """Test create a new user with an email is successful"""
        email = 'test@test.com'
        password = 'test12345'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new ser is normalized"""
        email = 'test@TEST.com'
        user = get_user_model().objects.create_user(email, 'test12345')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test for valid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test create a new super user"""
        user = get_user_model() \
            .objects.create_superuser('test@test.com', 'test12345')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
