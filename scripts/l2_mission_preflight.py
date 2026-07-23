#!/usr/bin/env python3
"""
L2 Mission Preflight Validator
Dependency-free Python stdlib only.
Validates branch, fast-path files, tree state, and private path tracking before accepting delegated missions.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

FAST_PATH_FILES = [
    "1_Command_Brain_Core/1.2_Headquarters_Memory/ubiquitous_language.md",
    "1_Command_Brain_Core/1.1_Command_Center_State_and_Protocols/00_Live_State_and_GSD/state.md",
    "1_Command_Brain_Core/1.2_Headquarters_Memory/active-context.md",
    "1_Command_Brain_Core/1.2_Headquarters_Memory/key-workspaces.md",
]

PRIVATE_PATHS = [".hermes/", ".env", ".env.*"]


def run_git(args, cwd=None, check=True):
    """Run git command and return stdout or raise on error."""
    cmd = ["git"] + args
    result = subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if check and result.returncode != 0:
        raise subprocess.CalledProcessError(result.returncode, cmd, result.stdout, result.stderr)
    return result.stdout.strip()


def is_git_repo(cwd=None):
    try:
        run_git(["rev-parse", "--is-inside-work-tree"], cwd=cwd)
        return True
    except subprocess.CalledProcessError:
        return False


def get_repo_root(cwd=None):
    return run_git(["rev-parse", "--show-toplevel"], cwd=cwd)


def get_current_branch(cwd=None):
    return run_git(["rev-parse", "--abbrev-ref", "HEAD"], cwd=cwd)


def get_head_sha(cwd=None):
    return run_git(["rev-parse", "HEAD"], cwd=cwd)


def get_origin_main_sha(cwd=None):
    try:
        return run_git(["rev-parse", "origin/main"], cwd=cwd)
    except subprocess.CalledProcessError:
        return None


def get_ahead_behind(cwd=None):
    """Return (ahead, behind) counts relative to origin/main."""
    try:
        output = run_git(["rev-list", "--left-right", "--count", "origin/main...HEAD"], cwd=cwd)
        behind, ahead = map(int, output.split())
        return ahead, behind
    except Exception:
        return None, None


def is_dirty(cwd=None):
    output = run_git(["status", "--porcelain"], cwd=cwd, check=False)
    return bool(output.strip())


def get_tracked_private_paths(cwd=None):
    """Return list of tracked files matching private patterns."""
    try:
        tracked = run_git(["ls-files"], cwd=cwd).splitlines()
    except Exception:
        return []
    bad = []
    for path in tracked:
        for priv in PRIVATE_PATHS:
            if priv.endswith("/"):
                if path.startswith(priv) or path.startswith(priv.rstrip("/")):
                    bad.append(path)
            elif "*" in priv:
                # Simple .env.* match
                if path.startswith(".env."):
                    bad.append(path)
            else:
                if path == priv or path.startswith(priv):
                    bad.append(path)
    return list(set(bad))


def check_fast_path_files(root: Path):
    missing = []
    for rel in FAST_PATH_FILES:
        if not (root / rel).exists():
            missing.append(rel)
    return missing


def validate(cwd=None, json_output=False):
    report = {
        "status": "PASS",
        "checks": {},
        "failures": [],
        "repo_root": None,
        "branch": None,
        "head_sha": None,
        "origin_main_sha": None,
        "ahead_behind": None,
        "dirty": None,
        "tracked_private": [],
        "missing_fast_path": [],
    }

    if not is_git_repo(cwd):
        report["status"] = "FAIL"
        report["failures"].append("Not inside a Git repository")
        if json_output:
            print(json.dumps(report, indent=2))
        else:
            print("FAIL: Not inside a Git repository")
        return 1

    root = Path(get_repo_root(cwd))
    report["repo_root"] = str(root)
    branch = get_current_branch(cwd)
    report["branch"] = branch
    report["head_sha"] = get_head_sha(cwd)
    report["origin_main_sha"] = get_origin_main_sha(cwd)
    ahead, behind = get_ahead_behind(cwd)
    report["ahead_behind"] = {"ahead": ahead, "behind": behind} if ahead is not None else None
    report["dirty"] = is_dirty(cwd)
    report["tracked_private"] = get_tracked_private_paths(cwd)
    report["missing_fast_path"] = check_fast_path_files(root)

    failures = []

    if branch == "main":
        failures.append("Current branch is main (must be l2/*)")

    if not branch.startswith("l2/"):
        failures.append(f"Branch '{branch}' does not start with l2/")

    if report["dirty"]:
        failures.append("Working tree is dirty (must be clean)")

    if report["missing_fast_path"]:
        failures.append(f"Missing fast-path files: {report['missing_fast_path']}")

    if report["tracked_private"]:
        failures.append(f"Private/runtime paths tracked: {report['tracked_private']}")

    if failures:
        report["status"] = "FAIL"
        report["failures"] = failures
        if json_output:
            print(json.dumps(report, indent=2))
        else:
            print("L2 MISSION PREFLIGHT: FAIL")
            for f in failures:
                print(f"  - {f}")
            print(f"Repo: {report['repo_root']}")
            print(f"Branch: {branch}")
            print(f"HEAD: {report['head_sha']}")
            if report["origin_main_sha"]:
                print(f"origin/main: {report['origin_main_sha']}")
            if report["ahead_behind"]:
                print(f"Ahead/Behind: {report['ahead_behind']['ahead']}/{report['ahead_behind']['behind']}")
            print(f"Dirty: {report['dirty']}")
        return 1

    report["status"] = "PASS"
    if json_output:
        print(json.dumps(report, indent=2))
    else:
        print("L2 MISSION PREFLIGHT: PASS")
        print(f"Repo root: {report['repo_root']}")
        print(f"Branch: {branch}")
        print(f"HEAD: {report['head_sha']}")
        if report["origin_main_sha"]:
            print(f"origin/main: {report['origin_main_sha']}")
        if report["ahead_behind"]:
            print(f"Ahead/Behind origin/main: {report['ahead_behind']['ahead']} / {report['ahead_behind']['behind']}")
        print(f"Dirty: {report['dirty']}")
        print("All fast-path files present.")
        print("No private/runtime paths tracked.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="L2 Mission Preflight Validator")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON")
    parser.add_argument("--cwd", default=None, help="Override working directory")
    args = parser.parse_args()

    cwd = args.cwd or os.getcwd()
    exit_code = validate(cwd=cwd, json_output=args.json)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
