class Solution:
    def isValid(self, s: str) -> bool:
        # mapping_dic={
        #             "(":")",
        #             "[":"]",
        #             "{":"}"
        #         }

        # stack=[]

        # for symbol in s:
        #     if symbol in  mapping_dic:
        #         stack.append(symbol)
        #     else:
        #         if mapping_dic.get(stack[-1])!=symbol:
        #             return False

        #         if stack is None:
        #             return False
        # return True

        ''' understanded the last in first out output'''
        '''Lesson Learned: In stack problems, never search the whole stack. Always think in terms of peek (stack[-1]) and pop() because a stack follows Last In, First Out (LIFO).'''
        mapping_dic={
                ")":"(",
                "]":"[",
                "}":"{"
            }

        stack=[]

        for symbol in s:
            # print(symbol)
            if symbol in '([{':
                stack.append(symbol)
            else:
                if not stack:
                    return False
                if stack[-1]==mapping_dic.get(symbol):
                #    stack.remove(mapping_dic.get(symbol))
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True

