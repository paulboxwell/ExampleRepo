"Add test cases for convert_numbers_to_words function across a range of inputs
    let numToWord = (num) => {
        switch(typeof num){
            case 'number':{
                let words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
                return num < 10 ? words[num] : (num > 9 && num < 20) ? `${words[Math.floor(num/10)]}teen` : (num > 19 && num < 100) ? `${words[Math.floor((num-20)/10)]}ty${words[num%10]}`;
            }
        };
    test({
      name: 'Test case for convert_numbers_to_words function',
      fn: () => {
        let expected = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
        for(let i = 0; i < expected.length; i++){
          expect(numToWord(i)).toBe(expected[i]);
        }
      }
    });
    test({
      name: 'Test case for convert_numbers_to_words function with teens',
      fn: () => {
        let numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19];
        for(let i = 0; i < numbers.length; i++){
          expect(numToWord(numbers[i])).toBe(`${words[Math.floor(numbers[i]/10)]}teen`);
        }
      }
    });
    test({
      name: 'Test case for convert_numbers_to_words function with hundreds',
      fn: () => {
        let numbers = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109];
        for(let i = 0; i < numbers.length; i++){
          expect(numToWord(numbers[i])).toBe(`${words[Math.floor((numbers[i]-100)/10)]}ty${words[numbers[i]%10]}`);
        }
      }
    });"