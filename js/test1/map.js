// 高阶函数
// function map(fn, arr) {
//     let newarr = [];
//     for (i=0; i<=arr.length; i++) {
//         newarr[i] = fn(arr[i]);
//     }

//     return newarr;
// };

// console.log(map(x => x + 10, [1,2,3,4]))
// console.log(map(function (x) {return x + 10} , [1,2,3,4]))


// 生成器版
// function * map(fn, arr) {
//     for (i=0; i<arr.length; i++) {
//         yield fn(arr[i]);
//     }
// }

// for (let i of map(x=>x+10, [1,2,3,4,5])) {
//     console.log(i);
// }

let gen = function * (fn, arr) {
    for (i=0; i<arr.length; i++) {
        yield fn(arr[i]);
    }
}(x => x + 10, [1,2,3,4,5])

for (let i of gen) {
    console.log(i)
}
