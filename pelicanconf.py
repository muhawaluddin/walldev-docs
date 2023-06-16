AUTHOR = 'Wall'
SITENAME = 'Walldev Docs'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Makassar'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Walldev', 'https://walldev.netlify.com/'),
         ('Muh Awaluddin', 'https://muhawaluddin.netlify.com/'),
         )

# Social widget
SOCIAL = (('Facebook', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "output/theme/pelican-alchemy/alchemy"

SITESUBTITLE = "Isinya Documentasi"
SITEIMAGE= "theme/images/LOGO.png"

THEME_CSS_OVERRIDES = ['theme/pelican-alchemy/alchemy/static/css/oldstyle.css']