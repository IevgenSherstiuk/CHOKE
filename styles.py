import flet as ft

def cell_style(N:str):
       try: N = int(N)
       except: N = -1

       if N == -1:
              empty_style = ft.ButtonStyle(             
                     color={ft.MaterialState.DEFAULT: ft.colors.BLUE_100},
                     bgcolor={ft.MaterialState.DEFAULT: ft.colors.BLUE_100},
                     padding={ft.MaterialState.DEFAULT: 1},     
                     overlay_color=ft.colors.BLUE_100,
                     #elevation={"pressed": 1, "": 1},
                     side={ft.MaterialState.DEFAULT: ft.BorderSide(0, ft.colors.BLUE_100)})
              return  empty_style
       elif N == 0:
              cell_style = ft.ButtonStyle(
                     color={ft.MaterialState.HOVERED: ft.colors.WHITE,
                            ft.MaterialState.FOCUSED: ft.colors.RED,
                            ft.MaterialState.DEFAULT: ft.colors.WHITE},
                     bgcolor={ft.MaterialState.FOCUSED: ft.colors.GREEN_ACCENT_200,
                                   ft.MaterialState.HOVERED: ft.colors.AMBER_600,
                                   ft.MaterialState.DEFAULT: ft.colors.AMBER_900},
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
                     padding={ft.MaterialState.DEFAULT: 1},
                     animation_duration=300,
                     side= {ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                            ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE60)},
                     shape={ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=30),
                            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10)})
              
       return cell_style
    



