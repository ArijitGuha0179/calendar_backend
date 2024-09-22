from django.apps import AppConfig


class CalendarApiConfig(AppConfig):
    # Use BigAutoField as the primary key type for all models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Name of the app
    name = 'calendar_api'
