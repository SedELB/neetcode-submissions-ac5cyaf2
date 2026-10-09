class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        # [[7,1], [4,2], [1, 2], [0,1]]
        for pair in pairs:
            ttt = ((target - pair[0]) / pair[1]) # 3s, then 3s
            stack.append(ttt) #[3, 3]
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                # if the time to arrival is lesser than the one in front, it joins its car fleet.
                stack.pop() 
                # we remove it cuz it 'joined' the fleet, so we leave one element representing
                # both of them.

        return len(stack) # length of stack is the number of distinct car fleets.
            

