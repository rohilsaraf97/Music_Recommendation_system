import urllib.request
import re
import random
import pandas as pd

def songPlayer(data):
    df = pd.DataFrame(
        {
            'songs': data['Song Name'].tolist()
        }
    )
    randomSong = df['songs'][random.randint(0, len(df) - 1)].replace(' ', '+')
    print(randomSong)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + randomSong)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print("https://www.youtube.com/watch?v=" + video_ids[0])
    return "https://www.youtube.com/watch?v=" + video_ids[0]
