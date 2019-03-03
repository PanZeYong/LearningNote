'use strict';

/**
 * let 和 var 命令
 * 
 * var：存在变量提升，即脚本开始运行时，变量就已经存在，如果没有赋值的话则输出 undefined
 * 
 * let 命令要点
 * 1、在所在代码块有效；
 * 2、不能存在变量提升，即变量需要先声明后才能使用，否则会报错；
 * 3、暂时性死区
 * 4、不允许重复声明（不允许在相同作用域内，重复声明同一变量）
 * 5、充当块级作用域
 *
 *  ES6 明确规定，如果区块中存在 let 和 const 命令，那么这个区块对这些命令声明的变量，从一开始就形成了封闭作用域。凡是在声明之前使用这些变量，就会报错。
 *  ES6 规定暂时性死区和修订变量提升，主要是为了减少运行时错误，防止在变量声明声明前就使用该变量，从而导致意料之外的行为。
 *  
 *  总之，在代码块中，使用 let 命令声明变量之前，该变量都是不可用的。这在语法上称为“暂时性死区”（temporal dead zone，简称 TDZ）
 *  总之，暂时性死区的本质就是，只要一进入当前作用域，所要使用的变量已经存在，但是不可获取，只有等到声明变量的那一行代码出现，才可以获取和使用该变量。
 *  
 *  块级作用域
 *
 *  ES5 只有全局作用域和局部作用域，没有块级作用域 。可能会在以下场景导致问题：
 *  1、内层变量可能会覆盖外层变量
 *  2、用来计数的循环变量泄漏为全局变量
 *
 *  ES5 规定，函数只能在顶层作用域和函数作用域之中声明，不能在块级作用域声明
 *  ES6 引入了块级作用域，明确允许在块级作用域之中声明函数；
 *  ES6 规定在块级作用域之中，函数声明语句的行为类似于 let，在块级作用域之外不可引用
 *
 *  ES6 新增 let 命令为 JavaScript 增加块级作用域
 *  ES6 允许块级作用域的任意嵌套，外层作用域无法读取内层作用域的变量，内层作用域可以定义外层作用域的同名变量
 *  ES6 规定：适用于 ES6 实现的浏览器
 * （1）允许在块级作用域内声明函数（使用大括号情况下）
 * （2）函数声明类似于 var，即会提升到全局作用域或者函数作用域的头部
 * （3）函数声明还会提升所在的块级作用域的头部
 *
 * const 命令
 * 1、声明一个只读的常量。一旦声明，常量的值就不能改变
 * 2、一旦声明，必须立即初始化，不能等到以后再赋值
 * 3、只在声明所在的块级作用域内有效
 * 4、常量不提升，存在暂时性死区，只能在声明的位置后面使用
 * 5、不可重复声明
 * 6、对于复合类型的变量，变量名不是指向数据，而是指向数据所在的地址，即内存地址。const 只保证变量指向的地址不变，并不保证地址的数据不变
 * 7、如果想冻结对象，可使用 Object.freeze()
 *
 * ES5 声明变量的方法：var 命令和 function 命令
 * ES6 声明变量方法：var 命令、function 命令、let 命令、const 命令、import 命令和 class 命令
 *
 * 全局对象的属性
 * 1、在浏览器中指的是 window 对象；
 * 2、在 Node.js 中指的是 global 对象
 * 3、ES5 中全局对象的属性与全局变量时等价的，即使用 var 命令和 function 命令声明的全局变量成为全局对象的属性
 * 4、ES6 规定：为了保持兼容性，var 命令和 function 命令声明的全局变量，依旧是全局对象的属性；
 * 	  let 命令、const 命令和 class 命令声明的全局变量，不属于全局对象的属性，也就是说，从 ES6 开始，全局变量将逐步与全局对象的属性脱钩
 */

var a = [];
for (var i = 0; i < 10; i++) {
	console.log('For: ' + i);
	a[i] = function() {
		console.log('Function: ' + i);
	};
}
a[6]();

var a = [];
for (let i = 0; i < 10; i++) {
	console.log('For: ' + i);
	a[i] = function() {
		console.log('Function: ' + i);
	};
}
a[6]();

// console.log(c);
// console.log(d);

// var c = 1;
// let d = 2;

// ---------- 暂时性死区 ----------
/*var temp = 123;

if (true) {
	temp = 234;
	let temp;    // 使用 let 命令声明变量，绑定到代码块，在声明之前使用则会报错
}*/

