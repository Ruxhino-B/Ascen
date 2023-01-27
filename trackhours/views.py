from django.core.mail import EmailMessage
from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response

from .models import WorkDay, SendReport
from .serialize import WorkdaySerialize, SendReportSerializer

from .generatePDF import extend_item


# Create your vie

class WorkDayListCreateAPI(generics.ListCreateAPIView):
    serializer_class = WorkdaySerialize

    def get_queryset(self):
        user = self.request.user
        return WorkDay.objects.filter(user=user.id)

    def create(self, request, *args, **kwargs):
        serialize = WorkdaySerialize(data=request.data)
        if serialize.is_valid():
            start_time = serialize.validated_data['start_time']
            print(start_time.day)
            query = WorkDay.objects.filter(start_time__day=start_time.day)
            if query:
                return Response({'error': 'This Date Exits'}, status.HTTP_400_BAD_REQUEST)
            else:
                serialize.save()
                return Response(serialize.data, status=status.HTTP_200_OK)


class WorkDayRetriveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkdaySerialize

    def get_queryset(self):
        user = self.request.user
        return WorkDay.objects.filter(user=user)


class SendReportCreate(generics.CreateAPIView):
    serializer_class = SendReportSerializer
    queryset = SendReport.objects.all()

    def create(self, request, *args, **kwargs):
        serialize = SendReportSerializer(data=request.data)
        if serialize.is_valid():
            start_day = serialize.validated_data['start_day']
            end_day = serialize.validated_data['end_date']
            emaili = serialize.validated_data['email']
            print(start_day.day)
            query = WorkDay.objects.filter(start_time__day__gte=start_day.day, start_time__day__lte=end_day.day)
            if query:
                extend_item(query)
                email = EmailMessage(
                    'Ascen',
                    'Body',
                    'system@ruxhino.al',
                    [
                        emaili,
                        'ruxhino@gmail.com',
                    ],
                    reply_to=['another@example.com'],
                    headers={'Message-ID': 'foo'},
                )
                email.attach_file('table_grids.pdf')
                email.send()
                # serialize.save()
                return Response(serialize.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'The Range is Empty'}, status.HTTP_400_BAD_REQUEST)
