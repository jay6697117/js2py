// // JavaScript 版本
// function processData(data, callback = null) {
//   const result = [];
//   for (const item of data) {
//     let processed;
//     if (callback) {
//       processed = callback(item);
//     } else {
//       processed = item * 2;
//     }
//     result.push(processed);
//   }
//   return result;
// }

// // 使用示例
// const numbers = [1, 2, 3, 4, 5];
// const result = processData(numbers, x => x ** 2);
// console.log(result);

// JavaScript 包结构示例
// my-package/
// ├── package.json
// ├── index.js
// ├── utils/
// │   ├── math.js
// │   └── string.js
// └── tests/
//     └── test.js

// index.js - 主入口文件
export { add, multiply } from './utils/math.js';
export { capitalize, reverse } from './utils/string.js';

// utils/math.js
export function add(a, b) {
    return a + b;
}
export function multiply(a, b) {
    return a * b;
}

// utils/string.js
export function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}
export function reverse(str) {
    return str.split('').reverse().join('');
}