all_games = {
    'rows': 12,
    'columns': 12,
    'description': 'Main screen',
    'controls': [
        {
            'type': 'button',
            'name': 'start_game',
            'dimensions': (1, 1),
            'position': (1, 9),
            'text': 'Start',
            'key': pygame.K_a,
            'key_up': 'start_game'
        }, {
            'type': 'button',
            'name': 'settings',
            'dimensions': (1, 1),
            'position': (3, 9),
            'text': 'Settings',
            'key': pygame.K_b,
            'key_up': 'settings'
        }, {
            'type': 'button',
            'name': 'joystick_test',
            'dimensions': (1, 1),
            'position': (5, 9),
            'text': 'Joystick Test',
            'key': pygame.K_c,
            'key_up': 'joystick_test'
        }, {
            'type': 'button',
            'name': 'favourites',
            'dimensions': (1, 1),
            'position': (7, 9),
            'text': 'Favourites',
            'key': pygame.K_d,
            'key_up': 'favourites_list'
        }, {
            'type': 'button',
            'name': 'roms',
            'dimensions': (1, 1),
            'position': (9, 9),
            'text': 'ROMs',
            'key': pygame.K_e,
            'key_up': 'roms_list'
        }, {
            'type': 'list',
            'name': 'gamelist',
            'dimensions': (10, 7),
            'position': (1, 1),
            'data_source': 'game_list',
            'focused': True,
            'lines': 30
        }, {
            'type': 'container',
            'name': 'button_group',
            'dimensions': (10, 1),
            'position': (1, 11),
            'controls': [{
                'type': 'button',
                'name': 'group_button_one',
                'dimensions': (2, 1),
                'position': (0, 0),
                'text': 'Group button 1'
            }, {
                'type': 'button',
                'name': 'group_button_two',
                'dimensions': (2, 1),
                'position': (2, 0),
                'text': 'Group button 2'
            }]
        }
    ]
}
