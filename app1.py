import customtkinter 
from CTkMessagebox import CTkMessagebox
from PyPDF2 import PdfReader, PdfWriter

janela = customtkinter.CTk()
janela.geometry("350x250")
janela.winfo_toplevel().title("Dividir PDF")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def executar():
    CTkMessagebox(title="Info", icon="check", message="Feito com Sucesso !")
    pdf_reader = PdfReader("GNRE_Lote.pdf")

    for index, page in enumerate(pdf_reader.pages):
        pdf_writer =PdfWriter()
        pdf_writer.add_page(page)
        with open(f"page_{index + 1}.pdf","wb") as out:
            pdf_writer.write(out)

def fechar():
    janela.destroy()
    
texto = customtkinter.CTkLabel(janela, text="Click do Botão de Executar!")
texto.pack(padx=50, pady=10)

botao = customtkinter.CTkButton(janela, text="Executar", command=executar)
botao.pack(padx=100, pady=10,)

botao = customtkinter.CTkButton(janela, text="Sair", command=fechar)
botao.pack(padx=100, pady=10,)

texto = customtkinter.CTkLabel(janela, text="Desenvolvido por, Danilo Santos")
texto.pack(padx=80, pady=10)

janela.mainloop()