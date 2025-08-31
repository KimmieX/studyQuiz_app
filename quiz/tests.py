from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Quiz
from django.contrib.auth import get_user_model, User

# Create your tests here.
class QuizAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

        self.quiz_data = {
            "title": "Test Quiz",
            "description": "A simple test quiz",
            "category": "General",
            "user": self.user.id
        }

    def test_create_quiz(self):
        response = self.client.post("/api/quizzes/", self.quiz_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], self.quiz_data["title"])

    def test_list_quizzes(self):
        Quiz.objects.create(**self.quiz_data)
        response = self.client.get("/api/quizzes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_quiz_detail(self):
        quiz = Quiz.objects.create(**self.quiz_data)
        response = self.client.get(f"/api/quizzes/{quiz.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.quiz_data["title"])

