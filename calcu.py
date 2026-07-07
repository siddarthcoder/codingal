import math

angle_degrees = 45

angle_radians = math.radians(angle_degrees)

sin_val = math.sin(angle_radians)
cos_val = math.cos(angle_radians)
tan_val = math.tan(angle_radians)

print(f"Angle: {angle_degrees}°")
print(f"Sine: {sin_val:.4f}")
print(f"Cosine: {cos_val:.4f}")