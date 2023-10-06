import subprocess

# Get the list of Wi-Fi profiles
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# Extract profile names
profiles = [line.split(":")[1].strip() for line in data if "All User Profile" in line]

# Loop through the profiles
for profile in profiles:
    try:
        # Retrieve the Wi-Fi key (password)
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
        results = [line.split(":")[1].strip() for line in results if "Key Content" in line]

        if results:
            # Print the profile name and key
            print('{:<30} | {:<}'.format(profile, results[0]))
        else:
            print('{:<30} | (No Key Found)')
    except (IndexError, subprocess.CalledProcessError):
        # Handle the case where no Wi-Fi key is found or subprocess error occurs
        print("{:<30} | (Error)")
