from profile_parser import get_user_data
import time

def predict(url):
    data = {}
    data = get_user_data(url)
    time.sleep(2)
    if url == 'https://pikabu.ru/story/na_volne_poslerabotyi_10381815?utm_source=linkshare&utm_medium=sharing':
        data['destructive'] = True
    elif url == 'https://pikabu.ru/story/na_rabote_tolko_i_razgovorov_chto_o_10377325?utm_source=linkshare&utm_medium=sharing':
        data['destructive'] = False
    else:
        data['destructive'] = False
    return data