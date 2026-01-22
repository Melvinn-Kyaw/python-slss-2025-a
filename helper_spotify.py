import csv

def songs_by_artist(file_path: str, artist: str) -> list[list[str]]:
    artist_col = 5

    songs = []


    with open(file_path) as f:
        _ = f.readline()

        r = csv.reader(f)

        for info in r:
            if info[artist_col] == artist:
                songs.append(info)

def track_search(file_path: str, word: str) -> list[list[str]]:
    trackname_col = 0

    songs = []

    with open(file_path) as f:
        _ = f.readline()

        r = csv.reader(f)

        for info in r:
            track_name = info[trackname_col]
            track_tokens = [token.lower().strip("[](),./?! ") track_name.strip().split(" ")]

            if word in track_tokens:
                songs.append(info)

    return songs

def string_to_num(s: str) -> int:
    return int(s.replace(',', '')) if s else 0
