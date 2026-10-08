# Podstawy Programowania

Repozytorium zawiera materiały do przedmiotu **Computer Science 1 / Podstawy Programowania** dla studentów studiów inżynierskich Politechniki Warszawskiej.

Materiały mają interaktywną formę i mozna je uruchomić przez: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sgepner/Computer-Science-1.git/master)

> **Od zera do bohatera.**

Kurs jest przeznaczony dla osób, które nigdy wcześniej nie programowały. Jego celem nie jest możliwie szybkie nauczenie jednego konkretnego języka programowania. Chcemy przede wszystkim zbudować **solidne zrozumienie podstawowych pojęć programistycznych i myślenia algorytmicznego**.

Języki programowania się zmieniają.  
Narzędzia się zmieniają.  
Biblioteki i frameworki się zmieniają.  
Podstawowe koncepcje pozostają.

---

## Czego uczymy się na tym kursie?

Uczymy się, jak opisać problem w postaci algorytmu, a następnie jak przekształcić ten algorytm w działający program.

Zaczynamy od absolutnych podstaw:

- zmiennych i typów danych,
- operacji arytmetycznych i logicznych,
- operacji wejścia i wyjścia,
- instrukcji warunkowych,
- pętli,
- funkcji i dzielenia problemu na mniejsze części,
- pamięci, adresów i wskaźników,
- tablic,
- plików,
- dynamicznej alokacji pamięci,
- pracy z tekstem (string),
- struktur.

Po drodze poznajemy również podstawowe zagadnienia algorytmiczne: iterację, przetwarzanie zbiorów danych, sortowanie, proste obliczenia numeryczne oraz pierwsze pojęcia związane z kosztem algorytmu.

Chcemy rozumieć **co komputer rzeczywiście robi**, a nie jedynie wiedzieć, jakie polecenie należy wpisać.

---

## Dlaczego C?

Bardzo naturalne jest pytanie:

> Po co dzisiaj uczyć się C? Czy nie lepiej od razu zacząć od czegoś nowocześniejszego, jak Python albo Java?

Języki "wysokopoziomowe" takie jak Python są niezwykle użyteczne.
Jednocześnie bardzo skutecznie ukrywają przed programistą wiele szczegółów działania programu.

Na tym kursie celowo chcemy te szczegóły zobaczyć.

W C:

- dane mają jawnie określony typ (statyczne typowanie),
- różne typy zajmują różną ilość pamięci,
- zmienna znajduje się pod konkretnym adresem,
- możemy jawnie pracować z adresami,
- tablica ma konkretną reprezentację w pamięci,
- przekazanie wartości do funkcji i przekazanie adresu to dwie różne rzeczy,
- pamięć dynamiczną trzeba samodzielnie przydzielić i zwolnić,
- napis nie jest magicznym obiektem — jest odpowiednio zorganizowanym fragmentem pamięci,
- programista odpowiada za wiele operacji, które języki wyższego poziomu wykonują automatycznie.

To sprawia, że C bywa wymagający. Właśnie dlatego jest również bardzo dobrym językiem dydaktycznym.

Jeżeli coś działa, chcemy wiedzieć **dlaczego**.  
Jeżeli coś nie działa, chcemy wiedzieć **co dokładnie poszło źle**.

Celem kursu nie jest przekonywanie, że wszystkie przyszłe programy należy pisać w C. Chodzi o pokazanie mechanizmów, które języki wyższego poziomu często przed nami ukrywają.

Kiedy te mechanizmy zostaną zrozumiane, nauka kolejnego języka jest znacznie łatwiejsza. Python, C++, Java, Rust, Julia czy MATLAB oferują inną składnię i inne abstrakcje, ale pod nimi nadal znajdują się te same podstawowe idee: dane, operacje, przepływ sterowania, funkcje, pamięć i algorytmy.

---

## Dlaczego nie programowanie obiektowe?

