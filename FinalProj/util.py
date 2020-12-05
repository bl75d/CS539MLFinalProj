class Color:
    """Class for color printing to terminal.
    
    Usage:
    ```
        >>> print(Color.GREEN + "HI", Color.RESET)
        HI <in green text>
    ```
    """
    # Bold
    GREEN = "\033[;1m\033[1;32m"
    RED = "\033[;1m\033[1;31m"
    YELLOW = "\033[;1m\033[1;33m"
    BLUE = "\033[;1m\033[1;34m"

    # Not Bold
    G = "\033[;0m\033[0;32m"
    R = "\033[;0m\033[0;31m"
    Y = "\033[;0m\033[0;33m"
    B = "\033[;0m\033[0;34m"

    RESET = "\033[;0m\033[0;0m"