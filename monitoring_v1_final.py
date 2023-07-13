from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import tkinter as tk
import customtkinter as ck

root = ck.CTk()
root.title("Google News Searcher")
ck.set_default_color_theme("green")
ck.set_appearance_mode("System")

search_list = ["battery passport", "battery pass", "battery regulation", "battery recycling",
                "battery reuse", "battery remanufacturing", "battery repairability", "resource efficiency",
                "battery performance", "circular design", "circular battery design", "battery design",
                "sustainable battery", "battery durability", "EV batteries", "resource availability",
                "battery raw material", "mobility scenario", "e-mobility", "cell manufacturing", "Li-ion battery",
                "battery manufacturing", "battery production", "product passport", "battery composition",
                "cobalt mining", "lithium mining", "giga factory", "circular economy"]

class box:
    def __init__(self):
        self.checkbox_list = []
        self.variables = []
        self.row_count = 1
        self.column_count = 1
        for i in search_list:
            self.checked = tk.BooleanVar()
            self.row_count += 1
            self.column_count += 1
            self.check = ck.CTkCheckBox(root, text=i, variable=self.checked, onvalue=True, offvalue=False)
            self.check.grid(row=self.row_count if self.row_count <= 14 else self.row_count - 14,
                            column=1 if self.column_count <= 14 else self.column_count == 2, sticky="nsew")
            self.checkbox_list.append(self.check)
            self.variables.append(self.checked)

    def search(self):
        options = Options()
        options.page_load_strategy = "eager"
        driver = webdriver.Firefox(options=options)
        for i in range(len(search_list)):
            if self.variables[i].get() == True:
                search_string = f"https://news.google.com/search?q={search_list[i]}%20when%3A7d&hl=en-GB&gl=GB&ceid=GB%3Aen"
                driver.get(search_string)
                driver.execute_script(f"window.open('{search_string}');")
                
                for window_handle in driver.window_handles:
                    driver.switch_to.window(window_handle)
                    try:
                        driver.find_element(By.CLASS_NAME, "lssxud").click() #automatically click "reject all" on all cookie disclaimer pages
                    except:
                        pass

    def check_all_boxes(self):
        for i in self.checkbox_list:
            i.select()
            self.checked.set(True)

    def uncheck_all_boxes(self):
        for i in self.checkbox_list:
            i.deselect()
            self.checked.set(False)

    def update_search_list(self):
        new_list = self.search_list_text.get("1.0", tk.END).splitlines()
        search_list.clear()
        search_list.extend(new_list)
        self.update_checkboxes()

    def update_checkboxes(self):
        for i, checkbox in enumerate(self.checkbox_list):
            checkbox.configure(text=search_list[i])

    def clear_checkboxes(self):
        for checkbox in self.checkbox_list:
            checkbox.destroy()
        self.checkbox_list.clear()
        self.variables.clear()

    def create_checkboxes(self):
        self.row_count = 1
        self.column_count = 1
        for i in search_list:
            self.checked = tk.BooleanVar()
            self.row_count += 1
            self.column_count += 1
            self.check = ck.CTkCheckBox(root, text=i, variable=self.checked, onvalue=True, offvalue=False)
            self.check.grid(row=self.row_count if self.row_count <= 14 else self.row_count - 14,
                            column=1 if self.column_count <= 14 else self.column_count == 2, sticky="nsew")
            self.checkbox_list.append(self.check)
            self.variables.append(self.checked)

boxes = box()

def change_appearance_mode(new_appearance_mode: str):
    ck.set_appearance_mode(new_appearance_mode)

search_button = ck.CTkButton(root, text="Search Google News", command=boxes.search)
search_button.grid(row=0, column=0)

check_all = ck.CTkButton(root, text="check all", command=boxes.check_all_boxes)
check_all.grid(row=0, column=1)

uncheck_all = ck.CTkButton(root, text="uncheck all", command=boxes.uncheck_all_boxes)
uncheck_all.grid(row=0, column=3)

appearance_mode_label = ck.CTkLabel(root, text="Appearance Mode:", anchor="w")
appearance_mode_label.grid(row=2, column=3)

appearance_mode_menu = ck.CTkOptionMenu(root, values=["System", "Dark", "Light"], command=change_appearance_mode)
appearance_mode_menu.grid(row=3, column=3)

search_list_label = ck.CTkLabel(root, text="Search List (scrollable):")
search_list_label.grid(row=2, column=4, sticky="w")

search_list_text = tk.Text(root, height=10, width=30)
search_list_text.grid(row=3, column=4, padx=10, rowspan=2)

search_list_text.insert(tk.END, "\n".join(search_list))

update_list_button = ck.CTkButton(root, text="Update List", command=boxes.update_search_list)
update_list_button.grid(row=5, column=4, pady=10)

boxes.search_list_text = search_list_text

def main():
    root.mainloop()

if __name__ == "__main__":
    main()