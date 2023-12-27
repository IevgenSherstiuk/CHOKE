import flet as ft
from inductor import N_culculate
from styles import cell_style
from btns_handler import btns_from_df, update_btns


async def main(page: ft.Page):

 
    page.title = "Калькулятор цены дроселя"
    page.scroll = True
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = 'center'
    page.theme_mode = 'light'
    page.theme = ft.Theme(color_scheme_seed=ft.colors.LIGHT_BLUE_700)

    #inputs
    I = ft.TextField(label="  Current Intensity, A", height=40, width=250, content_padding=ft.padding.all(5), text_align='center')
    L = ft.TextField(label="  Inductance, mGn", height=40, width=250, content_padding=ft.padding.all(5), text_align='center')
    

    #GET DATA_FRAME
    H_list = [5,10,15,20,25,30,40,50]
    Mu_list = [19, 26, 40, 60, 90, 125, 147, 160, 175, 200, 300, 400, 500, 700, 1000, 3000, 10000, 30000, 50000, 90000]
    
    

    N_df = await N_culculate(1, 50, H_list, Mu_list)         #<<<<<main calculation



    async def N_culc(e):
        N_df = await N_culculate(float(I.value), float(L.value), H_list, Mu_list) #>>>>main calculation
        update_btns(btns_matrix, N_df)
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

        output_text.value = f"THE COST IS {e.control.text}"
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
        #N_df = await N_culculate(float(I.value), float(L.value), H_list, Mu_list) #>>>>main calculation
        #update_btns(btns_matrix, N_df)
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
    cln_empty = ft.Column(controls=[text_Mu]*19, spacing=5)
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
            cln5, cln6, cln7], alignment=ft.MainAxisAlignment.CENTER, spacing=5, scroll='always')
    matrix = ft.Stack([scrolled_Row, cln_empty, Mu_])
    



    #PAGE_BLOCKS - DESIGN
    title_text = ft.Container(ft.Text('CHOKE COST CALCULATOR', color=ft.colors.CYAN_900, size=22), bgcolor=ft.colors.TEAL_50, padding=20, border_radius=20, width=4000)
    title_text.alignment = ft.alignment.bottom_center
      
    culc_btn = ft.Container(ft.ElevatedButton('CALCULATE', on_click=N_culc))
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
    

    await page.add_async(title_text,
            ft.Container(content=ft.Row([I, L], alignment=ft.MainAxisAlignment.CENTER, spacing=30, scroll='hidden', wrap=True), padding=20),
            culc_btn,
            popup_H,
            popup_Mu,
            output_text,
            matrixCtr)
    
    await page.update_async()


ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

