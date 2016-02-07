settings = {
    'rows': 12,
    'columns': 12,
    'description': 'Settings screen',
    'controls': [
        {
            'type': 'button',
            'name': 'start_scanner',
            'dimensions': (2, 1),
            'position': (1, 1),
            'text': 'Scan ROMs',
            'key': pygame.K_a,
            'key_up': 'start_scanner'
        },
        {
            'type': 'button',
            'name': 'redefine_keys',
            'dimensions': (2, 1),
            'position': (4, 1),
            'text': 'Redefine keys',
            'key': pygame.K_b,
            'key_up': 'redefine_keys'
        },
        {
            'type': 'label',
            'name': 'rom_path_label',
            'dimensions': (2, 1),
            'position': (1, 3),
            'text': 'ROM Path:'
        },
        {
            'type': 'text',
            'name': 'rom_path',
            'dimensions': (3, 1),
            'position': (4, 3),
            'key': pygame.K_c
        }
    ]
}
