from tkinter import *
import datetime

# ----------------------------- Color palette -----------------------------
BG_COLOR = "#11131a"          # app background (near-black navy)
CARD_BG = "#1c1f2b"           # card background
CARD_BG_HOVER = "#242838"     # card background on hover
ACCENT = "#7c5cff"            # accent purple
ACCENT_SOFT = "#a996ff"       # softer accent for secondary text
TEXT_MAIN = "#f5f5fa"         # main light text
TEXT_MUTED = "#8b8fa3"        # muted label text
DIVIDER = "#2a2e3d"

FONT_FAMILY = "Consolas"       # falls back gracefully on most systems
VALUE_FONT = (FONT_FAMILY, 46, "bold")
VALUE_FONT_SMALL = (FONT_FAMILY, 30, "bold")
LABEL_FONT = (FONT_FAMILY, 12, "bold")
HEADER_FONT = (FONT_FAMILY, 14, "bold")
BRAND_FONT = (FONT_FAMILY, 20, "bold")


def make_card(parent, value_text, caption, value_font=VALUE_FONT, width=150, height=140):
    """Create a rounded-feel 'card' widget containing a big value and a caption underneath.
    Returns the value Label so its text can be updated later.
    """
    card = Frame(parent, bg=CARD_BG, width=width, height=height, highlightthickness=0)
    card.grid_propagate(False)
    card.pack_propagate(False)

    value_label = Label(card, text=value_text, font=value_font, bg=CARD_BG, fg=TEXT_MAIN)
    value_label.pack(expand=True, pady=(18, 0))

    caption_label = Label(card, text=caption.upper(), font=LABEL_FONT, bg=CARD_BG, fg=ACCENT_SOFT)
    caption_label.pack(pady=(0, 14))

    # simple hover effect for a modern "interactive" feel
    def on_enter(_):
        card.configure(bg=CARD_BG_HOVER)
        value_label.configure(bg=CARD_BG_HOVER)
        caption_label.configure(bg=CARD_BG_HOVER)

    def on_leave(_):
        card.configure(bg=CARD_BG)
        value_label.configure(bg=CARD_BG)
        caption_label.configure(bg=CARD_BG)

    for widget in (card, value_label, caption_label):
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)

    return card, value_label


def update_clock():
    now = datetime.datetime.now()

    lab_hr_val.config(text=now.strftime("%I"))
    lab_min_val.config(text=now.strftime("%M"))
    lab_sec_val.config(text=now.strftime("%S"))
    lab_ampm_val.config(text=now.strftime("%p"))

    lab_date_val.config(text=now.strftime("%d"))
    lab_month_val.config(text=now.strftime("%b").upper())
    lab_year_val.config(text=now.strftime("%Y"))
    lab_day_val.config(text=now.strftime("%A"))

    full_date_lbl.config(text=now.strftime("%A, %d %B %Y"))

    root.after(200, update_clock)


# ------------------------------- Window setup -------------------------------
root = Tk()
root.title("Personal Digital Clock")
root.geometry("1000x660")
root.configure(bg=BG_COLOR)
root.minsize(820, 480)

# ------------------------------- Header / brand -------------------------------
header = Frame(root, bg=BG_COLOR)
header.pack(fill=X, padx=40, pady=(30, 10))

Label(
    header, text="⏱︎", font=(FONT_FAMILY, 16), bg=BG_COLOR, fg=ACCENT
).pack(side=LEFT, padx=(0, 8))

Label(
    header, text="Personal Digital Clock", font=BRAND_FONT, bg=BG_COLOR, fg=TEXT_MAIN
).pack(side=LEFT)

full_date_lbl = Label(header, text="", font=(FONT_FAMILY, 13), bg=BG_COLOR, fg=TEXT_MUTED)
full_date_lbl.pack(side=RIGHT)

# thin divider under the header
Frame(root, bg=DIVIDER, height=1).pack(fill=X, padx=40)

# ------------------------------- TIME section -------------------------------
section_time = Frame(root, bg=BG_COLOR)
section_time.pack(fill=X, padx=40, pady=(30, 10))

Label(
    section_time, text="TIME", font=HEADER_FONT, bg=BG_COLOR, fg=ACCENT
).pack(anchor=W, pady=(0, 12))

time_row = Frame(section_time, bg=BG_COLOR)
time_row.pack(fill=X)

card_hr, lab_hr_val = make_card(time_row, "00", "Hrs")
card_hr.pack(side=LEFT, padx=(0, 16))

card_min, lab_min_val = make_card(time_row, "00", "Mins")
card_min.pack(side=LEFT, padx=16)

card_sec, lab_sec_val = make_card(time_row, "00", "Secs")
card_sec.pack(side=LEFT, padx=16)

card_ampm, lab_ampm_val = make_card(time_row, "AM", "AM / PM", value_font=VALUE_FONT_SMALL)
card_ampm.pack(side=LEFT, padx=(16, 0))

# ------------------------------- DATE section -------------------------------
section_date = Frame(root, bg=BG_COLOR)
section_date.pack(fill=X, padx=40, pady=(30, 10))

Label(
    section_date, text="DATE", font=HEADER_FONT, bg=BG_COLOR, fg=ACCENT
).pack(anchor=W, pady=(0, 12))

date_row = Frame(section_date, bg=BG_COLOR)
date_row.pack(fill=X)

card_date, lab_date_val = make_card(date_row, "00", "Date")
card_date.pack(side=LEFT, padx=(0, 16))

card_month, lab_month_val = make_card(date_row, "JAN", "Month")
card_month.pack(side=LEFT, padx=16)

card_year, lab_year_val = make_card(date_row, "0000", "Year")
card_year.pack(side=LEFT, padx=16)

card_day, lab_day_val = make_card(date_row, "Day", "Weekday", value_font=(FONT_FAMILY, 26, "bold"))
card_day.pack(side=LEFT, padx=(16, 0))

# ------------------------------- Footer -------------------------------
footer = Label(
    root, text="MADE BY : VERA-SAPIENTIA", font=(10),
    bg=BG_COLOR, fg=TEXT_MUTED
)
footer.pack(side=BOTTOM, pady=16)

update_clock()
root.mainloop()