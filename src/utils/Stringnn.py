def formater(text:str,num:int) -> str:
    """Format the text to be displayed in the UI"""
    out_text = ""
    i = 0
    while i < len(text):
        out_text += text[i:(i+num)]
        out_text += "\n"
        i+=num
    return out_text

# if __name__ == '__main__':
#     print(formater("Entry 控件是 Tkinter GUI 编程中的基础控件之一，它的作用就是允许用户输入内容，从而实现 GUI 程序与用户的交互，比如当用户登录软件时，输入用户名和密码，此时就需要使用 Entry 控件.",15))