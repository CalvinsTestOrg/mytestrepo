import pickle
import os
import sqlite3

# Vulnerable to SQL injection
def get_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # VULNERABILITY: SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

# Vulnerable to command injection
def backup_user_files(user_folder):
    # VULNERABILITY: Command Injection
    os.system(f"tar -czf backup.tar.gz {user_folder}")

# Vulnerable to arbitrary code execution
def load_user_settings(settings_file):
    # VULNERABILITY: Insecure Deserialization
    with open(settings_file, 'rb') as f:
        settings = pickle.load(f)
    return settings

# Vulnerable to path traversal
def read_user_file(filename):
    # VULNERABILITY: Path Traversal
    base_path = "/var/app/user_files/"
    file_path = base_path + filename
    with open(file_path, 'r') as f:
        return f.read()

# Example usage
if __name__ == "__main__":
    user_input = input("Enter username: ")
    print(get_user_data(user_input))
