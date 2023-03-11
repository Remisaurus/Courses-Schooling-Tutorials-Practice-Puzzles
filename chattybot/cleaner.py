import re

def remove_chat_metadata(chat_export_file):
    date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"  # e.g. "9/16/22, 06:34"
    dash_whitespace = r"\s-\s"  # " - "
    username = r"([\w\s]+)"  # e.g. "Remi"
    metadata_end = r":\s"  # ": "
    pattern = date_time + dash_whitespace + username + metadata_end
    emoji_pattern = re.compile("["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                u"\U00002702-\U000027B0"
                u"\U000024C2-\U0001F251"
                u"\U0001f926-\U0001f937"
                u'\U00010000-\U0010ffff'
                u"\u200d"
                u"\u2640-\u2642"
                u"\u2600-\u2B55"
                u"\u23cf"
                u"\u23e9"
                u"\u231a"
                u"\u3030"
                u"\ufe0f"
                 "]+", flags=re.UNICODE)
    
    with open(chat_export_file, "r", encoding='utf8') as corpus_file:
        content = corpus_file.read()
    no_emoji = emoji_pattern.sub(r'', content) # no emoji
    cleaned_corpus = re.sub(pattern, "", no_emoji)
    dezenogeven = list(cleaned_corpus.split("\n"))
    while '' in dezenogeven:
        dezenogeven.remove('')
    while ' ' in dezenogeven:
        dezenogeven.remove(' ')
    return dezenogeven 

def remove_non_message_text(export_text_lines):
    messages = []
    filter_out_msgs = ['<Media omitted>', 'terry', 'Terry', 'TERRY', 'Yorick', 'yorick', 'YORICK', 'tomas', 'Tomas', 'TOMAS', 'Remi', 'remi', 'REMI', 'nigel', 'Nigel', 'NIGEL', 'Bart', 'bart', 'BART', 'Maarten', 'maarten', 'MAARTEN', 'martijn', 'Martijn', 'MARTIJN', 'baldwin', 'Baldwin', 'BALDWIN', 'joeri', 'Joeri', 'JOERI', 'Roel', 'roel', 'ROEL', 'Boris', 'boris', 'dwayne', 'Lyr', 'Kara', 'kara', 'Nanda', 'nanda', 'https://', 'mama', 'Mama', 'mamma', 'Mamma', 'mam', 'Mam', 'pappa', 'Pappa', 'papa', 'Papa', 'oma', 'Oma', 'opa', 'Opa', 'Elvin', 'elvin', 'juana', 'Juana', 'aming', 'Aming', 'liming', 'Liming', 'Elia', 'elia', 'straat', 'bolle', 'Bolle', 'lea', 'Lea', 'meijer', 'Meijer', 'Youtube', 'youtube', 'raym', 'Raym', 'nan', 'bor', 'Wouter']
    for every in export_text_lines:
        x = 0
        for all in filter_out_msgs:
            if all in every:
                x += 1
        if x == 0:
            messages.append(every)
        else:
            continue
    return tuple((msg for msg in messages))

def clean_corpus(chat_export_file):
    message_corpus = remove_chat_metadata(chat_export_file)
    cleaned_corpus = remove_non_message_text(message_corpus)
    return cleaned_corpus
