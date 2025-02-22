{% extends "base.html" %} {% block result %}
<div class="">
    <img src="../static/img/logo.png" alt="" class="" />
    <h1>Succesful</h1>
    <h2>Thank you!</h2>
</div>

<div style="text-align: center;">
    <table style="border-style: solid; border-color: black; text-align: left; width: 766px; height: 60px; background-color: rgb(238, 238, 238);" cellpadding="2" cellspacing="2">
        <tbody>
            <tr>
                <td style="vertical-align: top;">Serial Number<br>
                </td>
                <td style="vertical-align: top;">Account Number<br>
                </td>
                <td style="vertical-align: top;">Name<br>
                </td>
                <td style="vertical-align: top;">Units Held<br>
                </td>
                <td style="vertical-align: top;">Right Due<br>
                </td>
                <td style="vertical-align: top;">Amount<br>
            </tr>

            <tr>
                <td style="vertical-align: top;">{{session.get('SN')}} <br>
                </td>
                <td style="vertical-align: top;">{{session.get('ACNO')}}<br>
                </td>
                <td style="vertical-align: topnam;">{{session.get('NAME')}}<br>
                </td>
                <td style="vertical-align: top;">{{session.get('UNIT_HELD')}}<br>
                </td>
                <td style="vertical-align: top;">{{session.get('RIGHT_DUE')}}<br>
                </td>
                <td style="vertical-align: top;">{{session.get('AMOUNT')}}<br>
            </tr>
            <div>
            </div>
        </tbody>
    </table>
    <br>
    <p><br>
        <table style="border-style: solid; border-color: black; text-align: left; width: 766px; height: 60px; background-color: rgb(238, 238, 238);" cellpadding="2" cellspacing="2">
            <tbody>
                <tr>
                    </td>
                    <td style="vertical-align: top;">Number of ordinary<br>shares accepted<br>
                    </td>
                    <td style="vertical-align: top;">Additional ordinary<br>shares applied for:<br>
                    </td>
                </tr>
                <tr>
                    <form method="post" action="{{url_for('acceptance')}}">
                        </td>
                        <td style="vertical-align: top;"><input value="{{session.get('RIGHT_APPLIED')}}" name="applied"><br>
                        </td>
                        <td style="vertical-align: top;"><input value="{{session.get('ADDITIONAL')}}" name="additional"><br>
                        </td>
                        <td> <input name="submit" value="submit" type="submit">
                        </td>
                    </form>
                </tr>
            </tbody>
        </table>
    </p>
</div>
<div>

</div>
{% endblock %}