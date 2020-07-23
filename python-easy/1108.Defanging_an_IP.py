import string

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


def main():
    IP = "1.1.1.1"
    x = Solution()
    print(x.defangIPaddr(IP))

if __name__ == "__main__":
    main()
