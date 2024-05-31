#checks if a page exists
import requests

def is_404(url):
    try:
        response = requests.get(url)
        #print(response.status_code)
        return response.status_code == 404
    except requests.ConnectionError:
        print("failed to connect to url")
        return False

# usage
# url = "https://mangapill.com/chapters/1063-20202500/dragon-ball-chapter-202.5"
# if is_404(url):
#     print(f"{url} is a 404")
# else:
#     print(f"{url} is not a 404")

def check_chapter(row_data):
    url="https://mangapill.com/chapters/"+str(row_data[0])+"-"+str(row_data[1])+str(row_data[2])+str(row_data[3])+"00"  #
    if not is_404(url):
        print(url)
        return True
    else:
        return False

    