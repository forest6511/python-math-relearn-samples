"""examples/ の各ファイルを実行し、本に載っている
実行結果（outputs/）と一致するかを確かめる。

本のコードはこの repo から差し込んで作るので、
ここが緑なら本のコードは動き、本に載る結果も正しい。
"""

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = sorted((ROOT / "examples").glob("*.py"))


def test_examples_exist():
    # 0件のまま緑にしない（本のコードは98ブロック）
    assert len(EXAMPLES) >= 98


@pytest.mark.parametrize(
    "path", EXAMPLES, ids=lambda p: p.stem
)
def test_example_runs_and_matches_book(path):
    result = subprocess.run(
        [sys.executable, str(path)],
        capture_output=True,
        text=True,
        timeout=120,
        cwd=ROOT,
    )
    assert result.returncode == 0, result.stderr
    expected = ROOT / "outputs" / f"{path.stem}.txt"
    if expected.exists():
        want = expected.read_text(
            encoding="utf-8"
        ).rstrip("\n")
        assert result.stdout.rstrip("\n") == want
