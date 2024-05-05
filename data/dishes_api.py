import flask
from flask import jsonify


from data import db_session
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired



class DishesForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField("Содержание")
    is_private = BooleanField("Описание")
    submit = SubmitField('Применить')


blueprint = flask.Blueprint(
    'dishes_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/dishes')
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(DishesForm).all()
    return jsonify(
        {
            'dishes'    :
                [item.to_dict(only=('title', 'content', 'dishes.name'))
                 for item in news]
        }
    )