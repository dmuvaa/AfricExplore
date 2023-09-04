#!/usr/bin/python3

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField, validators
from wtforms.validators import ValidationError
from datetime import date


class BookingForm(FlaskForm):
    class Meta:
        csrf = False

    city = StringField('City')
    
    start_date = DateField('Start Date', format='%Y-%m-%d', validators=[validators.DataRequired()])

    end_date = DateField('End Date', format='%Y-%m-%d', validators=[validators.DataRequired()])
    
    guests = IntegerField('Number of Guests', validators=[validators.NumberRange(min=1, message='Number of guests should be at least 1.')])
    children = IntegerField('Number of Children Under 13', validators=[validators.NumberRange(min=1, message='Number of children should be at least 1.')])
    
    submit = SubmitField('Search')

    def validate_start_date(form, field):
        if field.data < date.today():
            raise ValidationError('Start Date cannot be in the past.')
    
    def validate_end_date(form, field):
        if field.data < date.today():
            raise ValidationError('End Date cannot be in the past.')
        if form.start_date.data and field.data < form.start_date.data:
            raise ValidationError('End Date cannot be before the Start Date.')