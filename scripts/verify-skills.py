#!/usr/bin/env python3
"""
verify-skills.py — Claude Design-Skill Registry Verification Script
Checks that all expected registry files, skill directories, and raw URLs are accessible.
Usage: python3 scripts/verify-skills.py
"""

import os
import sys
import json
import urllib.request
import urllib.error

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED_FILES = [
    "sources/design-skill-urls.txt",
    "registries/design-skills.json",
    "registries/design-skills.md",
    "registries/design-skills.csv",
    "registries/raw-links.md",
    "reports/install-plan.md",
    "reports/manual-review.md",
    "reports/rejected-risk.md",
    "reports/reference-only.md",
    "reports/dedupe-map.md",
    "reports/token-minimization-plan.md",
    "reports/rollback-plan.md",
    "reports/inspection-log.md",
    "scripts/verify-skills.py",
]

REQUIRED_SKILL_DIRS = [
    ("skills/frontend-design/frontend-design", "LINK_ONLY"),
    ("skills/frontend-design/canvas-design", "LINK_ONLY"),
    ("skills/frontend-design/design-taste-frontend", "COPY_ALLOWED"),
    ("skills/frontend-design/interface-design", "COPY_ALLOWED"),
    ("skills/brand-guidelines/brand-guidelines", "LINK_ONLY"),
    ("skills/accessibility/accessibility", "COPY_ALLOWED"),
    ("skills/motion/design-motion-principles", "COPY_ALLOWED"),
    ("skills/motion/remotion-video-creation", "COPY_ALLOWED"),
    ("skills/design-systems/design-system", "COPY_ALLOWED"),
    ("skills/marketing-design/creative-direction", "COPY_ALLOWED"),
    ("skills/skill-development/skill-development", "LINK_ONLY"),
]

RAW_URLS_TO_CHECK = [
    ("frontend-design", "https://raw.githubusercontent.com/anthropics/claude-code/main/plugins/frontend-design/skills/frontend-design/SKILL.md"),
    ("brand-guidelines", "https://raw.githubusercontent.com/anthropics/skills/main/skills/brand-guidelines/SKILL.md"),
    ("canvas-design", "https://raw.githubusercontent.com/anthropics/skills/main/skills/canvas-design/SKILL.md"),
    ("design-taste-frontend", "https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md"),
    ("interface-design", "https://raw.githubusercontent.com/Dammyjay93/interface-design/main/.claude/skills/interface-design/SKILL.md"),
    ("design-motion-principles", "https://raw.githubusercontent.com/kylezantos/design-motion-principles/main/skills/design-motion-principles/SKILL.md"),
    ("accessibility", "https://raw.githubusercontent.com/addyosmani/web-quality-skills/main/skills/accessibility/SKILL.md"),
    ("remotion-video-creation", "https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/skills/remotion-video-creation/SKILL.md"),
    ("creative-direction", "https://raw.githubusercontent.com/rampstackco/claude-skills/main/skills/creative-direction/SKILL.md"),
    ("design-system", "https://raw.githubusercontent.com/rampstackco/claude-skills/main/skills/design-system/SKILL.md"),
]


def check_file(rel_path):
    full_path = os.path.join(REPO_ROOT, rel_path)
    if not os.path.isfile(full_path):
        return False, f"MISSING: {rel_path}"
    size = os.path.getsize(full_path)
    if size == 0:
        return False, f"EMPTY: {rel_path}"
    return True, f"OK ({size} bytes): {rel_path}"


def check_skill_dir(rel_dir, copy_type):
    full_dir = os.path.join(REPO_ROOT, rel_dir)
    skill_md = os.path.join(full_dir, "SKILL.md")
    metadata = os.path.join(full_dir, "source-metadata.json")
    errors = []

    if not os.path.isdir(full_dir):
        return False, f"MISSING DIR: {rel_dir}"
    if not os.path.isfile(skill_md):
        errors.append(f"MISSING SKILL.md in {rel_dir}")
    if not os.path.isfile(metadata):
        errors.append(f"MISSING source-metadata.json in {rel_dir}")

    if errors:
        return False, "; ".join(errors)

    # For COPY_ALLOWED, verify SKILL.md is not a stub (should have real content)
    if copy_type == "COPY_ALLOWED":
        with open(skill_md) as f:
            content = f.read()
        if "See canonical source" in content and len(content) < 200:
            errors.append(f"WARN: {rel_dir}/SKILL.md looks like a stub but copy_type is COPY_ALLOWED")

    # Validate source-metadata.json is valid JSON
    with open(metadata) as f:
        try:
            data = json.load(f)
            required_fields = ["skill_name", "source_url", "raw_url", "decision", "license_status"]
            for field in required_fields:
                if field not in data:
                    errors.append(f"MISSING field '{field}' in {rel_dir}/source-metadata.json")
        except json.JSONDecodeError as e:
            errors.append(f"INVALID JSON in {rel_dir}/source-metadata.json: {e}")

    if errors:
        return False, "; ".join(errors)
    return True, f"OK: {rel_dir}/"


