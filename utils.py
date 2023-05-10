# utilities.py

def id_stat_list(player, stat):
    """ Create the list [player: {'id': player.id, 'first name': 
        player.firstname, 'last name': player.lastname,  'position': player.position},
         'stat': stat]
    """


    player = {'ID': player['ID'], 'First Name': player['First Name'], 
            'Last Name': player['Last Name'], 'Position': player['Position']}

    try:
        if player['Stats'][stat]:
            b = int(player['Stats'][stat])

    except KeyError:
        b = 0

    return {'player': player, 'stat': b}







