# serializers allow complex data such as query sets and model instances to be converted
# to native python data types, these data types are easily rendered into json,xml content types

from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    # method fields have corresponding methods as defined below
    # get_rater
    rater = serializers.SerializerMethodField(read_only=True)
    # get_agent
    agent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        exclude = ["updated_at", "pkid"]

    def get_rater(self, obj):
        return obj.rater.username

    def get_agent(self, obj):
        # agent goes to profile model, in profile model the relationship btn profile and user model is the user
        return obj.agent.user.username
