// JavaScript 版本
function processData(data, callback = null) {
  const result = [];
  for (const item of data) {
    let processed;
    if (callback) {
      processed = callback(item);
    } else {
      processed = item * 2;
    }
    result.push(processed);
  }
  return result;
}

// 使用示例
const numbers = [1, 2, 3, 4, 5];
const result = processData(numbers, x => x ** 2);
console.log(result);
