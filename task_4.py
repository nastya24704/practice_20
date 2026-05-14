class RomanNumber:
    """Class for representing Roman numerals."""
    
    roman_map = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }

    def __init__(self, roman_string: str) -> None:
        """
        Initialize Roman number with given string.

        Parameters:
            roman_string: String representation of Roman numeral
        """
        if self.is_roman(roman_string):
            self.rom_value = roman_string
        else:
            print("ошибка")
            self.rom_value = None

    def decimal_number(self):
        """
        Convert Roman numeral to decimal.

        Returns:
            Integer value of Roman numeral or None if invalid
        """
        if self.rom_value is None:
            return None
        
        result = 0
        i = 0
        roman_len = len(self.rom_value)
        
        while i < roman_len:
            if i + 1 < roman_len and self.rom_value[i:i+2] in self.roman_map:
                result += self.roman_map[self.rom_value[i:i+2]]
                i += 2
            else:
                result += self.roman_map[self.rom_value[i]]
                i += 1
        
        return result

    def __str__(self) -> str:
        """Return string representation of Roman number."""
        if self.rom_value is None:
            return "None"
        return self.rom_value

    def __repr__(self) -> str:
        """Return representation for list output."""
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

num_1 = RomanNumber('VI')
print(num_1.rom_value)
print(num_1.decimal_number())
print(num_1)
num_2 = RomanNumber('IIII')
print(num_2.rom_value)
num_3 = RomanNumber('XXIV')
print(num_3.decimal_number())
num_4 = RomanNumber('QER2')
nums = []
nums.append(num_1)
nums.append(num_2)
nums.append(num_3)
nums.append(num_4)
print(nums)
print(RomanNumber.is_roman('MMMCMLXXXVI'))
print(RomanNumber.is_roman('MMМMMLXXXVI'))
