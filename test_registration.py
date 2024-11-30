import pytest
import re
from regis import register_user, RegistrationError

# Test case for empty username
def test_empty_username():
    with pytest.raises(RegistrationError) as exc_info:
        register_user("", "test@example.com", "Password123")
    assert str(exc_info.value) == "Username cannot be empty"

# Test case for invalid email format
def test_invalid_email():
    with pytest.raises(RegistrationError) as exc_info:
        register_user("username", "invalid-email", "Password123")
    assert str(exc_info.value) == "Invalid email format"

# Test case for weak password
def test_weak_password():
    with pytest.raises(RegistrationError) as exc_info:
        register_user("username", "test@example.com", "short")
    assert str(exc_info.value) == "Password too weak"

# Test case for successful registration
def test_successful_registration():
    result = register_user("username", "test@example.com", "Password123")
    assert result == "Registration successful"

# Test case for valid email format
def test_valid_email():
    result = register_user("username", "valid.email@example.com", "Password123")
    assert result == "Registration successful"

# Test case for password length exactly 6 characters
def test_password_length_six():
    result = register_user("username", "test@example.com", "Pass12!")
    assert result == "Registration successful"

