class RomanNumber:
    """Class for representing Roman numerals."""
    
    roman_map = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }
    
    int_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    def __init__(self, value):
        """
        Initialize Roman number with either string or integer.

        Parameters:
            value: Roman numeral string or decimal integer
        """
        if isinstance(value, str):
            if self.is_roman(value):
                self.rom_value = value
                self.int_value = self._roman_to_decimal(value)
            else:
                print("ошибка")
                self.rom_value = None
                self.int_value = None
        elif isinstance(value, int):
            if self.is_int(value):
                self.int_value = value
                self.rom_value = self._decimal_to_roman(value)
            else:
                print("ошибка")
                self.int_value = None
                self.rom_value = None
        else:
            print("ошибка")
            self.rom_value = None
            self.int_value = None

    def decimal_number(self):
        """
        Convert Roman numeral to decimal.

        Returns:
            Integer value of Roman numeral or None if invalid
        """
        if self.rom_value is None:
            return None
        return self._roman_to_decimal(self.rom_value)

    def roman_number(self):
        """
        Convert decimal to Roman numeral string.

        Returns:
            Roman numeral string or None if invalid
        """
        if self.int_value is None:
            return None
        return self._decimal_to_roman(self.int_value)

    def _roman_to_decimal(self, roman: str) -> int:
        """Convert Roman string to decimal (internal use)."""
        result = 0
        i = 0
        length = len(roman)
        
        while i < length:
            if i + 1 < length and roman[i:i+2] in self.roman_map:
                result += self.roman_map[roman[i:i+2]]
                i += 2
            else:
                result += self.roman_map[roman[i]]
                i += 1
        
        return result

    def _decimal_to_roman(self, number: int) -> str:
        """Convert decimal to Roman string (internal use)."""
        result = ""
        num = number
        
        for value, symbol in self.int_map:
            while num >= value:
                result += symbol
                num -= value
        
        return result

    def __str__(self) -> str:
        """Return string representation of Roman number."""
        if self.rom_value is None:
            return "None"
        return self.rom_value

    @staticmethod
    def is_roman(value: str) -> bool:
        """
        Check if string is valid Roman numeral.

        Parameters:
            value: String to check

        Returns:
            True if valid Roman numeral, False otherwise
        """
        if not isinstance(value, str) or len(value) == 0:
            return False
        
        allowed_chars = {'M', 'D', 'C', 'L', 'X', 'V', 'I'}
        for ch in value:
            if ch not in allowed_chars:
                return False
        
        invalid_patterns = ['IIII', 'XXXX', 'CCCC', 'MMMM', 'DD', 'LL', 'VV']
        for pattern in invalid_patterns:
            if pattern in value:
                return False
        
        prev_value = float('inf')
        count = 0
        
        for ch in value:
            current = 0
            if ch == 'M':
                current = 1000
            elif ch == 'D':
                current = 500
            elif ch == 'C':
                current = 100
            elif ch == 'L':
                current = 50
            elif ch == 'X':
                current = 10
            elif ch == 'V':
                current = 5
            elif ch == 'I':
                current = 1
            else:
                return False
            
            if current > prev_value:
                if prev_value * 2 != current and prev_value * 10 != current:
                    return False
                if count > 1:
                    return False
            
            if current == prev_value:
                count += 1
                if count > 3:
                    return False
                if current in [5, 50, 500]:
                    return False
            else:
                count = 1
            
            prev_value = current
        
        return True

    @staticmethod
    def is_int(value: int) -> bool:
        """
        Check if integer can be represented as Roman numeral.

        Parameters:
            value: Integer to check

        Returns:
            True if representable as Roman, False otherwise
        """
        if not isinstance(value, int):
            return False
        
        if value <= 0 or value >= 4000:
            return False
        
        return True


num_1 = RomanNumber(214)
print(num_1.int_value)
print(num_1.roman_number())
print(num_1.rom_value)
print(num_1)

num_2 = RomanNumber(5690)
print(num_2.int_value)

num_3 = RomanNumber('DXCVII')
print(num_3.int_value)
print(num_3.rom_value)
print(num_3)

print(RomanNumber.is_int(-614))
print(RomanNumber.is_int(3758))
