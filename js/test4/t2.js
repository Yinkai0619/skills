//打印以下数组中平方大于10,且为偶数的数值
const arr = [1,2,3,4,5];

// 1
console.log(arr.filter(x => x % 2 ===0).map(x => x * x).filter(x => x > 10 ))

// 2
let newarr = [];
arr.forEach((x,y) => {
    // console.log(y,':',x * x)
    if (x % 2 === 0) {
        n = x * x;
        if (n > 10) {newarr.push(n)}
    }
})
console.log(newarr)

// 3
newarr2 = []
// arr.filter(x => x % 2 === 0).forEach(x => {
//     let n = x * x;
//     if (n > 10) newarr2.push(n)
//     // if ((n = x * x) > 10) newarr2.push(n)
// })
arr.forEach(x => {
    if (x%2 === 0) {
        let n = x * x;
        if (n > 10) newarr2.push(n)
        // if ((n = x * x) > 10) newarr2.push(n)
    }
})
console.log(newarr2)

// 4
const s = Math.sqrt(10)
// console.log(s)
console.log(arr.filter(x => !(x % 2) && x > s).map(x => x * x))