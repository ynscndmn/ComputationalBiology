# DNA Motif Search (Rosalind SUBS Solution) 🧬

## 1. Problem Overview
Identifying identical DNA intervals across different organisms is highly suggestive of conserved biological functions. These shared intervals are defined as **motifs**. A fundamental task in molecular biology is searching a genome for these known motifs to understand evolutionary relationships and functional regions.

The complexity of this search arises from **repeats**—intervals of DNA that occur multiple times, such as the **Alu repeat** in humans. These repeats indicate that the language of DNA is highly structured and non-random.

**Original Problem:** [Rosalind - Finding a Motif in DNA (SUBS)](https://rosalind.info/problems/subs/)



## 2. Technical Definition
Given two DNA strings $s$ and $t$, the goal is to find all locations of $t$ as a contiguous substring within $s$.

- **Substring Constraint:** $t$ must be contained within $s$ and $|t| \leq |s|$.
- **Indexing:** In bioinformatics standards, positions are **1-based**. The position of a symbol is the total number of symbols found to its left, including itself.
- **Overlapping:** The search must identify all starting positions $j$, even if the occurrences of $t$ overlap within the sequence.

### Example
- **Input (s):** `GATATATGCATATACTT`
- **Motif (t):** `ATAT`
- **Output:** `2 4 10`

---

## 3. Implementation Logic
The solution implements a **sliding window** algorithm with a time complexity of $O(n \times m)$. This approach ensures that every possible window in the genome is compared against the target motif, capturing overlapping sequences accurately.



### Functional Architecture
The program is designed with a modular structure:
- **Core Algorithm:** A specialized function handles string slicing and 1-based index collection.
- **Data Handling:** Functions are separated for processing predefined sample datasets and real-time user inputs.

---

## 4. Interface Structure
The tool features a minimalist Command Line Interface (CLI) controlled via a central menu:

1. **Run Sample Dataset:** Executes the algorithm using the standard Rosalind sample to verify logic.
2. **Manual Input Mode:** Allows for the entry of custom DNA strings ($s$) and motifs ($t$) for ad-hoc analysis.
3. **Exit:** Safely terminates the application.

---
*Developed for Computational Biology Lecture and Rosalind algorithm challenges.*

---
## 5. Author
- **Name:** Yunus Can Duman
- **Institution:** Ege University, Computer Engineering Student
