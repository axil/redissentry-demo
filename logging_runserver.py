LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'formatters': {
        'full': {
            'format': '%(asctime)s %(process)-5d %(name)-12s %(levelname)-8s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },

    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'full',
            'filename': 'runserver.log',
            'maxBytes': 100000,
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'full',
#            'args': [sys.stdout],
        },
    },

    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['null'],
            'propagate': False,
        },
        'django': {
            'level': 'ERROR',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
    }
}
LOGGING_TYPE = 'runserver'
