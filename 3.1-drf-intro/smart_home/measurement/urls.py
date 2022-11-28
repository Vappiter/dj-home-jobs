from django.urls import path

from measurement.views import SensorView, SensorCreate, SensorUpdate, MeasurementCreate, SensorDetail

urlpatterns = [
    path('sensors/', SensorCreate.as_view()),
    path('sensors/<int:pk>/', SensorUpdate.as_view()),
    path('measurement/', MeasurementCreate.as_view()),
    path('detail/<int:pk>/', SensorDetail.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
