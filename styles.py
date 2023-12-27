import flet as ft

def cell_style(N:str):
       try: N = int(N)
       except: N = -1

       if N == -3:
                     Mu_style = ft.ButtonStyle(             
                            color={ft.MaterialState.DEFAULT: ft.colors.DEEP_ORANGE_900},
                            bgcolor={ft.MaterialState.DEFAULT: ft.colors.BLUE_100},
                            padding={ft.MaterialState.DEFAULT: 1},     
                            overlay_color=ft.colors.BLUE_200,
                            side={ft.MaterialState.DEFAULT: ft.BorderSide(2, ft.colors.DEEP_ORANGE_900)})
                     return  Mu_style


       elif N == -2:
                     H_style = ft.ButtonStyle(             
                            color={ft.MaterialState.DEFAULT: ft.colors.CYAN_800},
                            bgcolor={ft.MaterialState.DEFAULT: ft.colors.BLUE_100},
                            padding={ft.MaterialState.DEFAULT: 1},     
                            overlay_color=ft.colors.BLUE_200,
                            side={ft.MaterialState.DEFAULT: ft.BorderSide(2, ft.colors.CYAN_800)})
                     return  H_style


       elif N == -1:
              empty_style = ft.ButtonStyle(             
                     color={ft.MaterialState.DEFAULT: ft.colors.BLUE_100},
                     bgcolor={ft.MaterialState.DEFAULT: ft.colors.BLUE_100},
                     padding={ft.MaterialState.DEFAULT: 1},     
                     overlay_color=ft.colors.BLUE_100,
                     side={ft.MaterialState.DEFAULT: ft.BorderSide(0, ft.colors.BLUE_100)})
              return  empty_style
       


       elif N == -4:
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
       
       elif N == -5:
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
       
       if N == -6:
                     Mu_text = ft.ButtonStyle(             
                            color={ft.MaterialState.DEFAULT: ft.colors.DEEP_ORANGE_900},
                            bgcolor={ft.MaterialState.DEFAULT: ft.colors.BLUE_100},
                            padding={ft.MaterialState.DEFAULT: 1},     
                            overlay_color=ft.colors.BLUE_100,
                            side={ft.MaterialState.DEFAULT: ft.BorderSide(2, ft.colors.BLUE_100)},
                            shape={ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=0),
                                   ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=0)})
                     return  Mu_text



       elif N == 0:
              cell_style = ft.ButtonStyle(
                     color={ft.MaterialState.HOVERED: ft.colors.WHITE,
                            ft.MaterialState.FOCUSED: ft.colors.RED,
                            ft.MaterialState.DEFAULT: ft.colors.WHITE},
                     bgcolor={ft.MaterialState.FOCUSED: ft.colors.GREEN_ACCENT_200,
                                   ft.MaterialState.HOVERED: ft.colors.AMBER_600,
                                   ft.MaterialState.DEFAULT: ft.colors.AMBER_900},
                     elevation={"pressed": 0, "": 0},
                     padding={ft.MaterialState.DEFAULT: 1},
                     animation_duration=300,
                     side= {ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                            ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE60)},
                     shape={ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=30),
                            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=30)})
                     
       
       else:       
              if N < 0: color = ft.colors.LIGHT_BLUE_100
              elif N < 1000: color = ft.colors.LIGHT_BLUE_300
              elif N < 2000: color = ft.colors.LIGHT_BLUE_500
              elif N < 3000: color = ft.colors.LIGHT_BLUE_700
              else : color = ft.colors.LIGHT_BLUE_900
     


              cell_style = ft.ButtonStyle(
                     color={ft.MaterialState.HOVERED: ft.colors.WHITE,
                            ft.MaterialState.FOCUSED: ft.colors.RED,
                            ft.MaterialState.DEFAULT: ft.colors.WHITE},
                     bgcolor={ft.MaterialState.FOCUSED: ft.colors.GREEN_ACCENT_200,
                                   ft.MaterialState.HOVERED: ft.colors.AMBER_600,
                                   ft.MaterialState.DEFAULT: color},
                     elevation={"pressed": 0, "": 0},
                     padding={ft.MaterialState.DEFAULT: 1},
                     animation_duration=300,
                     side= {ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                            ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE60)},
                     shape={ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=30),
                            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10)})
              
       return cell_style
    



