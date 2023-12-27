import flet as ft
from styles import cell_style


def update_btns(btns_matrix, df):
    for row in btns_matrix:
        for btn in btns_matrix[row]:

            btn_index = btns_matrix[row].index(btn) 

            if row[0] == '0': new_value = str(df[int(row[-1])-1][btn_index])
            else: new_value = str(df[int(row[-2:])-1][btn_index])
        
            btn.text = new_value  #<<< err if axis dublicated need to handle
            btn.style = cell_style(new_value)



async def btns_from_df(df):
        
        btns_matrix = {}

        i = 0    
        btn101 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}01')
        btn102 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}02')
        btn103 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}03')
        btn104 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}04')
        btn105 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}05')
        btn106 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}06')
        btn107 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}07')
        btn108 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}08')
        btn109 = ft.ElevatedButton(f"{df[i][8]}", style=cell_style(df[i][8]), data=f'{i+1}09')
        btn110 = ft.ElevatedButton(f"{df[i][9]}", style=cell_style(df[i][9]), data=f'{i+1}10')
        btn111 = ft.ElevatedButton(f"{df[i][10]}", style=cell_style(df[i][10]), data=f'{i+1}11')
        btn112 = ft.ElevatedButton(f"{df[i][11]}", style=cell_style(df[i][11]), data=f'{i+1}12')
        btn113 = ft.ElevatedButton(f"{df[i][12]}", style=cell_style(df[i][12]), data=f'{i+1}13')
        btn114 = ft.ElevatedButton(f"{df[i][13]}", style=cell_style(df[i][13]), data=f'{i+1}14')
        btn115 = ft.ElevatedButton(f"{df[i][14]}", style=cell_style(df[i][14]), data=f'{i+1}15')
        btn116 = ft.ElevatedButton(f"{df[i][15]}", style=cell_style(df[i][15]), data=f'{i+1}16')
        btn117 = ft.ElevatedButton(f"{df[i][16]}", style=cell_style(df[i][16]), data=f'{i+1}17')
        btn118 = ft.ElevatedButton(f"{df[i][17]}", style=cell_style(df[i][17]), data=f'{i+1}18')
        btn119 = ft.ElevatedButton(f"{df[i][18]}", style=cell_style(df[i][18]), data=f'{i+1}19')
        btn120 = ft.ElevatedButton(f"{df[i][19]}", style=cell_style(df[i][19]), data=f'{i+1}20')
        btns_matrix[f'{i+1}'] = [btn101, btn102, btn103, btn104, btn105, btn106, btn107, btn108,
                                btn109, btn110, btn111, btn112, btn113, btn114, btn115, btn116, btn117, btn118, btn119, btn120]
        

        i = 1    
        btn201 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}01')
        btn202 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}02')
        btn203 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}03')
        btn204 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}04')
        btn205 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}05')
        btn206 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}06')
        btn207 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}07')
        btn208 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}08')
        btn209 = ft.ElevatedButton(f"{df[i][8]}", style=cell_style(df[i][8]), data=f'{i+1}09')
        btn210 = ft.ElevatedButton(f"{df[i][9]}", style=cell_style(df[i][9]), data=f'{i+1}10')
        btn211 = ft.ElevatedButton(f"{df[i][10]}", style=cell_style(df[i][10]), data=f'{i+1}11')
        btn212 = ft.ElevatedButton(f"{df[i][11]}", style=cell_style(df[i][11]), data=f'{i+1}12')
        btn213 = ft.ElevatedButton(f"{df[i][12]}", style=cell_style(df[i][12]), data=f'{i+1}13')
        btn214 = ft.ElevatedButton(f"{df[i][13]}", style=cell_style(df[i][13]), data=f'{i+1}14')
        btn215 = ft.ElevatedButton(f"{df[i][14]}", style=cell_style(df[i][14]), data=f'{i+1}15')
        btn216 = ft.ElevatedButton(f"{df[i][15]}", style=cell_style(df[i][15]), data=f'{i+1}16')
        btn217 = ft.ElevatedButton(f"{df[i][16]}", style=cell_style(df[i][16]), data=f'{i+1}17')
        btn218 = ft.ElevatedButton(f"{df[i][17]}", style=cell_style(df[i][17]), data=f'{i+1}18')
        btn219 = ft.ElevatedButton(f"{df[i][18]}", style=cell_style(df[i][18]), data=f'{i+1}19')
        btn220 = ft.ElevatedButton(f"{df[i][19]}", style=cell_style(df[i][19]), data=f'{i+1}20')
        btns_matrix[f'{i+1}'] = [btn201, btn202, btn203, btn204, btn205, btn206, btn207, btn208,
                                btn209, btn210, btn211, btn212, btn213, btn214, btn215, btn216, btn217, btn218, btn219, btn220]
        
        i = 2    
        btn301 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}01')
        btn302 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}02')
        btn303 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}03')
        btn304 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}04')
        btn305 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}05')
        btn306 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}06')
        btn307 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}07')
        btn308 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}08')
        btn309 = ft.ElevatedButton(f"{df[i][8]}", style=cell_style(df[i][8]), data=f'{i+1}09')
        btn310 = ft.ElevatedButton(f"{df[i][9]}", style=cell_style(df[i][9]), data=f'{i+1}10')
        btn311 = ft.ElevatedButton(f"{df[i][10]}", style=cell_style(df[i][10]), data=f'{i+1}11')
        btn312 = ft.ElevatedButton(f"{df[i][11]}", style=cell_style(df[i][11]), data=f'{i+1}12')
        btn313 = ft.ElevatedButton(f"{df[i][12]}", style=cell_style(df[i][12]), data=f'{i+1}13')
        btn314 = ft.ElevatedButton(f"{df[i][13]}", style=cell_style(df[i][13]), data=f'{i+1}14')
        btn315 = ft.ElevatedButton(f"{df[i][14]}", style=cell_style(df[i][14]), data=f'{i+1}15')
        btn316 = ft.ElevatedButton(f"{df[i][15]}", style=cell_style(df[i][15]), data=f'{i+1}16')
        btn317 = ft.ElevatedButton(f"{df[i][16]}", style=cell_style(df[i][16]), data=f'{i+1}17')
        btn318 = ft.ElevatedButton(f"{df[i][17]}", style=cell_style(df[i][17]), data=f'{i+1}18')
        btn319 = ft.ElevatedButton(f"{df[i][18]}", style=cell_style(df[i][18]), data=f'{i+1}19')
        btn320 = ft.ElevatedButton(f"{df[i][19]}", style=cell_style(df[i][19]), data=f'{i+1}20')
        btns_matrix[f'{i+1}'] = [btn301, btn302, btn303, btn304, btn305, btn306, btn307, btn308,
                                btn309, btn310, btn311, btn312, btn313, btn314, btn315, btn316, btn317, btn318, btn319, btn320]
        

        i = 3   
        btn401 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}01')
        btn402 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}02')
        btn403 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}03')
        btn404 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}04')
        btn405 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}05')
        btn406 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}06')
        btn407 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}07')
        btn408 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}08')
        btn409 = ft.ElevatedButton(f"{df[i][8]}", style=cell_style(df[i][8]), data=f'{i+1}09')
        btn410 = ft.ElevatedButton(f"{df[i][9]}", style=cell_style(df[i][9]), data=f'{i+1}10')
        btn411 = ft.ElevatedButton(f"{df[i][10]}", style=cell_style(df[i][10]), data=f'{i+1}11')
        btn412 = ft.ElevatedButton(f"{df[i][11]}", style=cell_style(df[i][11]), data=f'{i+1}12')
        btn413 = ft.ElevatedButton(f"{df[i][12]}", style=cell_style(df[i][12]), data=f'{i+1}13')
        btn414 = ft.ElevatedButton(f"{df[i][13]}", style=cell_style(df[i][13]), data=f'{i+1}14')
        btn415 = ft.ElevatedButton(f"{df[i][14]}", style=cell_style(df[i][14]), data=f'{i+1}15')
        btn416 = ft.ElevatedButton(f"{df[i][15]}", style=cell_style(df[i][15]), data=f'{i+1}16')
        btn417 = ft.ElevatedButton(f"{df[i][16]}", style=cell_style(df[i][16]), data=f'{i+1}17')
        btn418 = ft.ElevatedButton(f"{df[i][17]}", style=cell_style(df[i][17]), data=f'{i+1}18')
        btn419 = ft.ElevatedButton(f"{df[i][18]}", style=cell_style(df[i][18]), data=f'{i+1}19')
        btn420 = ft.ElevatedButton(f"{df[i][19]}", style=cell_style(df[i][19]), data=f'{i+1}20')
        btns_matrix[f'{i+1}'] = [btn401, btn402, btn403, btn404, btn405, btn406, btn407, btn408,
                                btn409, btn410, btn411, btn412, btn413, btn414, btn415, btn416, btn417, btn418, btn419, btn420]
        

        i = 4    
        btn501 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}01')
        btn502 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}02')
        btn503 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}03')
        btn504 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}04')
        btn505 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}05')
        btn506 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}06')
        btn507 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}07')
        btn508 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}08')
        btn509 = ft.ElevatedButton(f"{df[i][8]}", style=cell_style(df[i][8]), data=f'{i+1}09')
        btn510 = ft.ElevatedButton(f"{df[i][9]}", style=cell_style(df[i][9]), data=f'{i+1}10')
        btn511 = ft.ElevatedButton(f"{df[i][10]}", style=cell_style(df[i][10]), data=f'{i+1}11')
        btn512 = ft.ElevatedButton(f"{df[i][11]}", style=cell_style(df[i][11]), data=f'{i+1}12')
        btn513 = ft.ElevatedButton(f"{df[i][12]}", style=cell_style(df[i][12]), data=f'{i+1}13')
        btn514 = ft.ElevatedButton(f"{df[i][13]}", style=cell_style(df[i][13]), data=f'{i+1}14')
        btn515 = ft.ElevatedButton(f"{df[i][14]}", style=cell_style(df[i][14]), data=f'{i+1}15')
        btn516 = ft.ElevatedButton(f"{df[i][15]}", style=cell_style(df[i][15]), data=f'{i+1}16')
        btn517 = ft.ElevatedButton(f"{df[i][16]}", style=cell_style(df[i][16]), data=f'{i+1}17')
        btn518 = ft.ElevatedButton(f"{df[i][17]}", style=cell_style(df[i][17]), data=f'{i+1}18')
        btn519 = ft.ElevatedButton(f"{df[i][18]}", style=cell_style(df[i][18]), data=f'{i+1}19')
        btn520 = ft.ElevatedButton(f"{df[i][19]}", style=cell_style(df[i][19]), data=f'{i+1}20')
        btns_matrix[f'{i+1}'] = [btn501, btn502, btn503, btn504, btn505, btn506, btn507, btn508,
                                btn509, btn510, btn511, btn512, btn513, btn514, btn515, btn516, btn517, btn518, btn519, btn520]
        

        i = 5    
        btn601 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}01')
        btn602 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}02')
        btn603 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}03')
        btn604 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}04')
        btn605 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}05')
        btn606 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}06')
        btn607 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}07')
        btn608 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}08')
        btn609 = ft.ElevatedButton(f"{df[i][8]}", style=cell_style(df[i][8]), data=f'{i+1}09')
        btn610 = ft.ElevatedButton(f"{df[i][9]}", style=cell_style(df[i][9]), data=f'{i+1}10')
        btn611 = ft.ElevatedButton(f"{df[i][10]}", style=cell_style(df[i][10]), data=f'{i+1}11')
        btn612 = ft.ElevatedButton(f"{df[i][11]}", style=cell_style(df[i][11]), data=f'{i+1}12')
        btn613 = ft.ElevatedButton(f"{df[i][12]}", style=cell_style(df[i][12]), data=f'{i+1}13')
        btn614 = ft.ElevatedButton(f"{df[i][13]}", style=cell_style(df[i][13]), data=f'{i+1}14')
        btn615 = ft.ElevatedButton(f"{df[i][14]}", style=cell_style(df[i][14]), data=f'{i+1}15')
        btn616 = ft.ElevatedButton(f"{df[i][15]}", style=cell_style(df[i][15]), data=f'{i+1}16')
        btn617 = ft.ElevatedButton(f"{df[i][16]}", style=cell_style(df[i][16]), data=f'{i+1}17')
        btn618 = ft.ElevatedButton(f"{df[i][17]}", style=cell_style(df[i][17]), data=f'{i+1}18')
        btn619 = ft.ElevatedButton(f"{df[i][18]}", style=cell_style(df[i][18]), data=f'{i+1}19')
        btn620 = ft.ElevatedButton(f"{df[i][19]}", style=cell_style(df[i][19]), data=f'{i+1}20')
        btns_matrix[f'{i+1}'] = [btn601, btn602, btn603, btn604, btn605, btn606, btn607, btn608,
                                btn609, btn610, btn611, btn612, btn613, btn614, btn615, btn616, btn617, btn618, btn619, btn620]
        

        i = 6   
        btn701 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}01')
        btn702 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}02')
        btn703 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}03')
        btn704 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}04')
        btn705 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}05')
        btn706 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}06')
        btn707 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}07')
        btn708 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}08')
        btn709 = ft.ElevatedButton(f"{df[i][8]}", style=cell_style(df[i][8]), data=f'{i+1}09')
        btn710 = ft.ElevatedButton(f"{df[i][9]}", style=cell_style(df[i][9]), data=f'{i+1}10')
        btn711 = ft.ElevatedButton(f"{df[i][10]}", style=cell_style(df[i][10]), data=f'{i+1}11')
        btn712 = ft.ElevatedButton(f"{df[i][11]}", style=cell_style(df[i][11]), data=f'{i+1}12')
        btn713 = ft.ElevatedButton(f"{df[i][12]}", style=cell_style(df[i][12]), data=f'{i+1}13')
        btn714 = ft.ElevatedButton(f"{df[i][13]}", style=cell_style(df[i][13]), data=f'{i+1}14')
        btn715 = ft.ElevatedButton(f"{df[i][14]}", style=cell_style(df[i][14]), data=f'{i+1}15')
        btn716 = ft.ElevatedButton(f"{df[i][15]}", style=cell_style(df[i][15]), data=f'{i+1}16')
        btn717 = ft.ElevatedButton(f"{df[i][16]}", style=cell_style(df[i][16]), data=f'{i+1}17')
        btn718 = ft.ElevatedButton(f"{df[i][17]}", style=cell_style(df[i][17]), data=f'{i+1}18')
        btn719 = ft.ElevatedButton(f"{df[i][18]}", style=cell_style(df[i][18]), data=f'{i+1}19')
        btn720 = ft.ElevatedButton(f"{df[i][19]}", style=cell_style(df[i][19]), data=f'{i+1}20')
        btns_matrix[f'{i+1}'] = [btn701, btn702, btn703, btn704, btn705, btn706, btn707, btn708,
                                btn709, btn710, btn711, btn712, btn713, btn714, btn715, btn716, btn717, btn718, btn719, btn720]
        

        i = 7   
        btn801 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}01')
        btn802 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}02')
        btn803 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}03')
        btn804 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}04')
        btn805 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}05')
        btn806 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}06')
        btn807 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}07')
        btn808 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}08')
        btn809 = ft.ElevatedButton(f"{df[i][8]}", style=cell_style(df[i][8]), data=f'{i+1}09')
        btn810 = ft.ElevatedButton(f"{df[i][9]}", style=cell_style(df[i][9]), data=f'{i+1}10')
        btn811 = ft.ElevatedButton(f"{df[i][10]}", style=cell_style(df[i][10]), data=f'{i+1}11')
        btn812 = ft.ElevatedButton(f"{df[i][11]}", style=cell_style(df[i][11]), data=f'{i+1}12')
        btn813 = ft.ElevatedButton(f"{df[i][12]}", style=cell_style(df[i][12]), data=f'{i+1}13')
        btn814 = ft.ElevatedButton(f"{df[i][13]}", style=cell_style(df[i][13]), data=f'{i+1}14')
        btn815 = ft.ElevatedButton(f"{df[i][14]}", style=cell_style(df[i][14]), data=f'{i+1}15')
        btn816 = ft.ElevatedButton(f"{df[i][15]}", style=cell_style(df[i][15]), data=f'{i+1}16')
        btn817 = ft.ElevatedButton(f"{df[i][16]}", style=cell_style(df[i][16]), data=f'{i+1}17')
        btn818 = ft.ElevatedButton(f"{df[i][17]}", style=cell_style(df[i][17]), data=f'{i+1}18')
        btn819 = ft.ElevatedButton(f"{df[i][18]}", style=cell_style(df[i][18]), data=f'{i+1}19')
        btn820 = ft.ElevatedButton(f"{df[i][19]}", style=cell_style(df[i][19]), data=f'{i+1}20')
        btns_matrix[f'{i+1}'] = [btn801, btn802, btn803, btn804, btn805, btn806, btn807, btn808,
                                btn809, btn810, btn811, btn812, btn813, btn814, btn815, btn816, btn817, btn818, btn819, btn820]



        return btns_matrix


