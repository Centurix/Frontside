joystick_test = {
    'rows': 12,
    'columns': 12,
    'description': 'Joystick test',
    'controls': [
        {
            'type': 'button',
            'name': 'up',
            'dimensions': (1, 1),
            'position': (2, 1),
            'text': 'Up',
            'key': pygame.K_UP
        }, {
            'type': 'button',
            'name': 'down',
            'dimensions': (1, 1),
            'position': (2, 3),
            'text': 'Down',
            'key': pygame.K_DOWN
        }, {
            'type': 'button',
            'name': 'left',
            'dimensions': (1, 1),
            'position': (1, 2),
            'text': 'Left',
            'key': pygame.K_LEFT
        }, {
            'type': 'button',
            'name': 'right',
            'dimensions': (1, 1),
            'position': (3, 2),
            'text': 'Right',
            'key': pygame.K_RIGHT
        }
    ]
}
