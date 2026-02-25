# 🧬 Abelon Sequence: Hybrid Network Backoff Algorithm

[🇧🇷 Read in Portuguese](README-ptBR.md)

![Status](https://img.shields.io/badge/Status-Prototype-blue)
![Language](https://img.shields.io/badge/Language-Python-yellow)

## 📌 Overview
This repository explores the **Abelon Sequence**, a mathematical model of hybrid progression applied to the optimization of Network Backoff algorithms.

The goal of this project is to demonstrate how a controlled transition between an **initial linear growth** and a **subsequent exponential expansion**, combined with randomness (*Jitter*), can effectively mitigate the *Thundering Herd* problem in servers under heavy stress.

---

## 🧮 The Math Behind It (Generating Rule)
The sequence proposes a smooth start followed by a controlled burst. The rule dictates that, starting from the fourth position, the number is strictly the sum of all preceding terms:

* $A_1 = 1$
* $A_2 = 2$
* $A_3 = 3$
* For $n \ge 4$: $$A_n = \sum_{i=1}^{n-1} A_i$$

This generates the sequence: `1, 2, 3, 6, 12, 24, 48, 96...`

Mathematically, from the 4th term onwards, the sequence behaves as a Geometric Progression with a common ratio of 2 ($A_n = 2A_{n-1}$), but it carries an intrinsic self-verifying property (where the current term subtracted from the sum of the previous terms equals zero).

---

## 🛑 The Problem: Thundering Herd
When a server crashes, thousands of clients attempt to reconnect simultaneously.
* If they use fixed intervals (e.g., retrying every 1s), the server suffers an accidental DDoS attack and crashes again.
* If they use standard *Exponential Backoff* (1, 2, 4, 8, 16s), the wait time scales too quickly, harming the user experience during brief outages.



## 💡 The Solution: Abelon Protocol + Jitter
This algorithm solves the problem by dividing the backoff into two phases and injecting *Jitter* (controlled chaos) to prevent exact millisecond collisions:

1. **Persistence Phase (1, 2, 3 seconds):** Allows three quick, low-latency attempts. Ideal for momentary network fluctuations.
2. **Protection Phase (6, 12, 24 seconds...):** If the problem persists, the system applies a hard brake using exponential growth, protecting the server's integrity from overload.

---

## 🚀 How to Run the Simulation

This repository contains a Python script that simulates 5 clients attempting to connect to a server using the Abelon Sequence with and without *Jitter*.

### Prerequisites
* Python 3.x installed.

### Step-by-Step
1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/abelon-network-algorithm.git](https://github.com/YOUR_USERNAME/abelon-network-algorithm.git)
