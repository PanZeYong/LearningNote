# Proxy

## 一、概览

`Proxy`，其功能很类似设计模式中的代理模式，可以这么理解：在没有设置代理时，外部可以直接访问对象；但是设置代理之后，外部要访问对象，必须由代理层进行拦截，再由代理层处理操作并把结果返回给外部，那么这时代理层充当了中间件，可以对外部进行拦截操作，比如可以对其进行过滤、修改等操作。

ES6 原生提供 `Proxy` 构造函数，用来生成 `Proxy` 实例：

```javascript
let proxy = new Proxy(target, handler);
```

以下对构造函数参数做下简单说明：

- `target`：将被拦截的目标对象；

- `handler`：定制各种拦截行为的对象，也可以理解为拦截器。

`Proxy` 支持的拦截操作总共有 `13` 种，详解见下。

## 二、`Proxy` 13 种拦截方法详细介绍

### 1、get(target, propKey, receiver)

用于拦截对象的读取属性，可以返回任何值。接收三个参数，含义解释如下：

- `target`：目标对象；

- `propKey`：被读取的属性；

- `receiver`：`Proxy` 或者继承 `Proxy` 的对象。

#### 可进行拦截的操作

- 访问属性：`proxy[foo]` 或 `proxy.foo`；

- 访问原型链上的属性: `Object.create(proxy)[foo]`；

- `Reflect.get()`。

#### `Proxy` 抛出异常 `TypeError` 的情况

- 如果要访问的目标属性是不可写以及不可配置的，则返回的值必须与该目标属性的值相同。

- 如果要访问的目标属性没有配置访问方法，即 `get` 方法是 `undefined` 的，则返回值必须为 `undefined`。

#### 例子

```javascript
var p = new Proxy({}, {
  get: function(target, prop, receiver) {
    console.log("called: " + prop);
    return 10;
  }
});

console.log(p.a); // "called: a"
```

### 2、set(target, propKey, value, receiver)

用来拦截设置对象属性的属性值操作，返回布尔值。返回 `true` 表示设置对象属性成功；返回 `false` 并且设置属性值的操作发生在严格模式下，那么 `Proxy` 会抛出 `TypeError` 错误。该方法接收四个参数，参数含义如下：

- `target`：目标对象；

- `propKey`：被设置的属性；

- `value`：被设置的属性的属性值；

- `receiver`：`Proxy` 实例本身或者继承 `Proxy` 的对象。

#### 可进行拦截的操作

- 指定属性值：`proxy[foo] = "bar"` 或者 `proxy.bar = "foo"`；

- 指定继承者的属性值: `Object.create(proxy)[foo] = bar`；

- `Reflect.set()`。

#### `Proxy` 抛出异常 `TypeError` 的情况

- 若目标属性是不可写及不可配置的，则不能改变它的值；

- 如果目标属性没有配置存储方法，即 `set` 方法是 `undefined` 的，则不能设置它的值；

- 在严格模式下，若 `set` 方法返回 `false`，则会抛出一个 `TypeError` 异常。

#### 例子

```javascript
var p = new Proxy({}, {
  set: function(target, prop, value, receiver) {
    console.log("called: " + prop + " = " + value);
    return true;
  }
});n

p.a = 10; // "called: a = 10"
```

### 3、apply(target, thisArg, args)

用于拦截函数的对象，返回任何值。方法接收三个参数：

- `target`：目标对象（函数）；

- `thisArg`：被调用时的上下文对象；

- `args`：被调用时的参数数组。

#### 可进行拦截的操作

- `proxy(...args)`；

- `Function.prototype.apply()` 和 `Function.prototype.call()`；

- `Reflect.apply()`。

#### `Proxy` 抛出异常 `TypeError` 的情况

`target` 必须是可以调用的，换句话说，它必须是函数对象。

#### 例子

```javascript
let proxy = new Proxy(target, {
  apply: function(target, thisArg, argumentsList) {
  }
});
```

### 4、has(target, prop)

方法用来拦截 `HasProperty` 操作，判断对象是否具有某一属性，也就是说该方法不是判断一个属性是对象自身的属性，还是继承的属性。返回的是一个布尔值，返回 `true` 表示不隐藏对象属性；返回 `false` 则隐藏对象属性，可以用于私有属性。接收两个参数：

- `target`：目标对象；

- `prop`：需要检查是否存在的属性。

#### 可进行拦截的操作

- 属性查询: `foo in proxy`；

- 继承属性查询: `foo in Object.create(proxy)`；

- with 检查: `with(proxy) { (foo); }`；

- `Reflect.has()`。

#### `Proxy` 抛出异常 `TypeError` 的情况

- 如果目标对象的某一属性本身不可被配置，则该属性不能够被代理隐藏；

- 如果目标对象为不可扩展对象，则该对象的属性不能够被代理隐藏。

