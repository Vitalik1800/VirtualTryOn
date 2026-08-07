import customtkinter as ctk


class ToolTip:

    def __init__(self, widget, text):

        self.widget = widget
        self.text = text

        self.tip = None

        widget.bind("<Enter>", self.show)
        widget.bind("<Leave>", self.hide)

    def show(self, _event=None):

        if self.tip:
            return

        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 30

        self.tip = ctk.CTkToplevel()

        self.tip.overrideredirect(True)

        self.tip.geometry(f"+{x}+{y}")

        label = ctk.CTkLabel(
            self.tip,
            text=self.text
        )

        label.pack(
            padx=6,
            pady=4
        )

    def hide(self, _event=None):

        if self.tip:
            self.tip.destroy()

            self.tip = None
