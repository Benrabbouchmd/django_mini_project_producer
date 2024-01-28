from rest_framework import serializers

from core.models import Riddle


answer_choice_keys = [
    'answer_choice_a', 'answer_choice_b', 'answer_choice_c', 'answer_choice_d'
]


class RiddleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riddle
        fields = "__all__"

    def validate_chosen_answer(self, value):
        """
        Check that the chosen answer is one of the answer choices.
        """
        if value not in [self.initial_data[choice_key] for choice_key in answer_choice_keys]:
            raise serializers.ValidationError("Chosen Answer Does Not Exist")
        return value

    def validate_correct_answer(self, value):
        """
        Check that the correct answer is one of the answer choices.
        """
        if value not in [self.initial_data[choice_key] for choice_key in answer_choice_keys]:
            raise serializers.ValidationError("Correct Answer Must Be One Of Choices")
        return value