#### 例子

```javascript
let prop = new Proxy(target, {
  has: function(target, prop) {
  }
});
```

需要注意的是对 `for ... in` 是不生效的。

### 5、construct(target, argumentsList, newTarget)

用于拦截 `new` 操作符，必须返回一个对象。可以接收三个参数：

- `target`：目标对象；

- `argumentsList`：构造函数的参数列表；

- `newTarget`：最初被调用的构造函数。

#### 可进行拦截的操作

- `new proxy(...args)`；

- `Reflect.construct()`。

#### `Proxy` 抛出异常 `TypeError` 的情况

- 如果不返回一个对象，则会报错。

#### 例子

```javascript
let proxy = new Proxy(function() {}, {
  construct: function(target, argumentsList, newTarget) {
    console.log('called: ' + argumentsList.join(', '));
    return { value: argumentsList[0] * 10 };
  }
});

console.log(new proxy(1).value);
```

### 6、deleteProperty（target, property）

用于拦截对对象属性的 `delete` 操作，返回布尔值，`true` 表示成功删除；`false` 表示删除失败。接收两个参数：

- `target`：目标对象；

- `property`：待删除对象属性。

#### 可进行拦截的操作

- 删除属性: `delete proxy[foo]` 和 `delete proxy.foo`；

- `Reflect.deleteProperty()`。

#### `Proxy` 抛出异常 `TypeError` 的情况

- 如果目标对象的属性是不可配置的，那么该属性不能被删除。

#### 例子

```javascript
let proxy = new Proxy({}, {
  deleteProperty: function(target, prop) {
    console.log('called: ' + prop);
    return true;
  }
});

delete proxy.a;
```

### 7、defineProperty(target, property, descriptor)

用于拦截对对象 `Object.defineProperty()` 操作，返回布尔值，表示定义属性是否成功。接收三个参数：

- `target`：目标对象；

- `property`：待定义的属性；

- `descriptor`：待定义或者修改属性的描述符。描述符只能是以下对象所包含的值，其它值则会被忽略。

	```json
	{
		enumerable: true | false,
		configurable: true | false,
		writable: true | false,
		value: number | string
		get: function () {}
		set: function () {}
	}
	```
	
#### 可进行拦截的操作

- `Object.defineProperty()`；

- `Reflect.defineProperty()`。

#### `Proxy` 抛出异常 `TypeError` 的情况

- 如果目标对象不可扩展（non-extensible），则 `definePropery` 不能添加目标对象不存在的属性，否则会报错；

- 如果目标对象某个属性不可写（writable）或者不可配置（configurable），那么 `defineProperty` 不能修改这两个配置；

- 在严格模式下， `false` 作为 `handler.defineProperty` 方法的返回值的话将会抛出 `TypeError` 异常。

#### 例子

```javascript
let proxy = new Proxy({}, {
  defineProperty: function(target, prop, descriptor) {
    console.log('called: ' + prop);
    return true;
  }
});

let desc = { configurable: true, enumerable: true, value: 10 };
Object.defineProperty(proxy, 'a', desc); // "called: a"
```

### 8、getOwnPropertyDescriptor(target, property)

用于拦截 `Object.getOwnPropertyDescriptor()` 的操作，返回属性描述对象或者 `undefined`。接收两个参数：

- `target`：目标对象；

- `property`：属性名称。

#### 可进行拦截的操作

- `Object.getOwnPropertyDescriptor()`；

- `Reflect.getOwnPropertyDescriptor()`。

#### `Proxy` 抛出异常 `TypeError` 的情况

- 如果目标对象不可扩展，并且不存在该属性，则不能设置为存在，否则会报错。

#### 例子

```javascript
let proxy = new Proxy({ a: 20}, {
  getOwnPropertyDescriptor: function(target, prop) {
    console.log('called: ' + prop);
    return { configurable: true, enumerable: true, value: 10 };
  }
});

console.log(Object.getOwnPropertyDescriptor(proxy, 'a').value);
```

### 9、getPrototypeOf(target)

用来拦截读取目标对象原型操作，必须返回一个对象或者 `null`。接收一个参数：

- `target`：目标对象。

#### 可进行拦截的操作

- `Object.getPrototypeOf()`；

- `Reflect.getPrototypeOf()`；

- `__proto__`；

- `Object.prototype.isPrototypeOf()`；

- `instanceof`。

#### `Proxy` 抛出异常 `TypeError` 的情况

- `getPrototypeOf()` 返回的对象既不是对象也不是 `null`；

- 目标对象是不可扩展的，`getPrototypeOf()` 返回的原型不是目标对象本身的原型。

#### 例子

