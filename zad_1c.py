import re

text = "Lorem ipsum dolor sit amet, consectetur; adipiscing elit. Sed eget mattis sem. Mauris egestas erat quam, " \
       "ut faucibus eros congue et. \n" \
       " In blandit, mi eu porta; lobortis, tortor nisl facilisis leo, at tristique augue " \
       "risus eu risus. "


def punctuation(string_text):
    new = re.sub(r'[^\w\s]', '', string_text)
    return new


print(punctuation(text))
