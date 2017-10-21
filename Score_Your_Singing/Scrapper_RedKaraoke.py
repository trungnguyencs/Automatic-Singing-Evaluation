import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
from time import clock

pages_to_scrape = 500
master_page = 'https://www.redkaraoke.com/karaoke/celine-dion/my-heart-will-go-on/11827/'
basePlayerUrl = "https://www.redkaraoke.com";
baseS3Url = "https://s3.amazonaws.com/";
#js file: https://d4rgvppl55fks.cloudfront.net/es/js/playerRecs.js

links_list = []
for i in range(pages_to_scrape):
    r = requests.get(master_page + 'recordings/p' + str(i))
    soup = BeautifulSoup(r.content, 'html.parser')
    for link in soup.find_all('a', attrs = {'class':'result result-recording'}):
        links_list.append('https://www.redkaraoke.com' + link.get('href'))
# Remove duplicated links
links_list_unique = set(links_list)

print(len(links_list))
print(len(links_list_unique))

def extractUserRecording(soup):
# Localize data in "userRecording" object
    pattern = re.compile(r"userRecording")
    data = soup.find('script', text=pattern)

    pattern = re.compile(r"userRecording\.([a-zA-Z0-9]+)=([^;]+);")
    data = soup.find('script', text=pattern)
    ur_string = re.findall(r"userRecording\.([a-zA-Z0-9]+)=([^;]+);",str(data))
    ur_dict = dict(ur_string)
    for key in ur_dict.keys():
        ur_dict[key] = ur_dict[key][1:-1]
    return ur_dict 

def getDownloadLink(ur_dict):
    isDueto = False

    if 'isDueto' in ur_dict.keys(): 
        isDueto = True
    else:
        isDueto = False

    if ur_dict['file'][-1] == '3':
        if ur_dict['lang'] == 'es':
            if isDueto:
                filepath = basePlayerUrl + "/data/duets/mp3/es/"
            elif 's3' in ur_dict.keys():
                filepath = baseS3Url + "redkaraoke/data/mp3/"
            else:
                filepath = basePlayerUrl + "/data/mp3/es/"
        elif ur_dict['lang'] == 'jp':
            if isDueto:
                filepath = basePlayerUrl + "/data/duets/mp3/jp/"
            elif 's3' in ur_dict.keys():
                filepath = baseS3Url + "redkaraokejp/data/mp3/"
            else:
                filepath = baseS3Url + "/data/mp3/jp/"
        else:
            if isDueto:
                filepath = basePlayerUrl + "/data/duets/mp3/en/"
            elif 's3' in ur_dict.keys():
                filepath = baseS3Url + "redkaraokecom/data/mp3/"
            else:
                filepath = basePlayerUrl + "/data/mp3/en/"
    else:
        if ur_dict['lang'] == 'es':
            if isDueto:
                filepath = basePlayerUrl + "/data/duets/vid/es/"
            elif 'isDueto' in ur_dict.keys():
                filepath = baseS3Url + "redkaraoke/data/vid/"
            else:
                filepath = basePlayerUrl + "/data/vid/es/"
        elif ur_dict['lang'] == 'jp':
            if isDueto:
                filepath = basePlayerUrl + "/data/duets/vid/jp/"
            elif 's3' in ur_dict.keys():
                filepath = baseS3Url + "redkaraokejp/data/vid/"
            else:
                filepath = baseS3Url + "/data/vid/jp/"
        else:
            if isDueto:
                filepath = basePlayerUrl + "/data/duets/vid/en/"
            elif 's3' in ur_dict.keys():
                filepath = baseS3Url + "redkaraokecom/data/vid/"
            else:
                filepath = basePlayerUrl + "/data/vid/en/"
    download_link = filepath + ur_dict['file']
    return download_link

counter = 0

#Initialize lists
view_list = []
like_list = []
comment_list = []
recording_list = []
follower_list = []
following_list = []
date_list = []
gender_loc_list = []

location_list = []
user_avatar_list = []
user_group_list = []
# song_id_list = []
user_name_list = []
language_list = []
song_title_list = []
artist_list = []
download_link_list = []
recording_link_list = []

# Send request for each link in links_list_unique
for link_sub in links_list_unique:
    r = requests.get(link_sub)
    soup = BeautifulSoup(r.content, 'lxml')
    
    try:
        counter = counter + 1
        
        # Extract information from html code:
        view = int(soup.find('li', attrs = {'class':'rec-views'}).text)
        like = soup.find('li', attrs = {'class':'rec-likes'}).text
        comment = int(soup.find('li', attrs = {'class':'rec-comments'}).text)
        recording = int(soup.find('li', attrs = {'class':'tam1'}).find('strong').text)
        follower = int(soup.find_all('ul', attrs = {'class':'stats'})[0].find_all('li')[5].find('strong').text)
        following = (soup.find_all('ul', attrs = {'class':'stats'})[0].find_all('li')[6].find('strong').text)
        date = soup.find_all('div', attrs = {'class':'infoTema_textoBlanco'})[2].text[3:]
        gender_loc = soup.find('div', attrs = {'class':'userdata'}).find('p').text

        recording_link = link_sub

        ur_dict = extractUserRecording(soup)
        download_link = getDownloadLink(ur_dict)
        print(download_link)
        
        location = ur_dict['loc']
        user_avatar = ur_dict['uavatar']
        user_group = ur_dict['ugroup']
#         song_id = ur_dict['sid']
        user_name = ur_dict['u']
        language = ur_dict['lang']
        song_title = ur_dict['title']
        artist = ur_dict['a']
                
    except (IndexError, AttributeError) as e:
        continue
        
    view_list.append(view)
    like_list.append(like)
    comment_list.append(comment)
    recording_list.append(recording)
    follower_list.append(follower)
    following_list.append(following)
    date_list.append(date)
    gender_loc_list.append(gender_loc)
    
    location_list.append(location)
    user_avatar_list.append(user_avatar)
    user_group_list.append(user_group)
#     song_id_list.append(song_id)
    user_name_list.append(user_name)
    language_list.append(language)
    song_title_list.append(song_title)
    artist_list.append(artist)
    download_link_list.append(download_link)
    recording_link_list.append(recording_link)

    print(counter)

print(len(view_list))

d = {'no_of_views': view_list, 'no_of_likes': like_list, 'no_of_comments': comment_list, 
     'no_of_recordings': recording_list, 'no_of_followers': follower_list, 'no_of_following': following_list,
     'date_recorded': date_list, 'gender + location': gender_loc_list, 
     'location': location_list, 'user_avatar': user_avatar_list, 'user_group': user_group_list,
     'user_name': user_name_list, 'language': language_list, 'song_title': song_title_list, 
     'artist': artist_list, 'download_link': download_link_list, 'recording_link': recording_link_list}

df = pd.DataFrame(data=d)

df.to_csv('./data/out.csv',index=False)