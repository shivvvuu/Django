# mypy: ignore-errors

DEBUG = True
SECRET_KEY = 'django-insecure-sp0s_*_^^n-5-f&t#*st9=-s2-2mjep+(g0&_i0mlqj3#nu(a('

LOGGING['formatters']['colored'] = {    # type : ignore
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
}
LOGGING['loggers']['core']['level'] = 'DEBUG'  # type : ignore
LOGGING['handlers']['console']['level'] = 'DEBUG'  # type : ignore
LOGGING['handlers']['console']['formatter'] = 'colored'  # type : ignore
