from django.apps import AppConfig

class EmployeeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lounge_app_services.employee'

    def ready(self):
        import lounge_app_services.employee.signals