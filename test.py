import flet as ft

from styles import cell_style

def main(page: ft.Page):
    page.theme_mode = 'light'



    def handle_change(e):
        print("on_change data : " + str(e.data))

    buy_btn_p1 = ft.Segment(
                    value="1",
                    label=ft.Text("48$"),
                    icon=ft.Icon(ft.icons.SHOPPING_CART),
                    )
    buy_btn_p2 = ft.Segment(
                    value="2",
                    label=ft.Text("Заказать  "))
    buy_btn_p3 = ft.Segment(
                    value="2",
                    icon=ft.Icon(ft.icons.INFO_OUTLINE))
                    #label=ft.Text("Заказать "))

    page.add(
        ft.SegmentedButton(
            on_change=handle_change,
            allow_empty_selection=True,
            show_selected_icon=False,
            segments=[buy_btn_p1, buy_btn_p2],
            style=cell_style(-8, None)
        )
    )


ft.app(target=main)
