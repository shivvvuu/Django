if IN_DOCKER:  # type: ignore # noqa:F821
    print('Running IN_DOCKER mode...')
    assert MIDDLEWARE[:1] == [  # type: ignore # noqa:F821
        'django.middleware.security.SecurityMiddleware'
    ]
