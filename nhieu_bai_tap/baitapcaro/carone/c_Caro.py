class c_Caro:
    """Lop co caro."""
    def __init__(self, row, column):
        """Khoi tao."""
        self.Board = []
        self.Max_row = row
        self.Max_column = column
        for i in range(self.Max_row):
            row = []
            for i in range(self.Max_column):
                row.append(0)
            self.Board.append(row)

    def mark(self, player, row, column):
        """Nguoi choi # mark o da chon."""
        self.Board[row][column] = player

    def isWinner(self, player, row, column):
        """Kiem tra chien thang."""
        # Kiem tra quanh o da chon
        if self.vertical_check(player, row, column) or\
                self.horizontal_check(player, row, column) or\
                self.left_diagonal_check(player, row, column) or\
                self.right_diagonal_check(player, row, column):
            return True
        return False

    def vertical_check(self, player, row, column):
        """Kiem tra theo hang doc."""
        # Bat dau tai diem dang xet
        count = 1
        # Xet phia tren diem dang xet
        for i in range(1, 5):
            if row - i >= 0 and self.Board[row - i][column] == player:
                count += 1
            else:
                break
        # Xet phia duoi diem dang xet
        for i in range(1, 5):
            if row + i < self.Max_row \
                    and self.Board[row + i][column] == player:
                count += 1
            else:
                break
        if count >= 5:
            return True
        else:
            return False

    def horizontal_check(self, player, row, column):
        """Kiem tra theo hang ngang."""
        # Bat dau tai diem dang xet
        count = 1

        # Xet phia trai diem dang xet
        for i in range(1, 5):
            if column - i >= 0 and self.Board[row][column - i] == player:
                count += 1
            else:
                break

        # Xet phia duoi diem dang xet
        for i in range(1, 5):
            if column + i < self.Max_column \
                        and self.Board[row][column + i] == player:
                count += 1
            else:
                break
        if count >= 5:
            return True
        else:
            return False

    def left_diagonal_check(self, player, row, column):
        """Kiem tra theo hang xeo trai."""
        # Bat dau tai diem dang xet
        count = 1

        # Xet phia tren diem dang xet
        for i in range(1, 5):
            if row - i >= 0 and column - i >= 0 \
                        and self.Board[row - i][column - i] == player:
                count += 1
            else:
                break

        # Xet phia duoi diem dang xet
        for i in range(1, 5):
            if row + i < self.Max_row \
                        and column + i < self.Max_column\
                        and self.Board[row + i][column + i] == player:
                count += 1
            else:
                break
        if count >= 5:
            return True
        else:
            return False

    def right_diagonal_check(self, player, row, column):
        """Kiem tra theo hang xeo trai."""
        # Bat dau tai diem dang xet
        count = 1

        # Xet phia tren diem dang xet
        for i in range(1, 5):
            if row - i >= 0 and column + i < self.Max_column\
                        and self.Board[row - i][column + i] == player:
                count += 1
            else:
                break

        # Xet phia duoi diem dang xet
        for i in range(1, 5):
            if row + i < self.Max_row and column - i <= 0 \
                        and self.Board[row + i][column - i] == player:
                count += 1
            else:
                break
        if count >= 5:
            return True
        else:
            return False
