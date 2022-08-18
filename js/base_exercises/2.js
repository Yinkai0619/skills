const sum = function _sum(n) {
    if (n === 1) return 1;
    return n + _sum(--n);
}

console.log(sum(5))