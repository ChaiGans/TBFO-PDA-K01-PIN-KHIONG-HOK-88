<h1 align="center">Tugas Besar Teori Bahasa Formal dan Otomata</h1>
<h1 align="center">K01 PIN-KHIONG-HOK-88</h3>
<h3 align="center">HTML Checker with Push Down Automata</p>

## Table of Contents

- [Overview](#overview)
- [Abstraction](#abstraction)
- [Built With](#built-with)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Features](#features)
- [File Structures Overview](#file-structures-overview)
- [Links](#links)


## Overview
<!-- ![Screenshot 2023-11-19 153812](https://github.com/FarelW/Algeo02-22045/assets/113753352/1a8d5aa7-ab9a-4e39-9aca-327a51e01efa) -->
Our Team members :
- 13522021 - Filbert
- 13522045 - Elbert Chailes
- 13522047 - Farel Winalda

<p>Our Lecturer : Dr. Judhi Santoso, M.Sc.</p>

Here is the purpose of making this project :
- To fulfill the requirements of the final assignment for the course IF2124 Teori Bahasa Formal dan Otomata.
- To implement Push Down Automata Theory in making a HTML tag checker
- To assist web developers in quickly identifying and correcting errors in HTML documents, particularly in the usage of specific tags, thereby streamlining the web development process.
- To contribute to research in the field of automata theory, demonstrating the practical utility of push down automata in real-world applications.

## Abstraction


In this project, leveraging push down automata, offers targeted validation of specific HTML tags. It enhances accuracy in identifying and correcting HTML errors, focusing on crucial tags. Ideal for educational purposes, it demonstrates automata theory in practical scenarios. This tool also streamlines web development by providing efficient, customizable validation, ensuring compliance with web standards and optimizing resource usage. It’s especially useful in legacy systems, ensuring the correct application of key HTML elements.

## Built With

- [Python](https://www.python.org/)

## Prerequisites

To run this project, you will need to perform several installations, including:
- `HTML5` : This is the markup language used for structuring the content of web pages. It's a fundamental part of web development.
- `Python version 3` : This is necessary in this project as the debugger and parser for HTML tag

## Installation

If you want to run this program you will need to do these steps

1. Clone this repository :
```shell
git clone https://github.com/ChaiGans/TBFO-PDA-K01-PIN-KHIONG-HOK-88
```

2. Open directory :
```shell
cd  TBFO-PDA-K01-PIN-KHIONG-HOK-88
```

3. Run the main program :
```shell
python main.py "pda.txt" "<file.html>"
```

Make sure you define the pda file and the html file to run this program

## Features
- `Error Line`: This feature shows where the error line is in "file.html"
- `Error input`: This feature shows the false input from "file.html"
- `Correction for input`: This feature shows the recommendation of the correct input for "file.html"

## File Structures Overview
```
TBFO-PDA-K01-PIN-KHIONG-HOK-88
├─── docs
|    |
|    └─── Laporan_TBFO.pdf
|
├─── tools
|    | 
|    ├─── pdagrouper.py
|    | 
|    ├─── tfmaker(1).py
|    | 
|    └───tfmaker(2).py
|
├─── main.py
|
├─── pda.py
|
├─── pda.txt
|
└─── README.md       
```

This repository contains main structures such as files and folder.
- `main.py` : this file contain the debugger and testing program to make a transition functions and file open.
- `main.py` : this file contain the parser for HTML Tag and for terminal argument parse.
- `pda.py` : this file contain the parser for PDA and convert it to a data structure and checker for html key to know where the error is
- `pda.txt` : this file contain the PDA such as states, input symbols, stack symbols, starting state, starting stack symbol, final states, pda type, and transition functions

## Links
- Repository : https://github.com/ChaiGans/TBFO-PDA-K01-PIN-KHIONG-HOK-88/
- Issue tracker :
   - If you encounter any issues with the program, come across any disruptive bugs, or have any suggestions for improvement, please don't hesitate to reach out by sending an email to elbertchailes888@gmail.com. Your feedback is greatly appreciated.
- Github main contributor :
   - Contributor 1 (Filbert) - https://github.com/Filbert88
   - Contributor 2 (Elbert Chailes) - https://github.com/ChaiGans
   - Contributor 3 (Farel Winalda) - https://github.com/FarelW

