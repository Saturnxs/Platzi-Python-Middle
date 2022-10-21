DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    # A list comprehension that is filtering the list of workers and returning only the ones that have
    # python as their language.
    all_pythons_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    
    # Filtering the list of workers and returning only the ones that have Platzi as their
    # organization.
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    
    # Filtering the list of workers and returning only the ones that have more than 18 years old.
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    
    #old_people = list(filter(lambda worker: worker["age"] > 70, DATA))
    # Adding a new key to the dictionary called `old` and setting it to `True` if the worker is older
    # than 70 years old.
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    
    
    print("Python devs: ")
    for worker in all_pythons_devs:
        print(worker)
        
    print("Platzi workers: ")
    for worker in all_platzi_workers:
        print(worker)
        
    print("Adults: ")
    for worker in adults:
        print(worker)
        
    print("Old people: ")
    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    run()