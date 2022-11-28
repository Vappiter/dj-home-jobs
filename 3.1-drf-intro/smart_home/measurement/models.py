from django.db import models



class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название датчика')
    description = models.CharField(max_length=150, verbose_name='Описание датчика')
    
    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        
    def __str__(self):
        return self.name     
    
class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.PROTECT, related_name='sensor', verbose_name='Ссылка на датчик')
    temperature = models.FloatField(verbose_name='Значение температуры')
    date_measurement = models.DateField(auto_now = True, verbose_name='Дата измерения')
    image = models.ImageField(null=True)
    
    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
    
    def __str__(self):
        return 'Измерение' 



# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
