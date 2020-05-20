# 65. Valid Number
#
# Validate if a given string can be interpreted as a decimal number.
#
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false
#
# Note: It is intended for the problem statement to be ambiguous. You should gather all
# requirements up front before implementing one. However, here is a list of characters
# that can be in a valid decimal number:
#
# Numbers 0-9
# Exponent - "e"
# Positive/negative sign - "+"/"-"
# Decimal point - "."
# Of course, the context of these characters also matters in the input.

import testlib


class Solution:
    states = {
        "empty": {
            "terminal": False,
            "transitions": {
                " ": "empty",
                "-": "sign",
                "+": "sign",
                "0": "int_part",
                "1": "int_part",
                ".": "decimal",
            },
        },
        "sign": {
            "terminal": False,
            "transitions": {"0": "int_part", "1": "int_part", ".": "decimal"},
        },
        "int_part": {
            "terminal": True,
            "transitions": {
                " ": "trailing_whitespace",
                "0": "int_part",
                "1": "int_part",
                ".": "int_decimal",
                "e": "exponent",
            },
        },
        "decimal": {
            "terminal": False,
            "transitions": {"0": "frac_part", "1": "frac_part"},
        },
        "int_decimal": {
            "terminal": True,
            "transitions": {
                " ": "trailing_whitespace",
                "0": "frac_part",
                "1": "frac_part",
                "e": "exponent",
            },
        },
        "frac_part": {
            "terminal": True,
            "transitions": {
                " ": "trailing_whitespace",
                "0": "frac_part",
                "1": "frac_part",
                "e": "exponent",
            },
        },
        "exponent": {
            "terminal": False,
            "transitions": {
                "-": "neg_exponent",
                "+": "pos_exponent",
                "0": "exp_part",
                "1": "exp_part",
            },
        },
        "neg_exponent": {
            "terminal": False,
            "transitions": {"0": "exp_part", "1": "exp_part"},
        },
        "pos_exponent": {
            "terminal": False,
            "transitions": {"0": "exp_part", "1": "exp_part"},
        },
        "exp_part": {
            "terminal": True,
            "transitions": {
                " ": "trailing_whitespace",
                "0": "exp_part",
                "1": "exp_part",
            },
        },
        "trailing_whitespace": {
            "terminal": True,
            "transitions": {" ": "trailing_whitespace"},
        },
    }

    def isNumber(self, s: str) -> bool:
        state_name = "empty"
        for c in s:
            if c in "123456789":
                c = "1"
            if c not in self.states[state_name]["transitions"]:
                return False
            state_name = self.states[state_name]["transitions"][c]
        return self.states[state_name]["terminal"]


if __name__ == "__main__":
    testdata = [
        ("0", True),
        (" 0.1 ", True),
        ("abc", False),
        ("1 a", False),
        ("2e10", True),
        (" -90e3   ", True),
        (" 1e", False),
        ("e3", False),
        (" 6e-1", True),
        (" 99e2.5 ", False),
        ("53.5e93", True),
        (" --6 ", False),
        ("-+3", False),
        ("95a54e53", False),
        ("01", True),
        ("1.", True),
        (".", False),
        ("2e0", True),
        ("3. ", True),
        ("-01", True),
        ("-01 ", True),
        ("+.8", True),
        ("46.e8", True),
        (" 005047e+6", True),
        ("4e+", False),
        ("166e-02767", True),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().isNumber(tc[0]), tc[1], tc), testdata
    )
