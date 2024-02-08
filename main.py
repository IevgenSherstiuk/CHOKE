import flet as ft
from inductor2 import N_calculate, calc_params
from styles import cell_style
from btns_handler import btns_from_df, update_btns
from time import sleep
from langs import LANGS
import json



def main(page: ft.Page):
      
    #SET LANGUAGE FROM LAST PARAMS 
    LNG = page.client_storage.get('LNG')
    if  LNG == ('' or None): LNG = 'ENG' #default value on first APP start 
    LNG_ = ft.Text()
    LNG_.value = LNG

    #FUNCs
    def lang(e):
        LNG_.value = change_lang.value
        LNG = LNG_.value
        info_text_1 = ft.Text(LANGS[LNG]['main']['info1'], size=14, text_align='center', weight=ft.FontWeight.BOLD, color='#243a5c')
        info_text_2 = ft.Text(LANGS[LNG]['main']['info2'], size=13, text_align='left')
        info_text_main = ft.Column([info_text_1, info_text_2], spacing=1)
        info_screen_main.title = info_text_main
        info_screen_mParams.title = ft.Text(LANGS[LNG]['params']['Core_paramsInfo'], size=15)
        info_screen_wParams.title = ft.Text(LANGS[LNG]['params']['Wire_paramsInfo'], size=15)
        info_screen_costParams.title = ft.Text(LANGS[LNG]['params']['Materials_costInfo'], size=15)
        info_screen_limitParams.title = ft.Text(LANGS[LNG]['params']['Limits_paramsInfo'], size=15)
        change_lang.label = LANGS[LNG]['params']['language']
        page.title = LANGS[LNG]['main']['title']
        I.label = LANGS[LNG]['main']['I']
        L.label = LANGS[LNG]['main']['L']
        Bmax.label = LANGS[LNG]['params']['Bmax']
        Kf.label = LANGS[LNG]['params']['Kf']
        qf.label = LANGS[LNG]['params']['qf']
        J.label = LANGS[LNG]['params']['J']
        nw.label = LANGS[LNG]['params']['nw']
        dw.label = LANGS[LNG]['params']['dw']
        Kw.label = LANGS[LNG]['params']['Kw']
        qw.label = LANGS[LNG]['params']['qw']
        rw.label = LANGS[LNG]['params']['rw']
        Uf.label = LANGS[LNG]['params']['Uf']
        Uw.label = LANGS[LNG]['params']['Uw']
        dmin.label = LANGS[LNG]['params']['dmin']
        Dmax.label = LANGS[LNG]['params']['Dmax']
        Nmax.label = LANGS[LNG]['params']['Nmax']
        to_site_modal.title = ft.Text(LANGS[LNG]['main']['confirm'])
        to_site_modal.content = ft.Text(LANGS[LNG]['main']['to_web'])
        yes_btn.text = LANGS[LNG]['main']['yes']
        no_btn.text = LANGS[LNG]['main']['no']
        mParams_title.value = LANGS[LNG]['params']['Core_params']
        wParams_title.value = LANGS[LNG]['params']['Wire_params']
        costParams_title.value = LANGS[LNG]['params']['Materials_cost']
        limitParams_title.value = LANGS[LNG]['params']['Limits_params']
        Core.value = LANGS[LNG]['main']['core']
        size_mm.value = LANGS[LNG]['main']['size']
        muF_title.value = LANGS[LNG]['main']['muF']
        weightF_title.value = LANGS[LNG]['main']['muF']
        Wire.value = LANGS[LNG]['main']['wire']
        wire_N_title.value = LANGS[LNG]['main']['N']
        wire_Pw_title.value = LANGS[LNG]['main']['Pw']
        weightW_title.value = LANGS[LNG]['main']['mw']
        buy_btn.text = LANGS[LNG]['main']['order']
        buy_btn_p2.label = ft.Text(f"{LANGS[LNG]['main']['order']}   ")
        text_H.value = LANGS[LNG]['main']['H_axis']
        title_text.title = ft.Text(LANGS[LNG]['main']['title'])
        calc_success_content.value = LANGS[LNG]['main']['success']
        calc_success_content_params.value = LANGS[LNG]['main']['success']
        new_Mu.label = LANGS[LNG]['main']['input_mu']
        Mu_btn.text = LANGS[LNG]['main']['input']
        new_H.label = LANGS[LNG]['main']['input_H']
        H_btn.text = LANGS[LNG]['main']['input']
        table_name.value = LANGS[LNG]['main']['table_name']
        params_title.title = ft.Text(LANGS[LNG]['params']['title'], color=ft.colors.BROWN_900, size=22)

        page.client_storage.set('LNG', LNG_.value)
        #page.client_storage.set('LNG', None) 
        page.update()

    change_lang = ft.Dropdown(  
            label=LANGS[LNG]['params']['language'],
            options=[
                ft.dropdown.Option("UA"),
                ft.dropdown.Option("ENG"),
                ft.dropdown.Option("RUS"),],
            width=250, height=40,
            content_padding=ft.padding.only(top=0, bottom=0),
            text_size=14,
            on_change=lang) 
    change_lang.alignment = ft.alignment.center
    change_lang.value = LNG_.value

    
    #CELL PRESSED CALC <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def N_calc(e):
        if isinstance(J.value, str): J.value = J.value.replace(',', '.').replace(' ', '')
        if isinstance(I.value, str): I.value = I.value.replace(',', '.').replace(' ', '')
        if isinstance(nw.value, str): nw.value = nw.value.replace(',', '.').replace(' ', '')
        Sw = float(I.value)/float(J.value)/float(nw.value)*1e-6

        #changing params depending changed value
        if (LANGS['UA']['main']['I'] in e.control.label) or (LANGS['ENG']['main']['I'] in e.control.label) or (LANGS['RUS']['main']['I'] in e.control.label):
            dw.value = round(2*(Sw/3.141592653589793)**0.5*1000,3)
        if (LANGS['UA']['main']['J'] in e.control.label) or (LANGS['ENG']['main']['J'] in e.control.label) or (LANGS['RUS']['main']['J'] in e.control.label):
            dw.value = round(2*(Sw/3.141592653589793)**0.5*1000,3)
        if (LANGS['UA']['main']['dw'] in e.control.label) or (LANGS['ENG']['main']['dw'] in e.control.label) or (LANGS['RUS']['main']['dw'] in e.control.label):
            dw_new = float(dw.value.replace(',', '.').replace(' ', ''))/1000
            Sw = 3.141592653589793*(dw_new**2)/4
            J_new = float(I.value)/Sw*1e-6/float(nw.value)
            J.value = round(J_new,2)
        if (LANGS['UA']['main']['nw'] in e.control.label) or (LANGS['ENG']['main']['nw'] in e.control.label) or (LANGS['RUS']['main']['nw'] in e.control.label):
            dw.value = round(2*(Sw/3.141592653589793)**0.5*1000,3)

            
        params = []

        for field in params_:
            if isinstance(field.value, str):            
                value = float(field.value.replace(',', '.').replace(' ', ''))
            else: value = float(field.value) 
            params.append(value)
            #save to local storage
            index = params_.index(field)
            page.client_storage.set(params_keys[index], value) #<< save to cashe for the last used params  
        params.append(Sw)
        

        N_df = N_calculate(H_list, Mu_list, params) #>>>>main calculation
        formating_grades = formating(N_df)
        minPrice_btn = update_btns(btns_matrix, N_df, formating_grades)
        #SET FOCUSED BUTTON
        get_values_from_calc(minPrice_btn)

        #animation
        calc_success.height = 40
        calc_success_param.height = 40
        page.update()
        sleep(2.0)
        calc_success.height = 0
        calc_success_param.height = 0
        page.update()



    def formating(df):
        prices = []
        for row in df:
            for cell in row:
                if cell['price']: prices.append(cell['price'])
        price_Min = min(prices)
        formating_grades = [price_Min, 1.5*price_Min, 3*price_Min] #<<< SET GRADES
        return formating_grades
    
