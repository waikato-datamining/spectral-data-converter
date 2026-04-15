from typing import List, Dict


def list_classes() -> Dict[str, List[str]]:
    return {
        "seppl.io.Reader": [
            "kasperl.reader",
            "sdc.reader",
        ],
        "seppl.io.DirectReader": [
            "sdc.reader",
        ],
        "seppl.io.Filter": [
            "kasperl.filter",
            "sdc.filter",
        ],
        "seppl.io.Writer": [
            "kasperl.writer",
            "sdc.writer",
        ],
        "seppl.io.DirectWriter": [
            "sdc.writer",
        ],
        "kasperl.api.Generator": [
            "kasperl.generator",
        ],
        "kasperl.api.DataFormatter": [
            "sdc.dataformatter",
        ],
        "sdc.api.Cleaner": [
            "sdc.cleaner",
        ],
    }
