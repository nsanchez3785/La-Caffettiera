MAILERS = {
    "default": {
        "BACKEND": "django.core.mail.backends.smtp.EmailBackend",
        "OPTIONS": {
            "host": "sandbox.smtp.mailtrap.io",
            "port": 2525,
            "username": "c49ee884ba91ff",
            "password": "26de620e1a157d",
            "use_tls": True,
        },
    },
}