Programowanie obiektowe jest ważne, ale **nie jest przedmiotem tego kursu**.

Zanim zaczniemy mówić o klasach, dziedziczeniu, polimorfizmie czy wzorcach projektowych, chcemy dobrze rozumieć bardziej podstawowe elementy programu:

**dane → operacje → decyzje → iteracja → funkcje → pamięć → struktury danych**

Dlatego koncentrujemy się na **programowaniu proceduralnym i strukturalnym**.

Najpierw chcemy nauczyć się rozwiązywać problemy za pomocą programu. Dopiero później przychodzi czas na bardziej zaawansowane sposoby organizowania dużych systemów programistycznych.

---

## Co powinieneś umieć po zakończeniu kursu?

Po ukończeniu przedmiotu powinieneś potrafić:

- przeanalizować prosty problem obliczeniowy lub inżynierski,
- sformułować algorytm jego rozwiązania,
- przekształcić algorytm w uporządkowany program,
- świadomie korzystać z warunków, pętli i funkcji,
- rozumieć podstawowe typy danych i ich konwersje,
- rozumieć związek pomiędzy zmienną a pamięcią komputera,
- posługiwać się wskaźnikami i tablicami,
- rozróżniać dane statyczne od dynamicznie alokowanych,
- odczytywać i zapisywać dane do plików,
- pracować z napisami i strukturami,
- rozpoznawać typowe błędy programistyczne,
- czytać i rozumieć stosunkowo proste programy w C,
- podejść do nauki nowego języka ze zrozumieniem koncepcji kryjących się pod jego składnią.

Najważniejszym efektem kursu nie jest zapamiętanie składni C (to i tak będziesz musiał zrobić).

Najważniejsze jest nauczenie się **myślenia programistycznego**.

---

## Jak uczyć się programowania?

Programowania nie da się nauczyć wyłącznie przez czytanie slajdów albo obserwowanie, jak ktoś inny pisze kod.

Pod tym względem przypomina ono matematykę, naukę gry na instrumencie albo robienie pompek:

**trzeba ćwiczyć.**

Czytaj przykłady.  
Kompiluj je.  
Modyfikuj.  
Psuj.  
Sprawdzaj, dlaczego przestały działać.  
Pisz własne programy.

Małe eksperymenty są jednym z najlepszych sposobów nauki programowania.

Repozytorium zawiera slajdy wykładowe, notebooki Jupyter oraz programy źródłowe używane podczas zajęć. Wiele przykładów jest celowo bardzo prostych, tak aby można było przyjrzeć się pojedynczej koncepcji bez zaciemniania jej niepotrzebną złożonością.

---

## Materiały

Repozytorium jest uporządkowane zgodnie z kolejnymi wykładami.

Materiał prowadzi w przybliżeniu przez następujące zagadnienia:

1. Wprowadzenie do programowania i języka C
2. Typy danych i wyrażenia
3. Wejście/wyjście i funkcje matematyczne
4. Instrukcje warunkowe i funkcje
5. Pętle i strukturalne sterowanie przebiegiem programu
6. Pamięć, adresy i wskaźniki
7. Tablice jednowymiarowe, sortowanie i pliki
8. Przetwarzanie danych z użyciem plików
9. Tablice dwuwymiarowe i pamięć dynamiczna
10. Dynamiczne tablice jedno- i dwuwymiarowe
11. Napisy
12. Struktury i dalsze zastosowania

Repozytorium zawiera również wiele małych programów w C ilustrujących omawiane na wykładzie zagadnienia.

---

# Computer Science 1

Lecture materials for the **Computer Science 1 / Programming Fundamentals** course for engineering students at the Warsaw University of Technology.

> **From Zero to Hero.**

This course is intended for students who may have never programmed before. Its goal is not to teach one particular programming language as quickly as possible. The goal is to build a **solid understanding of the fundamental ideas of programming and algorithmic thinking**.

Programming languages change. Tools change. Libraries and frameworks change. The basic concepts do not.

