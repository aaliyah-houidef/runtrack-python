def time_to_text(mins):
    heures = mins // 60
    minutes_restantes = mins % 60
    print(f"{heures} heures et {minutes_restantes} minutes")

time_to_text(657)  