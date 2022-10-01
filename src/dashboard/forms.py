from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import StringField, SelectField, TextAreaField, \
                           RadioField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Optional, Length

class Music(FlaskForm):
    music_img = FileField(label='Upload cover image', validators=[FileRequired(),
                                                                  FileAllowed(['jpg', 'jpeg', 'png', 'svg'])
                                                                  ])
    music_name = StringField(validators=[DataRequired(), Length(4, 30)])
    music_file = FileField(label='Song file', validators=[FileRequired(),
                                                          FileAllowed(['mp3', 'mp4', 'm4a', 'flac',
                                                                       'wav', 'wma', 'aac'])
                                                          ])
    artist = StringField(validators=[DataRequired(), Length(4, 25)])
    composer = StringField(validators=[DataRequired(), Length(4, 25)])
    lyricist = StringField(validators=[DataRequired(), Length(4, 25)])
    music_director = StringField(validators=[DataRequired(), Length(4, 25)])
    category = SelectField(choices=[('hip hop', 'Hip Hop'), ('pop', 'Pop'), ('rock', 'Rock')],
                           validators=[DataRequired()])
    lyrics = TextAreaField(validators=[DataRequired()])
    free_or_paid = RadioField(choices=[('free', 'Free'), ('paid', 'Paid')], validators=[DataRequired()])
    music_price = IntegerField(validators=[Optional()])
    submit = SubmitField('add music')