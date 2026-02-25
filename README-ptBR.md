# 🧬 Sequência de Abelon: Algoritmo Híbrido de Recuo de Rede (Backoff)

![Status](https://img.shields.io/badge/Status-Prototype-blue)
![Language](https://img.shields.io/badge/Language-Python-yellow)

## 📌 Visão Geral
Este repositório explora a **Sequência de Abelon**, um modelo matemático de progressão híbrida aplicado à otimização de algoritmos de recuo de rede (*Network Backoff*). 

O objetivo deste projeto é demonstrar como uma transição controlada entre um **crescimento linear inicial** e uma **expansão exponencial subsequente**, combinada com fatores de aleatoriedade (*Jitter*), pode mitigar o Efeito de Manada (*Thundering Herd*) em servidores sob estresse.

---

## 🧮 A Matemática por Trás (A Regra Geradora)
A sequência propõe um início suave seguido de uma explosão controlada. A regra de formação define que, a partir da quarta posição, o número é estritamente a soma de todos os termos precedentes:

* $A_1 = 1$
* $A_2 = 2$
* $A_3 = 3$
* Para $n \ge 4$: $$A_n = \sum_{i=1}^{n-1} A_i$$

Isso gera a sequência: `1, 2, 3, 6, 12, 24, 48, 96...`
Matematicamente, a partir do 4º termo, a sequência se comporta como uma Progressão Geométrica de razão 2 ($A_n = 2A_{n-1}$), mas carrega a propriedade intrínseca de autoverificação (onde o termo atual subtraído da soma dos anteriores resulta em zero).

---

## 🛑 O Problema: Efeito "Thundering Herd"
Quando um servidor cai, milhares de clientes tentam se reconectar simultaneamente. 
* Se usarem intervalos fixos (ex: tentar a cada 1s), o servidor sofre um ataque DDoS acidental e cai novamente.
* Se usarem o *Exponential Backoff* tradicional (1, 2, 4, 8, 16s), o tempo de espera escala muito rápido, prejudicando a experiência do usuário em falhas curtas.



## 💡 A Solução: Protocolo Abelon + Jitter
Este algoritmo resolve o problema dividindo o recuo em duas fases, adicionando o *Jitter* (caos controlado) para evitar colisões no mesmo milissegundo:

1. **Fase de Persistência (1, 2, 3 segundos):** Permite três tentativas rápidas e de baixa latência. Ideal para oscilações momentâneas de rede.
2. **Fase de Proteção (6, 12, 24 segundos...):** Se o problema persistir, o sistema freia bruscamente usando crescimento exponencial, protegendo a integridade do servidor.

---

## 🚀 Como Executar a Simulação

Este repositório contém um script em Python que simula 5 computadores tentando se conectar a um servidor usando a Sequência de Abelon com e sem *Jitter*.

### Pré-requisitos
* Python 3.x instalado.

### Passo a Passo
1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/abelon-network-algorithm.git](https://github.com/SEU_USUARIO/abelon-network-algorithm.git)
