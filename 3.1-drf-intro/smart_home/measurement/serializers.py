from rest_framework import serializers

from .models import Sensor, Measurement

class SensorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']
        
class MeasurementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'date_measurement', 'image']        


class MeasurementDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'date_measurement', 'image'] 
        
class SensorDetailSerializer(serializers.ModelSerializer):
    sensor = MeasurementDetailSerializers(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'sensor']    

# TODO: опишите необходимые сериализаторы
