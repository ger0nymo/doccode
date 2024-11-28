class Calculator {
  private value: number;

  constructor(initialValue: number = 0) {
    this.value = initialValue;
  }

  add(num: number): Calculator {
    this.value += num;
    return this;
  }

  subtract(num: number): Calculator {
    this.value -= num;
    return this;
  }

  multiply(num: number): Calculator {
    this.value *= num;
    return this;
  }

  divide(num: number): Calculator {
    if (num === 0) {
      throw new Error('Cannot divide by zero');
    }
    this.value /= num;
    return this;
  }

  getResult(): number {
    return this.value;
  }
}

const calc = new Calculator();
const result = calc.add(10).multiply(2).subtract(5).divide(3).getResult();
console.log(`The result is: ${result}`);
