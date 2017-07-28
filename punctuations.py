# -*- coding: utf-8 -*-

NON_STOPS = list((
    # Fullwidth ASCII variants
    u'\uFF02\uFF03\uFF04\uFF05\uFF06\uFF07\uFF08\uFF09\uFF0A\uFF0B\uFF0C\uFF0D'
    u'\uFF0F\uFF1A\uFF1B\uFF1C\uFF1D\uFF1E\uFF20\uFF3B\uFF3C\uFF3D\uFF3E\uFF3F'
    u'\uFF40\uFF5B\uFF5C\uFF5D\uFF5E\uFF5F\uFF60'

    # Halfwidth CJK punctuation
    u'\uFF62\uFF63\uFF64'

    # CJK symbols and punctuation
    u'\u3000\u3001\u3003'

    # CJK angle and corner brackets
    u'\u3008\u3009\u300A\u300B\u300C\u300D\u300E\u300F\u3010\u3011'

    # CJK brackets and symbols/punctuation
    u'\u3014\u3015\u3016\u3017\u3018\u3019\u301A\u301B\u301C\u301D\u301E\u301F'

    # Other CJK symbols
    u'\u3030'

    # Special CJK indicators
    u'\u303E\u303F'

    # Dashes
    u'\u2013\u2014'

    # Quotation marks and apostrophe
    u'\u2018\u2019\u201B\u201C\u201D\u201E\u201F'

    # General punctuation
    u'\u2026\u2027'

    # Overscores and underscores
    u'\uFE4F'

    # Small form variants
    u'\uFE51\uFE54'

    # Latin punctuation
    u'\u00B7'
))

#: A string of Chinese stops.
STOPS = list((
    u'\uFF01'  # Fullwidth exclamation mark
    u'\uFF1F'  # Fullwidth question mark
    u'\uFF61'  # Halfwidth ideographic full stop
    u'\u3002'  # Ideographic full stop
))