###########################################################################################################################


    #MAIN PAGE
    page.title = LANGS[LNG]['main']['title']
    page.theme_mode = 'light'
    page.theme = ft.Theme(color_scheme_seed=ft.colors.LIGHT_BLUE_700)

    #Inputs
    I = ft.TextField(label=LANGS[LNG]['main']['I'], height=35, width=150, content_padding=ft.padding.all(5), text_align='center', keyboard_type='NUMBER', on_submit=N_calc)
    I.value = page.client_storage.get('I')
    if (I.value == '') or (I.value == 0): I.value = 1
    L = ft.TextField(label=LANGS[LNG]['main']['L'], height=35, width=150, content_padding=ft.padding.all(5), text_align='center', keyboard_type='NUMBER', on_submit=N_calc)
    L.value = page.client_storage.get('L')
    if L.value == '': L.value = 50
    inputs = ft.Container(content=ft.Row([I, L], alignment=ft.MainAxisAlignment.CENTER, spacing=20, scroll='hidden', wrap=True))
    inputs.padding = ft.padding.only(top=15, bottom=0)

    #Additional Inputs
    Bmax = ft.TextField(label=LANGS[LNG]['params']['Bmax'], height=40, width=250, content_padding=ft.padding.all(5), text_align='center', keyboard_type='NUMBER', on_submit=N_calc)
    Bmax.value = page.client_storage.get('Bmax')
    if Bmax.value == '':  Bmax.value = 0.4
    Kf = ft.TextField(label=LANGS[LNG]['params']['Kf'], height=40, width=250, content_padding=ft.padding.all(5), text_align='center', keyboard_type='NUMBER', on_submit=N_calc)
    Kf.value = page.client_storage.get('Kf')
    if Kf.value == '':  Kf.value = 0.7
    qf = ft.TextField(label=LANGS[LNG]['params']['qf'], height=40, width=250, content_padding=ft.padding.all(5), text_align='center', keyboard_type='NUMBER', on_submit=N_calc)
    qf.value = page.client_storage.get('qf')
    if qf.value == '':  qf.value = 7.35
    J = ft.TextField(label=LANGS[LNG]['params']['J'], height=40, width=250, content_padding=ft.padding.all(5), text_align='center', keyboard_type='NUMBER', on_submit=N_calc)
    J.value = page.client_storage.get('J')
    if J.value == '':  J.value = 5.0
    nw = ft.TextField(label=LANGS[LNG]['params']['nw'], height=40, width=250, content_padding=ft.padding.all(5), text_align='center', keyboard_type='NUMBER', on_submit=N_calc)
    nw.value = page.client_storage.get('nw')
    if nw.value == '':  nw.value = 1
    dw = ft.TextField(label=LANGS[LNG]['params']['dw'], height=40, width=250, content_padding=ft.padding.all(5), text_align='center', keyboard_type='NUMBER', on_submit=N_calc)
    Sw = I.value/J.value/nw.value*1e-6 #Sw calc <<<<<<<<<<<<<<<<<<<<
    dw.value = round(2*(Sw/3.141592653589793)**0.5*1000,3)
    Kw = ft.TextField(label=LANGS[LNG]['params']['Kw'], height=40, width=250, content_padding=ft.padding.all(5), text_align='center', keyboard_type='NUMBER', on_submit=N_calc)
    Kw.value = page.client_storage.get('Kw')
    if Kw.value == '':  Kw.value = 0.3
    qw = ft.TextField(label=LANGS[LNG]['params']['qw'], height=40, width=250, content_padding=ft.padding.all(5), text_align='center', keyboard_type='NUMBER', on_submit=N_calc)
    qw.value = page.client_storage.get('qw')
    if qw.value == '':  qw.value = 8.96
    rw = ft.TextField(label=LANGS[LNG]['params']['rw'], height=40, width=250, content_padding=ft.padding.all(5), text_align='center', keyboard_type='NUMBER', on_submit=N_calc)
    rw.value = page.client_storage.get('rw')
    if rw.value == '':  rw.value = 0.0172
    Uf = ft.TextField(label=LANGS[LNG]['params']['Uf'], height=40, width=250, content_padding=ft.padding.all(5), text_align='center', keyboard_type='NUMBER', on_submit=N_calc)
    Uf.value = page.client_storage.get('Uf')
    if Uf.value == '':  Uf.value = 20
    Uw = ft.TextField(label=LANGS[LNG]['params']['Uw'], height=40, width=250, content_padding=ft.padding.all(5), text_align='center', keyboard_type='NUMBER', on_submit=N_calc)
    Uw.value = page.client_storage.get('Uw')
    if Uw.value == '':  Uw.value = 50
    dmin = ft.TextField(label=LANGS[LNG]['params']['dmin'], height=40, width=250, content_padding=ft.padding.all(5), text_align='center', keyboard_type='NUMBER', on_submit=N_calc)
    dmin.value = page.client_storage.get('dmin')
    if dmin.value == '':  dmin.value = 20
    Dmax = ft.TextField(label=LANGS[LNG]['params']['Dmax'], height=40, width=250, content_padding=ft.padding.all(5), text_align='center', keyboard_type='NUMBER', on_submit=N_calc)
    Dmax.value = page.client_storage.get('Dmax')
    if Dmax.value == '':  Dmax.value = 1000
    Nmax = ft.TextField(label=LANGS[LNG]['params']['Nmax'], height=40, width=250, content_padding=ft.padding.all(5), text_align='center', keyboard_type='NUMBER', on_submit=N_calc)
    Nmax.value = page.client_storage.get('Nmax')
    if Nmax.value == '':  Nmax.value = 10_000

    #infoPages

    info_text_1 = ft.Text(LANGS[LNG]['main']['info1'], size=14, text_align='center', weight=ft.FontWeight.BOLD, color='#243a5c')
    info_text_2 = ft.Text(LANGS[LNG]['main']['info2'], size=13, text_align='left')
    info_text = ft.Column([info_text_1, info_text_2], spacing=1)
    info_screen_main = ft.AlertDialog(title=info_text, actions_padding=30,
                                          content=ft.Image(src='inductor.png', fit=ft.ImageFit.CONTAIN))
    
    def open_info_main(e):
        page.dialog = info_screen_main
        info_screen_main.open = True
        page.update()

    info_screen_mParams = ft.AlertDialog(title=ft.Text(LANGS[LNG]['params']['Core_paramsInfo'], size=15), actions_padding=0)
    def open_info_mParams(e):
        page.dialog = info_screen_mParams
        info_screen_mParams.open = True
        page.update()

    info_screen_wParams = ft.AlertDialog(title=ft.Text(LANGS[LNG]['params']['Wire_paramsInfo'], size=15), actions_padding=0)
    def open_info_wParams(e):
        page.dialog = info_screen_wParams
        info_screen_wParams.open = True
        page.update()

    info_screen_costParams = ft.AlertDialog(title=ft.Text(LANGS[LNG]['params']['Materials_costInfo'], size=15), actions_padding=0)
    def open_info_costParams(e):
        page.dialog = info_screen_costParams
        info_screen_costParams.open = True
        page.update()

    info_screen_limitParams = ft.AlertDialog(title=ft.Text(LANGS[LNG]['params']['Limits_paramsInfo'], size=15), actions_padding=0)
    def open_info_limitParams(e):
        page.dialog = info_screen_limitParams
        info_screen_limitParams.open = True
        page.update()


    #MODAL WINDOWS "TO SITE"
    def close_dlg(e):
        to_site_modal.open = False
        page.update()

    yes_btn = ft.TextButton(LANGS[LNG]['main']['yes'], url='http://melta.com.ua/inductor-calc?', on_click=close_dlg)
    no_btn = ft.TextButton(LANGS[LNG]['main']['no'], on_click=close_dlg)
    to_site_modal = ft.AlertDialog(
                                modal=True,
                                title=ft.Text(LANGS[LNG]['main']['confirm']),
                                content=ft.Text(f"{LANGS[LNG]['main']['to_web']}", text_align='center'),
                                actions=[yes_btn, no_btn],
                                actions_alignment=ft.MainAxisAlignment.END,)

    def to_site(e):
        page.dialog = to_site_modal
        to_site_modal.open = True
        page.update()
        



    #adjustments panels
    lang_input = ft.Container(change_lang)
    lang_input.padding = ft.padding.only(top=30, bottom=40)


    mParams_info = ft.IconButton(ft.icons.INFO_OUTLINE_ROUNDED, on_click=open_info_mParams, icon_color=ft.colors.TEAL_600, data='mParams')
    mParams_title = ft.Text(LANGS[LNG]['params']['Core_params'], size=18)
    mParams = ft.Container(content=ft.Column([ft.Row([mParams_title, mParams_info], alignment='center'), Bmax, Kf, qf], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20), bgcolor=ft.colors.TEAL_50, padding=20, border_radius=10)
    mParams.alignment = ft.alignment.center

    wParams_info = ft.IconButton(ft.icons.INFO_OUTLINE_ROUNDED, on_click=open_info_wParams, icon_color=ft.colors.BROWN_300, data='wParams')
    wParams_title = ft.Text(LANGS[LNG]['params']['Wire_params'], size=18)
    wParams = ft.Container(content=ft.Column([ft.Row([wParams_title, wParams_info], alignment='center'), J, dw, nw, Kw, qw, rw], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20), bgcolor=ft.colors.ORANGE_50, padding=20, border_radius=10)
    wParams.alignment = ft.alignment.center

    costParams_info = ft.IconButton(ft.icons.INFO_OUTLINE_ROUNDED, on_click=open_info_costParams, icon_color=ft.colors.BROWN_600, data='costParams')
    costParams_title = ft.Text(LANGS[LNG]['params']['Materials_cost'], size=18)
    costParams = ft.Container(content=ft.Column([ft.Row([costParams_title, costParams_info], alignment='center'), Uf, Uw], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20), bgcolor=ft.colors.BROWN_50, padding=20, border_radius=10)
    costParams.alignment = ft.alignment.center


    limitParams_info = ft.IconButton(ft.icons.INFO_OUTLINE_ROUNDED, on_click=open_info_limitParams, icon_color=ft.colors.CYAN_800, data='limitParams')
    limitParams_title = ft.Text(LANGS[LNG]['params']['Limits_params'], size=18)
    limitParams = ft.Container(content=ft.Column([ft.Row([limitParams_title, limitParams_info], alignment='center'), dmin, Dmax, Nmax], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20), bgcolor=ft.colors.BLUE_50, padding=20, border_radius=10)
    limitParams.alignment = ft.alignment.center