/*function bar(x = y, y = 2) {
	return [x, y];
}

bar();    // 报错，因为变量 y 此时未声明*/

 // ---------- 不允许重复声明 ----------                                               
 function func(arg) {
 	// let arg;    // 报错 不能再函数内部重新声明参数
 	{
 		let arg;    // 不会报错，不在同一个作用域
 	}
 }

 func(1);

 // ---------- 块级作用域 ----------
 var tmp = new Date()
 // 内层变量覆盖外层变量
 function f() {
 	console.log(tmp);
 	if (false) {
 		var tmp = "hello world";    // 变量提升，一运行就存在，覆盖全局变量 tmp
 	}
 }

 f()

 // ---------- 用来计数的循环变量泄漏为全局变量 ----------
 var s = "Hello"
 for(var i = 0; i < s.length; i++) {
 	console.log(s[i])
 }
 console.log(i)

 // ---------- 使用 let 命令充当块级作用域 ----------
 function f1() {
 	let n = 5;
 	if (true) {
 		let n = 10;
 	}
 	console.log(n);
 }
 f1()

 // ---------- 外层作用域无法读取内层作用域的变量 ----------
/* {
 	{
 		{
 			{
 				{
 					let insane = "Hello World"
 				}
 				console.log(insane)
 			}
 		}
 	}
 }*/

// ---------- ES5 规定，函数只能在顶层作用域和函数作用域之中声明，不能在块级作用域声明 ----------
// 下面这两种情况在 ES5 是非法的，但是浏览器没有遵守这个约定，还是支持在块级作用域中声明函数，依然可以运行。但是严格模式下会报错（Chorme 不会）
// 情况一（在 ES5 严格模式下会报错；但是在 ES6 严格模式下则不会报错的情况是需要加上大括号，否则也会报错）
'use strict'
if (true) {
	function f() {}
}


// 情况二
try {
	function f() {}
} catch(e) {

}

// ---------- ES6 引入了块级作用域，明确允许在块级作用域之中声明函数 ----------
function f() {
	console.log('I am outside');
}
(function () {
	if (false) {
		// 重复声明一次函数 f
		function f() { console.log('I am inside'); }
	}
}());

// ---------- const 命令 -----------
const foo = Object.freeze();    // 冻结对象本身

// 常规模式下，下面一行代码不起作用
// 严格模式下，报错
// foo.prop = 2;

var constantize = (obj) => {
	Object.freeze(obj);    // 冻结对象本身
	Object.keys(obj).foreach((key, value) => {
		if (typeof obj[key] === 'object') {
			constantize(obj[key])
		}
	})
}

/**
 * 变量的解构赋值
 *
 * 注意圆括号在解构赋值中的作用
 *
 * ES6 允许按照一定模式，从数组和对象中提取值，对变量进行赋值，这被称为解构。（var [a, b] = [1, 2]）
 * 解构失败的话则被赋值为 undefined
 * 不完全解构：等号左边的模式，只匹配一部分的等号右边的数组。（var [x, y] = [1, 2, 3]）
 * 如果等号右边不是数组，或者严格来说不是可遍历的结构（Iterator），则会报错。（let [foo] = 1）
 * 解构赋值允许指定默认值
 * 如果默认值是一个表达式，那么这个表达式是惰性求值，即只有在用到的时候才会求值。
 *
 * 对象的解构赋值
 * 解构不仅可以用于数组，还可以用于对象
 * 对象的解构与数组的解构的区别：
 * 1、数组的元素是按次序排列的，变量的取值由它的位置决定；
 * 2、对象的属性没有次序，变量必须与属性同名，才能取到正确的值；
 * 对象的解构赋值的内部机制，是先找到同名属性，然后再赋给对应的变量。真正被赋值的是后者，而不是前者。（var {foo: foos, bar: barz} = {foo: "foos", bar: "barz"} ）
 * 对象的解构也可以指定默认值;
 * 默认值生效的条件是，对象的属性值严格等于 undefined;
 * 解构失败的话，变量的默认值等于 undefined;
 * 解构模式时嵌套的对象，而且子对象所在的父属性不存在，则会报错；（var {foo, {bar}} = {bar: "bar"}）=> var _baz = { baz: "baz" },
    bar = _baz.foo.bar;
 * 解构赋值允许，等号左边的模式之中，不放置任何变量名。
 *
 * 字符串的解构赋值
 *
 * 数值和布尔值的解构赋值
 * 1、如果等号右边是数值或者布尔值时，则先把它转换为对象
 * 2、只要等号右边不是对象，则先将其转为对象，undefined 和 null 除外，因为它们无法转换为对象，则会报错
 *
 * 函数参数的解构赋值
 * 1、函数的参数可以使用默认值；
 *
 * 不能使用圆括号的情况：
 * 1、变量声明语句中，不能带有圆括号；（var [(a)] = [1]）    // 报错
 * 2、函数参数中，模式不能带有圆括号；（ function f([(z)])）{return z;}    // 报错
 * 3、赋值语句中，不能将整个模式，或嵌套模式中的一层，放在圆括号之中；（（{p: a} = {p: 42}））
 *
 * 可以使用圆括号的情况只有一种：赋值语句的非模式部分，可以使用圆括号
 *
 * 用途：
 * 1、交换变量的值；（[x, y] = [y, x]）
 * 2、从函数返回多个值，可以返回数组或者对象；
 * 3、函数参数的定义；
 * 4、提取 JSON 数据；
 * 5、函数参数的默认值；
 * 6、遍历 Map 结构；
 * 7、输入模块的指定方法。
 */

