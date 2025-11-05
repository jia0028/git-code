import tkinter as tk
from tkinter import font
import random
from PIL import Image, ImageTk   # 需要 pip install pillow

# --------------------- 圖片路徑 ---------------------
# 把你的圖片（image_copy_3.png）放在同目錄，或改成絕對路徑
IMAGE_PATH = "image_copy_3.png"   # ← 改成你的圖片名

# --------------------- 彈窗類 ---------------------
class ImagePopup(tk.Toplevel):
    def __init__(self, master, img_photo):
        super().__init__(master)
        self.title("")
        self.configure(bg="#f0f0f0")
        self.overrideredirect(True)      # 去掉標題欄、邊框
        self.resizable(False, False)

        # 圖片標籤
        lbl = tk.Label(self, image=img_photo, bd=0)
        lbl.pack()

        # 隨機位置（稍微錯開，避免完全重疊）
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        win_w, win_h = 250, 180  # 根據你的圖片大小調整
        x = random.randint(100, screen_w - win_w - 100)
        y = random.randint(100, screen_h - win_h - 100)
        self.geometry(f"{win_w}x{win_h}+{x}+{y}")

        # 點擊關閉
        lbl.bind("<Button-1>", lambda e: self.destroy())
        self.bind("<Button-1>", lambda e: self.destroy())

        # 置頂
        self.lift()
        self.attributes("-topmost", True)


# --------------------- 主程式 ---------------------
def main():
    root = tk.Tk()
    root.withdraw()  # 隱藏主窗口

    # 載入圖片（只載入一次）
    try:
        img = Image.open(IMAGE_PATH)
        img = img.resize((230, 160), Image.LANCZOS)  # 調整大小
        photo = ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"圖片載入失敗: {e}")
        return

    popups = []  # 保存彈窗引用，避免被回收

    def spawn_popup():
        popup = ImagePopup(root, photo)
        popups.append(popup)
        # 每 1000ms（1秒）彈出一次
        root.after(1000, spawn_popup)

    # 啟動第一個
    root.after(500, spawn_popup)  # 延遲 0.5 秒開始

    root.mainloop()


if __name__ == "__main__":
    main()