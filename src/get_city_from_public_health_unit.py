def get_city_from_public_health_unit(public_health_unit):
    # http://www.health.gov.on.ca/en/common/system/services/phu/locations.aspx
    if 'Ajax' in public_health_unit:
        return 'Ajax'
    if 'Algoma' in public_health_unit:
        return 'Sault Ste. Marie'
    if 'Brant' in public_health_unit:
        return 'Brantford'
    if 'Chatham' in public_health_unit:
        return 'Chatham'
    if 'Durham' in public_health_unit:
        return 'Whitby'
    if 'Eastern Ontario' in public_health_unit:
        return 'Cornwall'
    if 'Grand River Hospital' in public_health_unit:
        return 'Kitchener'
    if 'Grey Bruce' in public_health_unit:
        return 'Owen Sound'
    if 'Haliburton' in public_health_unit:
        return 'Port Hope'
    if 'Halton' in public_health_unit:
        return 'Oakville'
    if 'Hamilton' in public_health_unit:
        return 'Hamilton'
    if 'Hastings' in public_health_unit:
        return 'Belleville'
    if 'Huron Perth' in public_health_unit:
        return 'Stratford'
    if 'Kingston' in public_health_unit:
        return 'Kingston'
    if 'London' in public_health_unit:
        return 'London'
    if 'Mackezie' in public_health_unit:
        return 'Richmond Hill'
    if 'Mississauga' in public_health_unit:
        return 'Mississauga'
    if 'Mount Sinai' in public_health_unit:
        return 'Toronto'
    if 'Niagara' in public_health_unit:
        return 'Niagara'
    if 'Northwestern' in public_health_unit:
        return 'Kenora'
    if 'North York' in public_health_unit:
        return 'Toronto'
    if 'Ottawa' in public_health_unit:
        return 'Ottawa'
    if 'Peel' in public_health_unit:
        return 'Peel'
    if 'Peterborough' in public_health_unit:
        return 'Peterborough'
    if 'Porcupine' in public_health_unit:
        return 'Timmins'
    if 'Simcoe' in public_health_unit:
        return 'Simcoe'
    if 'Scarborough' in public_health_unit:
        return 'Scarborough'
    if 'Southlake' in public_health_unit:
        return 'Newmarket'
    if 'Sudbury' in public_health_unit:
        return 'Sudbury'
    if 'Sunnybrook' in public_health_unit:
        return 'Toronto'
    if 'Toronto' in public_health_unit:
        return 'Toronto'
    if 'Waterloo' in public_health_unit:
        return 'Waterloo'
    if 'Wellington Dufferin Guelph' in public_health_unit:
        return 'Guelph'
    if 'Windsor' in public_health_unit:
        return 'Windsor'
    if 'York' in public_health_unit:
        return 'York'

    return public_health_unit
