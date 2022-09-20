import os
import sys

def get_flatpak_list():
    l = os.listdir("/var/lib/flatpak/app")
    return l

def get_flatpak_rawcmd(flatpak):
    with open(f"/var/lib/flatpak/app/{flatpak}/current/active/metadata",'r') as f:
        line = f.readline()
        while "command" not in line:
            line = f.readline()
        cmd = line.split("=")[1][:-1]
    return cmd

def main(args):
    flatpaks = get_flatpak_list()
    for flatpak in flatpaks:
        rawcmd = get_flatpak_rawcmd(flatpak)
        runcmd = f"flatpak run {flatpak}"
        os.system("mkdir -p ./bin")
        with open(f"./bin/{rawcmd}",'w') as f:
            f.write(f"#!/bin/sh\n/usr/bin/flatpak run {flatpak}")


if __name__ == "__main__":
    main(sys.argv)
