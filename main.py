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
    empty_btn = ft.Container(width=60)
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
                            content_padding=ft.padding.all(5),
                            width=60,
                            height=40,
                            color=ft.colors.CYAN_900)
        
        H_inst_strip.append(Value)
        H_inst.append(ft.Container(Value, padding=0))


    Mu_inst = []
    Mu_inst_strip = []
    for Mu in Mu_list:
        Value = ft.TextField(value=f"{Mu}",
                            text_align="center",
                            text_size=16,
                            border_radius=20,
                            border_width=2,
                            border_color=ft.colors.DEEP_ORANGE_900,
                            cursor_color=ft.colors.DEEP_ORANGE_900,
                            content_padding=ft.padding.all(5),
                            width=60,
                            height=40,
                            color=ft.colors.DEEP_ORANGE_900)

        Mu_inst_strip.append(Value)
        Mu_inst.append(ft.Row(controls=[Value,ft.Text('')], spacing=8))



#MAIN MATRIX 
    row_ = ft.Column(spacing=5, controls=H_inst, alignment=ft.MainAxisAlignment.CENTER)
    row0 = ft.Column(spacing=5, controls=btns_matrix[f'01'], alignment=ft.MainAxisAlignment.CENTER)
    row1 = ft.Column(spacing=5, controls=btns_matrix[f'02'], alignment=ft.MainAxisAlignment.CENTER)
    row2 = ft.Column(spacing=5, controls=btns_matrix[f'03'], alignment=ft.MainAxisAlignment.CENTER)
    row3 = ft.Column(spacing=5, controls=btns_matrix[f'04'], alignment=ft.MainAxisAlignment.CENTER)
    row4 = ft.Column(spacing=5, controls=btns_matrix[f'05'], alignment=ft.MainAxisAlignment.CENTER)
    row5 = ft.Column(spacing=5, controls=btns_matrix[f'06'], alignment=ft.MainAxisAlignment.CENTER)
    row6 = ft.Column(spacing=5, controls=btns_matrix[f'07'], alignment=ft.MainAxisAlignment.CENTER)
    row7 = ft.Column(spacing=5, controls=btns_matrix[f'08'], alignment=ft.MainAxisAlignment.CENTER)
    row8 = ft.Column(spacing=5, controls=btns_matrix[f'09'], alignment=ft.MainAxisAlignment.CENTER)
    row9 = ft.Column(spacing=5, controls=btns_matrix[f'10'], alignment=ft.MainAxisAlignment.CENTER)
    row10 = ft.Column(spacing=5, controls=btns_matrix[f'11'], alignment=ft.MainAxisAlignment.CENTER)
    row11 = ft.Column(spacing=5, controls=btns_matrix[f'12'], alignment=ft.MainAxisAlignment.CENTER)
    row12 = ft.Column(spacing=5, controls=btns_matrix[f'13'], alignment=ft.MainAxisAlignment.CENTER)
    row13 = ft.Column(spacing=5, controls=btns_matrix[f'14'], alignment=ft.MainAxisAlignment.CENTER)
    row14 = ft.Column(spacing=5, controls=btns_matrix[f'15'], alignment=ft.MainAxisAlignment.CENTER)
    row15 = ft.Column(spacing=5, controls=btns_matrix[f'16'], alignment=ft.MainAxisAlignment.CENTER)
    row16 = ft.Column(spacing=5, controls=btns_matrix[f'17'], alignment=ft.MainAxisAlignment.CENTER)
    row17 = ft.Column(spacing=5, controls=btns_matrix[f'18'], alignment=ft.MainAxisAlignment.CENTER)
    row18 = ft.Column(spacing=5, controls=btns_matrix[f'19'], alignment=ft.MainAxisAlignment.CENTER)
    row19 = ft.Column(spacing=5, controls=btns_matrix[f'20'], alignment=ft.MainAxisAlignment.CENTER)
 




    #horizontal_alignment=ft.MainAxisAlignment.CENTER    


    #----
    matrix = ft.Row([row_, row0, row1, row2, row3, row4,
                        row5, row6, row7, row8, row9, row10,
                        row11, row12, row13, row14, row15, row16,
                        row17, row18, row19], alignment=ft.MainAxisAlignment.CENTER, scroll='always')

    title_text = ft.Text('CHOKE COST CALCULATOR', color=ft.colors.CYAN_900, size=22)
    title_row = ft.Row(controls=[title_text], alignment=ft.MainAxisAlignment.CENTER)
    title_text_colmn = ft.Container(content=ft.Column([title_row], horizontal_alignment=ft.MainAxisAlignment.CENTER), bgcolor=ft.colors.TEAL_50, padding=20)
    output_text = ft.Text('Please select N-cell from table', color=ft.colors.BLUE_900, size=16)    
    culc_btn = ft.Container(ft.ElevatedButton('CALCULATE', on_click=N_culc))
    culc_btn.padding = ft.padding.only(bottom=20)
    #----


    await page.add_async(title_text_colmn,
            ft.Container(content=ft.Row([I, L], alignment=ft.MainAxisAlignment.CENTER, spacing=30), padding=20),
            culc_btn,
            output_text,
            ft.Container(content=matrix, bgcolor=ft.colors.BLUE_100, padding=30))
    await page.update_async()


ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

