from flask import Blueprint, render_template, redirect, request, flash, url_for
from Calc40000.CalcData import Weapon, Target
from Calc40000.Calc import Calculator
from dacite import from_dict

calc_server = Blueprint('calc_server', __name__)


@calc_server.route('/calc', methods=["POST", "GET"])
def calc_engine():

    if request.method == "POST":
        c = Calculator()
        req = request.form
        temp_wep = {
            "bs": int(req.get("bs")),
            "n_shots": int(req.get("n_shots")),
            "strength": int(req.get("strength")),
            "ap": int(req.get("ap")),
            "dmg": int(req.get('dmg')),
            "h_mod": int(req.get("h_mod")),
            "w_mod": int(req.get("w_mod"))
        }
        temp_target = {
            "toughness": int(req.get("toughness")),
            "save": int(req.get("save")),
            "inv": int(req.get("inv")),
            "wounds": int(req.get("wounds"))
        }

        h_rerolls = req.get('h_rerolls')
        w_rerolls = req.get("w_rerolls")
        weapon = from_dict(data=temp_wep, data_class=Weapon)
        target = from_dict(data=temp_target, data_class=Target)
        result = c.calculate(target, weapon, h_rerolls, w_rerolls)
        flash(result)
        return redirect(url_for('calc_server.calc_engine'))
    return render_template('calc_form.html')
