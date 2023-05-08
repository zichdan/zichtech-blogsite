from django.test import TestCase
from .models import Post


# Create your tests here.

class PostTestCase(TestCase):

    def setUp(self):
        
        self.post = Post.objects.create(
            tittle ="Test tittle",
            author = "Test author",
            content = "Test cotent"
        )

    def test_home_page(self):
        response = self.client.get('/')
        
        self.assertEqual(response.status_code,200)
        
        self.assertTemplateUsed(response,'index.html')
        
        self.assertContains(response,'List of posts')
        
        
    def test_post_creation(self):
        post_to_test = Post.objects.get(id=1)
        
        post_tittle = f"{post_to_test.tittle}"
        
        self.assertEqual(self.post.tittle, post_tittle)
        
        self.assertEqual(self.post.tittle, "Test tittle")
        self.assertEqual(self.post.author, "Test author")
