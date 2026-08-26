class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        mp = Counter(hand)
        hand.sort()
        cnt = 0
        for i in range(len(hand)):
            if mp[hand[i]]:
                for j in range(hand[i], hand[i]+groupSize):
                    if not mp[j]:
                        return False
                    mp[j]-=1
        return True



