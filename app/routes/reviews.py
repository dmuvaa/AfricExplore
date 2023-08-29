#!/usr/bin/python3

from flask import Blueprint, render_template


bp = Blueprint('reviews', __name__)
@bp.route('/reviews', methods=['GET'])

def list_reviews():
    """fetch reviews from database"""
    return render_template('review_form.html', reviews=[])
