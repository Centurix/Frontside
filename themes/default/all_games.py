all_games = {
    'rows': 12,
    'columns': 12,
    'description': 'Main screen',
    'controls': [
        {
            'type': 'button',
            'name': 'start_game',
            'width': 2,
            'height': 1,
            'top': 1,
            'left': 1,
            'text': 'Start',
            'key': pygame.K_a,
            'key_up': 'start_game'
        }, {
            'type': 'button',
            'name': 'settings',
            'width': 2,
            'height': 1,
            'top': 1,
            'left': 4,
            'text': 'Settings',
            'key': pygame.K_b,
            'key_up': 'settings'
        }, {
            'type': 'list',
            'name': 'gamelist',
            'width': 6,
            'height': 6,
            'top': 3,
            'left': 0
        }, {
            'type': 'container',
            'name': 'button_group',
            'width': 10,
            'height': 1,
            'top': 5,
            'left': 1,
            'controls': [{
                'type': 'button',
                'name': 'group_button_one',
                'width': 100,
                'height': 50,
                'top': 1,
                'left': 1,
                'text': 'Group button 1'
            }, {
                'type': 'button',
                'name': 'group_button_two',
                'width': 100,
                'height': 50,
                'top': 1,
                'left': 3,
                'text': 'Group button 2'
            }]
        }
    ]
}
