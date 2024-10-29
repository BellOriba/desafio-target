def invert_str(str):
    return "".join([str[char] for char in range(len(str) - 1, -1, -1)])

def main():
    string = "Teste"
    print(invert_str(string))

if __name__ == "__main__":
    main()