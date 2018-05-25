import subprocess as sp

def install_packages():
    print("Installing Packages with DNF")
    print("----------------------------")
    packages = ""
    with open("dnf_install", "r") as f:
        packages = f.read()
    packages = packages.split('\n')
    for package in packages:
        sp.call(["sudo", "dnf", "install", "-y", package])


def install_i3_gaps():
    print("\nInstalling i3-gaps from source")
    print("-------------------------------")
    gaps_dir = "/home/gregmccoy/Programming/i3-gaps"
    sp.call(["rm", "-rf", gaps_dir])
    sp.call(["git", "clone", "https://github.com/Airblader/i3", gaps_dir])
    sp.call(["autoreconf", "--force", "--install"], cwd=gaps_dir)
    sp.call(["rm", "-rf", gaps_dir + "/build"])
    sp.call(["mkdir", "-p", gaps_dir + "/build"])
    sp.call(["./configure", "--prefix=/usr", "--sysconfdir=/etc", "--disable-sanitizers"], cwd=gaps_dir)
    sp.call(["make"])
    sp.call(["sudo", "make", "install"])


def copr_install_flat_remix():
    print("\nInstalling Flat remix")
    sp.call(["sudo", "dnf", "copr", "enable", "daniruiz/flat-remix"])
    sp.call(["sudo", "dnf", "install", "flat-remix"])


def copy_configs():
    print("\nCopying config files")
    print("----------------------")
    sp.call(["cp", "../config", "/home/gregmccoy/.config/i3/config"])
    sp.call(["cp", "-a", "../.scripts", "/home/gregmccoy"])
    sp.call(["sudo", "cp", "../lock", "/bin/lock"])
    sp.call(["sudo", "cp", "../gtk-3.0/settings.ini", "/home/gregmccoy/.config/gtk-3.0/"])
    sp.call(["cp", "../.speedswapper", "~" ])
    sp.call(["cp", "-a", "../.vim/", "/home/gregmccoy"])
    sp.call(["cp", "../.vimrc", "/home/gregmccoy"])


#def install_gpmdp():
#    print("\n Installing Google Play Desktop Music Player")
#    sp.call(["wget", "https://github-production-release-asset-2e65be.s3.amazonaws.com/40008106/5b7132cc-0621-11e8-8a84-1e97eab3979e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20180523%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180523T145832Z&X-Amz-Expires=300&X-Amz-Signature=dc75e65830f99aaeb1ee66ecb8845bc6403e27ac9de9c5fc4c4523062f27110e&X-Amz-SignedHeaders=host&actor_id=15632035&response-content-disposition=attachment%3B%20filename%3Dgoogle-play-music-desktop-player-4.5.0.x86_64.rpm&response-content-type=application%2Foctet-stream", "-o", "/home/gregmccoy/Downloads/google-play-music-desktop-player-4.5.0.x86_64.rpm"])
#    sp.call(["sudo", "dnf", "install", "/home/gregmccoy/Downloads/google-play-music-desktop-player-4.5.0.x86_64.rpm"])


def copy_ssh():
    print("\nCopying SSH files")
    sp.call(["cp", "/home/gregmccoy/Nextcloud/Desktop/.ssh/*", "/home/gregmccoy/.ssh/"])


#install_packages()
#sp.call(["mkdir", "~/Programming"])
#sp.call(["mkdir", "~/.ssh"])
#install_i3_gaps()
#install_gpmdp()
copr_install_flat_remix()
copy_configs()
sp.call(["nextcloud"])
copy_ssh()


