# -*- coding: utf-8 -*-

data = {
    'ne': {
        'full': ('सोमवार', 'मगलवार', 'बुधवार', 'बिहिवार',
                 'शुक्रवार', 'शनिवार', 'आइतवार'),
        'short': ('सोम', 'मगल', 'बुध', 'बिहि', 'शुक्र', 'शनि', 'आइत'),
        'min': ('सो', 'म', 'बु', 'बि', 'शु', 'श', 'आ')
    },
    'en': {
        'full': ('Sombaar', 'Mangalbaar', 'Budhabaar', 'Bihibaar',
                 'Shukrabaar', 'Shanibaar', 'Aaitabaar'),
        'short': ('Som', 'Mangal', 'Budha', 'Bihi',
                  'Shukra', 'Shani', 'Aaita'),
        'min': ('So', 'Man', 'Bu', 'Bi', 'Shu', 'Sha', 'Aai')
    }
}


def get_nepday_of_week(inp, type='all', lang='ne'):
    '''Returns name of day of week in Nepali language.

    The index follows same format as python datetime.
    0 - Sombaar, ..., 6 - Aaitabaar
    '''
    if type == 'all':
        return {
            'full': data[lang]['full'][inp],
            'short': data[lang]['short'][inp],
            'min': data[lang]['min'][inp]
        }
    elif type == 'short':
        return data[lang]['short'][inp]
    elif type == 'min':
        return data[lang]['min'][inp]
    return data[lang]['full'][inp]
