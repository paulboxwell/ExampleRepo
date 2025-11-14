function testConvertNumbersToWords() {
  let result = "" + String(123).split("`).join("\") + "; " + convert_numbers_to_words(123); 
  console.log(result);
}
