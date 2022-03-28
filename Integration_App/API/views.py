from Integration_App.models import Student
from Integration_App.API.serializers import StudentSerializer


from rest_framework import generics

class ListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer