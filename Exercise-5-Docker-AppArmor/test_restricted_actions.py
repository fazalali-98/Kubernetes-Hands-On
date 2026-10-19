import docker

client = docker.from_env()

print("Checking whether the custom AppArmor profile can be tested...")

security_options = client.info().get("SecurityOptions", [])
print("Docker SecurityOptions:", security_options)

apparmor_available = any(
    "apparmor" in option.lower()
    for option in security_options
)

if not apparmor_available:
    print("\nRESULT: Custom AppArmor enforcement cannot be verified.")
    print("Docker does not report AppArmor support in this environment.")
    print("Run these security tests on a Linux host with AppArmor enabled.")
else:
    print("\nDocker reports AppArmor-related security support.")
    print("Verify the profile is loaded before testing restricted actions.")
