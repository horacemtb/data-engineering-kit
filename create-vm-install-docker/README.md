1. First, I created a VM with the following configurations in Yandex Compute Cloud:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/create-vm-install-docker/images/1.%20Create%20VM.png)

2. Then I followed the instructions at https://docs.docker.com/engine/install/ubuntu/ to install Docker on my VM:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/create-vm-install-docker/images/2.%20Uninstall%20all%20previous%20installations.png)

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/create-vm-install-docker/images/3.%20Install%20Docker.png)

3. After that I created a Unix group called docker and added my user to it, as described at https://docs.docker.com/engine/install/linux-postinstall/

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/create-vm-install-docker/images/4.%20Manage%20Docker%20as%20non-root%20user.png)

4. Finally, I pulled the hello-world image and ran it as a container on my VM:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/create-vm-install-docker/images/5.%20Docker%20run%20hello-world.png)