

def create_instructions(input_text):
    first_space_index = input_text.find(' ')
    where_to_search = input_text[:first_space_index]
    what_to_search = input_text[first_space_index+1:]

    search_keywords_urls = {
        'wrd':'https://en.wiktionary.org/wiki/',
        'wik':'https://en.m.wikipedia.org/wiki/',
        'yt':'https://www.youtube.com/results?search_query=',
        'map':'https://www.google.com/maps/search/',
        'amz':'https://www.amazon.ca/s?k=',
        'lyr':'https://genius.com/search?q=',
        'ef':'https://www.wordreference.com/enfr/',
        'fe':'https://www.wordreference.com/fren/',
        'eg':'https://www.wordreference.com/engr/',
        'ge':'https://www.wordreference.com/gren/',
        'εα':'https://www.wordreference.com/gren/',
        'goog':'https://www.google.com/search?q=',
        'red': 'https://www.reddit.com/search/?q=',
        'gh':'https://github.com/search?q=',
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
        'goog':'+',
        'red':'+',
        'gh':'+'
    }
    space_separator = space_separators.get(where_to_search)
    if not space_separator: space_separator = '_'
    formatted_search_term = what_to_search.replace(' ', space_separator)
    # check which actually need a space separator. I think some can just have a space in the URL be automatically converted to %20

    if where_to_search == 'red':
        formatted_search_term = formatted_search_term + '&include_over_18=1'

    url = search_keywords_urls.get(where_to_search) + formatted_search_term

    return url

def run_search(input_text):
    url = create_instructions(input_text)
    import webbrowser
    webbrowser.open(url)

if __name__ == "__main__":
    input_text = input("Enter search term: ")
    url = create_instructions(input_text)
    print(url)
    import webbrowser
    webbrowser.open(url)