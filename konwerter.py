import json
import yaml
import sys
import xml.etree.ElementTree as El_Tree

def parse_arguments():
    if len(sys.argv) != 3:
        print("Nieprawidłowa liczba argumentów!")
        sys.exit(1)

    path_file1 = sys.argv[1]
    path_file2 = sys.argv[2]

    return path_file1, path_file2

def main():
    path_file1, path_file2 = parse_arguments()

    # Tutaj możesz umieścić pozostały kod dla Task1

if __name__ == '__main__':
    main()

def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {file_path}")
    except json.JSONDecodeError:
        print(f"Błąd dekodowania pliku JSON: {file_path}")

# Przykładowe użycie
file_path = "input.json"  # Ścieżka do pliku .json
data = load_json_file(file_path)
if data:
    print("Wczytano dane z pliku .json:")
    print(data)

def save_to_json(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Sposób użycia: program.py pathFile1.x pathFile2.y')
        print('gdzie x i y to jeden z formatów .xml, .json i .yml (.yaml).')
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Tutaj dodaj kod wczytujący dane z pliku o nazwie input_file
    # i zapisujący je do zmiennej data

    # Przykładowe dane
    data = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com'
    }

    # Zapis danych do pliku w formacie JSON
    save_to_json(data, output_file)
    print(f'Dane zostały zapisane do pliku {output_file} w formacie JSON.')

def load_yaml(input_file):
    with open(input_file, 'r') as f:
        data = yaml.safe_load(f)
    return data

def validate_yaml(data):
    # Tutaj dodaj kod weryfikujący poprawność składni danych w formacie YAML
    # Możesz wykorzystać odpowiednie walidatory lub instrukcje warunkowe

    # Przykładowa walidacja - sprawdzanie czy dane są słownikiem
    if not isinstance(data, dict):
        raise ValueError('Niepoprawna składnia pliku YAML. Oczekiwano słownika.')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Sposób użycia: program.py pathFile.y')
        print('gdzie y to format .yml (.yaml).')
        sys.exit(1)

    input_file = sys.argv[1]

    # Wczytanie danych z pliku YAML
    data = load_yaml(input_file)

    # Walidacja danych
    validate_yaml(data)

    print(f'Dane zostały wczytane z pliku {input_file} w formacie YAML.')

def save_yaml(data, output_file):
    with open(output_file, 'w') as f:
        yaml.dump(data, f)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Sposób użycia: program.py pathFile.y output_file.y')
        print('gdzie y to format .yml (.yaml).')
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Tutaj można dodać kod wczytujący dane, które mają zostać zapisane w formacie YAML

    # Przykładowe dane do zapisania
    data = {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }

    # Tutaj można dodać kod wykonujący operacje na danych przed zapisem

    # Zapis danych do pliku YAML
    save_yaml(data, output_file)

    print(f'Dane zostały zapisane do pliku {output_file} w formacie YAML.')
def load_xml(input_file):
    try:
        tree = El_Tree.parse(input_file)
        root = tree.getroot()
        return root
    except El_Tree.ParseError:
        print('Błąd parsowania pliku XML.')
        sys.exit(1)
    except FileNotFoundError:
        print('Plik XML nie istnieje.')
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Sposób użycia: program.py pathFile.xml')
        print('gdzie xml to format .xml.')
        sys.exit(1)

    input_file = sys.argv[1]

    # Wczytanie danych z pliku XML
    xml_data = load_xml(input_file)

    # Tutaj można dodać kod wykonujący operacje na wczytanych danych

    # Przykładowa weryfikacja poprawności składni XML
    if xml_data.tag != 'root':
        print('Niepoprawny format pliku XML.')
        sys.exit(1)

    print('Dane zostały wczytane z pliku XML i zweryfikowane poprawnie.')

def save_xml(output_file, xml_data):
    try:
        tree = El_Tree.ElementTree(xml_data)
        tree.write(output_file, encoding='utf-8', xml_declaration=True)
        print('Dane zostały zapisane do pliku XML:', output_file)
    except:
        print('Wystąpił błąd podczas zapisu do pliku XML.')
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Sposób użycia: program.py input.xml output.xml')
        print('gdzie input.xml to plik wejściowy w formacie .xml, a output.xml to plik wyjściowy.')
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Tutaj można dodać kod wczytujący dane do obiektu XML

    # Przykładowe dane w formacie XML
    xml_data = El_Tree.Element('root')
    child1 = El_Tree.SubElement(xml_data, 'child1')
    child1.text = 'Hello'
    child2 = El_Tree.SubElement(xml_data, 'child2')
    child2.text = 'World'

    # Tutaj można dodać kod wykonujący operacje na danych XML

    # Zapis danych do pliku XML
    save_xml(output_file, xml_data)
