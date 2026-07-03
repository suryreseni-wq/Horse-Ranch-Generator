import math


def deg(angle):

    return math.radians(angle)


def circle(radius, count):

    result = []

    step = math.tau / count

    for i in range(count):

        a = i * step

        result.append((
            math.cos(a) * radius,
            math.sin(a) * radius
        ))

    return result


def clamp(v, a, b):

    return max(a, min(v, b))


def lerp(a, b, t):

    return a + (b - a) * t
