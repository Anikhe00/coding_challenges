function solution(str) {
  const result = [];
  for (let i = 0; i < str.length; i += 2) {
    result.push(str[i] + (str[i + 1] || "_"));
  }
  return result;
}
