'''
Instagram bot, primary reason:
1) Post random motivation photos at edugated page
2) 
'''


import webbrowser as wb

#wb.open("https://www.instagram.com/edugated/?hl=en" ) # professional profile
wb.open("https://www.instagram.com/khanshariqahmed/?hl=en") # personal profile


from instapy_cli import client

username = 'khanshariqahmed'
password = 'Shariqkhan29!!'
image = r'C:\Users\srkst\Desktop\project\python_practice\flaskenv\seleniumpy\photo.jpg'


# To add direct post to instagram
'''
text = 'This will be the caption of your photo.' + '\r\n' + 'You can also use hashtags! #hash #tag #now'

with client(username, password) as cli:
    cli.upload(image, text)

'''

with client(username, password) as cli:
    cli.upload(image, story=True) # add photo to story

