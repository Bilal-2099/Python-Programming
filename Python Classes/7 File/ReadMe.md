# Practice 7: File Handling

## 📌 Overview  
This Jupyter notebook (`Practice 7 File.ipynb`) focuses on Python’s file-handling capabilities — reading from and writing to files, working with file paths, and managing different file modes.

## 🧾 What’s Inside  
- Opening files in different modes (`'r'`, `'w'`, `'a'`, `'rb'`, `'wb'`).  
- Reading text, iterating over file lines, writing strings, and appending data.  
- Working with relative vs absolute file paths.  
- Using context managers (`with` statement) to ensure files are properly closed.  
- Practical exercises where you:
  - Read a text file and count the number of lines/words.
  - Write a log file with timestamped entries.
  - Append new data to an existing file and then read the updated content.

## 🎯 Learning Goals  
By the end of this notebook you should be able to:
- Open and close files correctly in Python.
- Choose the correct file mode for the task (read, write, append, binary).
- Read, write, and append data to files.
- Use context managers to handle files safely.
- Work with file paths and understand differences between absolute/relative paths.

## 🧑‍💻 How to Use  
1. Open the notebook in Jupyter or VS Code (supports `.ipynb`).  
2. Run each code cell: read the explanation, execute it, observe the result.  
3. Modify the examples:  
   - Change filenames or paths.  
   - Write your own file of text and read/append to it.  
   - Convert the code to use binary mode (for writing/reading images or non-text data).  
4. Challenge yourself:
   - Create a file cleanup function: if file size exceeds a limit, archive it into a new file.  
   - Write a program that scans a directory of `.txt` files, reads each, and summarizes total word count.

## 🔍 Why This Matters  
Working with files is central to many real-world tasks:  
- Logging application data, reading configuration files.  
- Loading/saving data sets for analytics.  
- Interacting with legacy systems or exported data from other tools.  

## 📚 What Comes Next  
After you feel comfortable with file handling, move on to:
- **Error Handling & Exceptions** (deal with file-not-found, permission errors).  
- **CSV/JSON/XML Data Processing** (structured file formats).  
- **Working with Directories & OS module** (list files, rename, move).  
- **Integrating File I/O into Projects** (e.g., your expense tracker saving to files or a database).

---

*Keep practicing and exploring small variations in how you read or write files — that’s how you build real confidence.*  
