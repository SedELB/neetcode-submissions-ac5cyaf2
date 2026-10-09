class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            # Tant que la pile n'est pas vide ET que la température d'aujourd'hui 
            # est plus chaude que la température du jour au sommet de la pile
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # On récupère l'index du jour "passé" qui attendait
                prev = stack.pop()
                output[prev] = i - prev
            
            stack.append(i)

        return output






