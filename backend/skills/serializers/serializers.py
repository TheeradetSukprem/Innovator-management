from rest_framework import serializers
from skills.views import Skill

class SkillSerializer(serializers.ModelSerializer):
        class Meta:
                model = Skill
                fields = "__all__"