############################################################################################################################################################################################################################################################################

    #GET DATA_FRAME
    H_list = [5,10,15,20,30,40,50]
    Mu_list = [14,19,26,40,60,90,125,147,160,175,205,500,750,900,2300,3000,5000,10000]
    
    params_ = [L, I, Bmax, Kf, qf, J, dw, nw, Kw, qw, rw, Uf, Uw, dmin, Dmax, Nmax]
    params_keys = ['L', 'I', 'Bmax', 'Kf', 'qf', 'J', 'dw', 'nw', 'Kw', 'qw', 'rw', 'Uf', 'Uw', 'dmin', 'Dmax', 'Nmax']
    params = [field.value for field in params_]
    params.append(Sw)
    N_df = N_calculate(H_list, Mu_list, params)        #<<<<< started page main calculation
    #color formating
    formating_grades = formating(N_df)
    


    size_mm = ft.Text('')
    muF_title = ft.Text('')
    weightF_title = ft.Text('')
    wire_N_title = ft.Text('')
    wire_Pw_title = ft.Text('')
    weightW_title = ft.Text('')

    def get_N(e):
        #move to btn instant in dic >> to change color
        for row in btns_matrix:
            for btn in btns_matrix[row]:
                if  'amber700'in str(btn.style.bgcolor): btn.style = cell_style(-7, None) #<< reset color from FOCUSED
                
        if 'None' not in e.control.text:
            LNG = LNG_.value
            key = e.control.data[0][0]
            btn_index = int(e.control.data[0][-2:])-1
            btns_matrix[key][btn_index].focus()

            h = H_list[int(e.control.data[0][0])-1]
            mu = Mu_list[int(e.control.data[0][1:])-1]
            N = int(e.control.text)
            
            params_ = [I, L, Bmax, Kf, qf, qw, J, dw, rw, Uf, Uw]
            params = [float(field.value) for field in params_]
            Sw = params[0]/params[6]*10**-6
            params.append(Sw)
            results = calc_params(N, h, mu, params)

            Core.value = LANGS[LNG]['main']['core']
            size_mm.value = LANGS[LNG]['main']['size']
            Size.value = f"{int(results['d'])}x{int(results['D'])}/{int(results['h'])} {size_mm.value}"
            muF_title.value = LANGS[LNG]['main']['muF']
            muF.value = f"{muF_title.value} {int(results['mu'])}"
            weightF_title.value = LANGS[LNG]['main']['mf']
            weightF.value = f"{weightF_title.value} {int(results['mf'])}"

            Wire.value = LANGS[LNG]['main']['wire']
            wire_N_title.value = LANGS[LNG]['main']['N']
            wire_N.value = f"{wire_N_title.value} {int(results['N'])}"
            wire_Pw_title.value = LANGS[LNG]['main']['Pw']
            wire_Pw.value = f"{wire_Pw_title.value} {round(results['Pw'], 2)}"
            weightW_title.value = LANGS[LNG]['main']['mw']
            weightW.value = f"{weightW_title.value} {int(results['mw'])}"
            
            buy_btn_p1.label = ft.Text(f"{round((results['pf']+results['pw']),1)}$")
            page.update()


    def get_values_from_calc(minPrice_btn):
        if 'None' not in minPrice_btn.text:
            LNG = LNG_.value
            h = H_list[int(minPrice_btn.data[0][0])-1]
            mu = Mu_list[int(minPrice_btn.data[0][1:])-1]
            N = int(minPrice_btn.text)
            
            params_ = [I, L, Bmax, Kf, qf, qw, J, dw, rw, Uf, Uw]
            params = [float(field.value) for field in params_]
            Sw = params[0]/params[6]*10**-6 #<<<<<<<<<<<<<<<<ERROR DIVISION BY ZERO - J
            params.append(Sw)
            results = calc_params(N, h, mu, params)

            Core.value = LANGS[LNG]['main']['core']
            Size.value = f"{int(results['d'])}x{int(results['D'])}/{int(results['h'])} {LANGS[LNG]['main']['size']}"
            muF.value = f"{LANGS[LNG]['main']['muF']} {int(results['mu'])}"
            weightF.value = f"{LANGS[LNG]['main']['mf']} {int(results['mf'])}"

            Wire.value = LANGS[LNG]['main']['wire']
            wire_N.value = f"{LANGS[LNG]['main']['N']} {int(results['N'])}"
            wire_Pw.value = f"{LANGS[LNG]['main']['Pw']} {round(results['Pw'], 2)}"
            weightW.value = f"{LANGS[LNG]['main']['mw']} {int(results['mw'])}"
            
            buy_btn_p1.label = ft.Text(f"{round((results['pf']+results['pw']), 1)}$")
            
            page.update()

   

    #BUTTONS generation  
    btns_matrix = btns_from_df(N_df, formating_grades)
    #for calculation start - find first NOT NoneType value
    for row in btns_matrix:
        for btn in btns_matrix[row]:
            if btn: minPrice_btn = btn #for calculation start - find first NOT NoneType value

    for row in btns_matrix:
        for btn in btns_matrix[row]:
            if btn.data[1] is None: btn.data[1] = 1000000000000000
            price = btn.data[1]
            if price < minPrice_btn.data[1]:
                minPrice_btn = btn   
            btn.on_click = get_N
    minPrice_btn.style = cell_style(0, None)


    #UPDs Lists Mu,H values
    #---Mu--
    def upd_Mu_Panel(e):
        popup_Mu.height = 55
        new_Mu.border_color = ft.colors.DEEP_ORANGE_900
        new_Mu.value = int(e.control.text)
        global Mu_index
        Mu_index = e.control.data
        page.update()
        sleep(0.28)
        new_Mu.text_size = 16
        page.update()

    def upd_Mu(e):
        Mu_list[Mu_index] = int(new_Mu.value)
        Mu_btns[Mu_index].text = new_Mu.value
        popup_Mu.height = 0
        new_Mu.value = None
        new_Mu.text_size = 0
        new_Mu.border_color = ft.colors.WHITE
        
        params = [float(field.value) for field in params_]
        Sw = float(I.value)/float(J.value)/float(nw.value)*1e-6
        params.append(Sw)
        N_df = N_calculate(H_list, Mu_list, params) #>>>>main calculation
        formating_grades = formating(N_df)
        update_btns(btns_matrix, N_df, formating_grades)
        page.update()
        

    #---Height--
    def upd_H_Panel(e):
        popup_H.height = 55
        new_H.border_color = ft.colors.CYAN_900
        new_H.value = int(e.control.text)
        global H_index
        H_index = e.control.data
        page.update()
        sleep(0.28)
        new_H.text_size = 16
        page.update()

    def upd_H(e):
        H_list[H_index] = int(new_H.value)
        H_btns[H_index].text = new_H.value
        popup_H.height = 0
        new_H.value = None
        new_H.text_size = 0
        new_H.border_color = ft.colors.WHITE

        params = [float(field.value) for field in params_]
        Sw = float(I.value)/float(J.value)/float(nw.value)*1e-6
        params.append(Sw)
        N_df = N_calculate(H_list, Mu_list, params) #>>>>main calculation
        formating_grades = formating(N_df)
        update_btns(btns_matrix, N_df, formating_grades)
        page.update()


    #AXIS VALUES
    H_btns = []
    for height in H_list:
        i = H_list.index(height)     
        Value = ft.ElevatedButton(f"{height}", style=cell_style(-2, None), data=i, on_click=upd_H_Panel)
        H_btns.append(Value)

    Mu_btns = []
    for Mu in Mu_list:
        i = Mu_list.index(Mu)
        Value = ft.ElevatedButton(f"{Mu}", style=cell_style(-3, None), data=i, on_click=upd_Mu_Panel)
        Mu_btns.append(Value)
    


    text_Mu = ft.ElevatedButton(content=ft.Text("μ", size=18), style=cell_style(-6, None), disabled=True)    
    text_H = ft.Text(LANGS[LNG]['main']['H_axis'], size=16, color=ft.colors.CYAN_800, text_align='center')

    #MAIN MATRIX 
    Mu_ = ft.Column(controls=[text_Mu] + Mu_btns, spacing=5)
    cln_empty = ft.Column(controls=[text_Mu]*19, spacing=5)
    cln0 = ft.Column(controls=[H_btns[0]] + btns_matrix['1'], spacing=5)
    cln1 = ft.Column(controls=[H_btns[1]] + btns_matrix['2'], spacing=5)
    cln2 = ft.Column(controls=[H_btns[2]] + btns_matrix['3'], spacing=5)
    cln3 = ft.Column(controls=[H_btns[3]] + btns_matrix['4'], spacing=5)
    cln4 = ft.Column(controls=[H_btns[4]] + btns_matrix['5'], spacing=5)
    cln5 = ft.Column(controls=[H_btns[5]] + btns_matrix['6'], spacing=5)
    cln6 = ft.Column(controls=[H_btns[6]] + btns_matrix['7'], spacing=5)
    #----
    scrolled_Row = ft.Row(controls=[cln_empty, cln0, cln1, cln2, cln3, cln4,
            cln5, cln6], alignment=ft.MainAxisAlignment.CENTER, spacing=5, scroll='hidden')
    matrix = ft.Stack([scrolled_Row, cln_empty, Mu_])
    

    


    #-----------PAGE_BLOCKS - DESIGN -----------------------------------------------------------------
        
    def to_Settings(route):
        page.go("/settings")

    info_btn = ft.IconButton(ft.icons.INFO_OUTLINE_ROUNDED, on_click=open_info_main, data='main')
    title_text = ft.AppBar(title=ft.Text(LANGS[LNG]['main']['title'], color=ft.colors.CYAN_900, size=22),
                        leading=info_btn,
                        bgcolor=ft.colors.TEAL_50,
                        center_title=True,
                        actions=[ft.IconButton(ft.icons.SETTINGS, on_click=to_Settings)])
    

    calc_success_content = ft.Text(LANGS[LNG]['main']['success'], size=22, color=ft.colors.CYAN_700,
                                                weight=ft.FontWeight.W_400, text_align='center')
    calc_success = ft.Container(content=calc_success_content, height=0,
                                                animate=ft.animation.Animation(1800, ft.AnimationCurve.FAST_LINEAR_TO_SLOW_EASE_IN))
    calc_success.padding = ft.padding.only(top=10)

    calc_success_content_params = ft.Text(LANGS[LNG]['main']['success'], size=22, color=ft.colors.CYAN_700,
                                                weight=ft.FontWeight.W_400, text_align='center')
    calc_success_param = ft.Container(content=calc_success_content_params, height=0,
                                                animate=ft.animation.Animation(1800, ft.AnimationCurve.FAST_LINEAR_TO_SLOW_EASE_IN))
    calc_success_param.padding = ft.padding.only(top=10)
    
    #BottomAppBar
    Core = ft.Text('', color=ft.colors.BLUE_100, size=16)
    Size = ft.Text('', color=ft.colors.BLUE_50, size=13)
    Wire = ft.Text('', color=ft.colors.ORANGE_200, size=16)
    wire_N = ft.Text('', color=ft.colors.YELLOW_50, size=13)
    muF = ft.Text('', color=ft.colors.BLUE_50, size=13)
    wire_Pw = ft.Text('', color=ft.colors.ORANGE_50, size=13)
    weightF = ft.Text('', color=ft.colors.BLUE_50, size=13)
    weightW = ft.Text('', color=ft.colors.ORANGE_50, size=13)

    buy_btn_p1 = ft.Segment(value="1", label=ft.Text("0$"), icon=ft.Icon(ft.icons.SHOPPING_CART))
    buy_btn_p2 = ft.Segment(value="2", label=ft.Text(f"{LANGS[LNG]['main']['order']}   "))
    buy_btn = ft.Container(ft.SegmentedButton(
            on_change=to_site,
            allow_empty_selection=True,
            show_selected_icon=False,
            segments=[buy_btn_p1, buy_btn_p2],
            style=cell_style(-8, None)))
    buy_btn.padding = ft.padding.only(bottom=20, top=0, left=0, right=0)
    #get values to BottomAppBar
    get_values_from_calc(minPrice_btn)


    #RESULTS TABLE
    results_cln1 = ft.Column([Core, muF, Size, weightF], spacing=6, horizontal_alignment=ft.CrossAxisAlignment.START)
    results_cln2 = ft.Column([Wire, wire_N, wire_Pw, weightW], spacing=6, horizontal_alignment=ft.CrossAxisAlignment.START)
    
    results_tbl = ft.Row([results_cln1, results_cln2
    ], alignment='center', spacing=30)
            


    text_cntr = ft.Container(ft.Column([results_tbl, buy_btn], spacing=18, horizontal_alignment=ft.CrossAxisAlignment.CENTER), bgcolor=ft.colors.CYAN_800)
    text_cntr.alignment = ft.alignment.center
    text_cntr.padding = ft.padding.only(bottom=0, top=15, left=0, right=0)

    output_bar = ft.BottomAppBar(text_cntr, bgcolor=ft.colors.BLUE_100, height=245)
    output_bar.padding = ft.padding.only(bottom=0, top=10, left=0, right=0)

    #MARIX-AXIS
    table_name = ft.Text(LANGS[LNG]['main']['table_name'], size=18, color=ft.colors.BLUE_900, weight=ft.FontWeight.W_400, text_align='center', )

    matrixCtr = ft.Container(content=ft.Column([text_H, matrix], spacing=4, horizontal_alignment='center', scroll=ft.ScrollMode.HIDDEN, height=355), bgcolor=ft.colors.BLUE_100, border_radius=0, width=4000)
    matrixCtr.alignment = ft.alignment.center
    matrixCtr.padding = ft.padding.only(bottom=150, top=10, left=5, right=5)


    new_Mu = ft.TextField(label=LANGS[LNG]['main']['input_mu'], height=40, width=200, content_padding=ft.padding.all(5), text_align='center', border_color=ft.colors.WHITE, text_size=0, keyboard_type='NUMBER')
    Mu_btn = ft.OutlinedButton(LANGS[LNG]['main']['input'], style=cell_style(-4, None), on_click=upd_Mu, width=80)
    popup_Mu = ft.Container(content=ft.Row([new_Mu,Mu_btn], alignment=ft.MainAxisAlignment.CENTER, spacing=5), padding=1,
                            visible=True, width=500, height=0, animate=ft.animation.Animation(2000, ft.AnimationCurve.FAST_LINEAR_TO_SLOW_EASE_IN))
    
    new_H = ft.TextField(label=LANGS[LNG]['main']['input_H'], height=40, width=200, content_padding=ft.padding.all(5), text_align='center', border_color=ft.colors.WHITE, text_size=0, keyboard_type='NUMBER')
    H_btn = ft.OutlinedButton(LANGS[LNG]['main']['input'], style=cell_style(-5, None), on_click=upd_H, width=80)
    popup_H = ft.Container(content=ft.Row([new_H,H_btn], alignment=ft.MainAxisAlignment.CENTER, spacing=5), padding=1,
                           visible=True, width=500, height=0, animate=ft.animation.Animation(2000, ft.AnimationCurve.FAST_LINEAR_TO_SLOW_EASE_IN))
    

    #ROUTING PAGES(VIEWS)
    main_view = ft.View("/",[
                title_text,
                calc_success,
                inputs,
                output_bar,
                popup_H,
                popup_Mu,
                table_name,
                matrixCtr,
                ],horizontal_alignment='center', padding=0)
    
    params_title = ft.AppBar(title=ft.Text(LANGS[LNG]['params']['title'], color=ft.colors.BROWN_900, size=22),
                               bgcolor=ft.colors.DEEP_ORANGE_100, center_title=True, actions=[])
    params_view = ft.View("/settings",
                    [params_title,
                    calc_success_param,
                    mParams,
                    wParams,
                    costParams,
                    limitParams,
                    lang_input,],
                    horizontal_alignment='center',
                    scroll=ft.ScrollMode.HIDDEN,
                    )
    
    def route_change(route):
        page.views.clear()
        page.views.append(main_view)
        if page.route == "/settings":
            page.views.append(params_view)
        page.update()

    def back(route):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = back


    page.go(page.route)

 

ft.app(target=main)#, view=ft.WEB_BROWSER, port=8000, route_url_strategy='hash')

