from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from todolist.models import Task, Comment, Tag
from users.models import User


# python manage.py test
class TaskTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.tu', password='testpassword')

        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_create_task(self):
        response = self.client.post(reverse('todolist:task-create'),
                                    data={'title': 'Test Task', 'description': 'Test Description'})

        self.assertEqual(response.status_code, 201)

        task = Task.objects.first()
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.description, 'Test Description')

    def test_view_task(self):
        self.task = Task.objects.create(title="Test Task", description="Test Description")
        response = self.client.get(reverse('todolist:task-retrieve', kwargs={'pk': self.task.pk}))

        self.assertEqual(response.status_code, 200)

        task = Task.objects.first()
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.description, 'Test Description')

    def test_update_task(self):
        self.task = Task.objects.create(title="Test Task", description="Test Description", owner=self.user)
        response = self.client.put(reverse('todolist:task-update', kwargs={'pk': self.task.pk}), data={
            'title': 'Replacement 1',
            'description': 'Replacement 2'})

        self.assertEqual(response.status_code, 200)

        task = Task.objects.first()
        self.assertEqual(task.title, 'Replacement 1')
        self.assertEqual(task.description, 'Replacement 2')

    def test_delete_task(self):
        self.task = Task.objects.create(title="Test Task", description="Test Description", owner=self.user)
        response = self.client.delete(reverse('todolist:task-destroy', kwargs={'pk': self.task.pk}))

        self.assertEqual(response.status_code, 204)

        task = Task.objects.first()
        self.assertIsNone(task)


class CommentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.tu', password='testpassword')
        self.task = Task.objects.create(title="Test Task", description="Test Description")

        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_create_comment(self):
        response = self.client.post(reverse('todolist:comment-create'),
                                    data={'task': self.task.pk, 'text': 'Test Comment'})

        self.assertEqual(response.status_code, 201)

        comment = Comment.objects.first()
        self.assertEqual(comment.text, 'Test Comment')
        self.assertEqual(comment.task, self.task)

    def test_view_comment(self):
        comment = Comment.objects.create(task=self.task, text='Test Comment')
        response = self.client.get(reverse('todolist:comment-retrieve', kwargs={'pk': comment.pk}))

        self.assertEqual(response.status_code, 200)

        retrieved_comment = Comment.objects.get(pk=comment.pk)
        self.assertEqual(retrieved_comment.text, 'Test Comment')
        self.assertEqual(retrieved_comment.task, self.task)

    def test_update_comment(self):
        comment = Comment.objects.create(task=self.task, text='Test Comment')
        response = self.client.put(reverse('todolist:comment-update', kwargs={'pk': comment.pk}),
                                   data={'text': 'Updated Comment',
                                         'task': self.task.pk})

        self.assertEqual(response.status_code, 200)

        updated_comment = Comment.objects.get(pk=comment.pk)
        self.assertEqual(updated_comment.text, 'Updated Comment')

    def test_delete_comment(self):
        comment = Comment.objects.create(task=self.task, text='Test Comment')
        response = self.client.delete(reverse('todolist:comment-destroy', kwargs={'pk': comment.pk}))

        self.assertEqual(response.status_code, 204)

        deleted_comment = Comment.objects.first()
        self.assertIsNone(deleted_comment)


class TagTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.tu', password='testpassword')

        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_create_tag(self):
        response = self.client.post(reverse('todolist:tag-create'), data={'name': 'Test Tag'})

        self.assertEqual(response.status_code, 201)

        tag = Tag.objects.first()
        self.assertEqual(tag.name, 'Test Tag')

    def test_view_tag(self):
        tag = Tag.objects.create(name='Test Tag')
        response = self.client.get(reverse('todolist:tag-retrieve', kwargs={'pk': tag.pk}))

        self.assertEqual(response.status_code, 200)

        retrieved_tag = Tag.objects.get(pk=tag.pk)
        self.assertEqual(retrieved_tag.name, 'Test Tag')

    def test_update_tag(self):
        tag = Tag.objects.create(name='Test Tag')
        response = self.client.put(reverse('todolist:tag-update', kwargs={'pk': tag.pk}),
                                   data={'name': 'Updated Tag'})

        self.assertEqual(response.status_code, 200)

        updated_tag = Tag.objects.get(pk=tag.pk)
        self.assertEqual(updated_tag.name, 'Updated Tag')

    def test_delete_tag(self):
        tag = Tag.objects.create(name='Test Tag')
        response = self.client.delete(reverse('todolist:tag-destroy', kwargs={'pk': tag.pk}))

        self.assertEqual(response.status_code, 204)

        deleted_tag = Tag.objects.first()
        self.assertIsNone(deleted_tag)


class MixTestCase(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Test Task", description="Test Description")
        self.tag = Tag.objects.create(name="Test Tag")

    def test_add_comment_to_task(self):
        comment = Comment.objects.create(task=self.task, text="Test Comment")
        self.task.refresh_from_db()
        self.assertIn(comment, self.task.comments.all())

    def test_add_tags_to_task(self):
        self.task.tags.add(self.tag)
        self.task.refresh_from_db()
        self.assertIn(self.tag, self.task.tags.all())
