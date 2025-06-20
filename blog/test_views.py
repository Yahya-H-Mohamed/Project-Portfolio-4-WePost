from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase, Client
from .models import Post

class TestBlogViews(TestCase):

    def setUp(self):
        """
        Set up users, a post, and a logged-in client for view testing.
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            password='otherpassword'
        )
        self.post = Post.objects.create(
            post_title='A Test Post',
            author=self.user,
            content='Some content for testing.'
        )
        # Log in client for set up
        self.client.login(username='testuser', password='testpassword')

    def test_post_list_view_get(self):
        """
        Tests the PostList view for a GET request.
        """
        # 'reverse' gets the URL from its name in urls.py
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')
        self.assertContains(response, 'A Test Post') # Check if post title is in the HTML