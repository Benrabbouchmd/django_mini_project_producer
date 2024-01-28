from rest_framework import serializers

from core.models import Riddle


answer_choice_keys = [
    'answer_choice_a', 'answer_choice_b', 'answer_choice_c', 'answer_choice_d'
]


class RiddleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riddle
        fields = "__all__"

    def validate(self, data):
        # Check that the chosen answer is one of the answer choices.
        if data['chosen_answer'] not in [data[choice_key] for choice_key in answer_choice_keys]:
            raise serializers.ValidationError({"chosen_answer": "Chosen Answer Does Not Exist"})

        # Check that the correct answer is one of the answer choices.
        if data['correct_answer'] not in [data[choice_key] for choice_key in answer_choice_keys]:
            raise serializers.ValidationError({"correct_answer": "Correct Answer Must Be One Of Choices"})

        return data
