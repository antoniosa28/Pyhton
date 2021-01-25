def tetraedricos(i):
    n=int(i)
    if(n>0):
        x = int((n*(n+1)*(n+2))/6)
        tetraedricos(n-1)
        print(x)
    else:
        return 1

def main():
    print("Digite quantos tetraédricos deseja entrar:")
    n = input()
    tetraedricos(n)

if __name__ == "__main__":
    main()