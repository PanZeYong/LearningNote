'use strict';

// var 存在变量提升
var a = [];
for (var i = 0; i < 10; i++) {
	a[i] = function() {
		console.log('Function: ' + i);
    };
    console.log(a[i]);
}
a[6]();

// let 不存在变量提升
var b = [];
for (let i = 0; i < 10; i++) {
	b[i] = function() {
		console.log('Function: ' + i);
    };
    console.log(b[i]);
}
b[6]();

console.log(c);
var c = 5;

// console.log(d);
// let d = 5;

// var tmp = 123;

// if (true) {
//   tmp = 'abc'; // ReferenceError
//   let tmp;
// }

function test(arg = 9) {
    // var arg = 8;
    // console.log(arg);
    // let test = 8;
    // var test = 8;
    {
        let arg
    }
}

// test();

// var tmp = new Date();

// function f() {
//   console.log(tmp);
//   if (true) {
//     var tmp = 'hello world';
//   }
// }

// f(); // undefined

// // 情况一
// if (true) {
//     function f() {}
//   }

// function f() { console.log('I am outside!'); }

// (function () {
//   if (false) {
//     // 重复声明一次函数f
//     function f() { console.log('I am inside!'); }
//   }

//   f();
// }());

// foo = Object.freeze({});
// foo.prop = 123;

// function test() {
//     console.log(this);
// }

// test();

function move({x, y} = { x: 0, y: 0 }) {
    console.log(x, y);
    return [x, y];
}

move({});

// 严格模式
(function(){
    'use strict';
    console.log(0o11 === 011);
  })()