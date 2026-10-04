import json

import cards
import objectives

FIXTURE = """\
                                             3.1.1          SECURITY REQUIREMENT
                                                            Limit system access to authorized users.
                                             ASSESSMENT OBJECTIVE
                                             Determine if:
                                             3.1.1[a]     authorized users are identified.
      a
      v                                      3.1.1[b]     processes acting on behalf of authorized users are
      ai                                                  identified.
                                             POTENTIAL ASSESSMENT METHODS AND OBJECTS
                                             Examine: [SELECT FROM: Access control policy].
CHAPTER THREE                                                                          PAGE 10
NIST SP 800-171A          ASSESSING SECURITY REQUIREMENTS FOR CONTROLLED UNCLASSIFIED INFORMATION
_________________________________________________________________________________________
                                             3.1.3[c]    designated sources and destinations are
CHAPTER THREE                                                                          PAGE 11
NIST SP 800-171A          ASSESSING SECURITY REQUIREMENTS FOR CONTROLLED UNCLASSIFIED INFORMATION
_________________________________________________________________________________________
                                                         identified.
                                             POTENTIAL ASSESSMENT METHODS AND OBJECTS
                                             3.13.11        SECURITY REQUIREMENT
                                             Employ FIPS-validated cryptography when used to protect the
                                             confidentiality of CUI.
                                             ASSESSMENT OBJECTIVE
                                             Determine if FIPS-validated cryptography is employed to protect the
                                             confidentiality of CUI.
                                             POTENTIAL ASSESSMENT METHODS AND OBJECTS
      r                                     SECURITY REQUIREMENT
      g                      3.5.4
      e fr
                                            Employ replay-resistant authentication mechanisms for
      s                                     all accounts.
      o m
                                            ASSESSMENT OBJECTIVE
                                            Determine if replay-resistant authentication mechanisms are
                                            implemented.
                                            POTENTIAL ASSESSMENT METHODS AND OBJECTS
      d                                    3.12.2[a]     deficiencies are identified. ____________________
      oi
                                                         a plan of action is developed to correct
      10.                                  3.12.2[b]     identified deficiencies.
                                           3.12.2[c]     the plan of action is implemented.
                                            POTENTIAL ASSESSMENT METHODS AND OBJECTS
"""


def test_vertically_centred_id_takes_the_line_above_it():
    objs = objectives.parse(FIXTURE)["objectives"]
    assert objs["3.12.2[a]"] == "deficiencies are identified."
    assert objs["3.12.2[b]"] == "a plan of action is developed to correct identified deficiencies."
    assert objs["3.12.2[c]"] == "the plan of action is implemented."


def test_control_number_on_the_line_below_its_heading():
    parsed = objectives.parse(FIXTURE)
    assert parsed["requirements"]["3.5.4"] == \
        "Employ replay-resistant authentication mechanisms for all accounts."
    assert parsed["objectives"]["3.5.4"] == \
        "replay-resistant authentication mechanisms are implemented."
    assert "3.13.11" in parsed["objectives"] and "3.13.11[a]" not in parsed["objectives"]


def test_no_control_has_both_a_bare_and_a_lettered_objective():
    objs = objectives.load()["objectives"]
    lettered = {o.split("[")[0] for o in objs if "[" in o}
    assert not lettered & {o for o in objs if "[" not in o}


def test_parse_lettered_objectives_with_continuations_and_margin_noise():
    objs = objectives.parse(FIXTURE)["objectives"]
    assert objs["3.1.1[a]"] == "authorized users are identified."
    assert objs["3.1.1[b]"] == "processes acting on behalf of authorized users are identified."


def test_page_headers_do_not_leak_into_objective_text():
    assert objectives.parse(FIXTURE)["objectives"]["3.1.3[c]"] == \
        "designated sources and destinations are identified."


def test_single_objective_control_uses_the_control_number():
    parsed = objectives.parse(FIXTURE)
    assert parsed["objectives"]["3.13.11"] == \
        "FIPS-validated cryptography is employed to protect the confidentiality of CUI."
    assert parsed["requirements"]["3.13.11"] == \
        "Employ FIPS-validated cryptography when used to protect the confidentiality of CUI."
    assert parsed["requirements"]["3.1.1"] == "Limit system access to authorized users."


# ---- the committed list, built from the NIST PDF ---------------------------

FAMILY_CONTROLS = {1: 22, 2: 3, 3: 9, 4: 9, 5: 11, 6: 3, 7: 6,
                   8: 9, 9: 2, 10: 6, 11: 3, 12: 4, 13: 16, 14: 7}


def test_committed_list_has_all_110_controls_and_320_objectives():
    data = objectives.load()
    assert len(data["requirements"]) == 110
    assert len(data["objectives"]) == 320
    per_family = {}
    for ctl in data["requirements"]:
        fam = int(ctl.split(".")[1])
        per_family[fam] = per_family.get(fam, 0) + 1
    assert per_family == FAMILY_CONTROLS


def test_every_objective_belongs_to_a_known_control_and_is_valid():
    data = objectives.load()
    for oid, text in data["objectives"].items():
        assert cards.valid_objective(oid), oid
        assert oid.split("[")[0] in data["requirements"], oid
        assert text and "PAGE" not in text and "ASSESSING SECURITY" not in text, oid
        assert "__" not in text and text.endswith("."), oid
    for ctl, text in data["requirements"].items():
        assert text.endswith(".") and text[0].isupper(), (ctl, text)


def test_known_objective_texts():
    objs = objectives.load()["objectives"]
    assert objs["3.5.6[a]"] == "a period of inactivity after which an identifier is disabled is defined."
    assert objs["3.5.6[b]"] == "identifiers are disabled after the defined period of inactivity."
    assert objs["3.13.11"].startswith("FIPS-validated cryptography is employed")


def test_committed_list_records_its_source():
    src = objectives.load()["source"]
    assert src["title"].startswith("NIST SP 800-171A")
    assert len(src["sha256"]) == 64


# ---- coverage ---------------------------------------------------------------

def test_coverage_splits_objectives_by_card(tmp_path):
    (tmp_path / "SOME_CARD.md").write_text(
        "default_repair: none\nobjectives: 3.5.6[a], 3.5.6[b]\n---\nx\n")
    cov = objectives.coverage(tmp_path)
    assert cov["covered"]["3.5.6[a]"] == ["SOME_CARD"]
    assert "3.5.6[a]" not in cov["uncovered"]
    assert len(cov["covered"]) + len(cov["uncovered"]) == 320
