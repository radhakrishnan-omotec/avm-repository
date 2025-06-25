import os




def baiting_simulation():
    filename = "Free_Movie_Download.txt"
    with open(filename, "w") as f:
        f.write("🎬 Congratulations! Click this fake link to download your movie: http://malicious-link")



    print(f"{filename} created. If this were a real USB bait, malware could have been executed.")
    print("🛡️ Do not trust free items or unknown USB drives.")




baiting_simulation()