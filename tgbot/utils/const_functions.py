def is_number(value) -> bool:
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False
