def k_mer_counter(dna, k):
    k_counter = {}
    for count in dna:
        if count in k_counter:
            k_counter[count] += 1
        else:
            k_counter[count] = 1
    return k_counter


if __name__ == "__main__":
    DNA = input("DNA sequence required: ")
    K_mers = int(input("The K-mers: "))
    print(k_mer_counter(DNA, K_mers))



