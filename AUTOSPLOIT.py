import subprocess
import os
import logging
import configparser

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

def scan_network():
    try:
        logger.info("Scanning network...")
        subprocess.run(["nmap", "-sn", config['NETWORK']['target_range']])
        logger.info("Network scan completed.")
    except Exception as e:
        logger.error(f"Error scanning network: {e}")

def enum_services():
    try:
        logger.info("Enumerating services...")
        subprocess.run(["nmap", "-p-", "-A", config['NETWORK']['target_ip']])
        logger.info("Service enumeration completed.")
    except Exception as e:
        logger.error(f"Error enumerating services: {e}")

def exploit_vulnerabilities():
    try:
        logger.info("Exploiting vulnerabilities...")
        os.system(config['EXPLOIT']['exploit_command'])
        logger.info("Vulnerability exploitation completed.")
    except Exception as e:
        logger.error(f"Error exploiting vulnerabilities: {e}")

def escalate_privileges():
    try:
        logger.info("Escalating privileges...")
        subprocess.run(["powershell.exe", config['PRIVILEGE_ESCALATION']['script_path']])
        logger.info("Privilege escalation completed.")
    except Exception as e:
        logger.error(f"Error escalating privileges: {e}")

def extract_credentials():
    try:
        logger.info("Extracting credentials...")
        os.system(config['CREDENTIAL_EXTRACTION']['tool_path'])
        logger.info("Credential extraction completed.")
    except Exception as e:
        logger.error(f"Error extracting credentials: {e}")

def main():
    logger.info("Automated Penetration Testing Tool")
    logger.info("Initializing...")

    try:
        while True:
            print("1. Scan Network")
            print("2. Enumerate Services")
            print("3. Exploit Vulnerabilities")
            print("4. Escalate Privileges")
            print("5. Extract Credentials")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                scan_network()
            elif choice == '2':
                enum_services()
            elif choice == '3':
                exploit_vulnerabilities()
            elif choice == '4':
                escalate_privileges()
            elif choice == '5':
                extract_credentials()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        logger.info("Exiting...")

if __name__ == "__main__":
    main()
