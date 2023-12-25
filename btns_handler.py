import flet as ft
from styles import cell_style


def update_btns(btns_matrix, df, H_list, Mu_list):
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
        btn011 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'0{i+1}1')
        btn012 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'0{i+1}2')
        btn013 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'0{i+1}3')
        btn014 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'0{i+1}4')
        btn015 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'0{i+1}5')
        btn016 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'0{i+1}6')
        btn017 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'0{i+1}7')
        btn018 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'0{i+1}8')
        btns_matrix[f'0{i+1}'] = [btn011, btn012, btn013, btn014, btn015, btn016, btn017, btn018]

        i = 1
        btn021 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'0{i+1}1')
        btn022 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'0{i+1}2')
        btn023 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'0{i+1}3')
        btn024 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'0{i+1}4')
        btn025 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'0{i+1}5')
        btn026 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'0{i+1}6')
        btn027 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'0{i+1}7')
        btn028 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'0{i+1}8')
        btns_matrix[f'0{i+1}'] = [btn021, btn022, btn023, btn024, btn025, btn026, btn027, btn028]
        
        i = 2
        btn031 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'0{i+1}1')
        btn032 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'0{i+1}2')
        btn033 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'0{i+1}3')
        btn034 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'0{i+1}4')
        btn035 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'0{i+1}5')
        btn036 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'0{i+1}6')
        btn037 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'0{i+1}7')
        btn038 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'0{i+1}8')
        btns_matrix[f'0{i+1}'] = [btn031, btn032, btn033, btn034, btn035, btn036, btn037, btn038]

        i = 3
        btn041 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'0{i+1}1')
        btn042 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'0{i+1}2')
        btn043 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'0{i+1}3')
        btn044 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'0{i+1}4')
        btn045 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'0{i+1}5')
        btn046 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'0{i+1}6')
        btn047 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'0{i+1}7')
        btn048 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'0{i+1}8')
        btns_matrix[f'0{i+1}'] = [btn041, btn042, btn043, btn044, btn045, btn046, btn047, btn048]

        i = 4
        btn051 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'0{i+1}1')
        btn052 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'0{i+1}2')
        btn053 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'0{i+1}3')
        btn054 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'0{i+1}4')
        btn055 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'0{i+1}5')
        btn056 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'0{i+1}6')
        btn057 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'0{i+1}7')
        btn058 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'0{i+1}8')
        btns_matrix[f'0{i+1}'] = [btn051, btn052, btn053, btn054, btn055, btn056, btn057, btn058]

        i = 5
        btn061 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'0{i+1}1')
        btn062 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'0{i+1}2')
        btn063 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'0{i+1}3')
        btn064 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'0{i+1}4')
        btn065 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'0{i+1}5')
        btn066 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'0{i+1}6')
        btn067 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'0{i+1}7')
        btn068 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'0{i+1}8')
        btns_matrix[f'0{i+1}'] = [btn061, btn062, btn063, btn064, btn065, btn066, btn067, btn068]

        i = 6
        btn071 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'0{i+1}1')
        btn072 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'0{i+1}2')
        btn073 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'0{i+1}3')
        btn074 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'0{i+1}4')
        btn075 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'0{i+1}5')
        btn076 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'0{i+1}6')
        btn077 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'0{i+1}7')
        btn078 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'0{i+1}8')
        btns_matrix[f'0{i+1}'] = [btn071, btn072, btn073, btn074, btn075, btn076, btn077, btn078]

        i = 7
        btn081 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'0{i+1}1')
        btn082 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'0{i+1}2')
        btn083 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'0{i+1}3')
        btn084 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'0{i+1}4')
        btn085 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'0{i+1}5')
        btn086 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'0{i+1}6')
        btn087 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'0{i+1}7')
        btn088 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'0{i+1}8')
        btns_matrix[f'0{i+1}'] = [btn081, btn082, btn083, btn084, btn085, btn086, btn087, btn088]

        i = 8
        btn091 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'0{i+1}1')
        btn092 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'0{i+1}2')
        btn093 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'0{i+1}3')
        btn094 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'0{i+1}4')
        btn095 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'0{i+1}5')
        btn096 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'0{i+1}6')
        btn097 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'0{i+1}7')
        btn098 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'0{i+1}8')
        btns_matrix[f'0{i+1}'] = [btn091, btn092, btn093, btn094, btn095, btn096, btn097, btn098]

        i = 9
        btn101 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}1')
        btn102 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}2')
        btn103 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}3')
        btn104 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}4')
        btn105 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}5')
        btn106 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}6')
        btn107 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}7')
        btn108 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}8')
        btns_matrix[f'{i+1}'] = [btn101, btn102, btn103, btn104, btn105, btn106, btn107, btn108]

        i = 10
        btn111 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}1')
        btn112 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}2')
        btn113 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}3')
        btn114 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}4')
        btn115 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}5')
        btn116 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}6')
        btn117 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}7')
        btn118 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}8')
        btns_matrix[f'{i+1}'] = [btn111, btn112, btn113, btn114, btn115, btn116, btn117, btn118]

        i = 11
        btn121 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}1')
        btn122 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}2')
        btn123 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}3')
        btn124 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}4')
        btn125 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}5')
        btn126 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}6')
        btn127 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}7')
        btn128 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}8')
        btns_matrix[f'{i+1}'] = [btn121, btn122, btn123, btn124, btn125, btn126, btn127, btn128]


        i = 12
        btn131 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}1')
        btn132 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}2')
        btn133 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}3')
        btn134 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}4')
        btn135 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}5')
        btn136 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}6')
        btn137 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}7')
        btn138 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}8')
        btns_matrix[f'{i+1}'] = [btn131, btn132, btn133, btn134, btn135, btn136, btn137, btn138]

        i = 13
        btn141 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}1')
        btn142 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}2')
        btn143 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}3')
        btn144 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}4')
        btn145 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}5')
        btn146 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}6')
        btn147 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}7')
        btn148 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}8')
        btns_matrix[f'{i+1}'] = [btn141, btn142, btn143, btn144, btn145, btn146, btn147, btn148]

        i = 14
        btn151 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}1')
        btn152 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}2')
        btn153 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}3')
        btn154 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}4')
        btn155 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}5')
        btn156 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}6')
        btn157 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}7')
        btn158 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}8')
        btns_matrix[f'{i+1}'] = [btn151, btn152, btn153, btn154, btn155, btn156, btn157, btn158]

        i = 15
        btn161 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}1')
        btn162 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}2')
        btn163 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}3')
        btn164 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}4')
        btn165 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}5')
        btn166 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}6')
        btn167 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}7')
        btn168 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}8')
        btns_matrix[f'{i+1}'] = [btn161, btn162, btn163, btn164, btn165, btn166, btn167, btn168]

        i = 16
        btn171 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}1')
        btn172 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}2')
        btn173 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}3')
        btn174 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}4')
        btn175 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}5')
        btn176 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}6')
        btn177 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}7')
        btn178 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}8')
        btns_matrix[f'{i+1}'] = [btn171, btn172, btn173, btn174, btn175, btn176, btn177, btn178]

        i = 17
        btn181 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}1')
        btn182 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}2')
        btn183 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}3')
        btn184 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}4')
        btn185 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}5')
        btn186 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}6')
        btn187 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}7')
        btn188 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}8')
        btns_matrix[f'{i+1}'] = [btn181, btn182, btn183, btn184, btn185, btn186, btn187, btn188]

        i = 18
        btn191 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}1')
        btn192 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}2')
        btn193 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}3')
        btn194 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}4')
        btn195 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}5')
        btn196 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}6')
        btn197 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}7')
        btn198 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}8')
        btns_matrix[f'{i+1}'] = [btn191, btn192, btn193, btn194, btn195, btn196, btn197, btn198]

        i = 19
        btn201 = ft.ElevatedButton(f"{df[i][0]}", style=cell_style(df[i][0]), data=f'{i+1}1')
        btn202 = ft.ElevatedButton(f"{df[i][1]}", style=cell_style(df[i][1]), data=f'{i+1}2')
        btn203 = ft.ElevatedButton(f"{df[i][2]}", style=cell_style(df[i][2]), data=f'{i+1}3')
        btn204 = ft.ElevatedButton(f"{df[i][3]}", style=cell_style(df[i][3]), data=f'{i+1}4')
        btn205 = ft.ElevatedButton(f"{df[i][4]}", style=cell_style(df[i][4]), data=f'{i+1}5')
        btn206 = ft.ElevatedButton(f"{df[i][5]}", style=cell_style(df[i][5]), data=f'{i+1}6')
        btn207 = ft.ElevatedButton(f"{df[i][6]}", style=cell_style(df[i][6]), data=f'{i+1}7')
        btn208 = ft.ElevatedButton(f"{df[i][7]}", style=cell_style(df[i][7]), data=f'{i+1}8')
        btns_matrix[f'{i+1}'] = [btn201, btn202, btn203, btn204, btn205, btn206, btn207, btn208]

        return btns_matrix


