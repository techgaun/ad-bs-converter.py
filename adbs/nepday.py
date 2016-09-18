# -*- coding: utf-8 -*-

data = {
    'ne': {
        'full': ('आइतवार', 'सोमवार', 'मगलवार', 'बुधवार',
                 'बिहिवार', 'शुक्रवार', 'शनिवार'),
        'short': ('आइत', 'सोम', 'मगल', 'बुध', 'बिहि', 'शुक्र', 'शनि'),
        'min': ('आ', 'सो', 'म', 'बु', 'बि', 'शु', 'श')
    },
    'en': {
        'full': ('Aaitabaar', 'Sombaar', 'Mangalbaar', 'Budhabaar',
                 'Bihibaar', 'Shukrabaar', 'Shanibaar'),
        'short': ('Aaita', 'Som', 'Mangal', 'Budha',
                  'Bihi', 'Shukra', 'Shani'),
        'min': ('Aai', 'So', 'Man', 'Bu', 'Bi', 'Shu', 'Sha')
    }
}


def get_nepday_of_week(inp, type='all', lang='ne'):
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
