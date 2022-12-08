#!/usr/bin/env python
import subprocess
from collections import defaultdict
from datetime import datetime
from typing import NamedTuple

import psutil
import argparse
import sys
import os


class TreeNode(NamedTuple):
    proc: psutil.Process
    children: list["TreeNode"]  #


def build_process_tree():
    procs = list(psutil.process_iter())
    children_by_ppid = defaultdict(list)
    proc_by_pid = {}
    for proc in procs:
        try:
            children_by_ppid[proc.ppid()].append(proc.pid)
            proc_by_pid[proc.pid] = proc
        except psutil.NoSuchProcess:
            pass

    def add_children_recursively(parent_node: TreeNode):
        for pid in sorted(children_by_ppid[parent_node.proc.pid]):
            if pid == parent_node.proc.pid:
                continue
            proc = proc_by_pid[pid]
            child_node = TreeNode(proc, [])
            parent_node.children.append(child_node)
            add_children_recursively(child_node)

    if 0 in proc_by_pid:
        root = TreeNode(proc_by_pid[0], [])
    else:
        root = TreeNode(proc_by_pid[1], [])
    add_children_recursively(root)

    return root


def print_tree(process_tree: TreeNode):
    user_width = 5
    print(
        f"{'USER':>{user_width}} {'PID':>5} {'PPID':>5} {'NIC':>3} {'%CPU':>5} {'%MEM':>5} {'#TH':>5}"
        f" {'STARTED':>19} COMMAND"
    )

    def _print_tree(node: TreeNode, indent: int = 0):
        try:
            cpu_percent = node.proc.cpu_percent()
        except psutil.Error:
            cpu_percent = float("nan")

        try:
            memory_percent = node.proc.memory_percent()
        except psutil.Error:
            memory_percent = float("nan")

        try:
            num_threads = node.proc.num_threads()
        except psutil.Error:
            num_threads = "?"

        try:
            cmdline = subprocess.list2cmdline(node.proc.cmdline())
        except psutil.Error:
            cmdline = "?"

        try:
            nice = node.proc.nice()
        except psutil.Error:
            nice = "?"

        print(
            f"{node.proc.username() or '?':>{user_width}} "
            f"{node.proc.pid:>5} "
            f"{node.proc.ppid() or '?':>5} "
            f"{nice:>3} "
            f"{cpu_percent: 5.1f} "
            f"{memory_percent: 5.1f} "
            f"{num_threads:>5} "
            f"{datetime.utcfromtimestamp(node.proc.create_time()):%Y-%m-%d %H:%M:%S} "
            f"{' '*indent}"
            f"{cmdline}"
        )

        for child in node.children:
            _print_tree(child, indent + 2)

    _print_tree(process_tree)


def main(argv=None):
    argv = argv or sys.argv

    arg_parser = argparse.ArgumentParser(
        prog=os.path.basename(argv[0]),
        description="something like ps -fHe but portable",
    )
    arg_parser.parse_args(args=argv[1:])

    process_tree = build_process_tree()
    print_tree(process_tree)


if __name__ == "__main__":
    main()
