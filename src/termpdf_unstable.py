
'''


▀▀█▀▀ █▀▀ █▀▀█ █▀▄▀█ ▒█▀▀█ ▒█▀▀▄ ▒█▀▀▀ 　 ▒█░░▒█ ░▀░ █▀▀ █░░░█ █▀▀ █▀▀█ 
░▒█░░ █▀▀ █▄▄▀ █░▀░█ ▒█▄▄█ ▒█░▒█ ▒█▀▀▀ 　 ░▒█▒█░ ▀█▀ █▀▀ █▄█▄█ █▀▀ █▄▄▀ 
░▒█░░ ▀▀▀ ▀░▀▀ ▀░░░▀ ▒█░░░ ▒█▄▄▀ ▒█░░░ 　 ░░▀▄▀░ ▀▀▀ ▀▀▀ ░▀░▀░ ▀▀▀ ▀░▀▀

*************************************************
TermPDF Viewer - view and navigate PDF files within the terminal.
*************************************************
*  Simple: TermPDF Viewer is a Python program that enables users to 
view and navigate PDF files directly within the terminal.
*************************************************
* Developed and engineered by:
* Felipe Alfonso Gonzalez <f.alfonso@res-ear.ch>
* Computer Science Engineer
* Chile
*************************************************
* Prerequisites:
* Python 3.x: The program is written in Python and requires a Python 3.x interpreter to run.
* PyMuPDF: A Python binding for the MuPDF library, used to handle PDF file rendering and interaction.
*   You can install it using pip: pip install PyMuPDF
*   Make sure to include the appropriate model or adapt it for your needs.
*************************************************
* How to run the TermPDF Viewer:

* Clone the TermPDF Viewer repository from GitHub.
* Navigate to the project directory:

* cd TermPDF-Viewer

* Install PyMuPDF library (if not already installed):
  pip install PyMuPDF
  pip install pynput

  
* Run the TermPDF Viewer:
* python termpdf.py

* The TermPDF Viewer will start, allowing you to: 
* Scan for PDF files in the current directory.
* Select a PDF file to view by entering its number.
* View the PDF with options to move back, forward, or return to the main menu.
* Quit and return to the main menu.
* To exit the TermPDF Viewer, use 'q' in the main menu.
*
*************************************************
* Important Notes:
* - The application has been tested on Linux and macOS.
* - For Windows, additional configurations may be required.
* - Make sure to fulfill the prerequisites before running the application.
* - For more information, please refer to the project documentation.
*************************************************
'''





import os
import fitz
import curses

def scan_pdf_files():
    pdf_files = [file for file in os.listdir('.') if file.lower().endswith('.pdf')]
    return pdf_files

def display_current_page(stdscr, current_page, total_pages, doc):
    if not (0 <= current_page < total_pages):
        stdscr.addstr("Invalid page number.")
        stdscr.refresh()
        return

    page = doc[current_page]
    pdf_text = page.get_text()

    try:
        stdscr.addstr(f'Page {current_page + 1} / {total_pages}\n')
        stdscr.addstr(pdf_text)
    except curses.error:
        lines = pdf_text.split('\n')
        for line in lines:
            stdscr.addstr(line[:curses.COLS - 1] + '\n')

    stdscr.refresh()

def display_pdf(stdscr, pdf_filename):
    doc = fitz.open(pdf_filename)
    total_pages = doc.page_count
    current_page = 0
    exit_viewer = False

    stdscr.clear()
    stdscr.addstr("\n - Additionally, you can use the left arrow key to go back and the right arrow key to go forward.")
    stdscr.addstr("   Note: Make sure to run the script in a terminal that supports arrow key input,")
    stdscr.addstr("   and on some platforms, arrow keys might not work in certain terminal environments.\n")

    while not exit_viewer:
        display_current_page(stdscr, current_page, total_pages, doc)
        key = stdscr.getch()

        if key == curses.KEY_RIGHT:
            current_page = min(current_page + 1, total_pages - 1)
        elif key == curses.KEY_LEFT:
            current_page = max(current_page - 1, 0)
        elif key == ord('q'):
            exit_viewer = True

    doc.close()

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    stdscr.refresh()

    print("\n"
      "▀▀█▀▀ █▀▀ █▀▀█ █▀▄▀█ ▒█▀▀█ ▒█▀▀▄ ▒█▀▀▀ 　 ▒█░░▒█ ░▀░ █▀▀ █░░░█ █▀▀ █▀▀█\n"
      "░▒█░░ █▀▀ █▄▄▀ █░▀░█ ▒█▄▄█ ▒█░▒█ ▒█▀▀▀ 　 ░▒█▒█░ ▀█▀ █▀▀ █▄█▄█ █▀▀ █▄▄▀\n"
      "░▒█░░ ▀▀▀ ▀░▀▀ ▀░░░▀ ▒█░░░ ▒█▄▄▀ ▒█░░░ 　 ░░▀▄▀░ ▀▀▀ ▀▀▀ ░▀░▀░ ▀▀▀ ▀░▀▀\n"
      "-------------------------------------------------------------------------\n"
      "TermPDF Viewer - view and navigate PDF files within the terminal.\n"
      "-------------------------------------------------------------------------\n"
      "*  Simple: TermPDF Viewer is a Python program that enables users to \n"
      "*  view and navigate PDF files directly within the terminal.\n"
      "-------------------------------------------------------------------------\n"
      "\n\n"
      "╭────────────-----────── TERMS OF USE ──────────----------───╮\n"
      "│  This software is licensed under the MIT License.          │\n"
      "│  By Felipe Alfonso González - github.com/felipealfonsog    │\n"
      "│  Computer Science Engineer - Email: f.alfonso@res-ear.ch   │\n"
      "╰───────────────────────────────────────────────---------────╯\n"
      "\n")

    print("Welcome to the TermPDF Viewer!")
    
    while True:
        print("\nMain Menu:")
        print("1. Scan for PDF files")
        print("2. View scanned PDF files")
        print("3. Quit")
        
        choice = stdscr.getch()

        if choice == ord('1'):
            pdf_files = scan_pdf_files()
            if not pdf_files:
                print("No PDF files found in the current directory.")
            else:
                print("Scanned PDF files:")
                for i, pdf_file in enumerate(pdf_files, start=1):
                    print(f"{i}. {pdf_file}")
        
        elif choice == ord('2'):
            pdf_files = scan_pdf_files()
            if not pdf_files:
                print("No PDF files found in the current directory.")
            else:
                print("Scanned PDF files:")
                for i, pdf_file in enumerate(pdf_files, start=1):
                    print(f"{i}. {pdf_file}")
                
                file_choice = input("Enter the number of the PDF file to view (or 'q' to go back): ")
                if file_choice == 'q':
                    continue
                try:
                    file_choice = int(file_choice) - 1
                    if 0 <= file_choice < len(pdf_files):
                        display_pdf(stdscr, pdf_files[file_choice])
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        
        elif choice == ord('3'):
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a valid number.")

if __name__ == '__main__':
    curses.wrapper(main)

