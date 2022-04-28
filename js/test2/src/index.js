// import foo, { A, B } from './moda.js'
// import bar from './moda.js'
import * as mod from './moda.js'

// foo();
mod.default();

let a = new mod.A();
a.show();

console.log(mod.B)