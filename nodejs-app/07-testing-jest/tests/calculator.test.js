const Calculator = require('../src/calculator');

describe('Calculator', () => {
  let calc;
  
  beforeEach(() => {
    calc = new Calculator();
  });
  
  describe('add', () => {
    it('should add two numbers', () => {
      expect(calc.add(2, 3)).toBe(5);
    });
    
    it('should handle negative numbers', () => {
      expect(calc.add(-1, -1)).toBe(-2);
    });
  });
  
  describe('divide', () => {
    it('should divide two numbers', () => {
      expect(calc.divide(10, 2)).toBe(5);
    });
    
    it('should throw error on division by zero', () => {
      expect(() => calc.divide(10, 0)).toThrow('Division by zero');
    });
  });
});
