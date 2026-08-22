def calculate_area_of_triangle(a, b, c):
    """
    Calculate the area of a triangle using Heron's formula.

    Parameters:
    a (float): Length of side a
    b (float): Length of side b
    c (float): Length of side c

    Returns:
    float: Area of the triangle
    """
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate the area using Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    
    return area

def print_colored_message(message, color):
    """
    Print a message in a specified color.

    Parameters:
    message (str): The message to print
    color (str): The color to use (e.g., 'red', 'green', 'blue')

    Returns:
    None
    """
    # Define ANSI color codes
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'blue': '\033[94m',
        'reset': '\033[0m'
    }
    
    # Get the color code, default to reset if not found
    color_code = colors.get(color, colors['reset'])
    
    # Print the colored message
    print(f"{color_code}{message}{colors['reset']}")