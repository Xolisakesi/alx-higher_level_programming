#!/usr/bin/python3
def safe_print_integer_err(value):
    """Prints an integer and returns True if printed correctly, else False with an error message in stderr."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return False
