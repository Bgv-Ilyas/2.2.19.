#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import argparse

def list_files(startpath, show_hidden=False, level=0, max_depth=None):
    if max_depth is not None and level > max_depth:
        return

    for root, dirs, files in os.walk(startpath):
        if not show_hidden:
            files = [f for f in files if not f.startswith('.')]
            dirs[:] = [d for d in dirs if not d.startswith('.')]

        if level == 0:
            print(root)
        else:
            indent = '  ' * (level - 1)
            print('{}{}'.format(indent, os.path.basename(root)))

        sub_indent = '  ' * level
        for file in files:
            print('{}{}'.format(sub_indent, file))

        for d in dirs:
            list_files(os.path.join(root, d), show_hidden, level + 1, max_depth)

def main():
    parser = argparse.ArgumentParser(description="Python Tree Utility")
    parser.add_argument("directory", nargs='?', default='.', help="Directory to display (default: current directory)")
    parser.add_argument("-a", "--all", action="store_true", help="Show hidden files and directories")
    parser.add_argument("-d", "--max-depth", type=int, help="Max display depth")
    args = parser.parse_args()

    directory = args.directory
    show_hidden = args.all
    max_depth = args.max_depth

    if not os.path.isdir(directory):
        print("Error: '{}' is not a directory.".format(directory))
        return

    print("Directory structure for '{}':".format(directory))
    list_files(directory, show_hidden, max_depth=max_depth)

if __name__ == "__main__":
    main()
