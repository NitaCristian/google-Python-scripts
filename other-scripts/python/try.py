def character_frequency(filename):
    try:
        file = open(filename)
    except OSError:
        return None

    frequcency = {}
    for line in file:
        for character in line:
            frequcency[character] = frequcency.get(character, 0) + 1

    file.close()
    return frequcency
