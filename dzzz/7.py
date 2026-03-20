speed = 25600
time = 2 * 3600
max_bits = speed * time
max_bites = max_bits // 8
pixels 3840 * 2160
bytes_per_pixel = max_bites // pixels

bits_per_pixel = bytes_per_pixel * 8
colors = 1 << bits_per_pixel
print(colors)
