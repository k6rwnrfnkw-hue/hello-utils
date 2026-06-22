# hello-utils

一个轻量的 Python 问候工具库，提供生成问候语和告别语的实用函数。

## 安装

无需额外依赖，直接将 `greet.py` 复制到项目中即可使用。

## 快速开始

```python
from greet import greet, shout, farewell

print(greet("Alice"))    # Hello, Alice!
print(shout("Alice"))    # HELLO, ALICE!
print(farewell("Alice")) # Goodbye, Alice!
```

## API 参考

### `greet(name)`

返回一条个性化问候语。

**参数**

| 参数 | 类型 | 说明 |
|------|------|------|
| `name` | `str` | 被问候的对象名称。若为空字符串或 `None`，则使用默认值 `"World"` |

**返回值**

`str` — 格式为 `"Hello, {name}!"` 的问候字符串。

**示例**

```python
from greet import greet

greet("Bob")   # "Hello, Bob!"
greet("")      # "Hello, World!"
greet(None)    # "Hello, World!"
```

---

### `shout(name)`

返回全大写的问候语。

**参数**

| 参数 | 类型 | 说明 |
|------|------|------|
| `name` | `str` | 被问候的对象名称，规则同 `greet()` |

**返回值**

`str` — `greet()` 结果的大写版本。

**示例**

```python
from greet import shout

shout("Bob")   # "HELLO, BOB!"
shout("")      # "HELLO, WORLD!"
```

---

### `farewell(name)`

返回一条个性化告别语。

**参数**

| 参数 | 类型 | 说明 |
|------|------|------|
| `name` | `str` | 告别对象的名称。若为空字符串或 `None`，则使用默认值 `"World"` |

**返回值**

`str` — 格式为 `"Goodbye, {name}!"` 的告别字符串。

**示例**

```python
from greet import farewell

farewell("Bob")   # "Goodbye, Bob!"
farewell("")      # "Goodbye, World!"
farewell(None)    # "Goodbye, World!"
```

## 运行示例脚本

```bash
python greet.py
```

输出：

```
Hello, Claude!
Goodbye, Claude!
```
