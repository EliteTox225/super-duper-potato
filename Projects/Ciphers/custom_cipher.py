"""Applies your custom cipher algorithm."""

def encrypt(message, key):
    """Returns the given message encrypted using your custom cipher."""
    activated_key = activate_key(key)
    new_message = apply_cipher(message, activated_key)
    return new_message

def decrypt(message, key):
    """Returns the given message encrypted using your custom cipher."""
    activated_key = []
    initial_key = activate_key(key)
    for digit in initial_key:
        activated_key.append(digit - (2 * digit))
    new_message = apply_cipher(message, activated_key)
    return new_message

def activate_key(key):
    """Returns the key in the usable format."""
    activated_key = []
    for digit in str(key):
        activated_key.append(int(digit))
    return activated_key

def apply_cipher(message, activated_key):
    """Returns the message alphabetically shifted by the given key."""
    new_message = ""
    char_count = 0
    shift = activated_key[0]
    for char in message:
        if char_count % 2 == 0:
            new_message += shift_character(char, shift)
        else:
            new_message += shift_character(char, -shift)
        char_count += 1
        shift = activated_key[(char_count) % len(activated_key)]
    return new_message
        
        
def shift_character(char, shift):
    """Returns the letter alphabetically shifted by the given amount."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    # Find the character that's 'shift' characters over.
    if char in numbers:
        new_index = numbers.index(char) + shift
        shifted_letter = numbers[new_index % len(numbers)]
    elif char.lower() in alphabet:
        new_index = alphabet.index(char.lower()) + shift
        shifted_letter = alphabet[new_index % len(alphabet)]
        # Preserve capitalization.
        if char.isupper():
            shifted_letter = shifted_letter.upper()
    else:
        # Symbol and whitespace characters stay the same.
        return char

    return shifted_letter
    
