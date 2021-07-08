#!/bin/bash

# Bash "strict mode", to help catch problems and bugs in the shell
# script. Every bash script you write should include this. See
# http://redsymbol.net/articles/unofficial-bash-strict-mode/ for
# details.
set -euo pipefail

# Tell apt-get we're never going to be able to give manual
# feedback:
export DEBIAN_FRONTEND=noninteractive

# Update the package listing, so we know what package exist:
apt-get update

# Install security updates:
apt-get -y upgrade

# Install a new package, without unnecessary recommended packages:
apt-get -y install --no-install-recommends libgl1-mesa-glx libglib2.0-0 ffmpeg wget

# We need the latest version of youtube-dl and yt-dlp:
wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
chmod a+rx /usr/local/bin/youtube-dl
hash -r
wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp
chmod a+rx /usr/local/bin/yt-dlp

wget http://http.us.debian.org/debian/pool/main/g/gcc-10/libgcc-s1_10.2.1-6_amd64.deb -O libgcc-s1_10.2.1-6_amd64.deb
dpkg -i libgcc-s1_10.2.1-6_amd64.deb
wget http://http.us.debian.org/debian/pool/main/a/aria2/libaria2-0_1.35.0-3_amd64.deb -O libaria2-0_1.35.0-3_amd64.deb
dpkg -i libaria2-0_1.35.0-3_amd64.deb
wget http://http.us.debian.org/debian/pool/main/a/aria2/aria2_1.35.0-3_amd64.deb -O aria2_1.35.0-3_amd64.deb
dpkg -i aria2_1.35.0-3_amd64.deb

echo "Youtube-DL version:"
youtube-dl --version
echo "Yt-DLP version:"
yt-dlp --version
echo "Aria2c version:"
aria2c --version

# Delete cached files we don't need anymore:
apt-get clean
rm -rf /var/lib/apt/lists/*
