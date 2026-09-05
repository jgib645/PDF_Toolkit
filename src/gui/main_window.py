import tkinter as tk
from tkinter import filedialog, ttk
import threading, queue, os
from pathlib import Path
from .widgets import create_progress_bar,status_label,cancel_button
from ..core.pdf_to_docx import PDFToDOCX
from ..core.pdf_to_csv import PDFToCSV
from ..utils.logging import get_logger
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF Toolkit")
        self.geometry("400x200")
        btn_docx=tk.Button(self,text="PDF → DOCX",command=self.run_docx)
        btn_csv=tk.Button(self,text="PDF → CSV",command=self.run_csv)
        btn_docx.pack(pady=5)
        btn_csv.pack(pady=5)
        self.progress=create_progress_bar(self)
        self.status=status_label(self)
        self.cancel_flag=threading.Event()
        cancel_button(self,self.on_cancel).pack(pady=5)
    def run_docx(self):
        path=filedialog.askopenfilename(filetypes=[("PDF Files","*.pdf")])
        if not path: return
        out=Path(path).with_name(Path(path).stem+"_converted.docx")
        self.start_conversion(PDFToDOCX(),path,str(out))
    def run_csv(self):
        path=filedialog.askopenfilename(filetypes=[("PDF Files","*.pdf")])
        if not path: return
        out=Path(path).with_name(Path(path).stem+"_converted.csv")
        self.start_conversion(PDFToCSV(),path,str(out))
    def start_conversion(self,converter,input_path,out_path):
        self.cancel_flag.clear()
        q=queue.Queue()
        t=threading.Thread(target=self.worker,args=(converter,input_path,out_path,q),daemon=True)
        t.start()
        self.after(100,self.check_queue,q,t)
    def worker(self,conv,input_path,out_path,q):
        logger=get_logger('pdf_toolkit',log_file_path=Path(out_path).with_suffix('.log'))
        summary=conv.convert(input_path,out_path,progress_cb=lambda cur,total:q.put((cur,total)))
        q.put(('done',summary))
    def check_queue(self,q,t):
        try:
            item=q.get_nowait()
        except queue.Empty:
            self.after(100,self.check_queue,q,t)
            return
        if isinstance(item,tuple) and item[0]=='done':
            self.status.config(text=f"Done: {item[1]}")
        else:
            cur,total=item
            self.progress['value']=cur
            self.progress['maximum']=total
            self.status.config(text=f"Page {cur}/{total}")
            self.after(100,self.check_queue,q,t)
    def on_cancel(self):
        self.cancel_flag.set()
if __name__=='__main__':
    MainWindow().mainloop()
