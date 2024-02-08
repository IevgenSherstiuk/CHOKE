info_page1 = """Inductor calculator
for operating conditions with DC magnetization.
    """

info_page2 = """Allows calculating the optimal dimensions of the toroidal core and the number of wire turns based on material prices.

• "Bluish" - the lowest price;

• "Green" - up to 150% of the lowest price;

• "Yellow" - up to 300% of the lowest price;

• "Red" - above 300% of the lowest price.
    """

ENG = {
    'params':{
        'title':'Other parameters',
        'language': ' Language',
####################
        'Core_params':'Core Parameters',
        'Core_paramsInfo':
        """
        • Ferromagnetic filling factor - is defined as the ratio of the volume of the entire material to the volume of the ferromagnetic material" is correct (from 0 to 1)
        
        • Density relates to the ferromagnetic material
        """,
        'Bmax':'Operating induction, T',
        'Kf':'Flling factor',
        'qf':'Density, g/cm³',
####################
        'Wire_params':'Wire Parameters',
        'Wire_paramsInfo':
        """
        • Packing factor of wire: from 0 to 1

        • Resistivity of wire material (for copper: 0.0172, aluminum: 0.028)
        """,
        'J':'Current density, A/mm²',
        'dw':'Wire diameter, mm',
        'nw':'Strands',
        'Kw':'Packing factor',
        'qw':'Density, g/cm³',
        'rw':'Resistivity, Ohm·mm²/m',
####################
        'Materials_cost':'Price per kg',
        'Materials_costInfo':
        """
        • Ferromagnetic and wire cost per 1 kg in any currency
        """,
        'Uf':'Ferromagnetic, $',
        'Uw':'Wire, $',
####################
        'Limits_params':'Limitations',
        'Limits_paramsInfo':
        """
        • These parameters allow limiting the inner diameter of the core (leave 0 for no limitation), the outer diameter (must be specified), and the maximum number of turns (default is 10000)
        """,
        'dmin':'Min. inner diameter, mm',
        'Dmax':'Max. outer diameter, mm',
        'Nmax':'Max. wire turns',},

    'main':{
        'title':'Inductor Calculator',
        'info1': info_page1,
        'info2': info_page2,
        'L':'Inductance, mH',
        'I':'Current, A',
        'table_name': 'Inductor winding table',
        'H_axis': 'Core Height, mm',
        'input_H': ' Height value, mm',
        'input_mu': ' μ Value',
        'input': 'Edit',
        'success': 'CALCULATION SACCESS',#'CALCULATED SUCCESSFULLY',
        #chain with params-main
        'J': 'Current density',
        'dw': 'Wire diameter',
        'nw': 'Strands',


        #bottom bar
        'core':'Core',
        'size':'mm',
        'muF':'μ:',
        'mf':'Weight (g):',

        'wire':'Wire',
        'N':'Turns:',
        'Pw':'Losses (W):',
        'mw':'Weight (g):',

        'order':'  Order   ',
        #modal window
        'confirm': 'Please confirm',
        'to_web':'Do you want to follow our website?',
        'yes': 'Yes',
        'no': 'No',
        }
}