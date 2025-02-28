from django.test import TestCase
import datetime
from django.utils import timezone
from polls.models import Questions

class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_questions(self):
        time = timezone.now() + datetime.timedelta(days=1, seconds=1)
        future_question = Questions(pub_date=time)
        self.assertIs(future_question.was_published_recently, False, "Future is not recent")
        
    def test_was_published_recentyl_with_recent_question(slef):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)