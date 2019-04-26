// function f(y = x) {
//     let x = 2;
//     console.log(y);
// }

// f ();

// var x = 1;
// function foo(x, y = function() { x = 2; }) {
//   x = 3;
//   y();
//   console.log(x);
// }

// foo()

// function foo (x, x=7, f) {
//     // let x = 6;
// }

// foo()

// var f = v => v;

// console.log(f(5));

// function foo() {
//     setTimeout(() => {
//         console.log('id:', this.id, this);
//     }, 100);
// }

// var id = 21;

// foo.call({ id: 42 });

// function Timer() {
//     this.s1 = 0;
//     this.s2 = 0;
//     // 箭头函数
//     setInterval(() => {
//         console.log("箭头：", this);
//         this.s1++
//     }, 1000);
//     // 普通函数
//     setInterval(function () {
//         console.log("普通：", this);
//       this.s2++;
//     }, 1000);
//   }

//   var timer = new Timer();

//   setTimeout(() => console.log('s1: ', timer.s1), 3100);
//   setTimeout(() => console.log('s2: ', timer.s2), 3100);

// var handler = {
//     id: '123456',

//     init: function() {
//       document.addEventListener('click',
//         event => {
//             console.log(this);
//             this.doSomething(event.type)
//         }, false);
//     },

//     doSomething: function(type) {
//       console.log('Handling ' + type  + ' for ' + this.id);
//     }
//   };

//   handler.init();

// function foo() {
//     return () => {
//         return () => {
//             return () => {
//                 console.log('id:', this.id);
//             };
//         };
//     };
// }

// var f = foo.call({id: 1});
// console.log(f()()());
// var t1 = f.call({id: 2})()(); // id: 1
// console.log(t1);
// var t2 = f().call({id: 3})(); // id: 1
// var t3 = f()().call({id: 4}); // id: 1

// const cat = {
//     lives: 9,
//     jumps: () => {
//         console.log(this);
//         this.lives--;
//     }
// }

// cat.jumps();

const evenSteven = (n) => {
    console.log('eventSteven: ', n);
    if (n > 0) {
        n = n - 1
        return () => {
            return evenSteven(n)
        }
    }
    return 'over';
}

// const _ = require('lodash')

const trampoline = (func) => {
    console.log('Func: ', func);
  let res = func()
  console.log('Res: ', res);
  while (res && res instanceof Function) {
    console.log('trampoline');

    res = res()
  }
  return res
}

// console.log(evenSteven(5));

console.log(trampoline(evenSteven(5)))