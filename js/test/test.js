// 闭包版：
// function counter() {
//     let c = 0;
//     return function() {
//         return ++c;
//     }
// }

// const inc = counter()    //内层函数
// console.log(inc())
// console.log(inc())
// console.log(inc())


//生成器版
function * counter() {
    let c = 0;
    while (true) {
        yield ++c;
    }
} 
const inc = counter()    //内层函数
// console.log(typeof(inc))
console.log(inc.next())
console.log(inc.next().value)
console.log(inc.next().value)