import os
import fileinput
import sys

# download new APT installation
aptchoi = input("Would you like to update apt?")
if aptchoi == "y":
    os.system('sudo apt-get update&& apt-get upgrade')

# edit ssh config
for line in fileinput.input(["/etc/ssh/ssh_config"], inplace=True):
    line = line.replace("#   PasswordAuthentication no", "#    PasswordAuthentication yes")
    # redirected to the file
    sys.stdout.write(line)

# function that deletes files with certain extension


def chfil(filex, file):
    directory = file
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if file.endswith(filex)]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
    os.system(f"rm {path_to_file}")


# Calls upon function to delete certain files.
filechoice = input("Would you like to remove files?")
if filechoice == "y":
    fi = True
    while fi:
        chfil(input("What type of file do you want to delete?"), input("What directory?"))
        fi = False
        fichoice = input("Would you like to delete more files?")
    if fichoice == "y":
        fi = True


# function shows status and return as variable


def statuscheck():
    a = os.system("service --status-all")
    return a


# if your status does not equal default status = alert
if statuscheck() != """ [ + ]  acpid
 [ - ]  alsa-utils
 [ - ]  anacron
 [ + ]  apparmor
 [ + ]  apport
 [ + ]  avahi-daemon
 [ + ]  bluetooth
 [ - ]  console-setup.sh
 [ + ]  cron
 [ + ]  cups
 [ + ]  cups-browsed
 [ + ]  dbus
 [ + ]  gdm3
 [ - ]  grub-common
 [ - ]  hwclock.sh
 [ + ]  irqbalance
 [ + ]  kerneloops
 [ - ]  keyboard-setup.sh
 [ + ]  kmod
 [ + ]  open-vm-tools
 [ + ]  openvpn
 [ - ]  plymouth
 [ + ]  plymouth-log
 [ + ]  procps
 [ - ]  pulseaudio-enable-autospawn
 [ - ]  rsync
 [ - ]  saned
 [ - ]  speech-dispatcher
 [ - ]  spice-vdagent
 [ + ]  udev
 [ + ]  ufw
 [ + ]  unattended-upgrades
 [ - ]  uuidd
 [ - ]  whoopsie
 [ - ]  x11-common
""":
    print("Consider checking your services, more than default amount")
