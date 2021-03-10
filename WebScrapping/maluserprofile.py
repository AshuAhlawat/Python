from bs4 import BeautifulSoup
import requests

def clicked(username):
    try:
        # GET REQUEST TO SITE
        r_completed = requests.get("https://myanimelist.net/profile/"+username)
        
                                # USER INFO SCRAPPING
        soup = BeautifulSoup(r_completed.text, 'lxml')

        #user personal data
        match_user_data = soup.find_all('span', class_='user-status-data')
        #user's friends
        match_friends_data = soup.find('a', class_="fl-r fs11 fw-n ff-Verdana")
        #user profile pic
        match_user_img = soup.find('img', class_="lazyload")['data-src']

        r = requests.get(match_user_img)
        with open("pp.jpg","wb") as f:
            f.write(r.content)
        
        # USER INFO POST
        try:
            user_info = {
                "user" : username,
                "pp" : match_user_img,
                "last_online" : match_user_data[0].text,
                "sex" : match_user_data[1].text,
                "birthday" : match_user_data[2].text,
                "joined" : match_user_data[4].text,
                "forum_posts" : match_user_data[5].text,
                "reviews" : match_user_data[6].text,
                "recommendations" : match_user_data[7].text,
                "friends" : match_friends_data.text,
            }
        except:
            user_info = {
                "user" : username,
                "pp" : match_user_img,
                "last_online" : match_user_data[0].text,
                "sex" : "Not Defined",
                "birthday" : match_user_data[1].text,
                "joined" : match_user_data[3].text,
                "forum_posts" : match_user_data[4].text,
                "reviews" : match_user_data[5].text,
                "recommendations" : match_user_data[6].text,
                "friends" : match_friends_data.text,
            }

                                # ANIME_INFO_DATA

        #days watched
        match_anime_days = soup.find('div',class_='stat-score').div.span.next_element.next_element
        #mean rating
        match_anime_mean = soup.find('span', class_='score-label').text
        #viewed status of anime
        match_anime_status = soup.find_all('li', class_='clearfix mb12')
        #viewed anime stats
        match_anime_stats = soup.find_all('span', class_='di-ib fl-r')
        
        #recent anime list
        try:
            match_anime_recent_ = soup.find('div',class_='updates anime')
            match_anime_recent = match_anime_recent_.find_all('a',class_='')
            recent_list=[]
            for match in match_anime_recent:
                recent_list.append(match.text)
        except:
            recent_list=[]

        #favourite anime list
        try:
            match_anime_favorite_ = soup.find('ul',class_='favorites-list anime')
            match_anime_favorite = match_anime_favorite_.find_all('div',class_='di-tc va-t pl8 data')
            favorite_list = []
            for match in match_anime_favorite:
                favorite_list.append(match.a.text)
        except :
            favorite_list = []

        #favorite characters list
        try:
            match_anime_character_ = soup.find('ul',class_="favorites-list characters")
            match_anime_character = match_anime_character_.find_all('div', class_='di-tc va-t pl8 data')
            character_list=[]
            for match in match_anime_character:
                character_list.append(match.a.text)
        except :
            character_list=[]

        #ANIME INFO POST
        anime_info = {
            "watching" : match_anime_status[0].span.text,
            "completed" : match_anime_status[1].span.text,
            "on_hold" : match_anime_status[2].span.text,
            "dropped" : match_anime_status[3].span.text,
            "plan_to_watch" : match_anime_status[4].span.text,
            "total" : match_anime_stats[0].text,
            "rewatched" : match_anime_stats[1].text,
            "episodes" : match_anime_stats[2].text,
            "days" : match_anime_days,
            "mean" : match_anime_mean,
            "recents" : recent_list,
            "favourites" : favorite_list,
            "characters" : character_list
        }

        #days manga read
        match_manga_days = soup.find('div', class_='stats manga').div.div.span.next_sibling
        #mean manga score
        match_manga_mean = soup.find('div', class_='stats manga').div.div.next_sibling.next_sibling.span.next_sibling.next_sibling.text
        
        #favourite manga list
        try:
            match_manga_favorite_ = soup.find('ul',class_='favorites-list manga')
            match_manga_favorite = match_manga_favorite_.find_all('div',class_='di-tc va-t pl8 data')
            favorite_list = []
            for match in match_manga_favorite:
                favorite_list.append(match.a.text)
        except :
            favorite_list = []
        
        #recent manga list
        try:
            match_manga_recent_ = soup.find('div', class_='updates manga')
            match_manga_recent = match_manga_recent_.find_all('a', class_="")
            recent_list=[]
            for match in match_manga_recent:
                recent_list.append(match.text)
        except:
            recent_list=[]
            
        manga_info = {
            "reading" : match_anime_status[8].span.text,
            "completed" : match_anime_status[9].span.text,
            "on_hold" : match_anime_status[10].span.text,
            "dropped" : match_anime_status[11].span.text,
            "plan_to_watch" : match_anime_status[12].span.text,
            "total" : match_anime_stats[3].text,
            "reread" : match_anime_stats[4].text,
            "chapters" : match_anime_stats[5].text,
            "volumes" : match_anime_stats[6].text,
            "days" : match_manga_days,
            "mean" : match_manga_mean,
            "recent" : recent_list,
            "favourite" : favorite_list
        }

        all_data={"user_info" : user_info, "anime_info" : anime_info, "manga_info" : manga_info}
        return all_data

    except:
        
        print("ERROR OCCURED")
        
        user_info = {
            "user" : "DOESNOTEXIST",
            "pp" : "",
            "last_online" : "",
            "sex" : "",
            "birthday" : "",
            "joined" : "",
            "forum_posts" : "",
            "reviews" : "",
            "recommendations" : "",
            "friends" : ""
        }
        anime_info = {
            "watching" : '',
            "completed" : '',
            "on_hold" :'',
            "dropped" :'',
            "plan_to_watch" :'',
            "total" : '',
            "rewatched" : '',
            "episodes" : '',
            "days" :'',
            "mean" :'',
            "recents" :'',
            "favourites" : '',
            "characters" : ''
        }
        manga_info = {
            "reading" :'',
            "completed" :'',
            "on_hold" : '',
            "dropped" : '',
            "plan_to_watch" : '',
            "total" :'',
            "reread" :'',
            "chapters" :'',
            "volumes" :'',
            "days" :'',
            "mean" :'',
            "recent" :'',
            "favourite" : '',
        }
        
        all_data={"user_info" : user_info, "anime_info" : anime_info, "manga_info" : manga_info}
        return all_data

    
username = str(input("ENTER USERNAME : "))
data = clicked(username)

print(data)