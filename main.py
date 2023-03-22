import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Крестики-нолики")

        # Создание кнопок
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.master, text=" ", font=('Arial', 60), width=3, height=1,
                                   command=lambda i=i, j=j: self.button_click(i, j))
                button.grid(row=i, column=j, sticky="nsew")
                row.append(button)
            self.buttons.append(row)

        # Создание счетчиков
        self.x_score = 0
        self.o_score = 0
        self.current_player = "X"
        self.status_text = tk.StringVar(value="Ходит игрок X")
        self.status_label = tk.Label(self.master, textvariable=self.status_text, font=('Arial', 20))
        self.status_label.grid(row=3, column=0, columnspan=3, sticky="nsew")
        self.score_text = tk.StringVar(value=f"X: {self.x_score} | O: {self.o_score}")
        self.score_label = tk.Label(self.master, textvariable=self.score_text, font=('Arial', 20))
        self.score_label.grid(row=4, column=0, columnspan=3, sticky="nsew")

    def button_click(self, i, j):
        button = self.buttons[i][j]
        if button["text"] == " ":
            button["text"] = self.current_player
            if self.check_win():
                self.show_win_message()
                self.reset_board()
            elif self.check_tie():
                self.show_tie_message()
                self.reset_board()
            else:
                self.switch_player()
                self.update_status()

    def check_win(self):
        # Проверка выигрышной комбинации
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != " ":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != " ":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != " ":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != " ":
            return True
        return False

    def check_tie(self):
        # Проверка на ничью
        for row in self.buttons:
            for button in row:
                if button["text"] == " ":
                    return False
        return True

    def show_tie_message(self):
        # Вывод сообщения о ничьей
        messagebox.showinfo("Игра окончена", "Ничья!")

    def show_win_message(self):
        # Вывод сообщения о победе
        winner = self.current_player
        messagebox.showinfo("Игра окончена", f" победили {winner}")

    def switch_player(self):
        # Смена игрока
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def update_status(self):
        # Обновление статуса игры
        self.status_text.set(f"Ходит игрок {self.current_player}")

    def reset_board(self):
        # Сброс игрового поля
        for row in self.buttons:
            for button in row:
                button["text"] = " "
        if self.current_player == "X":
            self.x_score += 1
        else:
            self.o_score += 1
        self.score_text.set(f"X: {self.x_score} | O: {self.o_score}")
        self.current_player = "X"
        self.update_status()


root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
