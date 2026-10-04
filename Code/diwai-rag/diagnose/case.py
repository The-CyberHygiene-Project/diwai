"""The case record: everything one diagnosis saw and said (the later email feature reads it)."""
import json
import time
from pathlib import Path


def write_case(base, data, forms_text):
    case = Path(base) / time.strftime("%Y%m%d-%H%M%S")
    n = 1
    while case.exists():                      # two runs in one second get separate folders
        n += 1
        case = Path(base) / (time.strftime("%Y%m%d-%H%M%S") + f"-{n}")
    case.mkdir(parents=True)
    (case / "case.json").write_text(json.dumps(data, indent=1, default=str))
    (case / "forms.txt").write_text(forms_text)
    return case
