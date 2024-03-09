import tkinter as tk
from newspaper import Article

def summarize():
    url = utext.get('1.0',"end").strip()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    published.config(state='normal')
    summary.config(state='normal')

    title.delete('1.0','end')
    title.insert('1.0', article.title)

    author.delete('1.0','end')
    author.insert('1.0', ", ".join(article.authors))

    published.delete('1.0','end')
    published.insert('1.0', article.publish_date)

    summary.delete('1.0','end')
    summary.insert('1.0', article.summary)

    title.config(state='disabled')
    author.config(state='disabled')
    published.config(state='disabled')
    summary.config(state='disabled')

root = tk.Tk()
root.title("News Article Summarizer")
root.geometry('800x600')


top_frame = tk.Frame(root, bg="#151E3D")
top_frame.pack(fill="x")

quick_info_label = tk.Label(top_frame, text="Quick Info", fg="black", bg="white", font=("Helvetica", 14, "bold"))
quick_info_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

tagline_label = tk.Label(top_frame, text="Staying Up to Date Made Easy", fg="white", bg="#151E3D", font=("Helvetica", 12,"italic"))
tagline_label.grid(row=0, column=1, padx=10, pady=5, sticky="e")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="URL:", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
utext = tk.Text(frame, height=1, width=70)
utext.grid(row=0, column=1, padx=5, pady=5)

btn = tk.Button(frame, text="Summarize", command=summarize,bg="#151E3D",fg="white")
btn.grid(row=0, column=2, padx=5, pady=5)

tk.Label(frame, text="Title:", font=("Helvetica", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
title = tk.Text(frame, height=1, width=70)
title.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Author(s):", font=("Helvetica", 12)).grid(row=2, column=0, padx=5, pady=5, sticky="w")
author = tk.Text(frame, height=1, width=70)
author.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Date Published:", font=("Helvetica", 12)).grid(row=3, column=0, padx=5, pady=5, sticky="w")
published = tk.Text(frame, height=1, width=70)
published.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame, text="Summary:", font=("Helvetica", 12)).grid(row=4, column=0, padx=5, pady=5, sticky="w")
summary = tk.Text(frame, height=15, width=70)
summary.grid(row=4, column=1, padx=5, pady=5)

for widget in (title, author, published, summary):
    widget.config(state='disabled', bg='#f0f0f0', wrap='word')

root.mainloop()
