#!/usr/bin/python3

from flask import Blueprint, render_template

bp = Blueprint('destinations', __name__)

@bp.route('/destinations', methods=['GET'])
def list_destinations():
    """Fetch destinations from database"""
    return render_template('destination_list.html', destinations=[])
