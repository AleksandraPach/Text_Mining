import re

hashtag = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
       "Sed #texting eget mattis sem. Mauris #frasista egestas erat #tweetext quam, \n" \
       "ut faucibus eros #frasier congue et. In blandit, mi eu porta lobortis, tortor nisl facilisis leo, " \
       "at tristique #frasistas augue risus eu risus. "


def hashtag_function(string):
    new = re.findall('#', string)
    return new


print(hashtag_function(hashtag))
