import flet as ft
from inductor import N_culculate
from styles import cell_style
from btns_handler import btns_from_df, update_btns


async def main(page: ft.Page):

 
    page.title = "Розрахунок дроселя"
    # page.scroll = True
    # page.vertical_alignment = ft.MainAxisAlignment.START
    # page.horizontal_alignment = 'center'
    page.theme_mode = 'light'
    page.theme = ft.Theme(color_scheme_seed=ft.colors.LIGHT_BLUE_700)

    #Inputs
    I = ft.TextField(label="Струм, А", height=40, width=250, content_padding=ft.padding.all(5), text_align='center')
    I.value = 1
    L = ft.TextField(label="Індуктивність, мГн", height=40, width=250, content_padding=ft.padding.all(5), text_align='center')
    L.value = 50

    #Additional Inputs
    Bmax = ft.TextField(label="Робоча індукція(B), Тл", height=40, width=250, content_padding=ft.padding.all(5), text_align='center')
    Bmax.value = 0.4
    Kf = ft.TextField(label="Коефіцієнт феромагнітного заповнення", height=40, width=250, content_padding=ft.padding.all(5), text_align='center')
    Kf.value = 0.7
    q = ft.TextField(label="Щільність феромагнетика, г/см³", height=40, width=250, content_padding=ft.padding.all(5), text_align='center')
    q.value = 7.35
    J = ft.TextField(label="Густина струму, А/мм²", height=40, width=250, content_padding=ft.padding.all(5), text_align='center')
    J.value = 5.09295817894066
    d2w = ft.TextField(label="Діаметр дроту, мм", height=40, width=250, content_padding=ft.padding.all(5), text_align='center')
    d2w.value = 0.111803398874989
    Nw = ft.TextField(label="Кількість жил дроту", height=40, width=250, content_padding=ft.padding.all(5), text_align='center')
    Nw.value = 10
    Kw = ft.TextField(label="Коефіцієнт заповнення дротом", height=40, width=250, content_padding=ft.padding.all(5), text_align='center')
    Kw.value = 0.6
    mCost = ft.TextField(label="Ціна осердя за 1 кг, грн", height=40, width=250, content_padding=ft.padding.all(5), text_align='center')
    mCost.value = 4000
    wCost = ft.TextField(label="Ціна дроту за 1 кг, грн", height=40, width=250, content_padding=ft.padding.all(5), text_align='center')
    wCost.value = 500
    dmin = ft.TextField(label="Мін. внутрішній діаметр, мм", height=40, width=250, content_padding=ft.padding.all(5), text_align='center')
    dmin.value = 0
    dmax = ft.TextField(label="Макс. зовнішній діаметр, мм", height=40, width=250, content_padding=ft.padding.all(5), text_align='center')
    dmax.value = 1000
    Nmax = ft.TextField(label="Макс. можлива к-сть витків дроту", height=40, width=250, content_padding=ft.padding.all(5), text_align='center')
    Nmax.value = 10_000

    #panels
    mParams = ft.Container(content=ft.Column([ft.Text('Параметри осердя', size=18), Bmax, Kf, q], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20), bgcolor=ft.colors.TEAL_50, padding=20, border_radius=10)
    mParams.alignment = ft.alignment.center

    wParams = ft.Container(content=ft.Column([ft.Text('Параметри дроту', size=18), J, d2w, Nw, Kw], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20), bgcolor=ft.colors.ORANGE_50, padding=20, border_radius=10)
    wParams.alignment = ft.alignment.center

    costParams = ft.Container(content=ft.Column([ft.Text('Вартість матеріалів', size=18), mCost, wCost], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20), bgcolor=ft.colors.BROWN_50, padding=20, border_radius=10)
    costParams.alignment = ft.alignment.center

    limitParams = ft.Container(content=ft.Column([ft.Text('Обмеженя параметрів', size=18), dmin, dmax, Nmax], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20), bgcolor=ft.colors.BLUE_50, padding=20, border_radius=10)
    limitParams.alignment = ft.alignment.center





    #GET DATA_FRAME
    H_list = [5,10,15,20,25,30,40,50]
    Mu_list = [19, 26, 40, 60, 90, 125, 147, 160, 175, 200, 300, 400, 500, 700, 1000, 3000, 10000, 30000, 50000, 90000]
    
    
    params_ = [Bmax, Kf, q, J, d2w, Nw, Kw, dmin, dmax, Nmax]
    params = [field.value for field in params_]
    N_df = await N_culculate(I.value, L.value, H_list, Mu_list, params)         #<<<<<main calculation



    async def N_culc(e):
        params = [float(field.value) for field in params_]
        N_df = await N_culculate(float(I.value), float(L.value), H_list, Mu_list, params) #>>>>main calculation
        update_btns(btns_matrix, N_df)

        print(I.value, L.value)
        print(params)
        print(Nmax.value)
        await page.update_async()




    async def get_N(e):
        #update all styles >> to reset selected cell style
        for row in btns_matrix.keys():
            for btn in btns_matrix[row]:
                btn.style = cell_style(btn.text)
        
        #move to btn instant in dic >> to change color
        if 'None' not in e.control.text:
            key = e.control.data[0]
            btn_index = int(e.control.data[-2:])-1
            btns_matrix[key][btn_index].style = cell_style(0)

        output_text.value = f"ЦIНА ДРОСЕЛЯ - {e.control.text}"
        await page.update_async()



    #BUTTONS generation  
    btns_matrix = await btns_from_df(N_df)
    for row in btns_matrix:
        for btn in btns_matrix[row]:
            btn.on_click = get_N

    #UPDs Lists Mu,H values
    #---Mu--
    async def upd_Mu_Panel(e):
        new_Mu.value = int(e.control.text)
        popup_Mu.visible = True
        global Mu_index
        Mu_index = e.control.data
        await page.update_async()

    async def upd_Mu(e):
        Mu_list[Mu_index] = int(new_Mu.value)
        Mu_btns[Mu_index].text = new_Mu.value
        popup_Mu.visible = False
        await page.update_async()

    #---Height--
    async def upd_H_Panel(e):
        new_H.value = int(e.control.text)
        popup_H.visible = True
        global H_index
        H_index = e.control.data
        await page.update_async()

    async def upd_H(e):
        H_list[H_index] = int(new_H.value)
        H_btns[H_index].text = new_H.value
        popup_H.visible = False
        await page.update_async()


    #AXIS VALUES

    H_btns = []
    for height in H_list:
        i = H_list.index(height)     
        Value = ft.ElevatedButton(f"{height}", style=cell_style(-2), data=i, on_click=upd_H_Panel)
        H_btns.append(Value)

    Mu_btns = []
    for Mu in Mu_list:
        i = Mu_list.index(Mu)
        Value = ft.ElevatedButton(f"{Mu}", style=cell_style(-3), data=i, on_click=upd_Mu_Panel)
        Mu_btns.append(Value)
    




    text_Mu = ft.ElevatedButton(content=ft.Text("Mu", size=17), style=cell_style(-6), disabled=True)    
    text_H = ft.Text('Высота Осердя', size=16, color=ft.colors.CYAN_800, text_align='center')

    #MAIN MATRIX 
    Mu_ = ft.Column(controls=[text_Mu] + Mu_btns, spacing=5)
    cln_empty = ft.Column(controls=[text_Mu]*21, spacing=5)
    cln0 = ft.Column(controls=[H_btns[0]] + btns_matrix[f'1'], spacing=5)
    cln1 = ft.Column(controls=[H_btns[1]] + btns_matrix[f'2'], spacing=5)
    cln2 = ft.Column(controls=[H_btns[2]] + btns_matrix[f'3'], spacing=5)
    cln3 = ft.Column(controls=[H_btns[3]] + btns_matrix[f'4'], spacing=5)
    cln4 = ft.Column(controls=[H_btns[4]] + btns_matrix[f'5'], spacing=5)
    cln5 = ft.Column(controls=[H_btns[5]] + btns_matrix[f'6'], spacing=5)
    cln6 = ft.Column(controls=[H_btns[6]] + btns_matrix[f'7'], spacing=5)
    cln7 = ft.Column(controls=[H_btns[7]] + btns_matrix[f'8'], spacing=5)  
    #----
    scrolled_Row = ft.Row(controls=[cln_empty, cln0, cln1, cln2, cln3, cln4,
            cln5, cln6, cln7], alignment=ft.MainAxisAlignment.CENTER, spacing=5, scroll='hidden')
    matrix = ft.Stack([scrolled_Row, cln_empty, Mu_])
    





    #PAGE_BLOCKS - DESIGN -----------------------------------------------------------------
    async def to_Settings(route):
        await page.go_async("/settings")

    title_text = ft.AppBar(title=ft.Text('Вартiсть Дроселя', color=ft.colors.CYAN_900, size=22),
                        bgcolor=ft.colors.TEAL_50,
                        center_title=True,
                        actions=[ft.IconButton(ft.icons.SETTINGS, on_click=to_Settings)])

      
    culc_btn = ft.Container(ft.ElevatedButton('РОЗРАХУВАТИ', on_click=N_culc))
    culc_btn.padding = ft.padding.only(bottom=20)

    output_text = ft.Text('Please select N-cell from table', color=ft.colors.BLUE_900, size=16) 

    matrixCtr = ft.Container(content=ft.Column([text_H, matrix], spacing=6, horizontal_alignment='center'), bgcolor=ft.colors.BLUE_100, border_radius=20, width=4000)
    matrixCtr.alignment = ft.alignment.center
    matrixCtr.padding = ft.padding.only(bottom=30, top=20, left=10, right=10)


    new_Mu = ft.TextField(label="Значення Mu", height=40, width=200, content_padding=ft.padding.all(5), text_align='center', border_color=ft.colors.DEEP_ORANGE_900)
    Mu_btn = ft.OutlinedButton('Змiнити', style=cell_style(-4), on_click=upd_Mu, width=80)
    popup_Mu = ft.Container(content=ft.Row([new_Mu,Mu_btn], alignment=ft.MainAxisAlignment.CENTER, spacing=5), padding=10, width=500, visible=False)
    new_H = ft.TextField(label="Значення H", height=40, width=200, content_padding=ft.padding.all(5), text_align='center', border_color=ft.colors.CYAN_900)
    H_btn = ft.OutlinedButton('Змiнити', style=cell_style(-5), on_click=upd_H, width=80)
    popup_H = ft.Container(content=ft.Row([new_H,H_btn], alignment=ft.MainAxisAlignment.CENTER, spacing=5), padding=10, width=500, visible=False)
    

    #ROUTING PAGES(VIEWS)
    async def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View("/",
                [title_text,
                ft.Container(content=ft.Row([I, L], alignment=ft.MainAxisAlignment.CENTER, spacing=30, scroll='hidden', wrap=True), padding=20),
                culc_btn,
                popup_H,
                popup_Mu,
                output_text,
                matrixCtr],
                horizontal_alignment='center',
                scroll=True))
        if page.route == "/settings":
            page.views.append(
                ft.View("/settings",
                    [ft.AppBar(title=ft.Text("Додатковi Параметры", color=ft.colors.BROWN_900, size=22), bgcolor=ft.colors.DEEP_ORANGE_100, center_title=True),
                    mParams,
                    wParams,
                    costParams,
                    limitParams],
                    horizontal_alignment='center',
                    scroll=True
                    ))
        await page.update_async()

    async def back(route):
        page.views.pop()
        top_view = page.views[-1]
        await page.go_async(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = back

    await page.go_async(page.route)

 

ft.app(target=main, view=ft.WEB_BROWSER, port=8000, route_url_strategy='hash')

