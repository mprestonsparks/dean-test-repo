# Security vulnerabilities for testing agent detection and fixes

import os
import subprocess
import pickle
import hashlib

# Hardcoded secrets (security issue)
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
SECRET_TOKEN = "super_secret_token_123"

def unsafe_file_operations(user_input):
    """
    Path traversal vulnerability - user input not sanitized
    """
    filename = f"/app/data/{user_input}"
    with open(filename, 'r') as f:
        return f.read()

def command_injection_risk(user_command):
    """
    Command injection vulnerability - user input executed directly
    """
    result = subprocess.run(f"ls {user_command}", shell=True, capture_output=True)
    return result.stdout.decode()

def unsafe_deserialization(pickled_data):
    """
    Unsafe pickle deserialization - can execute arbitrary code
    """
    return pickle.loads(pickled_data)

def weak_password_hashing(password):
    """
    Weak password hashing - should use bcrypt or similar
    """
    return hashlib.md5(password.encode()).hexdigest()

def sql_injection_risk(user_id):
    """
    SQL injection vulnerability - string formatting instead of parameterized queries
    """
    query = f"SELECT * FROM users WHERE id = {user_id}"
    # This would be executed directly without sanitization
    return query

class InsecureConfig:
    """
    Security configuration issues
    """
    def __init__(self):
        self.debug_mode = True
        self.ssl_verify = False
        self.allow_any_origin = True
    
    def get_database_url(self):
        # Credentials in code instead of environment variables
        return f"postgresql://admin:{DATABASE_PASSWORD}@localhost/mydb"
    
    def make_request(self, url):
        import requests
        # SSL verification disabled
        return requests.get(url, verify=False)

def insecure_random_generation():
    """
    Using predictable random number generation for security purposes
    """
    import random
    return random.randint(1000, 9999)  # Should use secrets module

def information_disclosure():
    """
    Potential information disclosure through error messages
    """
    try:
        with open("/etc/passwd", 'r') as f:
            return f.read()
    except Exception as e:
        # Detailed error message might reveal system information
        return f"Error accessing file: {str(e)}"

# Unsafe eval usage
def dangerous_eval(user_expression):
    """
    Arbitrary code execution through eval
    """
    return eval(user_expression)

# Missing input validation
def process_user_data(data):
    """
    No input validation or sanitization
    """
    # Directly process user data without checks
    result = data['operation'](data['value1'], data['value2'])
    return result

if __name__ == "__main__":
    # Example usage with security issues
    print(f"API Key: {API_KEY}")
    
    # These would be security risks in real usage
    user_file = "../../../etc/passwd"  # Path traversal attempt
    user_cmd = "; rm -rf /"  # Command injection attempt
    
    print(f"Weak hash: {weak_password_hashing('password123')}")
    print(f"Insecure token: {insecure_random_generation()}")