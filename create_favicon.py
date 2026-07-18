import math
from PIL import Image, ImageDraw

# Create 512x512 image with transparent background
size = 512
img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Rounded square dimensions
square_size = 420
padding = (size - square_size) // 2
corner_radius = 70

# Create a rounded rectangle mask
def create_rounded_rect_mask(size, square_size, corner_radius):
    mask = Image.new('L', (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    
    # Draw rounded rectangle
    x0, y0 = padding, padding
    x1, y1 = padding + square_size, padding + square_size
    
    # Draw the four corners
    mask_draw.rounded_rectangle([x0, y0, x1, y1], radius=corner_radius, fill=255)
    return mask

# Create gradient background
def create_purple_gradient(size, square_size, corner_radius):
    # Create base image for gradient
    gradient = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    gradient_draw = ImageDraw.Draw(gradient)
    
    # Premium purple gradient (soft, modern)
    purple_top = (147, 112, 219)    # Lavender
    purple_bottom = (128, 0, 128)   # Purple
    
    # Draw vertical gradient
    for y in range(padding, padding + square_size):
        ratio = (y - padding) / square_size
        r = int(purple_top[0] * (1 - ratio) + purple_bottom[0] * ratio)
        g = int(purple_top[1] * (1 - ratio) + purple_bottom[1] * ratio)
        b = int(purple_top[2] * (1 - ratio) + purple_bottom[2] * ratio)
        gradient_draw.line([(padding, y), (padding + square_size, y)], fill=(r, g, b))
    
    return gradient

# Create the rounded square with gradient
gradient = create_purple_gradient(size, square_size, corner_radius)
mask = create_rounded_rect_mask(size, square_size, corner_radius)

# Apply mask to gradient
background = Image.new('RGBA', (size, size), (0, 0, 0, 0))
background.paste(gradient, mask=mask)
img = background

# Draw elegant white heart
heart_size = 160
heart_x = size // 2
heart_y = size // 2

# Create heart using bezier-like curves
def draw_heart(draw, cx, cy, size, fill_color):
    # Heart shape points (simplified, clean design)
    points = []
    
    # Left side of heart
    points.extend([
        (cx - size//2, cy + size//6),
        (cx - size//2 + 10, cy - size//3),
        (cx - size//4, cy - size//2),
        (cx, cy - size//6),
    ])
    
    # Right side of heart
    points.extend([
        (cx, cy - size//6),
        (cx + size//4, cy - size//2),
        (cx + size//2 - 10, cy - size//3),
        (cx + size//2, cy + size//6),
    ])
    
    # Bottom point
    points.append((cx, cy + size//2 - 10))
    
    # Draw heart shape
    draw.polygon(points, fill=fill_color)

draw = ImageDraw.Draw(img)
draw_heart(draw, heart_x, heart_y, heart_size, 'white')

# Save the favicon
img.save('static/favicon.png', 'PNG')
