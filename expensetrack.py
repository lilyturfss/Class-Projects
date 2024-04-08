# Expense Tracker

import flet as ft
total = 0


class ExpenseTracker(ft.UserControl):
    pass

class Expense(ft.UserControl):
    def build(self):
        pass
    
    pass

def main(page: ft.Page):
    global total
    all_expenses = {}

    gasto = ft.TextField(label = "Cost", height = 60, color="#E75480", width = 80)

    # FUNCTIONS
    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        content=ft.Text("The value you have entered for the cost is invalid"),
        actions=[ft.TextButton("Ok", on_click=close_dlg)],
        actions_alignment=ft.MainAxisAlignment.END)

    def open_dlg():
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    def add_(e):
        global total
        try:
            total = int(gasto.value) + total
            expense = ft.Container(content = 
                                   ft.Row(controls = [
                                       ft.Container(content = ft.Text(f"Description: {name.value}", weight= ft.FontWeight.BOLD), width = 150, margin= 20), 
                                       ft.Text(f"{gasto.value}$", size = 30),
                                       
                                       ft.Row (controls =[
                                        ft.Text(f"Category: {categories_dd.value}", weight=ft.FontWeight.BOLD),
                                        
                                    ]
                                )
                            ], alignment=ft.MainAxisAlignment.START
                        ), bgcolor = "#E75480",  border_radius=10, height = 100, width = 650
                    )
            
            add_row.controls[3] = ft.Text(f"Total Expenses: {total}$", color="#E75480")
            page1.controls.append(expense)
            page.update()

            all_expenses[f"{name.value}"] = f"{gasto.value}"

            save(all_expenses)
        except ValueError:
            open_dlg()

    def save(all_expenses):
            x = 3
            with open("expenses.txt", "w") as file:
                for description, value in all_expenses.items():
                    file.write(f"{description}, {value}, {page1.controls[x].content.controls[2].controls[0].value}, {total}\n")
                    x += 1
        
    def load():
        global total
        with open("expenses.txt", "r") as file:
            for line in file:
                description, cost, category, total =  line.strip().split(',')
                total = int(total)

                expense = ft.Container(content = 
                                    ft.Row(controls = [
                                        ft.Container(content = ft.Text(f"Description: {description}", weight= ft.FontWeight.BOLD), width = 150, margin= 20), 
                                        ft.Text(f"{cost}$", size = 30),
                                        
                                        ft.Row (controls =[
                                            ft.Text(f"{category}", weight=ft.FontWeight.BOLD),  
                                        ]
                                    )
                                ], alignment=ft.MainAxisAlignment.START
                            ), bgcolor = "#E75480",  border_radius=10, height = 100, width = 650
                        )
                
                add_row.controls[3] = ft.Text(f"Total Expenses: {total}$", color="#E75480")
                page1.controls.append(expense)
                page.update()

                all_expenses[f"{description}"] = f"{cost}"

    # Page Attributes
    page.title = "Expense Tracker"
    page.horizontal_alignment = "CENTER"
    page.vertical_alignment = "CENTER"
    page.window_width = 650
    page.window_height = 700
    page.window_resizable = False 

    # Header
    Title = ft.Text("Expense Tracker", size = 40, color= "#E75480")
    Header = ft.Row(controls = [Title], alignment = ft.CrossAxisAlignment.START)

    add_button = ft.ElevatedButton(text= "Add Expense", on_click= add_, color= "#E75480")

    name =  ft.TextField(label = "Expense Description", color= "#E75480")
    categories_dd = ft.Dropdown(
                                width=150,
                                options=[
                                    ft.dropdown.Option("Choose an Option"),
                                    ft.dropdown.Option("Groceries"),
                                    ft.dropdown.Option("Entertainment"),
                                    ft.dropdown.Option("Housing"),
                                    ft.dropdown.Option("Transportation"),
                                    ft.dropdown.Option("Food"),
                                    ft.dropdown.Option("Utilities"),
                                    ft.dropdown.Option("Insurance"),
                                    ft.dropdown.Option("Medical"),
                                    ft.dropdown.Option("Savings"),
                                    ft.dropdown.Option("Personal"),
                                ], label= "Categories", height = 60
                            )
    add_row = ft.Row(controls = [add_button, gasto, categories_dd, ft.Text(f"Total Expenses: {total}$", color="#E75480")])
    page1 = ft.Column(controls = [Header, name, add_row], width = 900, height = 700, scroll= ft.ScrollMode.ALWAYS)
    
    page.add(page1)
    try: 
        load()
    except:
        pass
    page.update()

ft.app(target=main)