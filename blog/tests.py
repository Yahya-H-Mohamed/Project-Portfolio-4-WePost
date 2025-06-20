from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class TestModels(TestCase):

    def setUp(self):
        """
        Set up a user
        This runs before every test function.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.post = Post.objects.create(
            post_title='A Test Post',
            author=self.user,
            content='Some content for testing.',
            category='technology'
        )