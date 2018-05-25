import subprocess as sp
import shutil
import os, glob

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
    sp.call(["../configure", "--prefix=/usr", "--sysconfdir=/etc", "--disable-sanitizers"], cwd=gaps_dir + "/build")
    sp.call(["make"], cwd=gaps_dir + "/build")
    sp.call(["sudo", "make", "install"], cwd=gaps_dir + "/build")


def copr_install_flat_remix():
    print("\nInstalling Flat remix")
    sp.call(["sudo", "dnf", "copr", "-y", "enable", "daniruiz/flat-remix"])
    sp.call(["sudo", "dnf", "install", "-y", "flat-remix"])


def copy_configs():
    print("\nCopying config files")
    print("----------------------")
    sp.call(["mkdir", "/home/gregmccoy/.config/i3"])
    sp.call(["cp", "../config", "/home/gregmccoy/.config/i3/config"])
    sp.call(["cp", "-a", "../.scripts", "/home/gregmccoy"])
    sp.call(["sudo", "cp", "../lock", "/bin/lock"])
    sp.call(["sudo", "cp", "../gtk-3.0/settings.ini", "/home/gregmccoy/.config/gtk-3.0/"])
    sp.call(["cp", "../.speedswapper", "/home/gregmccoy" ])
    sp.call(["cp", "-a", "../.vim/", "/home/gregmccoy"])
    sp.call(["cp", "../.vimrc", "/home/gregmccoy"])
    sp.call(["cp", "../.bashrc", "/home/gregmccoy"])
    sp.call(["cp", "../.speedswapper", "/home/gregmccoy"])


def install_ffmpeg():
    print("\nInstalling ffmpeg with RPM Fusion")
    print("-----------------------------------")
    FEDORA_VERSION = "28"
    sp.call(["sudo", "dnf", "install", "-y", "http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-28.noarch.rpm", "https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-28.noarch.rpm"])
    sp.call(["sudo", "dnf", "install", "-y", "ffmpeg"])


def install_gcloud():
    print("\n Installing gcloud and kubectl")
    print("--------------------------------")
    sp.call(["sudo", "cp", "google-cloud-sdk.repo", "/etc/yum.repos.d/google-cloud-sdk.repo"])
    sp.call(["sudo", "dnf", "install", "-y", "google-cloud-sdk"])
    sp.call(["gcloud", "init"])
    sp.call(["sudo", "dnf", "install", "-y", "kubectl"])
    sp.call(["gcloud", "container", "clusters", "get-credentials", "gfa-cluster"])
    sp.call(["kubectl", "config", "set-context", "gke_gfa-cluster-175514_us-west1-a_gfa-cluster", "--namespace=gfa-namespace"])


def install_gpmdp():
    print("\n Installing Google Play Desktop Music Player")
    print("----------------------------------------------")
    sp.call(["wget", "https://github.com/MarshallOfSound/Google-Play-Music-Desktop-Player-UNOFFICIAL-/releases/download/v4.5.0/google-play-music-desktop-player-4.5.0.x86_64.rpm", "-o", "/home/gregmccoy/Downloads/google-play-music-desktop-player-4.5.0.x86_64.rpm"])
    sp.call(["sudo", "dnf", "install", "/home/gregmccoy/Downloads/google-play-music-desktop-player-4.5.0.x86_64.rpm"])


def copy_ssh():
    print("\nCopying SSH files")
    sp.call(["cp", "-a", "/home/gregmccoy/Nextcloud/Desktop/.ssh", "/home/gregmccoy/"])


def install_i3blocks():
    print("\n Installing i3blocks")
    print("----------------------")
    blocks_dir = "/home/gregmccoy/Programming/i3blocks"
    sp.call(["rm", "-rf", blocks_dir])
    sp.call(["git", "clone", "https://github.com/vivien/i3blocks", blocks_dir])
    sp.call(["make", "clean", "debug", blocks_dir])
    sp.call(["sudo", "make", "install"], cwd=blocks_dir)
    sp.call(["sudo", "mkdir", "/usr/share/i3blocks/"])
    for i in glob.glob(os.path.join(blocks_dir + "/scripts", '*')):
        print(i)
        sp.call(["sudo", "cp", i, "/usr/share/i3blocks/"])



install_packages()
sp.call(["mkdir", "~/Programming"])
sp.call(["mkdir", "~/.ssh"])
install_i3_gaps()
install_i3blocks()
install_gpmdp()
copr_install_flat_remix()
copy_configs()
sp.call(["nextcloud"])
copy_ssh()
install_ffmpeg()
install_gcloud()


