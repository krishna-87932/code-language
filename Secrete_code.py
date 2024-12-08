from string import ascii_lowercase,punctuation

class Encode:
    text = ""
    chars = ascii_lowercase
    codes = [2,22,222,3,33,333,4,44,444,5,55,555,6,66,666,7,77,777,7777,8,88,888,9,99,999,9999]
    temp_text = []
    temp_code = []
    code_dict = {
    }
    def main(self):

        for index, i in enumerate(self.chars) :
            if i not in self.chars:
                pass
            else:
                self.code_dict[i]=self.codes[index]
        for i in self.text.lower():
            self.temp_text.append(i)
        ordnary = punctuation
        for i in self.temp_text:
            if i == ' ':
                self.temp_code.append(' ')
            elif i in ordnary:
                pass
            else:
                self.temp_code.append(self.code_dict[i])
                self.temp_code.append('.')
        a = "".join(map(str,self.temp_code))

        return a

class Decode:
    input_string = ""
    result_list = []
    secondary = []
    final_list = []
    code_disct ={}
    def main(self):
    # Creating the list of give input 
        def list_maker(in_str ):
            split_parts = in_str.split(' ')
            
            for part in split_parts[:-1]: 
                self.result_list.append(part)
                self.result_list.append(' ') 
            self.result_list.append(split_parts[-1])

            for i in self.result_list:
                if i == " ":
                    self.secondary.append(i)
                else:
                    a = i.replace(" ",'')
                    self.secondary.append(a)

            for k in self.secondary:
                my_str = k.split('.')
                if k == " ":
                    self.final_list.append(' ')
                else:
                    for a in my_str[:-1]:
                        self.final_list.append(a)
            return self.final_list
        # Making the Dictionary of all combinations 
        def Dict_maker():
            codes = [2,22,222,3,33,333,4,44,444,5,55,555,6,66,666,7,77,777,7777,8,88,888,9,99,999,9999]
            for index,i in enumerate(ascii_lowercase):
                a = str(codes[index])
                self.code_disct[a] = i
        Dict_maker()
        code_list = list_maker(in_str=self.input_string)
        output_str = ""
        # Making final output 
        for i in code_list:
            if i == " ":
                output_str += " "
            else: 
                output_str+=(self.code_disct[i])
        return output_str
