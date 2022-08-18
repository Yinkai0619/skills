// Map函数的实现

/* 
//传统实现
function map(fn, arr) {
    let newarr = [];
    for (let i = 0; i < arr.length; i++) {
        newarr[i] = fn(arr[i])
    };
    return newarr;
};

console.log(map(x => x + 10, [1, 2, 3, 4]));
console.log(map(function (x) { return x + 10 }, [1, 2, 3, 4]));
 */



//生成器版实现
function* map(fn, arr) {
    for (let i = 0; i < arr.length; i++) {
        yield fn(arr[i]);
    };
};

for (let o of map(x => x + 10, [1, 2, 3, 4]))
    console.log(o);

