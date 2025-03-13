from enum import Enum

class LocationModifier(Enum):
    exact_match = "="
    regex_match_case_sensitive = "~"
    regex_match_case_insensitive = "~*"
    no_regex_match = "^~"
