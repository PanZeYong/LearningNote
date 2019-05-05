# Set 和 Map 数据结构

## 一、Set

### 1、概述

`Set` 是 JavaScript 一种新的数据结构，可以存储任何数据类型的值，成员具有唯一性。要生成 `Set` 数据结构，可以通过 `new Set()`，即调用 `Set` 构造函数，接收一个参数：可以是数组或者是具有 `iterator` 接口的其它数据结构。

```javascript
const set = new Set([1, 2, 3, 4, 3, 5, 1, 4]);    // {1, 2, 3, 4, 5}
```

可用于去重数组元素或者字符串重复字符。

```javascript
const array = [1, 2, 2, 3, 1, 6, 3];

[...new Set(array)]

Array.from(new Set(array))
```

`NaN` 和 `undefined` 也可以存储在 `Set` 结构中，并且 `NaN` 之间和 `undefined` 之间被认为是相同的。

```javascript
Set.prototype[Symbol.iterator] === Set.prototype.values

let set = new Set(['red', 'green', 'blue']);

for (let x of set) {
  console.log(x);
}
```

### 2、属性

- `Set.prototype.constructor`：构造函数，默认是 `Set` 函数。

- `Set.prototype.size`：返回 `Set` 对象成员的个数。

### 3、方法

#### 操作方法

`Set.prototype.add(value)`：在 `Set` 对象尾部添加新元素，返回 `Set` 对象。

`Set.prototype.delete(value)`：删除指定元素，返回布尔值，表示是否删除成功。

`Set.prototype.has(value)`：返回布尔值，表示 `Set` 对象是否包含指定原。

`Set.prototype.clear()`：清除所有的成员，没有返回值。

#### 遍历方法

- `Set.prototype.keys()`：返回键名的迭代器。

- `Set.prototype.values()`：返回键值的迭代器。

- `Set.prototype.entries()`：返回键值对的迭代器。

- `Set.prototype.forEach()`：遍历 `Set` 对象每个成员。

#### 应用

- 扩展运算符 `...` 内部使用 `for...of`。

- 实现并集（Union）、交集（Intersect）和差集（Difference）。

## 二、WeakSet

### 1、概述

`WeakSet` 与 `Set` 结构类似，只能存储对象，其具有唯一性。与 `Set` 有两个区别：

- 只能存储对象引用，不能存储其它数据类型的值；

- `WeakSet` 对象中存储的对象值都是被弱引用的，即如果没有其它对象引用对象值时，垃圾回收机制会自动收回该对象占用的内存。很难预测对象值是否存在于 `WeakSet` 对象中，正因如此，`WeakSet` 是**不可遍历的**。

### 2、属性

- `WeakSet.prototype.constructor`：返回构造函数，即 `WeakSet` 本身。

### 3、方法

- `WeakSet.prototype.add(value)`：像 `WeakSet` 实例对象添加新元素 `value`。

- `WeakSet.prototype.delete(value)`：从 `WeakSet` 实例对象删除指定元素。

- `WeakSet.prototype.has(value)`：判断指定值 `value` 是否存在于 `WeakSet` 实例对象，返回布尔值。

## 三、Map

### 1、概述

保存键值对，任意对象值或者原始值都可以作为键名，这是与 `Object` 区别之一，即 `Oject` 的键值对是 “字符串-值”，而 `Map` 的键值对是 “值-值”。调用构造函数 `Map()` 可以创建 `Map` 实例，构造函数接收一个参数：参数可以是数组(数组中每个成员是表示键值对的数组)或者具有 `Iterator` 接口的数据类型。

```javascript
const map = new Map([
  ['name', '张三'],
  ['title', 'Author']
]);
```

只有对同一个对象的引用，`Map` 才会视为同一个键名。可见，`Map` 的键是跟内存地址绑定的，只要内存地址不一样，键就不一样。

`Map` 默认遍历器接口是调用 `entries` 方法，即

