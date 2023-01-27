from rest_framework import serializers
from .models import WorkDay, SendReport


class WorkdaySerialize(serializers.ModelSerializer):
    class Meta:
        model = WorkDay
        fields = '__all__'



class SendReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendReport
        fields = '__all__'
