# Counter
import flet as ft

'''
SOURCES
https://stackoverflow.com/questions/69755091/set-min-max-screen-size-in-flutter-windows
https://stackoverflow.com/questions/73567187/how-do-i-change-the-size-of-the-flet-window-on-windows-or-specify-that-it-is-not 
https://flet.dev/docs/controls/text/ 
'''
def main(page: ft.Page):
    def add(e):
        numb = int(number.value)
        numb += 1
        number.value = str(numb)
        page.update()

    def sub(e):
        numb = int(number.value)
        numb -= 1
        if numb < 0:
            numb = 0
        number.value = str(numb)
        page.update()

    page.horizontal_alignment = "CENTER"
    page.vertical_alignment = "CENTER"
    page.bgcolor = "#e75480"
    page.window_width = 350   
    page.window_height = 700      
    page.window_resizable = False 

    title = ft.Text(value="COUNTER", color="white", size=50, height=60, weight=ft.FontWeight.BOLD)
    number = ft.Text(value="0", size=50, height=60, theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,)

    buttonplus = ft.ElevatedButton(text="+", on_click=add, width=80, height=40, color="pink")
    buttonminus = ft.ElevatedButton(text="-", on_click=sub, width=80, height=40, color="pink")
    buttonrow = ft.Row(controls=[buttonminus, buttonplus], alignment=ft.MainAxisAlignment.CENTER)

    bingus_image = ft.Image(src="https://static.wikia.nocookie.net/floppapedia-revamped/images/5/5f/ActualBingus.jpg/revision/latest?cb=20211029014151", 
                            width=200, 
                            height=200)
    mydog = ft.Image(src="https://drscdn.500px.org/photo/1085074296/q%3D50_w%3D1000_of%3D1/v2?sig=0ddf7a7f7f10b58d251b35538a0b6de4e5692c9bd133f365d8dc4cc1f2ada823", 
                    width=200, 
                    height=200)
    bingus_text = ft.Text(value="Bingus", size=20, height=40)
    mydog_text = ft.Text(value="My Dog", size=20, height=100)

    bingus = ft.Row(controls=[bingus_text, bingus_image], alignment=ft.MainAxisAlignment.END)
    mydogrow = ft.Row(controls=[mydog, mydog_text], alignment=ft.MainAxisAlignment.END)
 
    page.add(title, number, buttonrow, bingus, mydogrow)
ft.app(target=main)