---

## What is this course about?

During the course we learn how to describe a problem as an algorithm and how to translate that algorithm into a working program.

We start from the very beginning:

- variables and data types,
- arithmetic and logical operations,
- input and output,
- decisions and branching,
- loops,
- functions and decomposition of a problem into smaller parts,
- memory, addresses and pointers,
- arrays,
- files,
- dynamic memory allocation,
- strings,
- structures.

Along the way we also introduce basic algorithmic ideas: iteration, searching and processing data, sorting, working with collections of values, numerical examples and reasoning about the cost of an algorithm.

The intention is to understand **what the computer is actually doing**, rather than only learning which command to type.

---

## Why C?

A natural question is:

> Why learn C today? Why not simply start with Python?

Python is an excellent and extremely useful language. It is also very good at hiding many details from the programmer.

For an introductory course, we deliberately want to expose those details.

In C:

- data has an explicit type,
- different types occupy different amounts of memory,
- variables live somewhere in memory,
- addresses can be inspected and manipulated,
- arrays have a concrete representation,
- passing a value and passing an address are different operations,
- dynamic memory must be explicitly allocated and released,
- strings are not magical objects — they are data stored in memory,
- the programmer has direct responsibility for many operations that higher-level languages perform automatically.

This makes C demanding, but it also makes it an excellent teaching language.

When something works, we want to understand **why** it works.  
When something fails, we want to understand **what** went wrong.

The purpose is not to convince you that every future program should be written in C. The purpose is to make the mechanisms hidden by higher-level languages visible.

Once these ideas are understood, learning another programming language becomes much easier. Python, C++, Java, Rust, Julia, MATLAB and many others provide different abstractions and syntax, but underneath them remain the same fundamental ideas: data, operations, control flow, functions, memory and algorithms.

---

## Why not object-oriented programming?

Object-oriented programming is important, but it is **not the subject of this course**.

Before introducing classes, inheritance, polymorphism and design patterns, we want to understand the more fundamental building blocks of a program:

**data → operations → decisions → iteration → functions → memory → data structures**

The course therefore concentrates on **procedural and structured programming**.

The objective is to learn how to solve a problem with a computer before learning more advanced ways of organising large software systems.

---

## What should you know after this course?

After completing the course, you should be able to:

- analyse a simple engineering or computational problem,
- formulate an algorithm solving it,
- translate the algorithm into a structured program,
- use conditions, loops and functions consciously,
- understand basic data types and conversions,
- understand the relation between variables and memory,
- use pointers and arrays,
- distinguish between static and dynamically allocated data,
- read and write data files,
- work with strings and structures,
- recognise common programming errors,
- read and understand relatively simple C programs,
- approach a new programming language with an understanding of the concepts behind its syntax.

The most important outcome is not memorising C syntax.

The most important outcome is to be able to **think like a programmer**.

---

## How to learn programming

Programming cannot be learned only by reading slides or watching someone else write code.

It is much closer to learning mathematics, playing an instrument, or doing push-ups:

**you need practice.**

Read the examples.  
Compile them.  
Change them.  
Break them.  
Try to understand why they stopped working.  
Write your own programs.

Small experiments are one of the best ways to learn.

The repository contains lecture slides, Jupyter notebooks and source-code examples used during the course. Many examples are intentionally simple so that a single programming concept can be examined in isolation.

---

## Course materials

The repository is organised according to consecutive lectures.

The material progresses roughly through:

1. Introduction to programming and C
2. Data types and expressions
3. Input/output and mathematical functions
4. Branching and functions
5. Loops and structured control flow
6. Memory, addresses and pointers
7. One-dimensional arrays, sorting and files
8. File-based data processing
9. Two-dimensional arrays and dynamic memory
10. Dynamic one- and two-dimensional arrays
11. Strings
12. Structures and further applications

The repository also contains numerous small C programs illustrating the concepts discussed during lectures.
