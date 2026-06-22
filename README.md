# hello-utils

一个轻量级 Python 工具库，用于生成友好的问候语字符串。

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## 目录

- [项目简介](#项目简介)
- [安装方式](#安装方式)
- [快速开始](#快速开始)
- [API 文档](#api-文档)
  - [greet()](#greet)
  - [shout()](#shout)
- [使用示例](#使用示例)
- [运行测试](#运行测试)
- [贡献指南](#贡献指南)
- [许可证](#许可证)

---

## 项目简介

`hello-utils` 提供了一组简单易用的问候语生成函数，适用于：

- 快速生成个性化问候消息
- 作为学习 Python 模块化开发的示例项目
- 集成到更大型应用的消息模块中

---

## 安装方式

本项目无外部依赖，仅需 Python 3.7 或更高版本。

**克隆仓库：**

```bash
git clone https://github.com/your-username/hello-utils.git
cd hello-utils
```

**直接复制使用：**

将 `greet.py` 文件复制到你的项目目录，然后直接导入即可。

---

## 快速开始

```python
from greet import greet, shout

# 生成普通问候语
print(greet("Alice"))   # Hello, Alice!

# 生成大写问候语
print(shout("Bob"))     # HELLO, BOB!
```

---

## API 文档

### `greet()`

生成一条个性化问候语。

**签名：**

```python
def greet(name: str) -> str
```

**参数：**

| 参数   | 类型  | 必填 | 说明                              |
|--------|-------|------|-----------------------------------|
| `name` | `str` | 是   | 被问候对象的姓名。传入空字符串或 `None` 时返回默认问候语。 |

**返回值：**

- 类型：`str`
- 格式：`"Hello, {name}!"`
- 当 `name` 为空时返回 `"Hello, World!"`

**示例：**

```python
from greet import greet

greet("Alice")    # "Hello, Alice!"
greet("Claude")   # "Hello, Claude!"
greet("")         # "Hello, World!"
greet(None)       # "Hello, World!"
```

---

### `shout()`

生成一条全大写的问候语，用于强调或醒目场景。

**签名：**

```python
def shout(name: str) -> str
```

**参数：**

| 参数   | 类型  | 必填 | 说明                     |
|--------|-------|------|--------------------------|
| `name` | `str` | 是   | 被问候对象的姓名（同 `greet()`）。 |

**返回值：**

- 类型：`str`
- 格式：`"HELLO, {NAME}!"`（`greet()` 返回值的大写版本）

**示例：**

```python
from greet import shout

shout("Alice")    # "HELLO, ALICE!"
shout("Claude")   # "HELLO, CLAUDE!"
shout("")         # "HELLO, WORLD!"
```

---

## 使用示例

**批量生成问候语：**

```python
from greet import greet

names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(greet(name))
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

**直接运行脚本：**

```bash
python greet.py
# Hello, Claude!
```

**在其他模块中导入：**

```python
from greet import greet, shout

def send_welcome_email(username):
    subject = shout(username)    # "HELLO, ALICE!"
    body = greet(username)       # "Hello, Alice!"
    # ... 发送邮件逻辑
```

**处理空值场景：**

```python
from greet import greet

user_input = input("请输入你的名字（直接回车跳过）：").strip()
print(greet(user_input))   # 空输入时输出 "Hello, World!"
```

---

## 运行测试

目前测试可通过 Python 内置的 `doctest` 或 `unittest` 运行。

**使用 doctest（无需额外依赖）：**

```bash
python -m doctest greet.py -v
```

**手动验证（快速冒烟测试）：**

```bash
python -c "
from greet import greet, shout
assert greet('Alice') == 'Hello, Alice!'
assert greet('') == 'Hello, World!'
assert shout('Bob') == 'HELLO, BOB!'
print('所有断言通过')
"
```

**如果项目后续接入 pytest：**

```bash
pip install pytest
pytest tests/
```

---

## 贡献指南

欢迎所有形式的贡献！请按照以下步骤参与：

1. **Fork 本仓库**

2. **创建功能分支**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **编写代码并添加对应测试**

4. **确保所有测试通过**

   ```bash
   python -m doctest greet.py
   ```

5. **提交变更**（请使用清晰的 commit message）

   ```bash
   git commit -m "feat: 添加 farewell() 函数"
   ```

6. **推送分支并创建 Pull Request**

   ```bash
   git push origin feature/your-feature-name
   ```

**代码规范：**

- 遵循 [PEP 8](https://pep8.org/) 代码风格
- 每个公开函数必须包含 docstring
- 新功能需附带对应的测试用例

**报告问题：**

如发现 Bug 或有功能建议，请在 [Issues](https://github.com/your-username/hello-utils/issues) 中提交，并附上复现步骤或详细描述。

---

## 许可证

本项目基于 [MIT License](LICENSE) 开源，欢迎自由使用和修改。
