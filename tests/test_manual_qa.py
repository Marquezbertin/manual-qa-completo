"""Offline tests for the manual-qa-completo repository.

These tests verify the integrity of the manual itself (all modules present
in PT and EN) and exercise small, dependency-free QA helpers used as
examples in the modules.
"""
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODULES = [f"{n:02d}" for n in range(1, 12)]


def test_all_modules_have_pt_and_en():
    for mod in MODULES:
        pt = os.path.join(REPO_ROOT, mod, "PT", "indice.md")
        en = os.path.join(REPO_ROOT, mod, "EN", "index.md")
        assert os.path.isfile(pt), f"Missing {pt}"
        assert os.path.isfile(en), f"Missing {en}"


def test_module_03_has_estimate_example():
    path = os.path.join(REPO_ROOT, "03", "PT", "indice.md")
    content = open(path, encoding="utf-8").read()
    # 3-point estimate formula check from module 03
    assert "(3 + 4×5 + 10) / 6 = 5,5" in content


def test_module_06_api_script_present():
    path = os.path.join(REPO_ROOT, "06", "scripts", "test_api.py")
    assert os.path.isfile(path)


def test_readme_lists_all_modules():
    path = os.path.join(REPO_ROOT, "README.PT-BR.md")
    content = open(path, encoding="utf-8").read()
    for mod in MODULES:
        assert f"`{mod}`" in content, f"README missing module {mod}"


def test_three_point_estimate_helper():
    def estimate(ot, rl, ps):
        return (ot + 4 * rl + ps) / 6

    assert estimate(3, 5, 10) == 5.5
