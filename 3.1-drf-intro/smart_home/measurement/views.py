from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializers, MeasurementSerializers, SensorDetailSerializer

class SensorView (ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializers

class SensorCreate(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializers
    
class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializers

class MeasurementCreate(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializers
    
class SensorDetail(RetrieveAPIView):
     queryset = Sensor.objects.all()
     serializer_class = SensorDetailSerializer
    
# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
