for (let i=1; i<=9; i++) {
    line = ''
    for (let j=1; j<=i; j++) {
        // console.log(j, '*', i, '=', i*j);
        line += `${j}*${i}=${i*j}\t`
    }
    console.log(line)
}