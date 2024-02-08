

def custom_search(input_text):
    first_space_index = input_text.find(' ')
    where_to_search = input_text[:first_space_index]
    what_to_search = input_text[first_space_index+1:]

    search_keywords_urls = {
        'wrd':'https://en.wiktionary.org/wiki/',
        'wik':'https://en.m.wikipedia.org/wiki/',
        'yt':'https://www.youtube.com/results?search_query=',
        'map':'https://www.google.com/maps/search/',
        'amz':'https://www.amazon.ca/s?k=',
        'lyr':'https://genius.com/search?q=', # doesn't work
        'ef':'https://www.wordreference.com/enfr/',
        'fe':'https://www.wordreference.com/fren/',
        'eg':'https://www.wordreference.com/engr/',
        'ge':'https://www.wordreference.com/gren/',
        'εα':'https://www.wordreference.com/gren/',
        'goog':'https://www.google.com/search?q=',
        'cgpt':'handled in shortcuts app'
    }

    if where_to_search not in search_keywords_urls:
        where_to_search = 'goog'
        what_to_search = input_text

    space_separators = {
        'yt': '+',
        'map':'%20',
        'amz':'+',
        'ef':'%20',
        'fe':'%20',
        'eg':'%20',
        'ge':'%20',
        'εα':'%20',
        'goog':'+'
    }
    space_separator = space_separators.get(where_to_search)
    if not space_separator: space_separator = '_'
    formatted_search_term = what_to_search.replace(' ', space_separator)

    # add Reddit

    url = search_keywords_urls.get(where_to_search) + formatted_search_term

    return url