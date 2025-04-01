from tkinter import Tk, Label, PhotoImage

# Tkinter 윈도우 생성
window = Tk()
window.title("냥이들 ^^")

# 첫 번째 이미지 로드 및 Label 생성
img1 = PhotoImage(file="cat1.png")  # 첫 번째 이미지 파일 경로
label1 = Label(window, image=img1)
label1.pack(side="left")  # 가로 정렬

# 두 번째 이미지 로드 및 Label 생성
img2 = PhotoImage(file="cat2.png")  # 두 번째 이미지 파일 경로
label2 = Label(window, image=img2)
label2.pack(side="left")  # 가로 정렬

# Tkinter 이벤트 루프 실행
window.mainloop()
