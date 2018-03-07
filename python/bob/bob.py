def hey(phrase):
    phrase = phrase.strip()
    if len(phrase)<1:
        return "Fine. Be that way!"
    if phrase.isupper() and phrase[-1] == '?':
        return "Calm down, I know what I'm doing!"
    elif phrase.isupper():
        return "Whoa, chill out!"
    elif phrase[-1] == '?':
        return "Sure."
    else:
        return "Whatever."
