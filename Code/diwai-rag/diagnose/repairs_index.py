"""Which repairs may be offered for which finding: approved (diwai-repair list) AND made for
that finding (the repair's own CARD). Repair files are read with ast, never executed."""
import ast
from pathlib import Path


def approved_ids(list_output):
    out = set()
    for line in (list_output or "").splitlines():
        parts = line.split()
        if len(parts) == 2 and parts[1] == "approved":
            out.add(parts[0])
    return out


def _constant(tree, name):
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == name for t in node.targets):
            if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                return node.value.value
    return None


def cards_of(installed_dir):
    out = {}
    for p in sorted(Path(installed_dir).glob("*.py")):
        try:
            tree = ast.parse(p.read_text())
        except (OSError, SyntaxError, ValueError):
            continue
        rid, card = _constant(tree, "ID"), _constant(tree, "CARD")
        if rid and card:
            out[rid] = card
    return out


def allowed_repairs(installed_dir, list_output):
    ok = approved_ids(list_output)
    result = {}
    for rid, card in cards_of(installed_dir).items():
        if rid in ok:
            result.setdefault(card, []).append(rid)
    return result
