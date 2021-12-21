from string import ascii_uppercase

with open('Elements.csv') as f:
    elements_split = f.read().split("\n")
    elements = []
    for x in elements_split:
        elements.append(x.split(",")[:7])


def get_element_mass(symbol: str):

    for element in elements:
        if symbol.lower() == element[2].lower() and symbol.lower() != 'symbol':
            return [float(element[3])] + [int(i) for i in element[4:]]


def separate_molecule(molecule: str):

    atoms = []
    prev = 0
    for index in range(len(molecule)):
        if molecule[index] in ascii_uppercase and index > 0:
            atoms.append(molecule[prev:index])
            prev = index
    atoms.append(molecule[prev:len(molecule)])
    return atoms


def get_mass(molecule: str):

    molecule = molecule.replace(" ", "")
    mass, neutrons, protons, electrons = 0, 0, 0, 0
    
    for atom in separate_molecule(molecule):

        symbol = ""
        number = ""
        for letter in atom:
            if letter not in [str(y) for y in range(10)]:
                symbol += letter
            else:
                number += letter
        if number == "":
            number = 1
        number = int(number)

        atom_mass, atom_neutrons, atom_protons, atom_electrons = get_element_mass(symbol)
        mass += atom_mass * number
        neutrons += atom_neutrons * number
        protons += atom_protons * number
        electrons += atom_electrons * number

    return round(mass, 3), neutrons, protons, electrons

