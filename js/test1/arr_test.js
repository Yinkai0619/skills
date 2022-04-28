const arr = [1,2,3,4,5];
newarr = []

// arr.map(x => {
//     res = x * x;
//     if (res % 2 === 0 & res > 10) newarr.push(res) 
// })

// console.log(arr.filter(x => x * x % 2 === 0 & x * x > 10).map(x => x * x))
// console.log(arr.filter(x => x % 2 ===0 & x * x > 10).map(x => x * x))
// arr.filter(x => x % 2 ===0).forEach(x => {
//     let res = x * x;
//     if (res > 10) newarr.push(res)
// })

// arr.forEach(x => {
//     res = x * x;
//     if (res % 2 === 0 & res > 10) newarr.push(res)
// })
// console.log(newarr)

const s = Math.sqrt(10);
console.log(arr.filter(x => !(x%2) && x > s).map(x => x * x))