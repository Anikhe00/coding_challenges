def add_setting(settings, pairs):
    # Unpack the tuple
    key, value = pairs

    # Convert to lowercase
    key = key.lower()
    value = value.lower()

    # Check if key exists
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        # Add the setting
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, pairs):
    # Unpack the tuple
    key, value = pairs

    # Convert to lowercase
    key = key.lower()
    value = value.lower()

    # Check if key exists and update the value
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    # Convert to lowercase
    key = key.lower()

    # Check if the key exists and delete it
    if key in settings:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    else:
        result = "Current User Settings:"
        for key, value in settings.items():
            result += f"\n{key.capitalize()}: {value}"
    return result + "\n"

test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}