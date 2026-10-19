import docker

client = docker.from_env()

print("Building Flask image...")
image, logs = client.images.build(
    path=".",
    tag="flask-apparmor"
)

print("Image built:", image.tags)

print("\nDocker SecurityOptions:")
print(client.info().get("SecurityOptions", []))

print(
    "\nAppArmor is not enabled in this Docker environment."
    "\nThe custom AppArmor profile cannot be enforced here."
    "\nUse a Linux machine or VM with AppArmor enabled to complete"
    " the profile-enforcement portion of this exercise."
)
