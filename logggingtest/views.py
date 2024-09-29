import logging
from django.http import HttpResponse


logger = logging.getLogger("django")


def info_view(request):
    logger.info("This is an INFO message.")
    return HttpResponse("Logged INFO")


def error_view(request):
    try:
        1 / 0
    except ZeroDivisionError:
        logger.error("An ERROR occurred", exc_info=True)
    return HttpResponse("Logged ERROR")


def debug_view(request):
    logger.debug("This is a DEBUG message.")
    return HttpResponse("Logged DEBUG")
