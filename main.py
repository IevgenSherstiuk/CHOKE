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
        H_list = []
        for textfield in H_inst_strip:
            H_list.append(int(textfield.value)) 

        Mu_list = []
        for textfield in Mu_inst_strip:
            Mu_list.append(int(textfield.value))

        N_df = await N_culculate(float(I.value), float(L.value), H_list, Mu_list) #>>>>main calculation
        update_btns(btns_matrix, N_df, H_list, Mu_list)
        await page.update_async()


    async def get_N(e):
        #update all styles >> to reset selected cell style
        for row in btns_matrix.keys():
            for btn in btns_matrix[row]:
                btn.style = cell_style(btn.text)
        
        #move to btn instant in dic >> to change color
        if 'None' not in e.control.text:
            btn_index = int(e.control.data[-1])-1
            key = e.control.data[0:2]
            btns_matrix[key][btn_index].style = cell_style(0)

        output_text.value = f"THE COST IS {e.control.text}"
        await page.update_async()



    #BUTTONS generation  
    btns_matrix = await btns_from_df(N_df)
    for row in btns_matrix:
        for btn in btns_matrix[row]:
            btn.on_click = get_N


    #AXIS VALUES 
    H_inst = []
    H_inst_strip = []
    for height in H_list:
        Value = ft.TextField(value=f"{height}",
                            text_align="center",
                            text_size=16,
                            border_radius=20,
                            border_width=2,
                            border_color=ft.colors.CYAN_800,
                            cursor_color=ft.colors.CYAN_800,
                            content_padding=ft.padding.all(0),
                            width=60,
                            height=40,
                            color=ft.colors.CYAN_900)
        
        H_inst_strip.append(Value)
        H_inst.append(ft.Container(Value, padding=0))

    empty_btn = ft.Row(controls=[ft.TextField(value=f"0",
                            text_align="center",
                            text_size=16,
                            border_radius=20,
                            border_width=2,
                            border_color=ft.colors.DEEP_ORANGE_900,
                            cursor_color=ft.colors.DEEP_ORANGE_900,
                            content_padding=ft.padding.all(0),
                            width=60,
                            height=40,
                            color=ft.colors.DEEP_ORANGE_900),ft.Text('')], spacing=8)

    #ft.Container(width=60, height=40)
    Mu_inst = [empty_btn]
    Mu_inst_strip = []
    for Mu in Mu_list:
        Value = ft.TextField(value=f"{Mu}",
                            text_align="center",
                            text_size=16,
                            border_radius=20,
                            border_width=2,
                            border_color=ft.colors.DEEP_ORANGE_900,
                            cursor_color=ft.colors.DEEP_ORANGE_900,
                            content_padding=ft.padding.all(0),
                            width=60,
                            height=40,
                            color=ft.colors.DEEP_ORANGE_900)

        Mu_inst_strip.append(Value)
        Mu_inst.append(ft.Row(controls=[Value,ft.Text('')], spacing=8))


    #MAIN MATRIX 
    Mu_ = ft.Column(controls=Mu_inst, spacing= 5)
    cln0 = ft.Column(controls=[H_inst[0]] + btns_matrix[f'1'], spacing= 5)
    cln1 = ft.Column(controls=[H_inst[1]] + btns_matrix[f'2'], spacing= 5)
    cln2 = ft.Column(controls=[H_inst[2]] + btns_matrix[f'3'], spacing= 5)
    cln3 = ft.Column(controls=[H_inst[3]] + btns_matrix[f'4'], spacing= 5)
    cln4 = ft.Column(controls=[H_inst[4]] + btns_matrix[f'5'], spacing= 5)
    cln5 = ft.Column(controls=[H_inst[5]] + btns_matrix[f'6'], spacing= 5)
    cln6 = ft.Column(controls=[H_inst[6]] + btns_matrix[f'7'], spacing= 5)
    cln7 = ft.Column(controls=[H_inst[7]] + btns_matrix[f'8'], spacing= 5)
  
 




    #horizontal_alignment=ft.MainAxisAlignment.CENTER    


    #----
    matrix = ft.Row([Mu_, cln0, cln1, cln2, cln3, cln4,
                        cln5, cln6, cln7], alignment=ft.MainAxisAlignment.CENTER, spacing=4, scroll='always')

    title_text = ft.Text('CHOKE COST CALCULATOR', color=ft.colors.CYAN_900, size=22)
    title_row = ft.Row(controls=[title_text], alignment=ft.MainAxisAlignment.CENTER)
    title_text_colmn = ft.Container(content=ft.Column([title_row], horizontal_alignment=ft.MainAxisAlignment.CENTER), bgcolor=ft.colors.TEAL_50, padding=20)
    output_text = ft.Text('Please select N-cell from table', color=ft.colors.BLUE_900, size=16)    
    culc_btn = ft.Container(ft.ElevatedButton('CALCULATE', on_click=N_culc))
    culc_btn.padding = ft.padding.only(bottom=20)
    matrixCtr = ft.Container(content=matrix, bgcolor=ft.colors.BLUE_100, border_radius=20)
    matrixCtr.padding = ft.padding.only(bottom=30, top=30, left=10, right=10)

    await page.add_async(title_text_colmn,
            ft.Container(content=ft.Row([I, L], alignment=ft.MainAxisAlignment.CENTER, spacing=30, scroll='hidden', wrap=True), padding=20),
            culc_btn,
            output_text,
            matrixCtr)
    await page.update_async()


ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

