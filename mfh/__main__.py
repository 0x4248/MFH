# Multi file hash
# Multi File Hash creates several hashes of the head and tail of a file.
# GitHub: https://www.github.com/0x4248/mfh
# Licence: GNU General Public License v3.0
# By: 0x4248

import base64
import hashlib
import sys
import os
import argparse
import colorama
import json

def print_error(error):
    print(f"[ {colorama.Fore.RED}X{colorama.Style.RESET_ALL} ] {error}")

def print_success(success):
    print(f"[ {colorama.Fore.GREEN}✓{colorama.Style.RESET_ALL} ] {success}")

def generate_hash_file(file_path, head_lines, tail_lines, output, return_output=False, note=None, json=False):
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    with open(file_path, 'rb') as file:
        file_data = file.read()
        file_sha256 = hashlib.sha256(file_data).hexdigest()
        file_lines = file_data.decode('utf-8', errors='ignore').split('\n')
        head_lines_data = file_lines[:head_lines]
        tail_lines_data = file_lines[-tail_lines:]
        if json == True:
            hash_file = "MFH v1\n"
            hash_file += f"fn:{file_name}\n"
            hash_file += f"ln:{len(file_lines)}\n"
            hash_file += f"fs:{file_size}\n"
            if note is not None:
                hash_file += f"n:{note}\n"
            hash_file += f"sha256:{file_sha256}\n"
            hash_file += "HEAD:\n"

            for i in range(len(head_lines_data)):
                hash_file += f"h{i+1}:{hashlib.sha256(head_lines_data[i].encode()).hexdigest()}\n"
            hash_file += "TAIL:\n"
            for i in range(len(tail_lines_data)):
                hash_file += f"t{len(file_lines) - len(tail_lines_data) + i + 1}:{hashlib.sha256(tail_lines_data[i].encode()).hexdigest()}\n"
            if return_output:
                return hash_file
            if output is not None:
                with open(output, 'w') as output_file:
                    output_file.write(hash_file)
            else:
                print(hash_file)
        else:
            json_file = {
                "Version": "MFH v1",
                "File Name": file_name,
                "Line Numbers": len(file_lines),
                "File Size": file_size,
                "SHA256": file_sha256,
                "Head": [],
                "Tail": []
            }
            if note is not None:
                json_file["Note"] = note
            for i in range(len(head_lines_data)):
                json_file["Head"].append({f"Line {i+1}": hashlib.sha256(head_lines_data[i].encode()).hexdigest()})
            for i in range(len(tail_lines_data)):
                json_file["Tail"].append({f"Line {len(file_lines) - len(tail_lines_data) + i + 1}": hashlib.sha256(tail_lines_data[i].encode()).hexdigest()})
            if return_output:
                return json_file
            if output is not None:
                with open(output, 'w') as output_file:
                    json.dump(json_file, output_file, indent=4)
            else:
                print(json.dumps(json_file, indent=4))

def parse_hash_file(hash_file):
    hash_file = {
        "Version": "",
        "File Name": "",
        "Line Numbers": 0,
        "File Size": 0,
        "Note": "",
        "SHA256": "",
        "Head": [],
        "Tail": []
    }

    try:
        hash_file = json.loads(hash_file)
        return hash_file
    except:
        pass
    for line in hash_file.split('\n'):
        if line.startswith("fn:"):
            hash_file["File Name"] = line[3:]
        elif line.startswith("ln:"):
            hash_file["Line Numbers"] = int(line[3:])
        elif line.startswith("fs:"):
            hash_file["File Size"] = int(line[3:])
        elif line.startswith("sha256:"):
            hash_file["SHA256"] = line[7:]
        elif line.startswith("h"):
            hash_file["Head"].append(line)
        elif line.startswith("t"):
            hash_file["Tail"].append(line)
    return hash_file

def compare(hash_a, hash_b):
    hash_a = parse_hash_file(hash_a)
    hash_b = parse_hash_file(hash_b)

    if hash_a["File Name"] != hash_b["File Name"]:
        print_error(f"File names do not match: {hash_a['File Name']} != {hash_b['File Name']}")
    else:
        print_success(f"File names match: {hash_a['File Name']}")
    if hash_a["Line Numbers"] != hash_b["Line Numbers"]:
        print_error(f"Line numbers do not match: {hash_a['Line Numbers']} != {hash_b['Line Numbers']}")
    else:
        print_success(f"Line numbers match: {hash_a['Line Numbers']}")
    if hash_a["File Size"] != hash_b["File Size"]:
        print_error(f"File sizes do not match: {hash_a['File Size']} != {hash_b['File Size']}")
    else:
        print_success(f"File sizes match: {hash_a['File Size']}")
    if hash_a["SHA256"] != hash_b["SHA256"]:
        print_error(f"SHA256 hashes do not match: {hash_a['SHA256']} != {hash_b['SHA256']}")
    else:
        print_success(f"SHA256 hashes match: {hash_a['SHA256']}")
    for i in range(len(hash_a["Head"])):
        if hash_a["Head"][i] != hash_b["Head"][i]:
            print_error(f"Head hash {i+1} does not match:\t{hash_a['Head'][i]} != {hash_b['Head'][i]}")
        else:
            print_success(f"Head hash {i+1} matches:\t{hash_a['Head'][i]}")
    for i in range(len(hash_a["Tail"])):
        if hash_a["Tail"][i] != hash_b["Tail"][i]:
            print_error(f"Tail hash {i+1} does not match:\t{hash_a['Tail'][i]} != {hash_b['Tail'][i]}")
        else:
            print_success(f"Tail hash {i+1} matches:\t{hash_a['Tail'][i]}")


def compare_hash_file(file_path, hash_file_path):
    with open(file_path, 'rb') as file:
        with open(hash_file_path, 'r') as hash_file:
            hash_file = hash_file.read()
        hash_a = generate_hash_file(file_path, 10, 10, None, True)
        compare(hash_a, hash_file)

def compare_files(file_a, file_b, head_lines, tail_lines):
    hash_a = generate_hash_file(file_a, head_lines, tail_lines, None, True)
    hash_b = generate_hash_file(file_b, head_lines, tail_lines, None, True)
    compare(hash_a, hash_b)

def main():
    parser = argparse.ArgumentParser(description='Multi File Hash', prog='mfh')
    parser.add_argument('file', type=str, help='File to hash')
    parser.add_argument('-hl', type=int, default=10, help='Number of head lines to hash')
    parser.add_argument('-tl', type=int, default=10, help='Number of tail lines to hash')
    parser.add_argument('-o', type=str, default=None, help='Output file')
    parser.add_argument('-cf', type=str, default=None, help='Compare with other file (non hash file)')
    parser.add_argument('-ch', type=str, default=None, help='Compare with other hash file')
    parser.add_argument('-n', type=str, default=None, help='Add note to hash file')
    parser.add_argument('-j', type=bool, default=False, help='Output in JSON format')
    args = parser.parse_args()

    if args.cf is not None:
        compare_files(args.file, args.cf, args.hl, args.tl)
    elif args.ch is not None:
        compare_hash_file(args.file, args.ch)
    else:
        generate_hash_file(args.file, args.hl, args.tl, args.o, args.n)

if __name__ == "__main__":
    main()
