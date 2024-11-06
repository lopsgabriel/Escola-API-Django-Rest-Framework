from rest_framework.throttling import AnonRateThrottle

class MatricutaAnonRateThrottle(AnonRateThrottle):
    rate = '5/day'