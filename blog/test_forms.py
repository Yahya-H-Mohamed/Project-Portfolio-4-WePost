from django.test import TestCase
from .forms import PostForm, CommentForm

class TestForms(TestCase):

    def test_post_form_is_valid(self):
        """
        Tests that the PostForm is valid with correct data
        """
        form = PostForm({
            'post_title': 'A valid title',
            'category': 'education',
            'content': 'Some valid content.'
        })
        self.assertTrue(form.is_valid())

    def test_post_form_is_invalid_if_title_missing(self):
        """
        Tests that the PostForm is invalid if the title is empty
        """
        form = PostForm({
            'post_title': '', 
            'category': 'other',
            'content': 'Content without a title.'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('post_title', form.errors.keys())
        self.assertEqual(form.errors['post_title'][0], 'This field is required.')