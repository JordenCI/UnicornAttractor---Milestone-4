from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Bug, BugComment
from django.shortcuts import get_object_or_404


class TestViews(TestCase):

    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")
        bug = Bug.objects.create(
            name="test",
            description="testing",
            author_id=user.id)

    def test_get_bugs_page(self):
        page = self.client.get("/view_bugs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs.html")

    def test_get_bugs_complete_page(self):
        page = self.client.get("/view_bugs/complete_bugs")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "completed_bugs.html")

    def test_get_bug_details_page(self):
        user = User.objects.get(username="test")
        bug = Bug(
            name="Test title",
            description="Test description",
            author_id=user.id)
        bug.save()
        response = self.client.get('/view_bugs/{0}/'.format(bug.id))
        self.assertEqual(response.status_code, 200)

    def test_get_add_bug_page(self):
        page = self.client.get("/view_bugs/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "create_bug.html")

    def test_get_edit_bug_page(self):
        user = User.objects.get(username="test")
        bug = Bug(name="Create a Test", description="description", author_id=user.id)
        bug.save()

        page = self.client.get("/view_bugs/{0}/edit/".format(bug.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "create_bug.html")

    def test_get_edit_page_for_bug_that_does_not_exist(self):
        page = self.client.get("/view_bugs/100/edit/")
        self.assertEqual(page.status_code, 404)
