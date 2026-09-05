class Solution:
    def defangIPaddr(self, address: str) -> str:
        ip_addr_split = address.split('.')

        return '[.]'.join(ip_addr_split)
