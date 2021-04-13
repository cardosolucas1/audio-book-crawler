import json


def capture_audios(path):
    audios_names = []
    with open(path) as file:
        for line in file:
            formattedLine = line.strip("\n")
            audios_names.append({"name": formattedLine, "url": ""})
    return audios_names


def get_volumes_by_level(level):
    volumes = []
    for volume in range(1, 5):
        volumes.append(dict({
            "nome":  'Volume {}'.format(volume),
            "slug": 'volume-{}'.format(volume),
            "audios": capture_audios(
            "wetransfer-a1cb7d/audios/{}ano/volume{}/volume-{}.txt"
            .format(level, volume, volume)
        )}))
    return volumes


def create_audio_book_data():
    volumes_by_level = []
    for level in range(1, 6):
        volumes_by_level.append(dict({
            "ano": "{}º ano".format(level),
            "slug": "{}-ano".format(level),
            "order": 0,
            "volumes": get_volumes_by_level(level)
        }))
    return volumes_by_level


def export_list_as_json(lista):
    with open('audio_book_data.json', 'w') as f:
        return json.dump(lista, f, ensure_ascii=False)


export_list_as_json(create_audio_book_data())