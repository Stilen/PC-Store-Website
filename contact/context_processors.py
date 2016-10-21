def recaptcha(request):
    """context processor to add alerts to the site"""
    from django.conf import settings

    return {
        'RECAPTCHA_SITE_KEY': settings.RECAPTCHA_SITE_KEY,
    }