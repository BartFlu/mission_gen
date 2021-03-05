from flask import Blueprint, render_template


b_contact_terrain = Blueprint('contact_terrain', __name__)


@b_contact_terrain.route('/terrainHelper')
def terrain_helper_view():
    return render_template('terrain.html')


@b_contact_terrain.route('/contact')
def contact_view():
    return render_template('contact_view.html')
