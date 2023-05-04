from rest_framework import serializers
from .models import Feedback


<<<<<<< HEAD

class FeedBackSerializer(serializers.ModelSerializer):
=======
class FeedbackSerializer(serializers.ModelSerializer):
>>>>>>> 916fbbdbb0a9507d657e7ad84134b2c8f0442de3
    class Meta:
        model = Feedback
        fields = '__all__'