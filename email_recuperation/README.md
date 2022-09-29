# Create your views here.

# Mail config
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# SERVER_MAIL = 'no-reply@domain.com'
EMAIL_HOST='smtp-mail.outlook.com'
EMAIL_PORT=587
DEFAULT_FROM_EMAIL='tuemail@hotmail.com'
EMAIL_HOST_USER='tuemail@hotmail.com'
EMAIL_HOST_PASSWORD='clavesiña'
EMAIL_USE_TLS=True

# views.py

from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER

send_mail(
    'Asunto importante uwu',
    'Contexto del mensaje ewe.',
    EMAIL_HOST_USER,
    ['yourmail@gmail.com'],
    fail_silently=False,
    )

# Test console

python manage.py sendtestemail emailfortest@gmail.com