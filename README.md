# 🏭 Calculadora de Controle de Produção e Expedição

<img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python" alt="Python Badge"> <img src="https://img.shields.io/badge/Versão-1.0_(Beta)-orange?style=flat-square" alt="Version Badge"> <img src="https://img.shields.io/badge/Status-Funcional_(Em_Aprimoramento)-yellow?style=flat-square" alt="Status Badge">

---

<h2 style="color: #FF8C00;">📄 Descrição do Projeto</h2>

Ferramenta desenvolvida em **Python** para automatizar os cálculos operacionais de produção e expedição industrial.

> **👨‍💻 Nota do Desenvolvedor:**
>
> O objetivo aqui foi identificar um problema real de eficiência no meu ambiente de trabalho como <span style="color: #FFA500;"><b>Operador de Sala de Controle</b></span> e solucioná-lo através do código. Mais do que apenas uma ferramenta útil, este repositório serve como um laboratório de aprendizado, onde busco aplicar lógica de programação, estruturação de código e boas práticas para aprimorar minhas competências técnicas e consolidar meus estudos na área de desenvolvimento de software.

Esta versão (v1.0) elimina erros manuais no cálculo de embalagens, determinando a quantidade exata de material (Big Bags, Sacarias ou Granel) baseando-se no peso específico de cada batelada e na linha de produção selecionada.

### 🚀 Evolução: Interface Web
Embora a versão atual funcione via terminal (CLI), o plano de expansão para este projeto envolve a criação de uma **Interface Gráfica Web**.

A intenção é migrar a lógica atual para o framework **Flask**, transformando o script em uma aplicação web acessível via navegador. Isso permitirá uma interação mais visual e intuitiva, facilitando o input de dados e a leitura dos resultados em qualquer dispositivo da sala de controle.

---

<h2 style="color: #FF8C00;">⚖️ Entendendo os Fatores de Cálculo</h2>

O sistema utiliza constantes específicas para calcular o peso total produzido antes de dividir pelo tamanho da embalagem. É fundamental entender a origem desses números:

* **Fator 2.000 (kg):** Refere-se ao peso padrão de **uma batelada** para as linhas (**Ruminantes** e **Aves/Suínos**).
* **Fator 1.000 (kg):** Refere-se ao peso padrão de **uma batelada** para a linha (**Pet** e **Peixes**).

---

<h2 style="color: #FF8C00;">🛠️ Tabela de Opções e Lógica Matemática</h2>

Abaixo está detalhado como o algoritmo processa cada escolha do menu:

| ID | Linha / Produto | Peso da Batelada | Fórmula Aplicada |
| :--- | :--- | :--- | :--- |
| `1` | **Bag Ruminantes** | 2.000 kg | `(2000 * Qtd Bateladas) / Peso do Bag` |
| `2` | **Bag Pet/Peixes** | 1.000 kg | `(1000 * Qtd Bateladas) / Peso do Bag` |
| `3` | **Sac Ruminantes** | 2.000 kg | `(2000 * Qtd Bateladas) / Peso da Sacaria` |
| `4` | **Sac Aves/Suínos** | 2.000 kg | `(2000 * Qtd Bateladas) / Peso da Sacaria` |
| `5` | **Sac Pet/Peixes** | 2.000 kg* | `(2000 * Qtd Bateladas) / Peso da Sacaria` |
| `6` | **Exp Granel Ruminantes** | 2.000 kg | `(2000 * Qtd Bateladas) / Peso Específico` |
| `7` | **Exp Granel Aves/Suínos** | 2.000 kg | `(2000 * Qtd Bateladas) / Peso Específico` |
| `8` | **Exp Granel Pet/Peixes** | 1.000 kg | `(1000 * Qtd Bateladas) / Peso Específico` |
| `9` | **Envase Cães** | 1.000 kg | `(1000 * Qtd Bateladas) / Peso do Pacote` |
| `10`| **Carregamento Expedição** | N/A | `(Carga Total / Qtd Caixas) - 10 kg` |

> **Nota sobre a Opção 10:** O cálculo subtrai **10 kg** do resultado final de cada caixa. Essa é uma margem de segurança obrigatória para evitar o sobrepeso no caminhão e garantir conformidade com a balança.

---

<h2 style="color: #FF8C00;">💻 Como Utilizar</h2>

1.  **Execute o script:**
    ```bash
    python calculo_destino_producao.py
    ```
2.  **Interação:**
    * Selecione a linha desejada no menu.
    * Insira a quantidade de bateladas produzidas.
    * Insira a capacidade da embalagem (quando solicitado).
3.  **Resultado:**
    * O sistema exibirá o valor formatado no padrão brasileiro (ex: `1.250,50`).

---

<h2 style="color: #FF8C00;">🚧 Melhorias Futuras (Roadmap)</h2>

Como o projeto está em aprimoramento contínuo, as seguintes funcionalidades estão planejadas:

* [ ] Adicionar validação para impedir que o usuário digite letras onde deve ser números.
* [ ] Implementar um loop para que o programa não feche após um único cálculo.
* [ ] Criar um registro (log) automático dos cálculos do dia.
* [ ] **Desenvolvimento da Interface Web com Flask.**

---

<h2 style="color: #FF8C00;">📝 Licença</h2>

Este projeto está sob a licença MIT.

Copyright © 2025 **Diogo Neves Nunes Paulista**

<div align="left">
    <sub>Projeto desenvolvido para otimização de processos industriais.</sub>
</div>