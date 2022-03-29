const obj = {
    a:1,
    b:2,
    c:3
}

// var {a,b} = obj;
// console.log(a)
// console.log(b)

// var {a,b,c,d} = obj;
// console.log(a)
// console.log(b)
// console.log(c)
// console.log(d)

var {a:m,b:n,c,d:x=2000} = obj;
console.log(m,n,x)