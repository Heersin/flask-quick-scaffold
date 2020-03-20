from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class ClientForm(FlaskForm):
    contact = StringField('联系方式', validators=[DataRequired(message='邮箱手机皆可，不可为空')])
    index1 = StringField('指标1')
    gender = SelectField('性别', choices=[('female','女'),('male','男')],
                        validators=[DataRequired(message='不能为空')])
    status = BooleanField('是否患病',default=False)
    submit = SubmitField('提交测试')
    
