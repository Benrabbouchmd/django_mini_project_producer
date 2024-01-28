from django.test import TestCase, Client
from django.urls import reverse
from rest_framework_api_key.models import APIKey

from core.models import Riddle
from core.serializers import RiddleSerializer


class RiddleModelTests(TestCase):
    def setUp(self):
        self.riddle = Riddle.objects.create(
            question="Test Riddle",
            correct_answer="Choice C",
            answer_choice_a="Choice A",
            answer_choice_b="Choice B",
            answer_choice_c="Choice C",
            answer_choice_d="Choice D"
        )

    def test_riddle_creation(self):
        self.assertEqual(self.riddle.question, "Test Riddle")
        self.assertEqual(self.riddle.correct_answer, "Choice C")


class RiddleViewSetTests(TestCase):
    def setUp(self):
        self.riddle = Riddle.objects.create(
            question="Test Riddle",
            correct_answer="Choice D",
            answer_choice_a="Choice A",
            answer_choice_b="Choice B",
            answer_choice_c="Choice C",
            answer_choice_d="Choice D"
        )
        self.unauthenticated_client = Client()
        _, key = APIKey.objects.create_key(name="test")
        self.client.defaults['HTTP_AUTHORIZATION'] = f"Api-Key {key}"

    def test_riddle_me_this_unauthenticated(self):
        url = reverse('riddle-riddle-me-this', args=[self.riddle.id])
        data = {'chosen_answer': 'Choice A'}
        response = self.unauthenticated_client.post(url, data, format='json')

        self.assertEqual(response.status_code, 401)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')

    def test_riddle_me_this(self):
        url = reverse('riddle-riddle-me-this', args=[self.riddle.id])

        # Wrong Answer Test
        data = {'chosen_answer': 'Choice A'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['correct'], False)

        # Correct Answer Test
        data = {'chosen_answer': 'Choice D'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['correct'], True)

        # Missing Answer Test
        data = {'chosen_answer': 'Choice X'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['chosen_answer'], ["Chosen Answer Does Not Exist"])


class RiddleSerializerTests(TestCase):
    def test_validate_chosen_answer(self):
        data = {
            'question': 'Test Riddle',
            'correct_answer': 'Choice A',
            'answer_choice_a': 'Choice A',
            'answer_choice_b': 'Choice B',
            'answer_choice_c': 'Choice C',
            'answer_choice_d': 'Choice D',
            'chosen_answer': 'Invalid Choice'
        }
        serializer = RiddleSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('chosen_answer', serializer.errors)

    def test_validate_correct_answer(self):
        data = {
            'question': 'Test Riddle',
            'correct_answer': 'Invalid Choice',
            'answer_choice_a': 'Choice A',
            'answer_choice_b': 'Choice B',
            'answer_choice_c': 'Choice C',
            'answer_choice_d': 'Choice D',
            'chosen_answer': 'Choice A'
        }
        serializer = RiddleSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('correct_answer', serializer.errors)

