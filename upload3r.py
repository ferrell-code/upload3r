#!/usr/bin/env python3
import os
import argparse


# puts url of burp collaborator or personal server into payloads
def swap_string(filename, file_path, output_path, burp_collab):
    with open(file_path + filename) as file:
        newtext = file.read().replace("%upload3r%", burp_collab)
    with open(f"{output_path}{burp_collab}_{filename}", "a") as newf:
        newf.write(newtext)


script_path = os.path.dirname(os.path.realpath(__file__))
xml_path = script_path + "/xml/"
cwd = os.getcwd() + "/"
parser = argparse.ArgumentParser(description="create OOB upload files")
parser.add_argument("-o", type=str, metavar="PATH", help="Path for output", nargs=1, default=[cwd])
parser.add_argument("url", type=str, nargs=1, help='url of burp collaborator')
args = parser.parse_args()
domain_string = args.url[0]
output_path = args.o[0]

for f in os.listdir(xml_path):
    swap_string(f, xml_path, output_path, domain_string)
