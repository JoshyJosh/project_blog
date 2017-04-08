from django.test import TestCase
from .models import CodePost

# Create your tests here.


class CodePostTest(TestCase):

    def setUp(self):
        CodePost.objects.create(content="foo1", title="bar")
        CodePost.objects.create(content="foo2", title="bar")
        CodePost.objects.create(content="foo3", title="bar")

    def test_codepost_exists(self):
        if len(CodePost.objects.all()) > 0:
            codepost = True
        elif len(CodePost.objecs.all()) == 0:
            codepost = False

        self.assertIs(codepost, True)

    def test_codepost_setup(self):
        self.assertEqual(len(CodePost.objects.all()), 3)

    def test_codepost_slugs_update(self):
        self.assertEqual(CodePost.objects.filter(content="foo1").first().slug, "bar")
        self.assertEqual(CodePost.objects.filter(content="foo2").first().slug, "bar_1")
        self.assertEqual(CodePost.objects.filter(content="foo3").first().slug, "bar_2")
