import sys

from subprocess import check_output
from textwrap import dedent


def test_no_blocklist_imports():
    check = """\
    import sys
    import panel

    blocklist = {"pandas"}
    mods = blocklist & set(sys.modules)

    if mods:
        print(", ".join(mods), end="")
    """

    output = check_output([sys.executable, '-c', dedent(check)])

    assert output == b""


def test_limited_panel_imports():
    check = """\
    import sys
    import panel

    found = {k for k in sys.modules if k.startswith("panel")}
    expected = {
        "panel",
        "panel.__version",
        "panel._version",
        "panel.config",
        "panel.depends",
        "panel.util",
        "panel.util.checks",
        "panel.util.parameters",
    }
    mods = found - expected
    if mods:
        print(", ".join(mods), end="")
    """

    output = check_output([sys.executable, '-c', dedent(check)])

    assert output == b""
