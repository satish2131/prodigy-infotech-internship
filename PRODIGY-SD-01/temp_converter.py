

def to_celsius(value, unit):
    """Convert a temperature to Celsius."""
    unit = unit.lower()
    if unit in ("c", "celsius"):
        return value
    elif unit in ("f", "fahrenheit"):
        return (value - 32) * 5 / 9
    elif unit in ("k", "kelvin"):
        return value - 273.15
    else:
        raise ValueError("Unknown temperature unit.")


def from_celsius(celsius):
    """Convert Celsius temperature to Fahrenheit and Kelvin."""
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin


def convert_temperature(value, unit):
    """Convert given temperature to other two units."""
    celsius = to_celsius(value, unit)
    fahrenheit, kelvin = from_celsius(celsius)

    if unit.lower().startswith('c'):
        print(f"Input: {value:.2f} °C")
        print(f"-> Fahrenheit: {fahrenheit:.2f} °F")
        print(f"-> Kelvin: {kelvin:.2f} K")
    elif unit.lower().startswith('f'):
        print(f"Input: {value:.2f} °F")
        print(f"-> Celsius: {celsius:.2f} °C")
        print(f"-> Kelvin: {kelvin:.2f} K")
    elif unit.lower().startswith('k'):
        print(f"Input: {value:.2f} K")
        print(f"-> Celsius: {celsius:.2f} °C")
        print(f"-> Fahrenheit: {fahrenheit:.2f} °F")
    else:
        print("Unknown unit.")


def main():
    print("===  Temperature Converter ===")
    print("Supported units: Celsius (C), Fahrenheit (F), Kelvin (K)\n")

    while True:
        user_input = input("Enter temperature (e.g., 25 C) or 'q' to quit: ").strip()
        if user_input.lower() in ['q', 'quit', 'exit']:
            print("Goodbye!")
            break

        try:
            parts = user_input.split()
            if len(parts) != 2:
                print("❗ Please enter in format: <value> <unit> (e.g., 100 F)")
                continue

            value = float(parts[0])
            unit = parts[1]

            convert_temperature(value, unit)

        except ValueError:
            print("⚠️ Invalid input! Example: 25 C or 300 K")


if __name__ == "__main__":
    main()
