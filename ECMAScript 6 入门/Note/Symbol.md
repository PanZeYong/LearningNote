# Symbol

### 1、概述

Symbol 是 JavaScript 第七种基本数据类型，通过调用 `Symbol()` 函数返回的 symbol 值是独一无二的，可用于对象属性的标识符，这是仅有的目的。该函数接收一个参数：`description`，仅用于 symbol 的描述。需要注意的点：

- `Symbol()` 函数前不能使用 `new` 关键字；

- 每次调用 `Symbol()` 函数都是创建新的 `Symbol` 类型；

- 不能与其它类型的值进行运算；

- 可以通过 `String()` 或者 `toString()` 显示转换为字符串，也可以转换为布尔值 `Boolean()`，但是不能转为数值。

### 2、静态属性

- `Symbol​.prototype​.description`：一个只读属性，返回 `Symbol` 可选的描述字符串。

- `Symbol.hasInstance`：用于判断某对象是否为某构造器的实例，指向一个内部方法。比如，我们在判断是否为某个对象实例时，`foo instanceof Foo`，实际上内部调用的是：`Foo[Symbol.hasInstance](foo)`

	```javascript
	class MyClass {
		[Symbol.hasInstance](foo) {
			return foo instanceof Array;
		}
	}
	
	class MyArray {  
  		static [Symbol.hasInstance](instance) {
    		return Array.isArray(instance);
  		}
	}
	```
	
- `Symbol.isConcatSpreadable`：使用方法 `Array.prototype.concat()` 时，表示其元素是否展开。对于数组，默认是展开的；而对于类似数组，默认是不展开的。该属性是一个布尔值，`true` 表示展开，`false` 表示不展开。

- `Symbol.species`：指向一个构造函数。有些类库是继承基类的，在创建实例希望返回基类的实例，那么可以使用该属性，指向一个构造函数，返回基类的属性。创建衍生对象会使用到该属性。

	```javascript
	class MyArray extends Array {
		static get [Symbol.species]() { return Array; }
	}
	
	const a = new MyArray();
	const b = a.map(x => x);
	
	b instanceof MyArray // false
	b instanceof Array // true
	```
	
- `Symbol.match`：指定匹配的是正则表达式，而不是字符串。如果一个对象指定该属性，那么会调用其指向的函数，并返回指向函数所返回的值。

	```javascript
	String.prototype.match(regexp)
	// 等同于
	regexp[Symbol.match](this)

	class MyMatcher {
		[Symbol.match](string) {
			return 'hello world'.indexOf(string);
		}
	}
	
	'e'.match(new MyMatcher()) // 1
	```
	
- `Symbol.replace`：指定了当一个字符串替换所匹配字符串时所调用的方法。通过 `String.prototype.replace` 调用时，该属性指向的函数被调用，并且返回对应的值。

- `Symbol.search`：指定一个搜索方法，接受用户输入的正则表达式，返回正则表达式匹配到字符串下标。通过 `String.prototype.search()` 调用。

	```javascript
	String.prototype.search(regexp)
	// 等同于
	regexp[Symbol.search](this)

	class MySearch {
  		constructor(value) {
    		this.value = value;
  		}
  		
  		[Symbol.search](string) {
  			return string.indexOf(this.value);
  		}
  	}
	'foobar'.search(new MySearch('foo')) // 0
	```
	
- `Symbol.split`：通过指定一个正则表达式的索引分割字符串。通过方法 `String.prototype.split()` 调用。

- `Symbol.iterator`：为每一个对象定义默认的迭代器，该迭代器可以被 `for...of` 使用。内置类型拥有默认的 `@@iterator` 方法：

	- `Array.prototype[@@iterator]()`
	
	- `TypedArray.prototype[@@iterator]()`
	
	- `String.prototype[@@iterator]()`
	
	- `Map.prototype[@@iterator]()`

	- `Set.prototype[@@iterator]()`

- `Symbol.toPrimitive`：将对象转换为原始值，接收一个字符串参数，表示运算模式：

	- `Number`：转换为数值；

	- `String`：转换为字符串；

	- `default`：既可以转换为数值，也可以转换为数值。

- `Symbol.toStringTag`：指定一个方法，用来定义对象的数据类型，只有 `Object.prototype.toString()` 方法才能读取。

- `Symbol.unscopables`：使用 `with` 关键字时，被 `with` 环境排除的数学。
	

### 3、静态方法

- `Symbol.for(key)`：接收一个参数：key，根据给定 key 从全局 Symbol 注册表中搜索是否存在以 key 作为键的 `Symbol`，如果存在就返回；否则创建新 `Symbol` 并且在全局环境中注册。这里的参数 key 既可以作为 `Symbol` 的描述字符串，也可以作为全局注册表中 key。

- `Symbol.keyFor(sym)`：用来获取 `Symbol` 注册表中与某个 `Symbol` 关联的键。

[参考链接](http://es6.ruanyifeng.com/#docs/symbol)

