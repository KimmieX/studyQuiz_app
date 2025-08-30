from django.contrib import admin
from .models import User, Quiz, Question, QuizAttempt, UserAnswer

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(QuizAttempt)
admin.site.register(UserAnswer)

