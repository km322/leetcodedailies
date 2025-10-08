class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sorted_potions = sorted(potions)
        result = []
        for spell in spells:
            idx = self.bs(sorted_potions, spell, success)
            result.append(len(sorted_potions) - idx if idx != -1 else 0)
        return result
    def bs(self, potions, strength, success):
        low, high = 0, len(potions) - 1
        idx = -1
        while low <= high:
            mid = (low + high) // 2
            if potions[mid] * strength >= success:
                idx = mid
                high = mid - 1
            else:
                low = mid + 1
        return idx
