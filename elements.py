def calculate_modifier(e1, e2):
    if e1 == 'ice':
        if e2 == 'fire':
            return 0.5
        if e2 == 'nature':
            return 2
        return 1
    if e1 == 'fire':
        if e2 == 'nature':
            return 2
        if e2 == 'ice':
            return 0.5
    if e1 == 'nature':
        if e2 == 'ice':
            return 2
        if e2 == 'fire':
            return 0.5

ice_adjectives = [
    'Glacial',
    'Frozen',
    'Chilled',
    'Arctic'
]

fire_adjectives = [
    'Burning',
    'Searing',
    'Charred',
    'Infernal'
]

nature_adjectives = [
    'Earthen',
    'Druidic',
]
elements = {
    'ice': ice_adjectives,
    'fire': fire_adjectives,
    'nature': nature_adjectives
}
