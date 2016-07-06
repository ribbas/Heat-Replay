from re import compile

# ----------------- Local variables ----------------- #

__reCompiles = []


# ----------------- Global methods ----------------- #

def compileTitleRe():
    """Generates and compiles regex patterns"""

    rePats = [
        r'[\{\(\[].*?[\)\]\}/\\]',
        r'^.*?\(',
        r'[\)\]\}\-\'\"\,:]',
        r'\s+'
    ]

    __reCompiles.extend([compile(pat) for pat in rePats])


def regexify(title):
    """Applies regular expression methods and trims whitespace to the specified
    format

    title: the string to be regexified
    """

    return __reCompiles[3].sub(  # replace multiple \s with one \s
        ' ', __reCompiles[2].sub(  # replace excess punctuations with one \s
            '', __reCompiles[1].sub(  # remove everything before '('
                '', __reCompiles[0].sub(  # remove everything between brackets
                    '', title.lower()  # convert to lower case first
                )
            )
        ).rstrip().lstrip()  # strip whitespace from beginning and end only
    )
