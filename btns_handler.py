import flet as ft
from styles import cell_style


def update_btns(btns_matrix, df, formating_grades):
    minPrice_value = 10000000000
    for row in btns_matrix:
        for btn in btns_matrix[row]:

            btn_index = btns_matrix[row].index(btn) 

            if row[0] == '0':
                newN_value = str(df[int(row[-1])-1][btn_index]['N'])
                newPrice_value = str(df[int(row[-1])-1][btn_index]['price'])
            else:
                if df[int(row[-2:])-1][btn_index]:
                    newN_value = str(df[int(row[-2:])-1][btn_index]['N'])
                    newPrice_value = str(df[int(row[-2:])-1][btn_index]['price'])
                else:
                    newN_value = None
                    newPrice_value = None       
            btn.text = newN_value
            btn.style = cell_style(newPrice_value, formating_grades)
            #SET FOCUSED BUTTON - minPriceBtn
            if newPrice_value != ('None' or None):
                if float(newPrice_value) < float(minPrice_value):
                    minPrice_value = newPrice_value
                    minPrice_btn = btn

    minPrice_btn.style = cell_style(0, None)
    return minPrice_btn


def btns_from_df(df, formating_grades):

        btns_matrix = {}

        i = 0    
        btn101 = ft.ElevatedButton(f"{df[i][0]['N']}", style=cell_style(df[i][0]['price'], formating_grades), data=[f'{i+1}01', df[i][0]['price']])
        btn102 = ft.ElevatedButton(f"{df[i][1]['N']}", style=cell_style(df[i][1]['price'], formating_grades), data=[f'{i+1}02', df[i][1]['price']])
        btn103 = ft.ElevatedButton(f"{df[i][2]['N']}", style=cell_style(df[i][2]['price'], formating_grades), data=[f'{i+1}03', df[i][2]['price']])
        btn104 = ft.ElevatedButton(f"{df[i][3]['N']}", style=cell_style(df[i][3]['price'], formating_grades), data=[f'{i+1}04', df[i][3]['price']])
        btn105 = ft.ElevatedButton(f"{df[i][4]['N']}", style=cell_style(df[i][4]['price'], formating_grades), data=[f'{i+1}05', df[i][4]['price']])
        btn106 = ft.ElevatedButton(f"{df[i][5]['N']}", style=cell_style(df[i][5]['price'], formating_grades), data=[f'{i+1}06', df[i][5]['price']])
        btn107 = ft.ElevatedButton(f"{df[i][6]['N']}", style=cell_style(df[i][6]['price'], formating_grades), data=[f'{i+1}07', df[i][6]['price']])
        btn108 = ft.ElevatedButton(f"{df[i][7]['N']}", style=cell_style(df[i][7]['price'], formating_grades), data=[f'{i+1}08', df[i][7]['price']])
        btn109 = ft.ElevatedButton(f"{df[i][8]['N']}", style=cell_style(df[i][8]['price'], formating_grades), data=[f'{i+1}09', df[i][8]['price']])
        btn110 = ft.ElevatedButton(f"{df[i][9]['N']}", style=cell_style(df[i][9]['price'], formating_grades), data=[f'{i+1}10', df[i][9]['price']])
        btn111 = ft.ElevatedButton(f"{df[i][10]['N']}", style=cell_style(df[i][10]['price'], formating_grades), data=[f'{i+1}11', df[i][10]['price']])
        btn112 = ft.ElevatedButton(f"{df[i][11]['N']}", style=cell_style(df[i][11]['price'], formating_grades), data=[f'{i+1}12', df[i][11]['price']])
        btn113 = ft.ElevatedButton(f"{df[i][12]['N']}", style=cell_style(df[i][12]['price'], formating_grades), data=[f'{i+1}13', df[i][12]['price']])
        btn114 = ft.ElevatedButton(f"{df[i][13]['N']}", style=cell_style(df[i][13]['price'], formating_grades), data=[f'{i+1}14', df[i][13]['price']])
        btn115 = ft.ElevatedButton(f"{df[i][14]['N']}", style=cell_style(df[i][14]['price'], formating_grades), data=[f'{i+1}15', df[i][14]['price']])
        btn116 = ft.ElevatedButton(f"{df[i][15]['N']}", style=cell_style(df[i][15]['price'], formating_grades), data=[f'{i+1}16', df[i][15]['price']])
        btn117 = ft.ElevatedButton(f"{df[i][16]['N']}", style=cell_style(df[i][16]['price'], formating_grades), data=[f'{i+1}17', df[i][16]['price']])
        btn118 = ft.ElevatedButton(f"{df[i][17]['N']}", style=cell_style(df[i][17]['price'], formating_grades), data=[f'{i+1}18', df[i][17]['price']])
        btns_matrix[f'{i+1}'] = [btn101, btn102, btn103, btn104, btn105, btn106, btn107, btn108,
                                btn109, btn110, btn111, btn112, btn113, btn114, btn115, btn116, btn117, btn118]
        

        i = 1    
        btn201 = ft.ElevatedButton(f"{df[i][0]['N']}", style=cell_style(df[i][0]['price'], formating_grades), data=[f'{i+1}01', df[i][0]['price']])
        btn202 = ft.ElevatedButton(f"{df[i][1]['N']}", style=cell_style(df[i][1]['price'], formating_grades), data=[f'{i+1}02', df[i][1]['price']])
        btn203 = ft.ElevatedButton(f"{df[i][2]['N']}", style=cell_style(df[i][2]['price'], formating_grades), data=[f'{i+1}03', df[i][2]['price']])
        btn204 = ft.ElevatedButton(f"{df[i][3]['N']}", style=cell_style(df[i][3]['price'], formating_grades), data=[f'{i+1}04', df[i][3]['price']])
        btn205 = ft.ElevatedButton(f"{df[i][4]['N']}", style=cell_style(df[i][4]['price'], formating_grades), data=[f'{i+1}05', df[i][4]['price']])
        btn206 = ft.ElevatedButton(f"{df[i][5]['N']}", style=cell_style(df[i][5]['price'], formating_grades), data=[f'{i+1}06', df[i][5]['price']])
        btn207 = ft.ElevatedButton(f"{df[i][5]['N']}", style=cell_style(df[i][5]['price'], formating_grades), data=[f'{i+1}07', df[i][6]['price']])
        btn208 = ft.ElevatedButton(f"{df[i][7]['N']}", style=cell_style(df[i][7]['price'], formating_grades), data=[f'{i+1}08', df[i][7]['price']])
        btn209 = ft.ElevatedButton(f"{df[i][8]['N']}", style=cell_style(df[i][8]['price'], formating_grades), data=[f'{i+1}09', df[i][8]['price']])
        btn210 = ft.ElevatedButton(f"{df[i][9]['N']}", style=cell_style(df[i][9]['price'], formating_grades), data=[f'{i+1}10', df[i][9]['price']])
        btn211 = ft.ElevatedButton(f"{df[i][10]['N']}", style=cell_style(df[i][10]['price'], formating_grades), data=[f'{i+1}11', df[i][10]['price']])
        btn212 = ft.ElevatedButton(f"{df[i][11]['N']}", style=cell_style(df[i][11]['price'], formating_grades), data=[f'{i+1}12', df[i][11]['price']])
        btn213 = ft.ElevatedButton(f"{df[i][12]['N']}", style=cell_style(df[i][12]['price'], formating_grades), data=[f'{i+1}13', df[i][12]['price']])
        btn214 = ft.ElevatedButton(f"{df[i][13]['N']}", style=cell_style(df[i][13]['price'], formating_grades), data=[f'{i+1}14', df[i][13]['price']])
        btn215 = ft.ElevatedButton(f"{df[i][14]['N']}", style=cell_style(df[i][14]['price'], formating_grades), data=[f'{i+1}15', df[i][14]['price']])
        btn216 = ft.ElevatedButton(f"{df[i][15]['N']}", style=cell_style(df[i][15]['price'], formating_grades), data=[f'{i+1}16', df[i][15]['price']])
        btn217 = ft.ElevatedButton(f"{df[i][16]['N']}", style=cell_style(df[i][16]['price'], formating_grades), data=[f'{i+1}17', df[i][16]['price']])
        btn218 = ft.ElevatedButton(f"{df[i][17]['N']}", style=cell_style(df[i][17]['price'], formating_grades), data=[f'{i+1}18', df[i][17]['price']])
        btns_matrix[f'{i+1}'] = [btn201, btn202, btn203, btn204, btn205, btn206, btn207, btn208,
                                btn209, btn210, btn211, btn212, btn213, btn214, btn215, btn216, btn217, btn218]
        i = 2    
        btn301 = ft.ElevatedButton(f"{df[i][0]['N']}", style=cell_style(df[i][0]['price'], formating_grades), data=[f'{i+1}01', df[i][0]['price']])
        btn302 = ft.ElevatedButton(f"{df[i][1]['N']}", style=cell_style(df[i][1]['price'], formating_grades), data=[f'{i+1}02', df[i][1]['price']])
        btn303 = ft.ElevatedButton(f"{df[i][2]['N']}", style=cell_style(df[i][2]['price'], formating_grades), data=[f'{i+1}03', df[i][2]['price']])
        btn304 = ft.ElevatedButton(f"{df[i][3]['N']}", style=cell_style(df[i][3]['price'], formating_grades), data=[f'{i+1}04', df[i][3]['price']])
        btn305 = ft.ElevatedButton(f"{df[i][4]['N']}", style=cell_style(df[i][4]['price'], formating_grades), data=[f'{i+1}05', df[i][4]['price']])
        btn306 = ft.ElevatedButton(f"{df[i][5]['N']}", style=cell_style(df[i][5]['price'], formating_grades), data=[f'{i+1}06', df[i][5]['price']])
        btn307 = ft.ElevatedButton(f"{df[i][6]['N']}", style=cell_style(df[i][6]['price'], formating_grades), data=[f'{i+1}07', df[i][6]['price']])
        btn308 = ft.ElevatedButton(f"{df[i][7]['N']}", style=cell_style(df[i][7]['price'], formating_grades), data=[f'{i+1}08', df[i][7]['price']])
        btn309 = ft.ElevatedButton(f"{df[i][8]['N']}", style=cell_style(df[i][8]['price'], formating_grades), data=[f'{i+1}09', df[i][8]['price']])
        btn310 = ft.ElevatedButton(f"{df[i][9]['N']}", style=cell_style(df[i][9]['price'], formating_grades), data=[f'{i+1}10', df[i][9]['price']])
        btn311 = ft.ElevatedButton(f"{df[i][10]['N']}", style=cell_style(df[i][10]['price'], formating_grades), data=[f'{i+1}11', df[i][10]['price']])
        btn312 = ft.ElevatedButton(f"{df[i][11]['N']}", style=cell_style(df[i][11]['price'], formating_grades), data=[f'{i+1}12', df[i][11]['price']])
        btn313 = ft.ElevatedButton(f"{df[i][12]['N']}", style=cell_style(df[i][12]['price'], formating_grades), data=[f'{i+1}13', df[i][12]['price']])
        btn314 = ft.ElevatedButton(f"{df[i][13]['N']}", style=cell_style(df[i][13]['price'], formating_grades), data=[f'{i+1}14', df[i][13]['price']])
        btn315 = ft.ElevatedButton(f"{df[i][14]['N']}", style=cell_style(df[i][14]['price'], formating_grades), data=[f'{i+1}15', df[i][14]['price']])
        btn316 = ft.ElevatedButton(f"{df[i][15]['N']}", style=cell_style(df[i][15]['price'], formating_grades), data=[f'{i+1}16', df[i][15]['price']])
        btn317 = ft.ElevatedButton(f"{df[i][16]['N']}", style=cell_style(df[i][16]['price'], formating_grades), data=[f'{i+1}17', df[i][16]['price']])
        btn318 = ft.ElevatedButton(f"{df[i][17]['N']}", style=cell_style(df[i][17]['price'], formating_grades), data=[f'{i+1}18', df[i][17]['price']])
        btns_matrix[f'{i+1}'] = [btn301, btn302, btn303, btn304, btn305, btn306, btn307, btn308,
                                btn309, btn310, btn311, btn312, btn313, btn314, btn315, btn316, btn317, btn318]
        

        i = 3   
        btn401 = ft.ElevatedButton(f"{df[i][0]['N']}", style=cell_style(df[i][0]['price'], formating_grades), data=[f'{i+1}01', df[i][0]['price']])
        btn402 = ft.ElevatedButton(f"{df[i][1]['N']}", style=cell_style(df[i][1]['price'], formating_grades), data=[f'{i+1}02', df[i][1]['price']])
        btn403 = ft.ElevatedButton(f"{df[i][2]['N']}", style=cell_style(df[i][2]['price'], formating_grades), data=[f'{i+1}03', df[i][2]['price']])
        btn404 = ft.ElevatedButton(f"{df[i][3]['N']}", style=cell_style(df[i][3]['price'], formating_grades), data=[f'{i+1}04', df[i][3]['price']])
        btn405 = ft.ElevatedButton(f"{df[i][4]['N']}", style=cell_style(df[i][4]['price'], formating_grades), data=[f'{i+1}05', df[i][4]['price']])
        btn406 = ft.ElevatedButton(f"{df[i][5]['N']}", style=cell_style(df[i][5]['price'], formating_grades), data=[f'{i+1}06', df[i][5]['price']])
        btn407 = ft.ElevatedButton(f"{df[i][6]['N']}", style=cell_style(df[i][6]['price'], formating_grades), data=[f'{i+1}07', df[i][6]['price']])
        btn408 = ft.ElevatedButton(f"{df[i][7]['N']}", style=cell_style(df[i][7]['price'], formating_grades), data=[f'{i+1}08', df[i][7]['price']])
        btn409 = ft.ElevatedButton(f"{df[i][8]['N']}", style=cell_style(df[i][8]['price'], formating_grades), data=[f'{i+1}09', df[i][8]['price']])
        btn410 = ft.ElevatedButton(f"{df[i][9]['N']}", style=cell_style(df[i][9]['price'], formating_grades), data=[f'{i+1}10', df[i][9]['price']])
        btn411 = ft.ElevatedButton(f"{df[i][10]['N']}", style=cell_style(df[i][10]['price'], formating_grades), data=[f'{i+1}11', df[i][10]['price']])
        btn412 = ft.ElevatedButton(f"{df[i][11]['N']}", style=cell_style(df[i][11]['price'], formating_grades), data=[f'{i+1}12', df[i][11]['price']])
        btn413 = ft.ElevatedButton(f"{df[i][12]['N']}", style=cell_style(df[i][12]['price'], formating_grades), data=[f'{i+1}13', df[i][12]['price']])
        btn414 = ft.ElevatedButton(f"{df[i][13]['N']}", style=cell_style(df[i][13]['price'], formating_grades), data=[f'{i+1}14', df[i][13]['price']])
        btn415 = ft.ElevatedButton(f"{df[i][14]['N']}", style=cell_style(df[i][14]['price'], formating_grades), data=[f'{i+1}15', df[i][14]['price']])
        btn416 = ft.ElevatedButton(f"{df[i][15]['N']}", style=cell_style(df[i][15]['price'], formating_grades), data=[f'{i+1}16', df[i][15]['price']])
        btn417 = ft.ElevatedButton(f"{df[i][16]['N']}", style=cell_style(df[i][16]['price'], formating_grades), data=[f'{i+1}17', df[i][16]['price']])
        btn418 = ft.ElevatedButton(f"{df[i][17]['N']}", style=cell_style(df[i][17]['price'], formating_grades), data=[f'{i+1}18', df[i][17]['price']])
        btns_matrix[f'{i+1}'] = [btn401, btn402, btn403, btn404, btn405, btn406, btn407, btn408,
                                btn409, btn410, btn411, btn412, btn413, btn414, btn415, btn416, btn417, btn418]
        

        i = 4    
        btn501 = ft.ElevatedButton(f"{df[i][0]['N']}", style=cell_style(df[i][0]['price'], formating_grades), data=[f'{i+1}01', df[i][0]['price']])
        btn502 = ft.ElevatedButton(f"{df[i][1]['N']}", style=cell_style(df[i][1]['price'], formating_grades), data=[f'{i+1}02', df[i][1]['price']])
        btn503 = ft.ElevatedButton(f"{df[i][2]['N']}", style=cell_style(df[i][2]['price'], formating_grades), data=[f'{i+1}03', df[i][2]['price']])
        btn504 = ft.ElevatedButton(f"{df[i][3]['N']}", style=cell_style(df[i][3]['price'], formating_grades), data=[f'{i+1}04', df[i][3]['price']])
        btn505 = ft.ElevatedButton(f"{df[i][4]['N']}", style=cell_style(df[i][4]['price'], formating_grades), data=[f'{i+1}05', df[i][4]['price']])
        btn506 = ft.ElevatedButton(f"{df[i][5]['N']}", style=cell_style(df[i][5]['price'], formating_grades), data=[f'{i+1}06', df[i][5]['price']])
        btn507 = ft.ElevatedButton(f"{df[i][6]['N']}", style=cell_style(df[i][6]['price'], formating_grades), data=[f'{i+1}07', df[i][6]['price']])
        btn508 = ft.ElevatedButton(f"{df[i][7]['N']}", style=cell_style(df[i][7]['price'], formating_grades), data=[f'{i+1}08', df[i][7]['price']])
        btn509 = ft.ElevatedButton(f"{df[i][8]['N']}", style=cell_style(df[i][8]['price'], formating_grades), data=[f'{i+1}09', df[i][8]['price']])
        btn510 = ft.ElevatedButton(f"{df[i][9]['N']}", style=cell_style(df[i][9]['price'], formating_grades), data=[f'{i+1}10', df[i][9]['price']])
        btn511 = ft.ElevatedButton(f"{df[i][10]['N']}", style=cell_style(df[i][10]['price'], formating_grades), data=[f'{i+1}11', df[i][10]['price']])
        btn512 = ft.ElevatedButton(f"{df[i][11]['N']}", style=cell_style(df[i][11]['price'], formating_grades), data=[f'{i+1}12', df[i][11]['price']])
        btn513 = ft.ElevatedButton(f"{df[i][12]['N']}", style=cell_style(df[i][12]['price'], formating_grades), data=[f'{i+1}13', df[i][12]['price']])
        btn514 = ft.ElevatedButton(f"{df[i][13]['N']}", style=cell_style(df[i][13]['price'], formating_grades), data=[f'{i+1}14', df[i][13]['price']])
        btn515 = ft.ElevatedButton(f"{df[i][14]['N']}", style=cell_style(df[i][14]['price'], formating_grades), data=[f'{i+1}15', df[i][14]['price']])
        btn516 = ft.ElevatedButton(f"{df[i][15]['N']}", style=cell_style(df[i][15]['price'], formating_grades), data=[f'{i+1}16', df[i][15]['price']])
        btn517 = ft.ElevatedButton(f"{df[i][16]['N']}", style=cell_style(df[i][16]['price'], formating_grades), data=[f'{i+1}17', df[i][16]['price']])
        btn518 = ft.ElevatedButton(f"{df[i][17]['N']}", style=cell_style(df[i][17]['price'], formating_grades), data=[f'{i+1}18', df[i][17]['price']])
        btns_matrix[f'{i+1}'] = [btn501, btn502, btn503, btn504, btn505, btn506, btn507, btn508,
                                btn509, btn510, btn511, btn512, btn513, btn514, btn515, btn516, btn517, btn518]
        

        i = 5    
        btn601 = ft.ElevatedButton(f"{df[i][0]['N']}", style=cell_style(df[i][0]['price'], formating_grades), data=[f'{i+1}01', df[i][0]['price']])
        btn602 = ft.ElevatedButton(f"{df[i][1]['N']}", style=cell_style(df[i][1]['price'], formating_grades), data=[f'{i+1}02', df[i][1]['price']])
        btn603 = ft.ElevatedButton(f"{df[i][2]['N']}", style=cell_style(df[i][2]['price'], formating_grades), data=[f'{i+1}03', df[i][2]['price']])
        btn604 = ft.ElevatedButton(f"{df[i][3]['N']}", style=cell_style(df[i][3]['price'], formating_grades), data=[f'{i+1}04', df[i][3]['price']])
        btn605 = ft.ElevatedButton(f"{df[i][4]['N']}", style=cell_style(df[i][4]['price'], formating_grades), data=[f'{i+1}05', df[i][4]['price']])
        btn606 = ft.ElevatedButton(f"{df[i][5]['N']}", style=cell_style(df[i][5]['price'], formating_grades), data=[f'{i+1}06', df[i][5]['price']])
        btn607 = ft.ElevatedButton(f"{df[i][6]['N']}", style=cell_style(df[i][6]['price'], formating_grades), data=[f'{i+1}07', df[i][6]['price']])
        btn608 = ft.ElevatedButton(f"{df[i][7]['N']}", style=cell_style(df[i][7]['price'], formating_grades), data=[f'{i+1}08', df[i][7]['price']])
        btn609 = ft.ElevatedButton(f"{df[i][8]['N']}", style=cell_style(df[i][8]['price'], formating_grades), data=[f'{i+1}09', df[i][8]['price']])
        btn610 = ft.ElevatedButton(f"{df[i][9]['N']}", style=cell_style(df[i][9]['price'], formating_grades), data=[f'{i+1}10', df[i][9]['price']])
        btn611 = ft.ElevatedButton(f"{df[i][10]['N']}", style=cell_style(df[i][10]['price'], formating_grades), data=[f'{i+1}11', df[i][10]['price']])
        btn612 = ft.ElevatedButton(f"{df[i][11]['N']}", style=cell_style(df[i][11]['price'], formating_grades), data=[f'{i+1}12', df[i][11]['price']])
        btn613 = ft.ElevatedButton(f"{df[i][12]['N']}", style=cell_style(df[i][12]['price'], formating_grades), data=[f'{i+1}13', df[i][12]['price']])
        btn614 = ft.ElevatedButton(f"{df[i][13]['N']}", style=cell_style(df[i][13]['price'], formating_grades), data=[f'{i+1}14', df[i][13]['price']])
        btn615 = ft.ElevatedButton(f"{df[i][14]['N']}", style=cell_style(df[i][14]['price'], formating_grades), data=[f'{i+1}15', df[i][14]['price']])
        btn616 = ft.ElevatedButton(f"{df[i][15]['N']}", style=cell_style(df[i][15]['price'], formating_grades), data=[f'{i+1}16', df[i][15]['price']])
        btn617 = ft.ElevatedButton(f"{df[i][16]['N']}", style=cell_style(df[i][16]['price'], formating_grades), data=[f'{i+1}17', df[i][16]['price']])
        btn618 = ft.ElevatedButton(f"{df[i][17]['N']}", style=cell_style(df[i][17]['price'], formating_grades), data=[f'{i+1}18', df[i][17]['price']])
        btns_matrix[f'{i+1}'] = [btn601, btn602, btn603, btn604, btn605, btn606, btn607, btn608,
                                btn609, btn610, btn611, btn612, btn613, btn614, btn615, btn616, btn617, btn618]
        

        i = 6   
        btn701 = ft.ElevatedButton(f"{df[i][0]['N']}", style=cell_style(df[i][0]['price'], formating_grades), data=[f'{i+1}01', df[i][0]['price']])
        btn702 = ft.ElevatedButton(f"{df[i][1]['N']}", style=cell_style(df[i][1]['price'], formating_grades), data=[f'{i+1}02', df[i][1]['price']])
        btn703 = ft.ElevatedButton(f"{df[i][2]['N']}", style=cell_style(df[i][2]['price'], formating_grades), data=[f'{i+1}03', df[i][2]['price']])
        btn704 = ft.ElevatedButton(f"{df[i][3]['N']}", style=cell_style(df[i][3]['price'], formating_grades), data=[f'{i+1}04', df[i][3]['price']])
        btn705 = ft.ElevatedButton(f"{df[i][4]['N']}", style=cell_style(df[i][4]['price'], formating_grades), data=[f'{i+1}05', df[i][4]['price']])
        btn706 = ft.ElevatedButton(f"{df[i][5]['N']}", style=cell_style(df[i][5]['price'], formating_grades), data=[f'{i+1}06', df[i][5]['price']])
        btn707 = ft.ElevatedButton(f"{df[i][6]['N']}", style=cell_style(df[i][6]['price'], formating_grades), data=[f'{i+1}07', df[i][6]['price']])
        btn708 = ft.ElevatedButton(f"{df[i][7]['N']}", style=cell_style(df[i][7]['price'], formating_grades), data=[f'{i+1}08', df[i][7]['price']])
        btn709 = ft.ElevatedButton(f"{df[i][8]['N']}", style=cell_style(df[i][8]['price'], formating_grades), data=[f'{i+1}09', df[i][8]['price']])
        btn710 = ft.ElevatedButton(f"{df[i][9]['N']}", style=cell_style(df[i][9]['price'], formating_grades), data=[f'{i+1}10', df[i][9]['price']])
        btn711 = ft.ElevatedButton(f"{df[i][10]['N']}", style=cell_style(df[i][10]['price'], formating_grades), data=[f'{i+1}11', df[i][10]['price']])
        btn712 = ft.ElevatedButton(f"{df[i][11]['N']}", style=cell_style(df[i][11]['price'], formating_grades), data=[f'{i+1}12', df[i][11]['price']])
        btn713 = ft.ElevatedButton(f"{df[i][12]['N']}", style=cell_style(df[i][12]['price'], formating_grades), data=[f'{i+1}13', df[i][12]['price']])
        btn714 = ft.ElevatedButton(f"{df[i][13]['N']}", style=cell_style(df[i][13]['price'], formating_grades), data=[f'{i+1}14', df[i][13]['price']])
        btn715 = ft.ElevatedButton(f"{df[i][14]['N']}", style=cell_style(df[i][14]['price'], formating_grades), data=[f'{i+1}15', df[i][14]['price']])
        btn716 = ft.ElevatedButton(f"{df[i][15]['N']}", style=cell_style(df[i][15]['price'], formating_grades), data=[f'{i+1}16', df[i][15]['price']])
        btn717 = ft.ElevatedButton(f"{df[i][16]['N']}", style=cell_style(df[i][16]['price'], formating_grades), data=[f'{i+1}17', df[i][16]['price']])
        btn718 = ft.ElevatedButton(f"{df[i][17]['N']}", style=cell_style(df[i][17]['price'], formating_grades), data=[f'{i+1}18', df[i][17]['price']])
        btns_matrix[f'{i+1}'] = [btn701, btn702, btn703, btn704, btn705, btn706, btn707, btn708,
                                btn709, btn710, btn711, btn712, btn713, btn714, btn715, btn716, btn717, btn718]
        

        return btns_matrix


