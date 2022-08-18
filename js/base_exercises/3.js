//计数器的实现

// 闭包版，高阶函数
/* function counter () {
    let c = 0;
    return function () {
        return ++c;
    }
}

const inc = counter();
console.log(inc())
console.log(inc())
console.log(inc()) */

//生成器版
function* conter() {
    let c = 0;
    while (true)
        yield ++c;
};

const inc = conter();
// console.log(inc.next()); 
// console.log(inc.next().value); 
// console.log(inc.next().value); 
for (let x of inc) {
    console.log(x);
    if (x === 100) break;
}


