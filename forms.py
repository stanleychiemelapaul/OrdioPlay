from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import URL


class VideosLinkForm(Form):
    
    video_link = StringField(
        'video_link', validators=[URL()]
     )