// 函数名前带有 * 是 Generator 函数，原生具有 Iterator 接口
function * fibs() {
	var a = 0;
	var b = 1;
	while(true) {
		yield b;      // 表示返回的值
		[a, b] = [b, a+b];
	}
}

var [first, second, third, fourth, fifth, sixth] = fibs();
console.log(sixth)

// ---------- 解构赋值允许指定默认值 ----------
/*var [foos = true] = []    // foo: true
var [x, y = "b"] = ["a", undefined]    // x = "a"    y = "b"
var [x = 1] = [null]    // null 如果一个数组成员是 null，默认值就不会生效*/

// ---------- 惰性求值 ----------
function f() {
  console.log('ssss')
}

let [x = f()] = [1]
// 等价于下面代码
'use strict';

function f() {
  console.log('ssss');
}

/*var _ = 1,
    x = _ === undefined ? f() : _;*/

/*// ES6 写法
var {foo, bar} = {foo: "foo", bar: "bar"}    // 等价于 var {foo: foo, bar: bar} = {foo: "foo", bar: "bar"} 
// ES5 写法
var _foo$bar = { foo: "foo", bar: "bar" },
    foo = _foo$bar.foo,
    bar = _foo$bar.bar;*/

/*let fooz;
({fooz} = {foo: "fooz"});    // 注意添加括号，变成代码块

// ---------- 解构赋值允许，等号左边的模式之中，不放置任何变量名----------
 ({} = [true, false]) // 等价于

 function _objectDestructuringEmpty(obj) { 
 	if (obj == null) 
 		throw new TypeError("Cannot destructure undefined"); 
 }

var _ref = [true, false];

_objectDestructuringEmpty(_ref);

_ref; 

({} = "abc")
({} = [])  

// ---------- 字符串解构赋值 ----------
const [a, b, c, d, e] = "hello"
let {length: len} = "hello"    // 属性赋值    

// ---------- 数值和布尔值的解构赋值 ----------
let {toString: s} = 123
Number.prototype.toString === s    // true       

// ---------- 函数参数的解构赋值 ----------
function add([x, y]) {
  return x + y
}    

// 为变量 x 和 y 指定默认值
function move({x = 0, y = 0} = {}) {
	return [x, y]
} 

function move() {
	var _ref = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {},
	    _ref$x = _ref.x,
	    x = _ref$x === undefined ? 0 : _ref$x,
	    _ref$y = _ref.y,
	    y = _ref$y === undefined ? 0 : _ref$y;

	return [x, y];
}

function move({x, y} = {x: 0, y: 0}) {
	return [x, y]
} 


function move() {
	var _ref = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : { x: 0, y: 0 },
	    x = _ref.x,
	    y = _ref.y;

	return [x, y];
}

// ---------- 用途 ----------
// 返回数组
function example() {
	return [1, 2, 3];
}
var [a, b, c] = example();

// 返回对象
function example() {
	return {
		foo: 1,
		bar: 2

	}
}

var { foo, bar } = example()

var map = new Map()
map.set('first', 'hello');
map.set('second', 'world');
for (let [key, value] of map) {
	console.log(key + " is " + value);
}*/

