def convert_to_cm(value, unit):
    if unit == 'inches':
        return value * 2.54
    elif unit == 'mm':
        return value / 10
    elif unit == 'cm':
        return value
    else:
        raise ValueError("Unsupported unit. Please use 'inches', 'mm', or 'cm'.")

def calculate_cardboard_length(length_cm, width_cm, height_cm):
    extra1 = 2.5  # cm
    extra2 = 5    # cm
    return (width_cm + height_cm + extra1) * ((length_cm + width_cm) * 2 + extra2)

def calculate_weight(cardboard_length, gsm):
    return (cardboard_length * (gsm/100)) / 100