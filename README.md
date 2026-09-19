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

## ファイル構成

- `examples/` — 各レシピのコード（`recipeNN_<内容>.py`）。本書の写経対象そのまま
- `requirements.txt` — 追加で必要なライブラリ（Colab には多くが標準で入っています）

## 動作環境

- Google Colab（推奨・インストール不要）
- またはローカル Python 3.10 以上

## 書籍について

中学・高校の数学を、Python で手を動かしながら学び直す本です。
50のレシピで、数直線・一次関数・確率・微分・積分・ベクトルまでを、図解とやさしい解説で進みます。