/**
 * 字符串的扩展
 *
 * 字符的 Unicode 表示法
 *
 * ES6 规定，将码点放入大括号，就能正确解读该字符。（\u{20BB7}）UTF-16
 * JavaScript 内部，字符是以 UTF-16 的格式储存，每个字符固定为 2 字节
 *
 * ES5 提供的方法
 * String.fromCharCode()：ES5 提供的方法，用于从码点返回对应字符，但是这个方法不能识别 32 位的 UTF-16；
 * charAt()：ES5 提供的方法，用于返回字符串给定位置的字符，无法识别大于 0xFFFF
 *
 * ES6 提供的方法：
 * codePointAt()：测试一个字符是由l两个字节还是由四个字节组成
 * String.fromCodePoint()：ES6 提供的方法，用于从码点返回对应字符，可以识别 32 位的 UTF-16
 * at()：ES6 提供的方法，用于返回字符串给定位置的字符，可以识别大于 0xFFFF（提案）
 * 
 * normalize()：用来将字符的不同表示方法统一为同样的形式，这称为 Unicode 正规化。参数值如下：
 * 1、NFC（默认参数），表示 “标准等价合成”，返回多个简单字符的合成字符。
 * 2、NFD，表示 “标准等价分解”，返回合成字符分解的多个简单字符。
 * 3、NFKC，表示 “兼容等价合成”，返回合成字符。
 * 4、NFKD，表示 “兼容等价分解”，返回合成字符分解的多个简单字符。
 * 
 * includes()：返回布尔值，表示是否找到了参数字符串。
 * startsWith()：返回布尔值，表示参数字符串是否在源字符串的头部。
 * endsWith()：返回布尔值，表示参数字符串是否在源字符串的尾部。
 *
 * String.raw()：用来充当模板字符串的处理函数，返回一个斜杠都被转义（即斜杠前面再加一个斜杠）的字符串
 * 
 * repeat()：返回一个新字符串，表示将源字符串c重复 n 次。
 * 1、参数是小数，会被取整
 * 2、参数是负数或者 Infinity，会报错
 * 3、0 到 -1 之间等于 0
 * 4、参数 NaN 等于 0
 * 5、参数是字符串，会先转为数字
 * 
 * padStart()：字符串补全功能，用于头部补全
 * padEnd()：字符串补全功能，用于尾部补全
 * 1、接收两个参数，第一个参数用来指定字符串d 最小长度，第二个参数用来补全的字符串
 * 2、如果原字符串的长度，等于或大于指定的最小长度，则返回原字符串
 * 3、如果用来补全的字符串与原字符串，两者的长度之和超过了指定的最小长度，则会截去超出位数的补全字符串
 * 4、如果省略第二个参数，则会用空格补全长度
 * 用途：
 * 1、为数值补全指定位数
 * 2、提示字符串格式
 * 字符串的遍历器接口
 * 1、ES6 为字符串添加遍历器接口，使得字符串可以被 for...of 循环遍历，还可以识别大于 0xFFFFFF 的码点，即 32 位的 UTF-16
 *
 * 模板字符串：增强版的字符串，用反引号（`）标识。既可以当普通字符串使用，也可以用来定义多行字符串，或者在字符串中嵌入变量。
 * 模板字符串嵌入变量，需要将变量名写在 $() 里
 * 模板字符串之中还能调用函数
 *
 * 标签（函数）模板：紧跟在一个函数名后面，该函数将被调用来处理这个模板字符串
 * 用途：
 * 1、过滤 HTML 字符串，防止用户输入恶意内容；
 * 2、多语言转换（国际化处理）
 * 
 */

/**
 * Symbol
 * ES6 引入的一种新的原始数据类型，表示独一无二的值， 是 JavaScript 语言的第七种数据类型，即 Undefined、Null、布尔值（Boolean）、字符串（String）、数值（Number）、对象（Object）
 * Symbol 值是通过 Symbol() 函数生成的，接收一个字符串作为参数
 * Symbol 函数前不能使用 new 命令，否则会报错。这是因为生成的 Symbol 是个原始类型的值，不是对象。类似于字符串的数据类型。
 * Symbol 值不能与其它类型的值j进行运算，否则会报错
 * Symbol 可以转为布尔值，但是不能转为数值。（Number(symbol))
 * Symbol 作为对象属性名时，不能用点运算符，并且属性名是公有的，需要用方括号
 *
 * Object.getOwnPropertySysmbols(object)：返回一个数组，成员是当前对象的所有用作对象属性名的 Symbol 值。
 * Object.getOwnPropertyNames(object)：无法获取 Symbol 类型
 * Reflect.ownKeys()：返回所有类型的键名，包括常规键名和 Symbol 键名
 *
 * 用途：
 * 1、非私有的内部用法
 */


/**
 * JS 数组去重
 *
 * 方法 1：indexOf
 */

/*function unique(array) {
	var res = []
	for (var i = 0, len = array.length; i < len; i++) {
		var current = array[i];
		if (res.indexOf(current) === -1) {
			res.push(current);
		}
	}
	return res;
}*/

// 方法 3：排序后去重
function unique(array) {
	var res = [];
	var sortArray = array.concat().sort();
	var seen;
	for (var i = 0, len = sortArray.length; i < len; i++) {
		// 如果第一个元素或者是相邻的元素不同
		if (!i || seen !== sortArray[i]) {
			res.push(sortArray[i]);
		}
		seen = sortArray[i];
	}
	return res;
}

console.log(unique([1, 2, 1, 3, '1', '2']))

