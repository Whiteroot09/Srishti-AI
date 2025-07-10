import subprocess

def run_as_admin(file_path, password):
    try:
        # Execute the command with password as input
        process = subprocess.Popen(['runas', '/user:Administrator', file_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = process.communicate(input=password.encode())
        process.wait()

        # Check if the command executed successfully
        if process.returncode != 0:
            print("Error running file as administrator. Return code:", process.returncode)
            print("Error message:", err.decode())

    except subprocess.CalledProcessError as e:
        # Handle any errors that occurred during execution
        print("Error running file as administrator:", e)

# Example usage
file_path = 'sub2.py'
password = '8016'
run_as_admin(file_path, password)
