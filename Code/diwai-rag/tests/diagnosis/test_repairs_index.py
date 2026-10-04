from diagnose.repairs_index import allowed_repairs, approved_ids

LIST = ("owui-cors-any-origin         approved\n"
        "wazuh-ruleset-missing        Repair 'wazuh-ruleset-missing' has changed since it was approved. It must be approved again.\n")


def test_only_approved_lines_count():
    assert approved_ids(LIST) == {"owui-cors-any-origin"}


def test_allowed_needs_both_approval_and_matching_card(tmp_path):
    (tmp_path / "owui_cors_any_origin.py").write_text('ID = "owui-cors-any-origin"\nCARD = "OPEN_WEBUI_ACCEPTS_ANY_ORIGIN"\n')
    (tmp_path / "wazuh_ruleset_missing.py").write_text('ID = "wazuh-ruleset-missing"\nCARD = "WAZUH_CUSTOM_RULES_NOT_LOADED"\n')
    assert allowed_repairs(tmp_path, LIST) == {"OPEN_WEBUI_ACCEPTS_ANY_ORIGIN": ["owui-cors-any-origin"]}


def test_repair_file_is_never_executed(tmp_path):
    (tmp_path / "evil.py").write_text('import os; os.system("touch PWNED")\nID = "evil"\nCARD = "X"\n')
    allowed_repairs(tmp_path, "evil approved\n")
    assert not (tmp_path / "PWNED").exists()


def test_missing_folder_or_empty_list_offers_nothing(tmp_path):
    assert allowed_repairs(tmp_path / "nope", "owui-cors-any-origin approved\n") == {}
    assert allowed_repairs(tmp_path, "") == {}


def test_real_installed_repairs_are_read():
    from pathlib import Path
    inst = Path("/usr/local/lib/diwai-repair/repairs")
    if inst.is_dir():
        got = allowed_repairs(inst, "owui-cors-any-origin approved\nwazuh-ruleset-missing approved\n")
        assert got.get("OPEN_WEBUI_ACCEPTS_ANY_ORIGIN") == ["owui-cors-any-origin"]