```javascript
// 五种触发代理的方法
var obj = {};
var p = new Proxy(obj, {
    getPrototypeOf(target) {
        return Array.prototype;
    }
});

console.log(
    Object.getPrototypeOf(p) === Array.prototype,  // true
    Reflect.getPrototypeOf(p) === Array.prototype, // true
    p.__proto__ === Array.prototype,               // true
    Array.prototype.isPrototypeOf(p),              // true
    p instanceof Array                             // true
);

// 两种异常情况
var obj = {};
var p = new Proxy(obj, {
    getPrototypeOf(target) {
        return "foo";
    }
});
Object.getPrototypeOf(p); // TypeError: "foo" is not an object or null

var obj = Object.preventExtensions({});
var p = new Proxy(obj, {
    getPrototypeOf(target) {
        return {};
    }
});
Object.getPrototypeOf(p); // TypeError: expected same prototype value
```

### 10、isExtensible(target)

用于拦截 `Object.isExtensible` 操作，必须返回布尔值或者可转换为 `Boolean` 的值。接收一个参数：

- `target`：目标对象。

#### 可进行拦截的操作

- `Object.isExtensible()`；

- `Reflect.isExtensible()`。

#### `Proxy` 抛出异常 `TypeError` 的情况

- `Object.isExtensible(proxy)` 与 `Object.isExtensible(target)` 返回的值必须相同，否则会报错。

#### 例子

```javascript
var p = new Proxy({}, {
  isExtensible: function(target) {
    console.log('called');
    return true;//也可以return 1;等表示为true的值
  }
});

console.log(Object.isExtensible(p));
```

### 11、ownKeys(target)

用来拦截对象自身属性的读取操作，必须返回一个数组，数组中每个成员是字符串或者 `Symbol` 值。接收一个参数：

- `target`：目标对象。

#### 可进行拦截的操作

- `Object.getOwnPropertyNames()`；

- `Object.getOwnPropertySymbols()`；

- `Object.keys()`；

- `for...in`。

####  `Proxy` 抛出异常 `TypeError` 的情况

- 返回的结果不是数组，或者返回的结果是数组，但是数组每一个成员不都是字符串或者 `Symbol`；

- 如果目标对象包含不可配置的属性，那么该属性必须被 `ownKeys` 方法返回；

- 如果目标对象是不可扩展的，那么返回的数组必须包含原目标对象所有的属性，并且不能包含多余的属性。

#### `ownKeys` 自动过滤三类属性

- 目标对象上不存在的属性；

- 属性名为 `Symbol` 值；

- 不可遍历（`enumerable`）的属性。

#### 例子

```javascript
var p = new Proxy({}, {
  ownKeys: function(target) {
    console.log('called');
    return ['a', 'b', 'c'];
  }
});

console.log(Object.getOwnPropertyNames(p));
```

### 12、preventExtensions(target)

用来拦截 `Object.preventExtensions()` 操作，返回布尔值或者可以转换为 `Boolean` 值。接收一个参数：

- `target`：目标对象。

#### 可进行拦截的操作

- `Object.preventExtensions()`；

- `Reflect.preventExtensions()`。

####  `Proxy` 抛出异常 `TypeError` 的情况

- 只有当目标对象是不可扩展，即 `Object.isExtensible(proxy)` 为 `false`，`proxy.preventExtensions` 才能返回 `true`，否则会报错。

#### 例子

```javascript
var proxy = new Proxy({}, {
  preventExtensions: function(target) {
    console.log('called');
    Object.preventExtensions(target);
    return true;
  }
});

Object.preventExtensions(proxy)
```

### 13、setPrototypeOf(target, prototype)

用来拦截 `Object.setPrototypeOf()` 操作，返回布尔值。接收两个参数：

- `target`：目标对象；

- `prototype`：原型对象或者 `null`。

#### 可进行拦截的对象

- `Object.setPrototypeOf()`；

- `Reflect.setPrototypeOf()`。

####  `Proxy` 抛出异常 `TypeError` 的情况

- 如果目标对象是不可扩展，那么 `setPrototypeOf` 不能改变目标对象的原型。

#### 例子

```javascript
var handler = {
  setPrototypeOf (target, proto) {
    throw new Error('Changing the prototype is forbidden');
  }
};
var proto = {};
var target = function () {};
var proxy = new Proxy(target, handler);
Object.setPrototypeOf(proxy, proto);
```

## 三、其它

### 1、Proxy.revocable()

方法返回一个对象 `{ "proxy": proxy, "revoke": revoke}`，属性 `proxy` 表示 `Proxy` 实例，`revoke` 是一个函数，可用于取消 `Proxy` 实例。

### 2、this 问题

在 `Proxy` 代理的情况下，目标对象内部的 `this` 会指向 `Proxy` 代理。

## 参考链接

[http://es6.ruanyifeng.com/#docs/proxy](http://es6.ruanyifeng.com/#docs/proxy)

[https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
