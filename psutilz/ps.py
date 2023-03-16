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
    children: list


def build_process_tree(procs: list):
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


def print_tree(process_tree: TreeNode, user_max_width=5):
    print(
        f"{'USER':>{user_max_width}} {'PID':>5} {'PPID':>5} {'NIC':>3} {'%CPU':>5} {'%MEM':>5} {'#TH':>5}"
        f" {'STARTED':>19} COMMAND"
    )

    def _print_tree(node: TreeNode, indent: int = 0):
        info = node.proc.info
        cpu_percent_str = (
            f"{info['cpu_percent']: 5.1f}"
            if info["cpu_percent"] is not None
            else "    ?"
        )
        memory_percent_str = (
            f"{info['memory_percent']: 5.1f}"
            if info["memory_percent"] is not None
            else "    ?"
        )
        cmd_str = (
            subprocess.list2cmdline(info["cmdline"])
            if info["cmdline"]
            else (info["name"] or "?")
        )
        print(
            f"{info['username'] or '?':>{user_max_width}} "
            f"{info['pid']:>5} "
            f"{info['ppid'] or '?':>5} "
            f"{info['nice'] or '?':>3} "
            f"{cpu_percent_str} "
            f"{memory_percent_str} "
            f"{info['num_threads'] or '?':>5} "
            f"{datetime.utcfromtimestamp(info['create_time']):%Y-%m-%d %H:%M:%S} "
            f"{' '*indent}"
            f"{cmd_str}"
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

    try:
        procs = list(
            psutil.process_iter(
                [
                    "pid",
                    "username",
                    "cmdline",
                    "name",
                    "num_threads",
                    "cpu_percent",
                    "memory_percent",
                    "ppid",
                    "nice",
                    "create_time",
                ]
            )
        )
        process_tree = build_process_tree(procs)
        user_max_width = max(len(proc.info["username"]) for proc in procs)
        print_tree(process_tree, user_max_width)
    except BrokenPipeError:
        pass


if __name__ == "__main__":
    main()
