from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username='meek',
            email='meek@meekness.com',
            password='terces'
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title='Grace',
            body="I will not abuse God's grace.",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'meek')
        self.assertEqual(self.post.title, 'Grace')
        self.assertEqual(self.post.body, "I will not abuse God's grace.")
        self.assertEqual(str(self.post), 'Grace')