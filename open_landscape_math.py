import math


class CoordinatePoint:
    """Defines a point on the globe"""
    latitude = None
    longitude = None

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude


def calculate_bounding_box(origin: CoordinatePoint, radius: int) -> (float, float, float, float):
    """Calculates the Bounding Box for the Overpass API"""

    upper_right = point_from_distance_and_angle(origin, radius, 45)
    lower_left = point_from_distance_and_angle(origin, radius, 225)

    return (lower_left.latitude, lower_left.longitude, upper_right.latitude, upper_right.longitude)


def point_from_distance_and_angle(point: CoordinatePoint, distance_in_m: float,
                                  angle_in_degrees: int) -> CoordinatePoint:
    """Calculates a point with the given angle and distance meters away from the given point"""

    lat1 = math.radians(point.latitude)
    lon1 = math.radians(point.longitude)

    distance = distance_in_m / 1000 / 6371
    angle = math.radians(angle_in_degrees)

    lat2 = math.asin(math.sin(lat1) * math.cos(distance) +
                     math.cos(lat1) * math.sin(distance) * math.cos(angle))
    lon2 = lon1 + math.asin((math.sin(distance) /
                             math.cos(lat2)) * math.sin(angle))

    return CoordinatePoint(latitude=math.degrees(lat2), longitude=math.degrees(lon2))