def check_url(name, url, timeout=10):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "verify-skills/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status == 200:
                content_length = len(resp.read())
                return True, f"OK ({content_length} bytes): {name}"
            return False, f"HTTP {resp.status}: {name} — {url}"
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}: {name} — {url}"
    except Exception as e:
        return False, f"ERROR: {name} — {e}"


def main():
    passed = 0
    failed = 0
    warnings = []

    print("=" * 60)
    print("Claude Design-Skill Registry — Verification Report")
    print("=" * 60)
    print()

    # 1. Required files
    print("── Required Files ──────────────────────────────────────")
    for rel_path in REQUIRED_FILES:
        ok, msg = check_file(rel_path)
        symbol = "✓" if ok else "✗"
        print(f"  {symbol} {msg}")
        if ok:
            passed += 1
        else:
            failed += 1
    print()

    # 2. Skill directories
    print("── Skill Directories ───────────────────────────────────")
    for rel_dir, copy_type in REQUIRED_SKILL_DIRS:
        ok, msg = check_skill_dir(rel_dir, copy_type)
        symbol = "✓" if ok else "✗"
        print(f"  {symbol} {msg}")
        if "WARN" in msg:
            warnings.append(msg)
        if ok:
            passed += 1
        else:
            failed += 1
    print()

    # 3. Raw URL accessibility
    print("── Raw URL Checks ──────────────────────────────────────")
    print("  (skipping URL checks by default — pass --check-urls to enable)")
    if "--check-urls" in sys.argv:
        for name, url in RAW_URLS_TO_CHECK:
            ok, msg = check_url(name, url)
            symbol = "✓" if ok else "✗"
            print(f"  {symbol} {msg}")
            if ok:
                passed += 1
            else:
                failed += 1
    else:
        print("  To verify raw URLs are accessible:")
        print("  python3 scripts/verify-skills.py --check-urls")
    print()

    # 4. JSON registry validation
    print("── Registry JSON Validation ────────────────────────────")
    registry_path = os.path.join(REPO_ROOT, "registries/design-skills.json")
    if os.path.isfile(registry_path):
        try:
            with open(registry_path) as f:
                registry = json.load(f)
            install_now = [s for s in registry if s.get("decision") == "INSTALL_NOW"]
            install_opt = [s for s in registry if s.get("decision") == "INSTALL_OPTIONAL"]
            manual = [s for s in registry if s.get("decision") == "MANUAL_REVIEW"]
            skips = [s for s in registry if s.get("decision") == "SKIP"]
            print(f"  ✓ Valid JSON: {len(registry)} candidates total")
            print(f"    INSTALL_NOW: {len(install_now)}")
            print(f"    INSTALL_OPTIONAL: {len(install_opt)}")
            print(f"    MANUAL_REVIEW: {len(manual)}")
            print(f"    SKIP: {len(skips)}")
            passed += 1
        except json.JSONDecodeError as e:
            print(f"  ✗ INVALID JSON in registries/design-skills.json: {e}")
            failed += 1
    else:
        print("  ✗ registries/design-skills.json not found")
        failed += 1
    print()

    # Summary
    print("=" * 60)
    total = passed + failed
    if failed == 0:
        print(f"ALL CHECKS PASSED ({passed}/{total})")
        if warnings:
            print(f"Warnings ({len(warnings)}):")
            for w in warnings:
                print(f"  ⚠ {w}")
    else:
        print(f"FAILURES: {failed}/{total} checks failed")
        print(f"Passed: {passed}")
    print("=" * 60)

    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
