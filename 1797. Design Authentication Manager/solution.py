class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.expiry = OrderedDict()
        self.life = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.evictExpired(currentTime)
        self.expiry[tokenId] = self.life + currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.evictExpired(currentTime)

        if tokenId in self.expiry:
            self.expiry.move_to_end(tokenId)
            self.expiry[tokenId] = self.life + currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.evictExpired(currentTime)
        return len(self.expiry)
    
    def evictExpired(self, currentTime: int) -> None:
        while self.expiry and next(iter(self.expiry.values())) <= currentTime:
            self.expiry.popitem(last= False)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
