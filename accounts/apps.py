from django.apps import AppConfig

class AccountsConfig(AppConfig):
    name = 'accounts'
    
    # Import the signals inside the ready function
    def ready(self):
        import accounts.signals
