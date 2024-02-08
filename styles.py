import flet as ft


def cell_style(price:str, formating_grades):
       if formating_grades: grade_1, grade_2, grade_3 = formating_grades


       try: price = float(price)
       except: price = -1

       if price == -3: #Mu_axis btns style
                     Mu_style = ft.ButtonStyle(             
                            color={ft.MaterialState.DEFAULT: ft.colors.DEEP_ORANGE_900},
                            bgcolor={ft.MaterialState.DEFAULT: ft.colors.BLUE_100},
                            padding={ft.MaterialState.DEFAULT: 1},
                            elevation={"pressed": 0, "": 0},     
                            overlay_color=ft.colors.BLUE_200,
                            side={ft.MaterialState.DEFAULT: ft.BorderSide(2, ft.colors.DEEP_ORANGE_900)})
                     return  Mu_style


       elif price == -2: #H_axis btns style
                     H_style = ft.ButtonStyle(             
                            color={ft.MaterialState.DEFAULT: ft.colors.CYAN_800},
                            bgcolor={ft.MaterialState.DEFAULT: ft.colors.BLUE_100},
                            padding={ft.MaterialState.DEFAULT: 1},
                            elevation={"pressed": 0, "": 0},     
                            overlay_color=ft.colors.BLUE_200,
                            side={ft.MaterialState.DEFAULT: ft.BorderSide(2, ft.colors.CYAN_800)})
                     return  H_style


       elif price == -1: 
              empty_style = ft.ButtonStyle(             
                     color={ft.MaterialState.DEFAULT: ft.colors.BLUE_100},
                     bgcolor={ft.MaterialState.DEFAULT: ft.colors.BLUE_100},
                     padding={ft.MaterialState.DEFAULT: 1},
                     elevation={"pressed": 0, "": 0},     
                     overlay_color=ft.colors.BLUE_100,
                     side={ft.MaterialState.DEFAULT: ft.BorderSide(0, ft.colors.BLUE_100)})
              return  empty_style
       


       elif price == -4: #Mu_change btns style
              Mu_edit_style = ft.ButtonStyle(
                     color={ft.MaterialState.FOCUSED: ft.colors.DEEP_ORANGE_900,
                            ft.MaterialState.DEFAULT: ft.colors.DEEP_ORANGE_900},
                     bgcolor={ft.MaterialState.HOVERED: ft.colors.DEEP_ORANGE_100,
                            ft.MaterialState.DEFAULT: ft.colors.DEEP_ORANGE_50},
                     padding={ft.MaterialState.DEFAULT: 1},
                     animation_duration=300,
                     side= {ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.DEEP_ORANGE_900),
                            ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.DEEP_ORANGE_900)},
                     shape={ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=3),
                            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=3)})
              return Mu_edit_style
       
       elif price == -5: #H_change btns style
              H_edit_style = ft.ButtonStyle(
                     color={ft.MaterialState.HOVERED: ft.colors.CYAN_900,
                            ft.MaterialState.DEFAULT: ft.colors.CYAN_900},
                     bgcolor={ft.MaterialState.HOVERED: ft.colors.CYAN_100,
                            ft.MaterialState.DEFAULT: ft.colors.CYAN_50},
                     padding={ft.MaterialState.DEFAULT: 1},
                     animation_duration=300,
                     side= {ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.CYAN_900),
                            ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.CYAN_900)},
                     shape={ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=3),
                            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=3)})
               
              return H_edit_style
       
       elif price == -6: # "μ"name
                     Mu_text = ft.ButtonStyle(             
                            color={ft.MaterialState.DEFAULT: ft.colors.DEEP_ORANGE_900},
                            bgcolor={ft.MaterialState.DEFAULT: ft.colors.BLUE_100},
                            padding={ft.MaterialState.DEFAULT: 1},     
                            overlay_color=ft.colors.BLUE_100,
                            side={ft.MaterialState.DEFAULT: ft.BorderSide(2, ft.colors.BLUE_100)},
                            shape={ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=0),
                                   ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=0)})
                     return  Mu_text
       
       elif price == 0: #FOCUSED after Calculation
              cell_style = ft.ButtonStyle(
                     color={ft.MaterialState.HOVERED: ft.colors.WHITE,
                            ft.MaterialState.FOCUSED: ft.colors.RED,
                            ft.MaterialState.DEFAULT: ft.colors.WHITE},
                     bgcolor={ft.MaterialState.FOCUSED: ft.colors.GREEN_ACCENT_200,
                                   ft.MaterialState.HOVERED: ft.colors.AMBER_600,
                                   ft.MaterialState.DEFAULT: ft.colors.AMBER_700},
                     elevation={"pressed": 0, "": 0},
                     padding={ft.MaterialState.DEFAULT: 1},
                     animation_duration=300,
                     side= {ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                            ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE60)},
                     shape={ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=30),
                            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=30)})
       
       elif price == -7: #reset after FOCUSED
              cell_style = ft.ButtonStyle(
                     color={ft.MaterialState.HOVERED: ft.colors.WHITE,
                            ft.MaterialState.FOCUSED: ft.colors.WHITE,
                            ft.MaterialState.DEFAULT: ft.colors.WHITE},
                     bgcolor={ft.MaterialState.FOCUSED: ft.colors.AMBER_900,
                                   ft.MaterialState.HOVERED: ft.colors.AMBER_600,
                                   ft.MaterialState.DEFAULT: ft.colors.CYAN_ACCENT_700},
                     elevation={"pressed": 0, "": 0},
                     padding={ft.MaterialState.DEFAULT: 1},
                     animation_duration=300,
                     side= {ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                            ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE60)},
                     shape={ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=30),
                            ft.MaterialState.FOCUSED: ft.RoundedRectangleBorder(radius=30),
                            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10)})
              
       elif price == -8: #buy_btns style
              buy_style = ft.ButtonStyle(             
                     color={ft.MaterialState.DEFAULT: ft.colors.WHITE},
                     bgcolor={ft.MaterialState.DEFAULT: ft.colors.BLUE_900},
                     padding={ft.MaterialState.DEFAULT: 10},
                     elevation={"pressed": 0, "": 0},     
                     overlay_color=ft.colors.BLUE_200,
                     side={ft.MaterialState.DEFAULT: ft.BorderSide(2, ft.colors.CYAN_800)})
              return  buy_style



       else:       
              if price == (grade_1 or 'minPrice'): color = ft.colors.CYAN_ACCENT_700
              elif price < grade_2: color = ft.colors.TEAL_400
              elif price < grade_3: color = '#bf8124'#'#ba8838'
              else : color = '#964739'
     


              cell_style = ft.ButtonStyle(
                     color={ft.MaterialState.HOVERED: ft.colors.WHITE,
                            ft.MaterialState.FOCUSED: ft.colors.WHITE,
                            ft.MaterialState.DEFAULT: ft.colors.WHITE},
                     bgcolor={ft.MaterialState.FOCUSED: ft.colors.AMBER_900,
                                   ft.MaterialState.HOVERED: ft.colors.AMBER_600,
                                   ft.MaterialState.DEFAULT: color},
                     elevation={"pressed": 0, "": 0},
                     padding={ft.MaterialState.DEFAULT: 1},
                     animation_duration=300,
                     side= {ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                            ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE60)},
                     shape={ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=30),
                            ft.MaterialState.FOCUSED: ft.RoundedRectangleBorder(radius=30),
                            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10)})
              
       return cell_style
    



