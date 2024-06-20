def hanoi_dp(n, source, target, auxiliary, dp):
    if n == 0:
        return 0
    if dp[n][source][target] != -1:
        return dp[n][source][target]
    
    # Langkah pertama: pindahkan n-1 cakram dari source ke auxiliary
    move1 = hanoi_dp(n-1, source, auxiliary, target, dp)
    # Langkah kedua: pindahkan cakram terakhir dari source ke target
    move2 = 1
    # Langkah ketiga: pindahkan n-1 cakram dari auxiliary ke target
    move3 = hanoi_dp(n-1, auxiliary, target, source, dp)
    
    dp[n][source][target] = move1 + move2 + move3
    return dp[n][source][target]

# Inisialisasi tabel dp
n = 3  # Jumlah cakram
dp = [[[-1 for _ in range(3)] for _ in range(3)] for _ in range(n+1)]

# Memulai pencarian solusi
langkah = hanoi_dp(n, 0, 2, 1, dp)
print("Jumlah langkah minimal: ", langkah)
