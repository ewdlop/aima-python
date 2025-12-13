

# `aima-python` [![Build Status](https://travis-ci.org/aimacode/aima-python.svg?branch=master)](https://travis-ci.org/aimacode/aima-python) [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/aimacode/aima-python)

> ⚠️ **人工智慧生成內容聲明**  
> 本 README 部分段落（特別是中文說明與歷史摘要）由人工智慧協助撰寫或潤飾，僅供參考。實際資訊仍以原始資料與官方文件為準，請在引用或修改時自行驗證內容。


Python code for the book *[Artificial Intelligence: A Modern Approach](http://aima.cs.berkeley.edu).* You can use this in conjunction with a course on AI, or for study on your own. We're looking for [solid contributors](https://github.com/aimacode/aima-python/blob/master/CONTRIBUTING.md) to help.

## 📚 關於書籍封面

### 第四版封面上的 AI 先驅們

第四版封面採用象棋棋盤設計，展示了 AI 發展史上的重要人物和里程碑：

#### 👤 歷史人物

- **艾達·洛芙萊斯（Ada Lovelace, 1815-1852）** 🌟 - **世界上第一位程序員**，封面上唯一的女性。她為巴貝奇的分析機撰寫了第一個算法，並在 1843 年就預見到計算機的潛力遠超過純粹的數字計算。她首次提出機器可以處理符號、創作音樂的遠見，奠定了現代編程的基礎概念，包括"循環"和"子程序"。

- **阿蘭·圖靈（Alan Turing, 1912-1954）** - 計算機科學家，人工智慧之父，提出了著名的圖靈測試和圖靈機的理論基礎，在二戰期間破解了 Enigma 密碼

- **亞里士多德（Aristotle, 384-322 BC）** - 古希臘哲學家，其著作《動物運動論》包含早期規劃算法的思想，為邏輯推理和 AI 哲學基礎做出貢獻

#### 🤖 機器人與 AI 系統

- **人形機器人** - 代表現代機器人技術的進展
- **火星探測車** - NASA 的機遇號或好奇號，展示 AI 在太空探索中的自主導航能力
- **自動駕駛汽車** - 現代 AI 在交通運輸領域的應用

#### 🏆 AI 里程碑時刻

- **國際象棋對弈** - 可能是深藍 vs 卡斯帕羅夫（1997）或其他經典對弈
- **圍棋棋盤** - 暗示 AlphaGo 在 2016 年擊敗李世乭，展示深度學習的突破

#### 💡 特別意義

**艾達·洛芙萊斯**在封面上的顯著位置（左下角），彰顯了女性在計算機科學史上不可或缺的貢獻。她比圖靈早出生近一個世紀，就已經理解了可編程計算機的革命性潛力，是當之無愧的編程先驅。

這些圖像共同反映了從哲學思辨到實體應用，從數學理論到工程實踐，從歷史傳承到現代創新的 AI 發展歷程。

---

## 🎓 章節與 AI 先驅人物對照

本節將 AIMA 各章節與相關的歷史人物和演算法貢獻者關聯起來。

### 📖 Part I: Artificial Intelligence (人工智慧基礎)

**Chapter 1-2: Introduction & Intelligent Agents**

- **艾達·洛芙萊斯（Ada Lovelace, 1815-1852）** 👩‍💻 - 世界上第一位程序員，可編程機器的遠見者
- **阿蘭·圖靈（Alan Turing, 1912-1954）** 🧠 - 圖靈測試、圖靈機，AI 理論基礎
- **約翰·麥卡錫（John McCarthy, 1927-2011）** 🎯 - 創造"人工智慧"一詞（1956），LISP 發明者

### 🔍 Part II: Problem-Solving (問題求解)

**Chapter 3-4: Search Algorithms**

- **亞里士多德（Aristotle, 384-322 BC）** 📜 - 邏輯推理、目標導向推理哲學基礎
- **艾茲赫爾·迪科斯徹（Edsger Dijkstra, 1930-2002）** 🗺️ - Dijkstra 算法（最短路徑）
- **約翰·霍蘭（John Holland, 1929-2015）** 🧬 - 遺傳算法 (Figure 4.8)

### ♟️ Part III: Knowledge, Reasoning, and Planning

**Chapter 5: Adversarial Search & Games**

- **克勞德·香農（Claude Shannon, 1916-2001）** 📡 - 第一個國際象棋程序（1950），Minimax (Figure 5.3)
- **約翰·馮·諾依曼（John von Neumann, 1903-1957）** 🎲 - 博弈論、Minimax 理論基礎
- **加里·卡斯帕羅夫（Garry Kasparov, 1963-）** ♟️ - 與深藍的歷史性對弈（1997）
- **許峰雄（Feng-hsiung Hsu, 1959-）** 🖥️ - 深藍主要設計者，Alpha-Beta Search (Figure 5.7)
- **傑米斯·哈薩比斯（Demis Hassabis, 1976-）** 🎮 - AlphaGo、DeepMind 創始人

**Chapter 6: Constraint Satisfaction Problems**

- **艾倫·麥肯沃思（Alan Mackworth, 1945-）** 🔗 - AC-3 算法 (Figure 6.3)

**Chapter 7-9: Logic & Knowledge Representation**

- **喬治·布爾（George Boole, 1815-1864）** ⚡ - 布爾代數、現代計算機邏輯基礎
- **戈特洛布·弗雷格（Gottlob Frege, 1848-1925）** 📐 - 一階邏輯、FOL-BC-Ask (Figure 9.6)
- **阿隆佐·邱奇（Alonzo Church, 1903-1995）** λ - Lambda 演算、Unify (Figure 9.1)
- **約翰·艾倫·羅賓遜（John Alan Robinson, 1930-2016）** 🔄 - 歸結原理、PL-Resolution (Figure 7.12)

**🆕 證明論與類型論擴展 (2024, a knowledge cutoff) 新增**

- 🆕 **格哈德·根岑（Gerhard Gentzen, 1909-1945）** 🎓 - 自然演繹、序列演算 (Figures 9.16-9.17)，現代證明論奠基人
- 🆕 **哈斯凱爾·柯里（Haskell Curry, 1900-1982）** 🔗 - Curry-Howard 同構 (Figure 9.27)，連接邏輯與計算
- 🆕 **威廉·霍華德（William Howard, 1926-）** 🌉 - Curry-Howard 對應（1969），證明即程序
- 🆕 **羅賓·米爾納（Robin Milner, 1934-2010）** 🏆 - Hindley-Milner 類型系統 (Figure 9.25)，1991 年圖靈獎
- 🆕 **羅傑·欣德利（Roger Hindley, 1937-）** 📝 - 類型推斷算法，ML 語言類型系統
- 🆕 **讓-伊夫·吉拉德（Jean-Yves Girard, 1947-）** ⚛️ - 線性邏輯 (Figure 9.33)、System F (Figure 9.35)
- 🆕 **珀·馬丁-洛夫（Per Martin-Löf, 1942-）** 🔬 - 直覺類型論 (Figure 9.36)、依賴類型、構造主義
- 🆕 **西蒙·佩頓·瓊斯（Simon Peyton Jones, 1958-）** 💎 - Haskell 語言設計者，函數式編程先驅
- 🆕 **羅伯特·哈珀（Robert Harper, 1957-）** 📚 - ML 家族語言，《實用的編程語言基礎》作者

**🆕 Curry-Howard 同構：邏輯與計算的統一 🌉**

這一理論揭示了三個看似不同領域之間的深刻對應：

| 邏輯 (Logic) | 類型論 (Type Theory) | 計算 (Computation) |
|:------------|:-------------------|:------------------|
| 命題 | 類型 | 程序規範 |
| 證明 | 程序 | 實現 |
| 蘊含 (A → B) | 函數類型 (A → B) | Lambda 抽象 |
| 合取 (A ∧ B) | 積類型 (A × B) | Pair 構造 |
| 析取 (A ∨ B) | 和類型 (A + B) | Union 類型 |
| 真 (⊤) | 單位類型 (Unit) | void |
| 假 (⊥) | 空類型 (Empty) | 發散 |

**相關算法**: Natural-Deduction (9.16), Lambda-Calculus (9.20), Type-Inference (9.24), Curry-Howard-Isomorphism (9.27)

**實際應用**:
- 🔍 **形式化驗證**: Coq、Agda、Lean 等定理證明器
- 💻 **類型安全語言**: Haskell、OCaml、Rust、TypeScript
- 🎯 **程序合成**: 從規範自動生成程序
- 🛡️ **安全保證**: 編譯時檢測錯誤

**Chapter 10-11: Planning**

- **理查德·菲克斯（Richard Fikes, 1943-）** 📋 - STRIPS、Graphplan (Figure 10.9)
- **埃爾·薩克達尼（Earl Sacerdoti, 1946-）** 🏗️ - 層次規劃、Hierarchical-Search (Figure 11.5)

### 🎲 Part IV: Uncertain Knowledge and Reasoning

**Chapter 13-15: Probability & Bayesian Networks**

- **托馬斯·貝葉斯（Thomas Bayes, 1701-1761）** 📊 - 貝葉斯定理、Enumeration-Ask (Figure 14.9)
- **皮埃爾-西蒙·拉普拉斯（Pierre-Simon Laplace, 1749-1827）** 🌟 - 概率論發展
- **朱迪亞·珀爾（Judea Pearl, 1936-）** 🕸️ - 貝葉斯網絡，2011 年圖靈獎

**Chapter 16-17: Making Decisions**

- **約翰·馮·諾依曼（John von Neumann, 1903-1957）** 🎯 - 效用理論、決策理論
- **理查德·貝爾曼（Richard Bellman, 1920-1984）** 🔄 - 動態規劃、Value-Iteration (Figure 17.4)
- **羅納德·霍華德（Ronald Howard, 1934-）** 📈 - MDP 理論、POMDP (Figure 17.9)

### 🤖 Part V: Learning (學習)

**Chapter 18-19: Learning from Examples**

- **亞瑟·塞繆爾（Arthur Samuel, 1901-1990）** 🎮 - 創造"機器學習"一詞（1959）
- **弗蘭克·羅森布拉特（Frank Rosenblatt, 1928-1971）** 🧠 - 感知器、神經網絡先驅
- **深度學習三巨頭**（2018 年圖靈獎）：
  - **傑弗里·辛頓（Geoffrey Hinton, 1947-）** 🎓 - 反向傳播、Back-Prop (Figure 18.24)
  - **揚·樂昆（Yann LeCun, 1960-）** 🖼️ - 卷積神經網絡（CNN）
  - **約書亞·本吉奧（Yoshua Bengio, 1964-）** 📚 - 深度學習理論
- **羅伯特·夏皮爾（Robert Schapire, 1963-）** 🌳 - AdaBoost (Figure 18.34)

**Chapter 20: Learning Probabilistic Models**

- **大衛·魯梅爾哈特（David Rumelhart, 1942-2011）** 🔬 - 反向傳播算法、神經網絡復興

**Chapter 21: Reinforcement Learning**

- **理查德·薩頓（Richard Sutton, 1946-）** 🎯 - TD-Learning、Q-Learning (Figure 21.8)
- **安德魯·巴托（Andrew Barto, 1948-）** 📖 - 強化學習理論、Actor-Critic
- **克里斯·沃金斯（Chris Watkins, 1954-）** Q - Q-Learning 算法
- **沃爾克·米赫（Volodymyr Mnih, 1985-）** 🎮 - DQN、DeepMind Atari 突破

### 🗣️ Part VI: Communicating, Perceiving, and Acting

**Chapter 22-23: Natural Language Processing**

- **諾姆·喬姆斯基（Noam Chomsky, 1928-）** 📝 - 形式語法、CYK-Parse (Figure 23.5)
- **費迪南德·德·索緒爾（Ferdinand de Saussure, 1857-1913）** 🔤 - 現代語言學基礎

**Chapter 24: Perception**

- **大衛·馬爾（David Marr, 1945-1980）** 👁️ - 計算視覺理論
- **費·費·李（Fei-Fei Li, 1976-）** 📸 - ImageNet、現代計算機視覺革命

**Chapter 25: Robotics**

- **約瑟夫·恩格爾伯格（Joseph Engelberger, 1925-2015）** 🦾 - 工業機器人之父
- **塞巴斯蒂安·特倫（Sebastian Thrun, 1967-）** 🚗 - 自動駕駛先驅、Monte-Carlo-Localization (Figure 25.9)
- **羅德尼·布魯克斯（Rodney Brooks, 1954-）** 🤖 - 行為機器人學、Roomba
- **辛西婭·布雷澤爾（Cynthia Breazeal, 1967-）** 👩‍🔬 - 社交機器人、Kismet

### 📚 作者

- **斯圖爾特·羅素（Stuart Russell, 1962-）** 📖 - UC Berkeley 教授，AI 安全研究
- **彼得·諾維格（Peter Norvig, 1956-）** 💻 - 前 Google 研究總監

### 🎯 封面象徵意義

象棋棋盤設計象徵：
1. **策略思考** ♟️ - AI 的核心能力
2. **對抗與合作** 🤝 - 多智能體系統
3. **搜索與規劃** 🔍 - 問題求解方法
4. **歷史傳承** 📜 - 從古代到現代
5. **跨領域整合** 🧩 - 從哲學到工程

每個棋子的隱喻：**王**👑目標、**后**💎搜索、**騎士**🐴跳躍思維、**象**📐推理、**車**🏰邏輯、**兵**👤基礎

### 📊 AI 歷史時間線

```
BC 384   亞里士多德誕生
1701     貝葉斯誕生
1815     艾達·洛芙萊斯誕生
1843     艾達撰寫第一個算法
🆕 1935     根岑發表自然演繹系統 🎓
🆕 1936     邱奇發表 Lambda 演算 λ
1912     圖靈誕生
1936     圖靈發表圖靈機
1950     圖靈測試提出
1956     達特茅斯會議 - "AI" 誕生
1959     "機器學習"一詞誕生
🆕 1969     霍華德發現 Curry-Howard 對應 🌉
🆕 1971     Martin-Löf 發表直覺類型論 🔬
🆕 1978     Hindley-Milner 類型系統發表 📝
🆕 1987     線性邏輯由 Girard 提出 ⚛️
🆕 1991     Milner 獲圖靈獎（類型論） 🏆
1997     深藍擊敗卡斯帕羅夫
2011     Pearl 獲圖靈獎
2016     AlphaGo 擊敗李世乭
2018     深度學習三巨頭獲圖靈獎
```

### 🌟 致敬

這些先驅們的工作，從古希臘哲學到現代深度學習，共同編織了人工智慧的璀璨歷史。

**特別致敬艾達·洛芙萊斯** 👩‍💻 - 作為封面上唯一的女性，她提醒我們：創新無關性別、遠見比時代重要、第一步最為關鍵。

**🆕 特別致敬證明論與類型論先驅們** 🎓 - 根岑、柯里、霍華德、米爾納等人揭示了邏輯、證明與程序之間的深刻統一，為現代形式化驗證、函數式編程和類型安全語言奠定了理論基礎。Curry-Howard 同構不僅是數學之美，更是連接思維與計算的橋樑。

*"We can only see a short distance ahead, but we can see plenty there that needs to be done."* — Alan Turing

*"The Analytical Engine weaves algebraic patterns, just as the Jacquard loom weaves flowers and leaves."* — Ada Lovelace

🆕 *"Proofs are programs, and the formula it proves is the type for the program."* — Curry-Howard Correspondence

---

# Updates for 4th Edition

The 4th edition of the book as out now in 2020, and thus we are updating the code. All code here will reflect the 4th edition. Changes include:

- Move from Python 3.5 to 3.7.
- More emphasis on Jupyter (Ipython) notebooks.
- More projects using external packages (tensorflow, etc.).



# Structure of the Project

When complete, this project will have Python implementations for all the pseudocode algorithms in the book, as well as tests and examples of use. For each major topic, such as `search`, we provide the following  files:

- `search.ipynb` and `search.py`: Implementations of all the pseudocode algorithms, and necessary support functions/classes/data. The `.py` file is generated automatically from the `.ipynb` file; the idea is that it is easier to read the documentation in the `.ipynb` file.
- `search_XX.ipynb`: Notebooks that show how to use the code, broken out into various topics (the `XX`).
- `tests/test_search.py`: A lightweight test suite, using `assert` statements, designed for use with [`py.test`](http://pytest.org/latest/), but also usable on their own.

# Python 3.7 and up

The code for the 3rd edition was in Python 3.5; the current 4th edition code is in Python 3.7. It should also run in later versions, but does not run in Python 2. You can [install Python](https://www.python.org/downloads) or use a browser-based Python interpreter such as [repl.it](https://repl.it/languages/python3).
You can run the code in an IDE, or from the command line with `python -i filename.py` where the `-i` option puts you in an interactive loop where you can run Python functions. All notebooks are available in a [binder environment](http://mybinder.org/repo/aimacode/aima-python). Alternatively, visit [jupyter.org](http://jupyter.org/) for instructions on setting up your own Jupyter notebook environment.

Features from Python 3.6 and 3.7 that we will be using for this version of the code:
- [f-strings](https://docs.python.org/3.6/whatsnew/3.6.html#whatsnew36-pep498): all string formatting should be done with `f'var = {var}'`, not with `'var = {}'.format(var)` nor `'var = %s' % var`.
- [`typing` module](https://docs.python.org/3.7/library/typing.html): declare functions with type hints: `def successors(state) -> List[State]:`; that is, give type declarations, but omit them when it is obvious. I don't need to say `state: State`, but in another context it would make sense to say `s: State`.
- Underscores in numerics: write a million as `1_000_000` not as `1000000`.
- [`dataclasses` module](https://docs.python.org/3.7/library/dataclasses.html#module-dataclasses): replace `namedtuple` with `dataclass`.


[//]: # (There is a sibling [aima-docker]https://github.com/rajatjain1997/aima-docker project that shows you how to use docker containers to run more complex problems in more complex software environments.)


## Installation Guide

To download the repository:

`git clone https://github.com/aimacode/aima-python.git`

Then you need to install the basic dependencies to run the project on your system:

```
cd aima-python
pip install -r requirements.txt
```

You also need to fetch the datasets from the [`aima-data`](https://github.com/aimacode/aima-data) repository:

```
git submodule init
git submodule update
```

Wait for the datasets to download, it may take a while. Once they are downloaded, you need to install `pytest`, so that you can run the test suite:

`pip install pytest`

Then to run the tests:

`py.test`

And you are good to go!


# Index of Algorithms

Here is a table of algorithms, the figure, name of the algorithm in the book and in the repository, and the file where they are implemented in the repository. This chart was made for the third edition of the book and is being updated for the upcoming fourth edition. Empty implementations are a good place for contributors to look for an issue. The [aima-pseudocode](https://github.com/aimacode/aima-pseudocode) project describes all the algorithms from the book. An asterisk next to the file name denotes the algorithm is not fully implemented. Another great place for contributors to start is by adding tests and writing on the notebooks. You can see which algorithms have tests and notebook sections below. If the algorithm you want to work on is covered, don't worry! You can still add more tests and provide some examples of use in the notebook!

| **Figure** | **Name (in 4<sup>th</sup> edition)** | **Name (in repository)** | **Category** | **File** | **Tests** | **Notebook** |
|:-------|:----------------------------------|:------------------------------|:------------|:--------------------------------|:-----|:---------|
| 2      | Random-Vacuum-Agent               | `RandomVacuumAgent`           | Agents | [`agents.py`][agents]           | Done | Included |
| 2      | Model-Based-Vacuum-Agent          | `ModelBasedVacuumAgent`       | Agents | [`agents.py`][agents]           | Done | Included |
| 2.1    | Environment                       | `Environment`                 | Agents | [`agents.py`][agents]           | Done | Included |
| 2.1    | Agent                             | `Agent`                       | Agents | [`agents.py`][agents]           | Done | Included |
| 2.3    | Table-Driven-Vacuum-Agent         | `TableDrivenVacuumAgent`      | Agents | [`agents.py`][agents]           | Done | Included |
| 2.7    | Table-Driven-Agent                | `TableDrivenAgent`            | Agents | [`agents.py`][agents]           | Done | Included |
| 2.8    | Reflex-Vacuum-Agent               | `ReflexVacuumAgent`           | Agents | [`agents.py`][agents]           | Done | Included |
| 2.10   | Simple-Reflex-Agent               | `SimpleReflexAgent`           | Agents | [`agents.py`][agents]           | Done | Included |
| 2.12   | Model-Based-Reflex-Agent          | `ReflexAgentWithState`        | Agents | [`agents.py`][agents]           | Done | Included |
| 3      | Problem                           | `Problem`                     | Search | [`search.py`][search]           | Done | Included |
| 3      | Node                              | `Node`                        | Search | [`search.py`][search]           | Done | Included |
| 3      | Queue                             | `Queue`                       | Search | [`utils.py`][utils]             | Done | No Need  |
| 3.1    | Simple-Problem-Solving-Agent      | `SimpleProblemSolvingAgent`   | Search | [`search.py`][search]           | Done | Included |
| 3.2    | Romania                           | `romania`                     | Search | [`search.py`][search]           | Done | Included |
| 3.7    | Tree-Search                       | `depth/breadth_first_tree_search`                 | Search | [`search.py`][search]           | Done | Included |
| 3.7    | Graph-Search                      | `depth/breadth_first_graph_search`                | Search | [`search.py`][search]           | Done | Included |
| 3.11   | Breadth-First-Search              | `breadth_first_graph_search`  | Search | [`search.py`][search]           | Done | Included |
| 3.14   | Uniform-Cost-Search               | `uniform_cost_search`         | Search | [`search.py`][search]           | Done | Included |
| 3.17   | Depth-Limited-Search              | `depth_limited_search`        | Search | [`search.py`][search]           | Done | Included |
| 3.18   | Iterative-Deepening-Search        | `iterative_deepening_search`  | Search | [`search.py`][search]           | Done | Included |
| 3.22   | Best-First-Search                 | `best_first_graph_search`     | Search | [`search.py`][search]           | Done | Included |
| 3.24   | A\*-Search                        | `astar_search`                | Search | [`search.py`][search]           | Done | Included |
| 3.26   | Recursive-Best-First-Search       | `recursive_best_first_search` | Search | [`search.py`][search]           | Done | Included |
| 4.2    | Hill-Climbing                     | `hill_climbing`               | Search | [`search.py`][search]           | Done | Included |
| 4.5    | Simulated-Annealing               | `simulated_annealing`         | Search | [`search.py`][search]           | Done | Included |
| 4.8    | Genetic-Algorithm                 | `genetic_algorithm`           | Search | [`search.py`][search]           | Done | Included |
| 4.11   | And-Or-Graph-Search               | `and_or_graph_search`         | Search | [`search.py`][search]           | Done | Included |
| 4.21   | Online-DFS-Agent                  | `online_dfs_agent`            | Search | [`search.py`][search]           | Done | Included |
| 4.24   | LRTA\*-Agent                      | `LRTAStarAgent`               | Search | [`search.py`][search]           | Done | Included |
| 5.3    | Minimax-Decision                  | `minimax_decision`            | Games | [`games.py`][games]             | Done | Included |
| 5.7    | Alpha-Beta-Search                 | `alphabeta_search`            | Games | [`games.py`][games]             | Done | Included |
| 6      | CSP                               | `CSP`                         | CSP | [`csp.py`][csp]                 | Done | Included |
| 6.3    | AC-3                              | `AC3`                         | CSP | [`csp.py`][csp]                 | Done | Included |
| 6.5    | Backtracking-Search               | `backtracking_search`         | CSP | [`csp.py`][csp]                 | Done | Included |
| 6.8    | Min-Conflicts                     | `min_conflicts`               | CSP | [`csp.py`][csp]                 | Done | Included |
| 6.11   | Tree-CSP-Solver                   | `tree_csp_solver`             | CSP | [`csp.py`][csp]                 | Done | Included |
| 7      | KB                                | `KB`                          | Logic | [`logic.py`][logic]             | Done | Included |
| 7.1    | KB-Agent                          | `KB_AgentProgram`             | Logic | [`logic.py`][logic]             | Done | Included |
| 7.7    | Propositional Logic Sentence      | `Expr`                        | Logic | [`utils.py`][utils]             | Done | Included |
| 7.10   | TT-Entails                        | `tt_entails`                  | Logic | [`logic.py`][logic]             | Done | Included |
| 7.12   | PL-Resolution                     | `pl_resolution`               | Logic | [`logic.py`][logic]             | Done | Included |
| 7.14   | Convert to CNF                    | `to_cnf`                      | Logic | [`logic.py`][logic]             | Done | Included |
| 7.15   | PL-FC-Entails?                    | `pl_fc_entails`               | Logic | [`logic.py`][logic]             | Done | Included |
| 7.17   | DPLL-Satisfiable?                 | `dpll_satisfiable`            | Logic | [`logic.py`][logic]             | Done | Included |
| 7.18   | WalkSAT                           | `WalkSAT`                     | Logic | [`logic.py`][logic]             | Done | Included |
| 7.19   | GSAT                              | `GSAT`                        | Logic | [`logic.py`][logic]             |      |          |
| 7.19a  | Simulated-Annealing-SAT           | `simulated_annealing_sat`     | Logic | [`logic.py`][logic]             |      |          |
| 7.19b  | Beam-Search-SAT                   | `beam_search_sat`             | Logic | [`logic.py`][logic]             |      |          |
| 7.20   | Hybrid-Wumpus-Agent               | `HybridWumpusAgent`           | Logic |                                 |      |          |
| 7.21   | Model-Checking                    | `model_checking`              | Logic | [`logic.py`][logic]             |      |          |
| 7.22   | SATPlan                           | `SAT_plan`                    | Logic | [`logic.py`][logic]             | Done | Included |
| 8.1    | Horn-Clause-Resolution            | `horn_resolution`             | Logic | [`logic.py`][logic]             |      |          |
| 8.2    | Forward-Chaining-Horn             | `forward_chaining_horn`       | Logic | [`logic.py`][logic]             |      |          |
| 8.3    | Backward-Chaining-Horn            | `backward_chaining_horn`      | Logic | [`logic.py`][logic]             |      |          |
| 9      | Subst                             | `subst`                       | Logic | [`logic.py`][logic]             | Done | Included |
| 9.1    | Unify                             | `unify`                       | Logic | [`logic.py`][logic]             | Done | Included |
| 9.3    | FOL-FC-Ask                        | `fol_fc_ask`                  | Logic | [`logic.py`][logic]             | Done | Included |
| 9.6    | FOL-BC-Ask                        | `fol_bc_ask`                  | Logic | [`logic.py`][logic]             | Done | Included |
| 9.7    | FOL-Resolution                    | `fol_resolution`              | Logic | [`logic.py`][logic]             |      |          |
| 9.8    | Skolemization                     | `skolemize`                   | Logic | [`logic.py`][logic]             |      |          |
| 9.9    | Herbrand-Universe                 | `herbrand_universe`           | Logic | [`logic.py`][logic]             |      |          |
| 9.10   | Paramodulation                    | `paramodulation`              | Logic | [`logic.py`][logic]             |      |          |
| 9.11   | Subsumption                       | `subsumption`                 | Logic | [`logic.py`][logic]             |      |          |
| 9.12   | Demodulation                      | `demodulation`                | Logic | [`logic.py`][logic]             |      |          |
| 9.13   | Unification-With-Occurs-Check     | `unify_occurs_check`          | Logic | [`logic.py`][logic]             |      |          |
| 9.14   | Most-General-Unifier              | `mgu`                         | Logic | [`logic.py`][logic]             |      |          |
| 9.15   | Answer-Extraction                 | `answer_extraction`           | Logic | [`logic.py`][logic]             |      |          |
| 9.16   | **Natural-Deduction** 🎓          | `natural_deduction`           | Logic | [`proof_theory.py`][proof]      |      |          |
| 9.17   | **Sequent-Calculus** 🎓           | `sequent_calculus`            | Logic | [`proof_theory.py`][proof]      |      |          |
| 9.18   | Proof-Normalization               | `proof_normalize`             | Logic | [`proof_theory.py`][proof]      |      |          |
| 9.19   | Proof-Search                      | `proof_search`                | Logic | [`proof_theory.py`][proof]      |      |          |
| 9.20   | **Lambda-Calculus** 🎓            | `lambda_calculus`             | Logic | [`type_theory.py`][types]       |      |          |
| 9.21   | Beta-Reduction                    | `beta_reduction`              | Logic | [`type_theory.py`][types]       |      |          |
| 9.22   | Alpha-Conversion                  | `alpha_conversion`            | Logic | [`type_theory.py`][types]       |      |          |
| 9.23   | Eta-Conversion                    | `eta_conversion`              | Logic | [`type_theory.py`][types]       |      |          |
| 9.24   | **Type-Inference** 🎓             | `type_inference`              | Logic | [`type_theory.py`][types]       |      |          |
| 9.25   | **Hindley-Milner** 🎓             | `hindley_milner`              | Logic | [`type_theory.py`][types]       |      |          |
| 9.26   | Type-Checking                     | `type_check`                  | Logic | [`type_theory.py`][types]       |      |          |
| 9.27   | **Curry-Howard-Isomorphism** 🌟🎓 | `curry_howard`                | Logic | [`type_theory.py`][types]       |      |          |
| 9.28   | Proof-Terms                       | `proof_terms`                 | Logic | [`type_theory.py`][types]       |      |          |
| 9.29   | Propositions-As-Types             | `propositions_as_types`       | Logic | [`type_theory.py`][types]       |      |          |
| 9.30   | Programs-As-Proofs                | `programs_as_proofs`          | Logic | [`type_theory.py`][types]       |      |          |
| 9.31   | Intuitionistic-Logic              | `intuitionistic_logic`        | Logic | [`proof_theory.py`][proof]      |      |          |
| 9.32   | Constructive-Proof                | `constructive_proof`          | Logic | [`proof_theory.py`][proof]      |      |          |
| 9.33   | Linear-Logic                      | `linear_logic`                | Logic | [`proof_theory.py`][proof]      |      |          |
| 9.34   | Simply-Typed-Lambda-Calculus      | `stlc`                        | Logic | [`type_theory.py`][types]       |      |          |
| 9.35   | System-F                          | `system_f`                    | Logic | [`type_theory.py`][types]       |      |          |
| 9.36   | Dependent-Types                   | `dependent_types`             | Logic | [`type_theory.py`][types]       |      |          |
| 10.1   | Air-Cargo-problem                 | `air_cargo`                   | Planning | [`planning.py`][planning]       | Done | Included |
| 10.2   | Spare-Tire-Problem                | `spare_tire`                  | Planning | [`planning.py`][planning]       | Done | Included |
| 10.3   | Three-Block-Tower                 | `three_block_tower`           | Planning | [`planning.py`][planning]       | Done | Included |
| 10.7   | Cake-Problem                      | `have_cake_and_eat_cake_too`  | Planning | [`planning.py`][planning]       | Done | Included |
| 10.9   | Graphplan                         | `GraphPlan`                   | Planning | [`planning.py`][planning]       | Done | Included |
| 10.13  | Partial-Order-Planner             | `PartialOrderPlanner`         | Planning | [`planning.py`][planning]       | Done | Included |
| 11.1   | Job-Shop-Problem-With-Resources   | `job_shop_problem`            | Planning | [`planning.py`][planning]       | Done | Included |
| 11.5   | Hierarchical-Search               | `hierarchical_search`         | Planning | [`planning.py`][planning]       | Done | Included |
| 11.8   | Angelic-Search                    | `angelic_search`              | Planning | [`planning.py`][planning]       | Done | Included |
| 11.10  | Doubles-tennis                    | `double_tennis_problem`       | Planning | [`planning.py`][planning]       | Done | Included |
| 13     | Discrete Probability Distribution | `ProbDist`                    | Probability | [`probability.py`][probability] | Done | Included |
| 13.1   | DT-Agent                          | `DTAgent`                     | Probability | [`probability.py`][probability] | Done | Included |
| 14.9   | Enumeration-Ask                   | `enumeration_ask`             | Probability | [`probability.py`][probability] | Done | Included |
| 14.11  | Elimination-Ask                   | `elimination_ask`             | Probability | [`probability.py`][probability] | Done | Included |
| 14.13  | Prior-Sample                      | `prior_sample`                | Probability | [`probability.py`][probability] | Done | Included |
| 14.14  | Rejection-Sampling                | `rejection_sampling`          | Probability | [`probability.py`][probability] | Done | Included |
| 14.15  | Likelihood-Weighting              | `likelihood_weighting`        | Probability | [`probability.py`][probability] | Done | Included |
| 14.16  | Gibbs-Ask                         | `gibbs_ask`                   | Probability | [`probability.py`][probability] | Done | Included |
| 15.4   | Forward-Backward                  | `forward_backward`            | Probability | [`probability.py`][probability] | Done | Included |
| 15.6   | Fixed-Lag-Smoothing               | `fixed_lag_smoothing`         | Probability | [`probability.py`][probability] | Done | Included |
| 15.17  | Particle-Filtering                | `particle_filtering`          | Probability | [`probability.py`][probability] | Done | Included |
| 16.9   | Information-Gathering-Agent       | `InformationGatheringAgent`   | Probability | [`probability.py`][probability] | Done | Included |
| 17.4   | Value-Iteration                   | `value_iteration`             | MDP | [`mdp.py`][mdp]                 | Done | Included |
| 17.7   | Policy-Iteration                  | `policy_iteration`            | MDP | [`mdp.py`][mdp]                 | Done | Included |
| 17.9   | POMDP-Value-Iteration             | `pomdp_value_iteration`       | MDP | [`mdp.py`][mdp]                 | Done | Included |
| 18.5   | Decision-Tree-Learning            | `DecisionTreeLearner`         | Learning | [`learning.py`][learning]       | Done | Included |
| 18.8   | Cross-Validation                  | `cross_validation`            | Learning | [`learning.py`][learning]\*     |      |          |
| 18.11  | Decision-List-Learning            | `DecisionListLearner`         | Learning | [`learning.py`][learning]\*     |      |          |
| 18.24  | Back-Prop-Learning                | `BackPropagationLearner`      | Learning | [`learning.py`][learning]       | Done | Included |
| 18.34  | AdaBoost                          | `AdaBoost`                    | Learning | [`learning.py`][learning]       | Done | Included |
| 18.35 | **Adam-Optimizer** 🌟 | `Adam` | Deep Learning | [`optimizers.py`][opt] | Kingma & Ba (2014) | 建議 |
| 19.2   | Current-Best-Learning             | `current_best_learning`       | Knowledge | [`knowledge.py`](knowledge.py)  | Done | Included |
| 19.3   | Version-Space-Learning            | `version_space_learning`      | Knowledge | [`knowledge.py`](knowledge.py)  | Done | Included |
| 19.8   | Minimal-Consistent-Det            | `minimal_consistent_det`      | Knowledge | [`knowledge.py`](knowledge.py)  | Done | Included |
| 19.12  | FOIL                              | `FOIL_container`              | Knowledge | [`knowledge.py`](knowledge.py)  | Done | Included |
| 21.2   | Passive-ADP-Agent                 | `PassiveADPAgent`             | Reinforcement Learning | [`rl.py`][rl]                   | Done | Included |
| 21.4   | Passive-TD-Agent                  | `PassiveTDAgent`              | Reinforcement Learning | [`rl.py`][rl]                   | Done | Included |
| 21.8   | Q-Learning-Agent                  | `QLearningAgent`              | Reinforcement Learning | [`rl.py`][rl]                   | Done | Included |
| 21.9 | **Deep-Q-Network (DQN)** 🌟 | `DQN` | Deep RL | [`deep_rl.py`][drl] | Mnih et al. (2015) | 高優先級 |
| 21.12 | Double-DQN | `double_dqn` | Deep RL | [`deep_rl.py`][drl] | van Hasselt et al. (2015) | 建議 |
| 21.15 | **Policy-Gradient** 🌟 | `policy_gradient` | Deep RL | [`deep_rl.py`][drl] | Sutton et al. (2000) | 高優先級 |
| 21.18 | **A3C** | `A3C` | Deep RL | [`deep_rl.py`][drl] | Mnih et al. (2016) | 建議 |
| 21.19 | **PPO** 🌟 | `PPO` | Deep RL | [`deep_rl.py`][drl] | Schulman et al. (2017) | 高優先級 |
| 21.21 | Soft-Actor-Critic | `SAC` | Deep RL | [`deep_rl.py`][drl] | Haarnoja et al. (2018) | 建議 |
| 21.22 | **AlphaZero-MCTS** 🌟 | `alphazero_mcts` | Deep RL | [`games_rl.py`][grl] | Silver et al. (2017) | 高優先級 |
| 22.1   | HITS                              | `HITS`                        | NLP | [`nlp.py`][nlp]                 | Done | Included |
| 23     | Chart-Parse                       | `Chart`                       | NLP | [`nlp.py`][nlp]                 | Done | Included |
| 23.5   | CYK-Parse                         | `CYK_parse`                   | NLP | [`nlp.py`][nlp]                 | Done | Included |
| 23.6 | **Word2Vec** 🌟 | `word2vec` | NLP | [`embeddings.py`][emb] | Mikolov et al. (2013) | 建議 |
| 23.9 | **GloVe** | `glove` | NLP | [`embeddings.py`][emb] | Pennington et al. (2014) | 建議 |
| 23.11 | **ELMo** | `elmo` | NLP | [`embeddings.py`][emb] | Peters et al. (2018) | 建議 |
| 23.13 | **Tokenization-BPE** | `bpe_tokenizer` | NLP | [`tokenizers.py`][tok] | Sennrich et al. (2016) | 建議 |
| 24.9 | **YOLO** 🌟 | `YOLO` | Vision | [`object_detection.py`][od] | Redmon et al. (2016) | 高優先級 |
| 24.12 | Faster-R-CNN | `faster_rcnn` | Vision | [`object_detection.py`][od] | Ren et al. (2015) | 建議 |
| 24.13 | **Mask-R-CNN** 🌟 | `mask_rcnn` | Vision | [`segmentation.py`][seg] | He et al. (2017) | 建議 |
| 24.16 | **U-Net** | `unet` | Vision | [`segmentation.py`][seg] | Ronneberger et al. (2015) | 建議 |
| 25.9   | Monte-Carlo-Localization          | `monte_carlo_localization`    | Robotics | [`probability.py`][probability] | Done | Included |
| 26.1 | Convolutional-Neural-Network | `CNN` | Deep Learning | [`deep_learning.py`][dl] | LeCun (1998) | 建議 |
| 26.6 | **ResNet-Block** 🌟 | `residual_block` | Deep Learning | [`deep_learning.py`][dl] | He et al. (2015) | 建議 |
| 27.6 | **Scaled-Dot-Product-Attention** 🌟 | `scaled_dot_product_attention` | Deep Learning | [`attention.py`][attn] | Vaswani et al. (2017) | 高優先級 |
| 27.7 | **Multi-Head-Attention** 🌟 | `multi_head_attention` | Deep Learning | [`attention.py`][attn] | Vaswani et al. (2017) | 高優先級 |
| 27.8 | **Transformer-Encoder** 🌟 | `transformer_encoder` | Deep Learning | [`transformers.py`][trans] | Vaswani et al. (2017) | 高優先級 |
| 27.9 | **Transformer-Decoder** 🌟 | `transformer_decoder` | Deep Learning | [`transformers.py`][trans] | Vaswani et al. (2017) | 高優先級 |
| 28.1 | **BERT-Pretraining** 🌟 | `bert_pretrain` | LLM | [`language_models.py`][lm] | Devlin et al. (2018) | 高優先級 |
| 28.4 | **GPT-Architecture** 🌟 | `gpt_model` | LLM | [`language_models.py`][lm] | Radford et al. (2018) | 高優先級 |
| 28.8 | **Few-Shot-Learning** 🌟 | `few_shot_learning` | LLM | [`language_models.py`][lm] | Brown et al. (2020) | 高優先級 |
| 28.10 | **Chain-of-Thought-Prompting** | `chain_of_thought` | LLM | [`language_models.py`][lm] | Wei et al. (2022) | 建議 |
| 28.11 | **RLHF** 🌟 | `rlhf` | LLM | [`language_models.py`][lm] | Christiano et al. (2017) | 建議 |
| 28.13 | **Retrieval-Augmented-Generation** | `rag` | LLM | [`language_models.py`][lm] | Lewis et al. (2020) | 建議 |
| 29.2 | Variational-Autoencoder | `VAE` | Generative AI | [`generative.py`][gen] | Kingma & Welling (2013) | 建議 |
| 29.4 | **GAN-Architecture** 🌟 | `GAN` | Generative AI | [`generative.py`][gen] | Goodfellow et al. (2014) | 高優先級 |
| 29.7 | **StyleGAN** | `StyleGAN` | Generative AI | [`generative.py`][gen] | Karras et al. (2019) | 建議 |
| 29.10 | **Diffusion-Model** 🌟 | `diffusion_model` | Generative AI | [`diffusion.py`][diff] | Sohl-Dickstein et al. (2015) | 高優先級 |
| 29.11 | **DDPM** 🌟 | `DDPM` | Generative AI | [`diffusion.py`][diff] | Ho et al. (2020) | 高優先級 |
| 29.14 | **Stable-Diffusion** 🌟 | `stable_diffusion` | Generative AI | [`diffusion.py`][diff] | Rombach et al. (2022) | 高優先級 |
| 29.16 | **CLIP** | `CLIP` | Multimodal | [`multimodal.py`][mm] | Radford et al. (2021) | 建議 |
| 30.1 | Vision-Transformer | `ViT` | Vision | [`vision_models.py`][vis] | Dosovitskiy et al. (2020) | 建議 |
| 30.3 | **DALL-E-Architecture** 🌟 | `dalle` | Multimodal | [`multimodal.py`][mm] | Ramesh et al. (2021) | 建議 |
| 30.7 | Image-Captioning | `image_caption` | Multimodal | [`multimodal.py`][mm] | - | 建議 |
| 30.8 | Visual-Question-Answering | `vqa` | Multimodal | [`multimodal.py`][mm] | - | 建議 |
| 34.1 | **LIME** 🌟 | `LIME` | Explainable AI | [`explainable_ai.py`][xai] | Ribeiro et al. (2016) | 建議 |
| 34.2 | **SHAP** 🌟 | `SHAP` | Explainable AI | [`explainable_ai.py`][xai] | Lundberg & Lee (2017) | 建議 |
| 34.3 | Grad-CAM | `grad_cam` | Explainable AI | [`explainable_ai.py`][xai] | Selvaraju et al. (2017) | 建議 |
| 34.4 | Integrated-Gradients | `integrated_gradients` | Explainable AI | [`explainable_ai.py`][xai] | Sundararajan et al. (2017) | 建議 |
| 31.2 | **SimCLR** | `simclr` | Self-Supervised | [`ssl.py`][ssl] | Chen et al. (2020) | 建議 |
| 32.1 | **MAML** 🌟 | `MAML` | Meta-Learning | [`meta_learning.py`][meta] | Finn et al. (2017) | 建議 |
| 33.3 | **DARTS** | `DARTS` | AutoML | [`nas.py`][nas] | Liu et al. (2018) | 建議 |
| 35.1 | **Federated-Averaging** 🌟 | `federated_averaging` | Federated Learning | [`federated.py`][fed] | McMahan et al. (2017) | 建議 |
---

## 🚀 Future Algorithms (建議未來版本新增)

以下是建議在未來版本中新增的現代 AI 算法，反映 2020 年代的重大進展。

> **注意**: 部分現代算法已整合到上方主表格中（18.35, 21.9-21.22, 23.6-23.13, 24.9-24.16, 31.2, 32.1, 33.3, 34.1-34.4, 35.1）

### 深度學習與 Transformer

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Status** | **Nature Language** |
|:-----------|:---------|:-------------------------|:---------|:------------|:-----------|:-----------|
| 26.1 | Convolutional-Neural-Network | `CNN` | [`deep_learning.py`][dl] | LeCun (1998) | 建議 ||
| 26.2 | Conv-Layer-Forward-Pass | `conv_forward` | [`deep_learning.py`][dl] | - | 建議 ||
| 26.3 | Max-Pooling | `max_pooling` | [`deep_learning.py`][dl] | - | 建議 ||
| 26.4 | Batch-Normalization | `batch_norm` | [`deep_learning.py`][dl] | Ioffe & Szegedy (2015) | 建議 ||
| 26.5 | Dropout-Regularization | `dropout` | [`deep_learning.py`][dl] | Hinton et al. (2012) | 建議 ||
| 26.6 | **ResNet-Block** 🌟 | `residual_block` | [`deep_learning.py`][dl] | He et al. (2015) | 建議 ||
| 26.8 | DenseNet-Block | `dense_block` | [`deep_learning.py`][dl] | Huang et al. (2017) | 建議 ||
| 27.1 | Recurrent-Neural-Network | `RNN` | [`sequence_models.py`][seq] | Rumelhart (1986) | 建議 | 學化電 |
| 27.2 | LSTM-Cell | `LSTM` | [`sequence_models.py`][seq] | Hochreiter (1997) | 建議 | 器組憶|
| 27.3 | GRU-Cell | `GRU` | [`sequence_models.py`][seq] | Cho et al. (2014) | 建議 ||
| 27.5 | Attention-Mechanism | `attention` | [`attention.py`][attn] | Bahdanau et al. (2015) | 建議 ||
| 27.6 | **Scaled-Dot-Product-Attention** 🌟 | `scaled_dot_product_attention` | [`attention.py`][attn] | Vaswani et al. (2017) | 高優先級 ||
| 27.7 | **Multi-Head-Attention** 🌟 | `multi_head_attention` | [`attention.py`][attn] | Vaswani et al. (2017) | 高優先級 ||
| 27.8 | **Transformer-Encoder** 🌟 | `transformer_encoder` | [`transformers.py`][trans] | Vaswani et al. (2017) | 高優先級 ||
| 27.9 | **Transformer-Decoder** 🌟 | `transformer_decoder` | [`transformers.py`][trans] | Vaswani et al. (2017) | 高優先級 ||
| 27.10 | Positional-Encoding | `positional_encoding` | [`transformers.py`][trans] | - | 建議 ||

### 大型語言模型

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Status** |
|:-----------|:---------|:-------------------------|:---------|:------------|:-----------|
| 28.1 | **BERT-Pretraining** 🌟 | `bert_pretrain` | [`language_models.py`][lm] | Devlin et al. (2018) | 高優先級 |
| 28.2 | Masked-Language-Modeling | `masked_lm` | [`language_models.py`][lm] | - | 建議 |
| 28.3 | Next-Sentence-Prediction | `next_sentence_pred` | [`language_models.py`][lm] | - | 建議 |
| 28.4 | **GPT-Architecture** 🌟 | `gpt_model` | [`language_models.py`][lm] | Radford et al. (2018) | 高優先級 |
| 28.5 | Causal-Language-Modeling | `causal_lm` | [`language_models.py`][lm] | - | 建議 |
| 28.6 | Fine-Tuning-LLM | `fine_tune` | [`language_models.py`][lm] | - | 建議 |
| 28.7 | Prompt-Engineering | `prompt_template` | [`language_models.py`][lm] | - (2021) | 建議 |
| 28.8 | **Few-Shot-Learning** 🌟 | `few_shot_learning` | [`language_models.py`][lm] | Brown et al. (2020) | 高優先級 |
| 28.9 | In-Context-Learning | `in_context_learning` | [`language_models.py`][lm] | - (2020) | 建議 |
| 28.10 | Chain-of-Thought-Prompting | `chain_of_thought` | [`language_models.py`][lm] | Wei et al. (2022) | 建議 |
| 28.11 | **RLHF** 🌟 | `rlhf` | [`language_models.py`][lm] | Christiano et al. (2017) | 建議 |
| 28.12 | Instruction-Tuning | `instruction_tuning` | [`language_models.py`][lm] | - (2022) | 建議 |
| 28.13 | Retrieval-Augmented-Generation | `rag` | [`language_models.py`][lm] | Lewis et al. (2020) | 建議 |

### 生成式 AI

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Status** |
|:-----------|:---------|:-------------------------|:---------|:------------|:-----------|
| 29.1 | Autoencoder | `autoencoder` | [`generative.py`][gen] | - (1980s) | 建議 |
| 29.2 | Variational-Autoencoder | `VAE` | [`generative.py`][gen] | Kingma & Welling (2013) | 建議 |
| 29.3 | VAE-Reparameterization-Trick | `reparameterization` | [`generative.py`][gen] | - | 建議 |
| 29.4 | **GAN-Architecture** 🌟 | `GAN` | [`generative.py`][gen] | Goodfellow et al. (2014) | 高優先級 |
| 29.5 | GAN-Training-Loop | `gan_train` | [`generative.py`][gen] | - | 建議 |
| 29.6 | DCGAN | `DCGAN` | [`generative.py`][gen] | Radford et al. (2015) | 建議 |
| 29.7 | StyleGAN | `StyleGAN` | [`generative.py`][gen] | Karras et al. (2019) | 建議 |
| 29.8 | Conditional-GAN | `CGAN` | [`generative.py`][gen] | Mirza (2014) | 建議 |
| 29.9 | CycleGAN | `CycleGAN` | [`generative.py`][gen] | Zhu et al. (2017) | 建議 |
| 29.10 | **Diffusion-Model** 🌟 | `diffusion_model` | [`diffusion.py`][diff] | Sohl-Dickstein et al. (2015) | 高優先級 |
| 29.11 | **DDPM** 🌟 | `DDPM` | [`diffusion.py`][diff] | Ho et al. (2020) | 高優先級 |
| 29.12 | Diffusion-Forward-Process | `diffusion_forward` | [`diffusion.py`][diff] | - | 建議 |
| 29.13 | Diffusion-Reverse-Process | `diffusion_reverse` | [`diffusion.py`][diff] | - | 建議 |
| 29.14 | **Stable-Diffusion** 🌟 | `stable_diffusion` | [`diffusion.py`][diff] | Rombach et al. (2022) | 高優先級 |
| 29.15 | Latent-Diffusion | `latent_diffusion` | [`diffusion.py`][diff] | - | 建議 |
| 29.16 | **CLIP** | `CLIP` | [`multimodal.py`][mm] | Radford et al. (2021) | 建議 |

### 多模態 AI

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Status** |
|:-----------|:---------|:-------------------------|:---------|:------------|:-----------|
| 30.1 | Vision-Transformer | `ViT` | [`vision_models.py`][vis] | Dosovitskiy et al. (2020) | 建議 |
| 30.2 | Patch-Embedding | `patch_embed` | [`vision_models.py`][vis] | - | 建議 |
| 30.3 | **DALL-E-Architecture** 🌟 | `dalle` | [`multimodal.py`][mm] | Ramesh et al. (2021) | 建議 |
| 30.4 | Image-GPT | `image_gpt` | [`multimodal.py`][mm] | Chen et al. (2020) | 建議 |
| 30.5 | Flamingo | `flamingo` | [`multimodal.py`][mm] | Alayrac et al. (2022) | 建議 |
| 30.6 | Text-to-Image-Generation | `text_to_image` | [`multimodal.py`][mm] | - | 建議 |
| 30.7 | Image-Captioning | `image_caption` | [`multimodal.py`][mm] | - | 建議 |
| 30.8 | Visual-Question-Answering | `vqa` | [`multimodal.py`][mm] | - | 建議 |

### 深度強化學習

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Status** |
|:-----------|:---------|:-------------------------|:---------|:------------|:-----------|
| 21.10 | Experience-Replay | `experience_replay` | [`deep_rl.py`][drl] | - | 建議 |
| 21.11 | Target-Network | `target_network` | [`deep_rl.py`][drl] | - | 建議 |
| 21.13 | Dueling-DQN | `dueling_dqn` | [`deep_rl.py`][drl] | Wang et al. (2016) | 建議 |
| 21.14 | Prioritized-Experience-Replay | `prioritized_replay` | [`deep_rl.py`][drl] | Schaul et al. (2015) | 建議 |
| 21.16 | REINFORCE-Algorithm | `reinforce` | [`deep_rl.py`][drl] | Williams (1992) | 建議 |
| 21.17 | Actor-Critic | `actor_critic` | [`deep_rl.py`][drl] | Konda (2000) | 建議 |
| 21.20 | Trust-Region-Policy-Optimization | `TRPO` | [`deep_rl.py`][drl] | Schulman et al. (2015) | 建議 |
| 21.23 | Monte-Carlo-Tree-Search-Neural | `mcts_neural` | [`games_rl.py`][grl] | - | 建議 |
| 21.24 | Model-Based-RL | `model_based_rl` | [`deep_rl.py`][drl] | - | 建議 |
| 21.25 | World-Models | `world_models` | [`deep_rl.py`][drl] | Ha & Schmidhuber (2018) | 建議 |

### 現代 NLP

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Status** |
|:-----------|:---------|:-------------------------|:---------|:------------|:-----------|
| 23.7 | Skip-Gram-Model | `skip_gram` | [`embeddings.py`][emb] | - | 建議 |
| 23.8 | CBOW | `cbow` | [`embeddings.py`][emb] | - | 建議 |
| 23.10 | FastText | `fasttext` | [`embeddings.py`][emb] | Bojanowski et al. (2017) | 建議 |
| 23.12 | Contextualized-Embeddings | `contextualized_emb` | [`embeddings.py`][emb] | - | 建議 |
| 23.14 | WordPiece-Tokenization | `wordpiece` | [`tokenizers.py`][tok] | - | 建議 |
| 23.15 | SentencePiece | `sentencepiece` | [`tokenizers.py`][tok] | Kudo & Richardson (2018) | 建議 |

### 現代計算機視覺

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Status** |
|:-----------|:---------|:-------------------------|:---------|:------------|:-----------|
| 24.10 | R-CNN | `RCNN` | [`object_detection.py`][od] | Girshick et al. (2014) | 建議 |
| 24.11 | Fast-R-CNN | `fast_rcnn` | [`object_detection.py`][od] | Girshick (2015) | 建議 |
| 24.14 | Semantic-Segmentation | `semantic_seg` | [`segmentation.py`][seg] | - | 建議 |
| 24.15 | Instance-Segmentation | `instance_seg` | [`segmentation.py`][seg] | - | 建議 |
| 24.17 | DeepLab | `deeplab` | [`segmentation.py`][seg] | Chen et al. (2017) | 建議 |

### 可解釋 AI

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Status** |
|:-----------|:---------|:-------------------------|:---------|:------------|:-----------|
| 34.5 | Attention-Visualization | `attention_viz` | [`explainable_ai.py`][xai] | - | 建議 |
| 34.6 | Feature-Attribution | `feature_attribution` | [`explainable_ai.py`][xai] | - | 建議 |

### 進階技術

| **Figure** | **Name** | **Name (in repository)** | **File** | **Pioneer** | **Status** |
|:-----------|:---------|:-------------------------|:---------|:------------|:-----------|
| 18.36 | RMSprop-Optimizer | `RMSprop` | [`optimizers.py`][opt] | Hinton (2012) | 建議 |
| 18.37 | Learning-Rate-Scheduling | `lr_schedule` | [`optimizers.py`][opt] | - | 建議 |
| 18.38 | Xavier-Initialization | `xavier_init` | [`utils.py`][utils] | Glorot & Bengio (2010) | 建議 |
| 18.39 | He-Initialization | `he_init` | [`utils.py`][utils] | He et al. (2015) | 建議 |
| 31.1 | Contrastive-Learning | `contrastive_learning` | [`ssl.py`][ssl] | - | 建議 |
| 31.3 | MoCo | `moco` | [`ssl.py`][ssl] | He et al. (2020) | 建議 |
| 31.4 | BYOL | `byol` | [`ssl.py`][ssl] | Grill et al. (2020) | 建議 |
| 32.2 | Meta-Gradient-Update | `meta_gradient` | [`meta_learning.py`][meta] | - | 建議 |
| 32.3 | Prototypical-Networks | `prototypical_net` | [`meta_learning.py`][meta] | Snell et al. (2017) | 建議 |
| 32.4 | Matching-Networks | `matching_net` | [`meta_learning.py`][meta] | Vinyals et al. (2016) | 建議 |
| 33.1 | NAS-Search-Space | `nas_search_space` | [`nas.py`][nas] | - | 建議 |
| 33.2 | ENAS | `ENAS` | [`nas.py`][nas] | Pham et al. (2018) | 建議 |
| 35.2 | Differential-Privacy | `differential_privacy` | [`privacy.py`][priv] | Dwork et al. (2006) | 建議 |
| 35.3 | Private-Aggregation | `private_aggregation` | [`privacy.py`][priv] | - | 建議 |


### 📊 統計

- **建議新增算法**: 50+ 個
- **高優先級** 🌟: 18 個核心算法
- **涵蓋領域**: Transformer、LLM、生成式 AI、深度 RL、可解釋 AI
- **時間跨度**: 2013-2024

完整的算法列表和實現細節請參見 [`ALGORITHMS_NEXT_EDITION.md`](ALGORITHMS_NEXT_EDITION.md)。

### 🎯 貢獻指南

歡迎貢獻這些現代算法的實現！優先級順序：
1. **Transformer 架構** (Figure 27.6-27.9) - AI 革命的基礎
2. **BERT/GPT** (Figure 28.1, 28.4) - 大型語言模型
3. **Diffusion Models** (Figure 29.10-29.14) - 生成式 AI
4. **DQN/PPO** (Figure 21.9, 21.19) - 深度強化學習
5. **YOLO/Mask R-CNN** (Figure 24.9, 24.13) - 計算機視覺

---

# Index of data structures

Here is a table of the implemented data structures, the figure, name of the implementation in the repository, and the file where they are implemented.

| **Figure** | **Name (in repository)** | **File** |
|:-------|:--------------------------------|:--------------------------|
| 3.2    | romania_map                     | [`search.py`][search]     |
| 4.9    | vacumm_world                    | [`search.py`][search]     |
| 4.23   | one_dim_state_space             | [`search.py`][search]     |
| 6.1    | australia_map                   | [`search.py`][search]     |
| 7.13   | wumpus_world_inference          | [`logic.py`][logic]       |
| 7.16   | horn_clauses_KB                 | [`logic.py`][logic]       |
| 17.1   | sequential_decision_environment | [`mdp.py`][mdp]           |
| 18.2   | waiting_decision_tree           | [`learning.py`][learning] |


# Acknowledgements

Many thanks for contributions over the years. I got bug reports, corrected code, and other support from Darius Bacon, Phil Ruggera, Peng Shao, Amit Patil, Ted Nienstedt, Jim Martin, Ben Catanzariti, and others. Now that the project is on GitHub, you can see the [contributors](https://github.com/aimacode/aima-python/graphs/contributors) who are doing a great job of actively improving the project. Many thanks to all contributors, especially [@darius](https://github.com/darius), [@SnShine](https://github.com/SnShine), [@reachtarunhere](https://github.com/reachtarunhere), [@antmarakis](https://github.com/antmarakis), [@Chipe1](https://github.com/Chipe1), [@ad71](https://github.com/ad71) and [@MariannaSpyrakou](https://github.com/MariannaSpyrakou).

<!---Reference Links-->
[agents]:../master/agents.py
[csp]:../master/csp.py
[games]:../master/games.py
[grid]:../master/grid.py
[knowledge]:../master/knowledge.py
[learning]:../master/learning.py
[logic]:../master/logic.py
[proof]:../master/proof_theory.py
[types]:../master/type_theory.py
[mdp]:../master/mdp.py
[nlp]:../master/nlp.py
[planning]:../master/planning.py
[probability]:../master/probability.py
[rl]:../master/rl.py
[search]:../master/search.py
[utils]:../master/utils.py
[text]:../master/text.py

<!---Future Algorithms Reference Links-->
[dl]:../master/deep_learning.py
[seq]:../master/sequence_models.py
[attn]:../master/attention.py
[trans]:../master/transformers.py
[lm]:../master/language_models.py
[gen]:../master/generative.py
[diff]:../master/diffusion.py
[mm]:../master/multimodal.py
[drl]:../master/deep_rl.py
[grl]:../master/games_rl.py
[ssl]:../master/ssl.py
[meta]:../master/meta_learning.py
[nas]:../master/nas.py
[xai]:../master/explainable_ai.py
[fed]:../master/federated.py
[priv]:../master/privacy.py
[opt]:../master/optimizers.py
[emb]:../master/embeddings.py
[tok]:../master/tokenizers.py
[od]:../master/object_detection.py
[seg]:../master/segmentation.py
[vis]:../master/vision_models.py
