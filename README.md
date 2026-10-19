# Pythonで学び直す中学・高校数学 — サンプルコード

書籍「**Pythonで学び直す中学・高校数学 ― 図解と50のレシピで、もう一度ゼロからわかる**」（森川 陽介）の
サンプルコード集です。

本書のコードは**すべて Google Colab にコピペして▶を押せば動く**ように作っています。
このリポジトリは、本書に載っているコードをそのまま実行できる形でまとめたものです。

Kindle 版: [Pythonで学び直す中学・高校数学](https://www.amazon.co.jp/dp/B0H6BMD3CZ)

## 使い方

### いちばん簡単（おすすめ）: Google Colab

インストール不要です。[Google Colab](https://colab.research.google.com/) を開いて、
本書のコード（または `examples/` の中のコード）をコピーして▶を押すだけで動きます。

### ローカルで動かす場合

```bash
python -m venv .venv
source .venv/bin/activate        # Windows は .venv\Scripts\activate
pip install -r requirements.txt

python examples/recipe01_numberline.py
```

本に載っている実行結果と同じになるかは、次で確かめられます。

```bash
python -m pytest -q        # examples/ を全部実行し、outputs/ と比べる
ruff format --check . && ruff check .
```

## ファイル構成

- `examples/` — 本書のコード（1ブロック1ファイル）。本書はこのファイルをそのまま差し込んで作っています
  - `recipeNN_<内容>.py` … 各レシピの「動かしてみる」
  - `recipeNN_<内容>_why.py` … 「なぜこうなるの」
  - `recipeNN_<内容>_try.py` … 「ちょっと変えてみる」
  - `setup_N.py` … 準備編（Colab の使い方）
- `outputs/` — 本書に載っている実行結果（`examples/` の同じ名前のファイルを実行した結果）
- `tests/` — `examples/` を実行して `outputs/` と一致するかを確かめるテスト
- `requirements.txt` — 追加で必要なライブラリ（Colab には多くが標準で入っています）

## 動作環境

- Google Colab（推奨・インストール不要）
- またはローカル Python 3.10 以上

## 書籍について

中学・高校の数学を、Python で手を動かしながら学び直す本です。
50のレシピで、数直線・一次関数・確率・微分・積分・ベクトルまでを、図解とやさしい解説で進みます。
