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

    def test_post_model_creation(self):
        """
        Test if Post is successfully made with valid data.
        """
        self.assertEqual(self.post.post_title, 'A Test Post')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.content, 'Some content for testing.')
        self.assertEqual(self.post.category, 'technology')
        self.assertFalse(self.post.edited) # Check the default value
    
    def test_post_model_str_method(self):
        """
        Tests to see if the displayed string matches the post data.
        """
        expected_string = f"Post Title: {self.post.post_title}, Post Author: {self.user}"
        self.assertEqual(str(self.post), expected_string)
