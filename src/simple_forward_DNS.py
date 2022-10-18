class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.end = False
        self.ip = None

    def insert(self, word, ip):
        node = self
        for i in range(len(word) + 1):
            if i == len(word):
                node.end = True
                node.ip = ip
                break

            index = ord(word[i]) - ord('a')
            if node.children[index] is None:
                node.children[index] = Trie()

            node = node.children[index]

    def search(self, word):
        node = self
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if node.children[index] is None:
                print("Not found")
                break
            node = node.children[index]
        if node.end:
            print(node.ip)


def domain_sanitizer(url):
    url = url.replace("https://", "")
    url = url.replace("http://", "")
    url = url.replace("www.", "")
    url = url.replace(".", "")
    return url.strip()


def ip_sanitizer(internet_protocol):
    return internet_protocol.strip()


def __main__():
    print("Hello User!")
    print("Welcome to Jay's DNS Server 😁")
    tree = Trie()
    while True:
        print("1. Insert 2. Search 3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            domain = input("Enter the domain name: ")
            ip = input("Enter the IP address: ")

            domain = domain_sanitizer(domain)
            ip = ip_sanitizer(ip)

            tree.insert(domain, ip)
        elif choice == "2":

            domain = input("Enter the domain name: ")
            domain = domain_sanitizer(domain)

            tree.search(domain)
        elif choice == "3":
            break
        else:
            print("Invalid choice")


__main__()