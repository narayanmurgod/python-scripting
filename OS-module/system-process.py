import os

def print_process_info():
    # Get the current process ID
    pid = os.getpid()
    
    # Get the parent process ID
    ppid = os.getppid()
    
    # Get the current process's user ID
    uid = os.getuid()
    
    # Get the current process's group ID
    gid = os.getgid()
    
    # Print the values
    print(f"Current Process ID (PID): {pid}")
    print(f"Parent Process ID (PPID): {ppid}")
    print(f"User ID (UID): {uid}")
    print(f"Group ID (GID): {gid}")

if __name__ == "__main__":
    print_process_info()
