def current_datetime():
    import datetime
    return str(datetime.datetime.now())[:19]
def current_date():
    import datetime
    return str(datetime.datetime.now())[:10]
def current_date_long():
    import datetime
    return datetime.datetime.now().strftime('%B %d, %Y')
def personal_Zoom_room_link():
    with open('credentials.txt') as f:
        #second line is the Zoom link
        link = f.readlines()[1].split('=')[1].strip()
    return link

commands_for_snippets = {
    "@dt": current_datetime,
    "@day": current_date,
    "@dtl": current_date_long,
    "@Zoomroom": personal_Zoom_room_link
}

# other ideas:
"""

"""