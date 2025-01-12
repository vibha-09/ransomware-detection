import os
import random
import string

def simulate_ransomware(directory):
    """
    Simulates ransomware by renaming files in the given directory without encryption.
    """
    # List all files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Ignore already renamed files (to prevent repeated renaming)
            if file.endswith(".encrypted"):
                continue

            # Rename the file to simulate ransomware's renaming behavior
            new_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + ".encrypted"
            new_path = os.path.join(root, new_name)
            os.rename(file_path, new_path)
            print(f"Renamed: {file_path} -> {new_path}")

if __name__ == "__main__":
    # Test directory to simulate ransomware activity
    test_directory = "./test_files"
    
    # Ensure the test directory exists
    os.makedirs(test_directory, exist_ok=True)

    # Create sample files for testing
    for i in range(5):
        file_path = os.path.join(test_directory, f"file_{i}.txt")
        with open(file_path, 'w') as f:
            f.write(f"This is test file {i}")

    # Simulate ransomware activity
    simulate_ransomware(test_directory)

    os._exit(0)