```javascript
Map.prototype[Symbol.iterator] === Map.prototype.entries
```

### 2、属性

- `Map.prototype.size`：返回 `Map` 实例成员的个数。

### 3、方法

#### 操作方法

- `Map.prototype.set(key, value)`：设置 `Map` 键为 `key`，值为 `value` 的成员，并返回当前 `Map` 对象。

- `Map.prototype.get(key)`：获取 `Map` 对象键为 `key`对应的值；如果找不到 `key`，则返回 `undefined`。

- `Map.prototype.has(key)`：返回布尔值，表示键为 `key` 的成员是否存在当前 `Map` 对象中。

- `Map.prototype.delete(key)`：如果键为 `key` 的元素存在当前对象 `Map` 中，则移除元素并返回 `true`；否则，则返回 `false`。

- `Map.prototype.clear()`：清除所有成员，没有返回值。

#### 遍历方法

`Map` 的遍历顺序是数据元素一开始插入的顺序。

- `Map.prototype.keys()`：返回键名的迭代器。

- `Map.prototype.values()`：返回键值的迭代器。

- `Map.prototype.entries()`：返回键值对的迭代器。

- `Map.prototype.forEach()`：遍历 `Map` 对象每个成员。

### 4、`Map` 与其它数据结构互相转换

- `Map` 转为数组

	通过开展运算符 `...` 则可以将 `Map` 对象转换为数组。

- 数组转换为 `Map`

	调用构造函数 `Map()`，数组作为参数传入，则可以进行转换。
	
- `Map` 转换为对象

	```javascript
	// 注意 Map 的键是否为字符串，如果为字符串，则可以作为对象的键名；否则则需要将其转换为字符串，再作为对象的键名
	function strMapToObj(strMap) {
		let obj = Object.create(null);
		for (let [k,v] of strMap) {
			obj[k] = v;
		}
		return obj;
	}
	```
	
- 对象转换为 `Map`

	```javascript
	function objToStrMap(obj) {
		let strMap = new Map();
		for (let k of Object.keys(obj)) {
			strMap.set(k, obj[k]);
		}
		return strMap;
	}
	```
	
- `Map` 转换为 `JSON`

	#### 键名为字符串，转换为对象 `JSON`。
	
	```javascript
	function strMapToJson(strMap) {
		return JSON.stringify(strMapToObj(strMap));
	}
	```
	
	#### 键名为非字符串，转换为数组 `JSON`。
	```javascript
	function mapToArrayJson(map) {
		return JSON.stringify([...map]);
	}
	```
	
- `JSON` 转换为 `Map`

	#### 键名为字符串，先转换为对象，再转换为 `Map`。
	```javascript
	function jsonToStrMap(jsonStr) {
		return objToStrMap(JSON.parse(jsonStr));
	}
	```
	
	#### 键名为非字符串，先转换为数组，再调用构造函数 `Map` 转换。
	```javascript
	function jsonToMap(jsonStr) {
		return new Map(JSON.parse(jsonStr));
	}
	```
	
## 四、WeakMap

一组键值对的集合，键名只能为对象，其它数据类型都不行；而键值任意数据类型都可以。其中键名是**弱引用**，基本原理与 `WeakSet` 一样。

### 1、方法

- `WeakMap.prototype.set(key, value)`：设置键为 `key`，键值为 `value` 的成员，并且返回当前 `WeakMap` 对象实例。

- `WeakMap.prototype.get(key)`：获取 `WeakMap` 对象中键为 `key` 的成员。

- `WeakMap.prototype.has(key)`：判断键为 `key` 的成员是否存在于对象 `WeakMap`。

- `WeakMap.prototype.delete(key)`：删除 `MapKey` 对象中键为 `key` 的成员。

### 2、用途

- DOM 节点作为键名；

- 部署私有属性。

[参考链接](http://es6.ruanyifeng.com/#docs/set-map)
