import re

class RegistrationError(Exception):
    """Custom exception for registration errors."""
    pass

def register_user(username, email, password):
    if not username:
        raise RegistrationError("Username cannot be empty")
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise RegistrationError("Invalid email format")
    
    if len(password) < 6:
        raise RegistrationError("Password too weak")
    
    return "Registration successful"

# User Interface Function
def registration_ui():
    print("=== User Registration ===")
    
    try:
        # Get user input
        username = input("Enter your username: ").strip()
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()
        
        # Call the register_user function
        result = register_user(username, email, password)
        print(result)
    
    except RegistrationError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    registration_ui()